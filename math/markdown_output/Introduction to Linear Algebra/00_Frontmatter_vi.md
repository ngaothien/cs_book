# **GIỚI THIỆU VỀ ĐẠI SỐ TUYẾN TÍNH**

Ấn bản lần thứ năm

GILBERT STRANG *Viện Công nghệ Massachusetts (MIT)* 

WELLESLEY - CAMBRIDGE PRESS Hộp 812060 Wellesley MA 02482

#### **Giới thiệu về Đại số tuyến tính, Ấn bản lần thứ 5**

Bản quyền ©2016 thuộc về Gilbert Strang

**ISBN 978-0-9802327-7-6** 

**Bảo lưu mọi quyền.** Không phần nào của cuốn sách này được phép sao chép, lưu trữ hoặc truyền đi 

dưới bất kỳ hình thức nào, bao gồm cả photocopy, mà không có sự cho phép bằng văn bản từ 

Wellesley - Cambridge Press. Việc dịch sang bất kỳ ngôn ngữ nào đều bị nghiêm cấm - 

các bản dịch được ủy quyền sẽ do nhà xuất bản sắp xếp.

BTEX **dàn trang bởi Ashley** C. **Fernandes** (info@problemsolvingpathway.com) In tại Hợp chủng quốc Hoa Kỳ

QA184.S78 2016 512'.5 93-14092

9876543

### **Các văn bản khác từ Wellesley** - **Cambridge Press**

**Khoa học Tính toán và Kỹ thuật,** Gilbert Strang ISBN 978-0-9614088-1-7

**Wavelets và Filter Banks,** Gilbert Strang và Truong Nguyen ISBN 978-0-9614088-7-9

**Giới thiệu về Toán học Ứng dụng,** Gilbert Strang ISBN 978-0-9614088-0-0

**Giải tích, Ấn bản lần thứ ba (2017),** Gilbert Strang ISBN 978-0-9802327-5-2

**Thuật toán cho Định vị Toàn cầu,** Kai Borre & Gilbert Strang ISBN 978-0-9802327-3-8

**Các tiểu luận về Đại số tuyến tính,** Gilbert Strang ISBN 978-0-9802327-6-9

**Phương trình vi phân và Đại số tuyến tính,** Gilbert Strang ISBN 978-0-9802327-9-0 **Phân tích Phương pháp Phần tử Hữu hạn,** ấn bản 2008, Gilbert Strang và George Fix

ISBN 978-0-9802327-0-7

#### **Wellesley** - **Cambridge Press**

Hộp thư 812060

Wellesley MA 02482 USA **www.wellesleycambridge.com** 

#### **linearalgebrabook@gmail.com**

**math.mit.edu/gs**  điện thoại(781)431-8488 fax (617) 253-4358

### Trang web của cuốn sách này là **math.mit.edu/linearalgebra.**

Solution Manual (Hướng dẫn giải) có thể được in từ trang web đó.

Tài liệu khóa học bao gồm giáo trình (syllabus), các bài kiểm tra và các bài giảng được ghi hình cũng có sẵn trên trang web của cuốn sách và trang web giảng dạy: **web.mit.edu/18.06** 

Đại số tuyến tính được bao gồm trong trang web OpenCourseWare của MIT **ocw.mit.edu.** Nơi này cung cấp các bài giảng video của toàn bộ khóa học đại số tuyến tính 18.06 và 18.06 SC. MATLAB® là thương hiệu đã đăng ký của The Math Works, Inc.

#### *Trang bìa trước nắm bắt một ý tưởng trung tâm của đại số tuyến tính.*

*Ax* = b có thể giải được khi b nằm trong không gian cột (column space) (màu đỏ) của *A.*

Một nghiệm cụ thể (particular solution) *y* nằm trong không gian hàng (row space) (màu vàng): *Ay* = *b.* 

Cộng thêm bất kỳ vectơ *z* nào từ không gian null (nullspace) (màu xanh lá) của A: *Az* = 0.

Nghiệm tổng quát là *x* = *y* + *z.* Khi đó *Ax* = *Ay* + *Az* = *b.* 

Thiết kế bìa lấy cảm hứng từ Lois Sellers và Gail Corbett.

# Mục lục

| <b>1 Giới thiệu về Vectơ (Introduction to Vectors)</b>                                   | <b>1</b>   |
|--------------------------------------------------------------------|------------|
| 1.1 Vectơ và Tổ hợp tuyến tính (Linear Combinations) . . . . .                      | 2          |
| 1.2 Độ dài và Tích vô hướng (Dot Products) . . . . .                             | 11         |
| 1.3 Ma trận (Matrices) . . . . .                                             | 22         |
| <b>2 Giải Hệ phương trình tuyến tính (Solving Linear Equations)</b>                                  | <b>31</b>  |
| 2.1 Vectơ và Phương trình tuyến tính . . . . .                         | 31         |
| 2.2 Ý tưởng về Khử (Elimination) . . . . .                              | 46         |
| 2.3 Khử bằng Ma trận . . . . .                           | 58         |
| 2.4 Quy tắc cho Các phép toán Ma trận . . . . .                          | 70         |
| 2.5 Ma trận nghịch đảo (Inverse Matrices) . . . . .                                     | 83         |
| 2.6 Khử = Phân tích nhân tử (Factorization): $A = LU$ . . . . .                | 97         |
| 2.7 Chuyển vị (Transposes) và Hoán vị (Permutations) . . . . .                          | 109        |
| <b>3 Không gian Vectơ và Không gian con (Vector Spaces and Subspaces)</b>                               | <b>123</b> |
| 3.1 Các Không gian của Vectơ . . . . .                                    | 123        |
| 3.2 Không gian null của $A$ : Giải $Ax = 0$ và $Rx = 0$ . . . . . | 135        |
| 3.3 Nghiệm tổng quát của $Ax = b$ . . . . .                    | 150        |
| 3.4 Sự độc lập, Cơ sở (Basis) và Chiều (Dimension) . . . . .                    | 164        |
| 3.5 Số chiều của Bốn Không gian con . . . . .                     | 181        |
| <b>4 Tính trực giao (Orthogonality)</b>                                             | <b>194</b> |
| 4.1 Tính trực giao của Bốn Không gian con . . . . .                  | 194        |
| 4.2 Hình chiếu (Projections) . . . . .                                          | 206        |
| 4.3 Xấp xỉ Bình phương Tối thiểu (Least Squares Approximations) . . . . .                         | 219        |
| 4.4 Cơ sở trực chuẩn (Orthonormal Bases) và Gram-Schmidt . . . . .                   | 233        |
| <b>5 Định thức (Determinants)</b>                                              | <b>247</b> |
| 5.1 Tính chất của Định thức . . . . .                       | 247        |
| 5.2 Hoán vị và Phần phụ đại số (Cofactors) . . . . .                           | 258        |
| 5.3 Quy tắc Cramer, Nghịch đảo, và Thể tích . . . . .                 | 273        |

| <b>6 Trị riêng và Vectơ riêng (Eigenvalues and Eigenvectors)</b>                           | <b>288</b> |
|-----------------------------------------------------------------|------------|
| 6.1 Giới thiệu về Trị riêng . . . . .                       | 288        |
| 6.2 Chéo hóa (Diagonalizing) một Ma trận . . . . .                            | 304        |
| 6.3 Hệ Phương trình Vi phân . . . . .                 | 319        |
| 6.4 Ma trận Đối xứng (Symmetric Matrices) . . . . .                                | 338        |
| 6.5 Ma trận Xác định Dương (Positive Definite Matrices) . . . . .                        | 350        |
| <b>7 Phân tích Giá trị Kỳ dị (The Singular Value Decomposition - SVD)</b>                 | <b>364</b> |
| 7.1 Xử lý Hình ảnh bằng Đại số Tuyến tính . . . . .                | 364        |
| 7.2 Cơ sở và Ma trận trong SVD . . . . .                     | 371        |
| 7.3 Phân tích Thành phần Chính (PCA bằng SVD) . . . . .     | 382        |
| 7.4 Hình học của SVD . . . . .                           | 392        |
| <b>8 Biến đổi Tuyến tính (Linear Transformations)</b>                                 | <b>401</b> |
| 8.1 Ý tưởng về một Biến đổi Tuyến tính . . . . .               | 401        |
| 8.2 Ma trận của một Biến đổi Tuyến tính . . . . .             | 411        |
| 8.3 Tìm kiếm một Cơ sở Tốt . . . . .                       | 421        |
| <b>9 Vectơ và Ma trận Phức (Complex Vectors and Matrices)</b>                           | <b>430</b> |
| 9.1 Số Phức . . . . .                                   | 431        |
| 9.2 Ma trận Hermitian và Unitary . . . . .                    | 438        |
| 9.3 Biến đổi Fourier Nhanh (Fast Fourier Transform) . . . . .                        | 445        |
| <b>10 Ứng dụng</b>                                          | <b>452</b> |
| 10.1 Đồ thị và Mạng . . . . .                              | 452        |
| 10.2 Ma trận trong Kỹ thuật . . . . .                          | 462        |
| 10.3 Ma trận Markov, Dân số, và Kinh tế học . . . . .       | 474        |
| 10.4 Quy hoạch Tuyến tính (Linear Programming) . . . . .                               | 483        |
| 10.5 Chuỗi Fourier: Đại số Tuyến tính cho Hàm số . . . . .     | 490        |
| 10.6 Đồ họa Máy tính . . . . .                                | 496        |
| 10.7 Đại số Tuyến tính cho Mật mã học . . . . .                  | 502        |
| <b>11 Đại số Tuyến tính Số (Numerical Linear Algebra)</b>                              | <b>508</b> |
| 11.1 Khử Gaussian trong Thực tế . . . . .                 | 508        |
| 11.2 Chuẩn (Norms) và Số Điều kiện (Condition Numbers) . . . . .                      | 518        |
| 11.3 Các Phương pháp Lặp và Tiền điều kiện (Preconditioners) . . . . .            | 524        |
| <b>12 Đại số Tuyến tính trong Xác suất &amp; Thống kê</b>        | <b>535</b> |
| 12.1 Trung bình, Phương sai, và Xác suất . . . . .                  | 535        |
| 12.2 Ma trận Hiệp phương sai (Covariance Matrices) và Xác suất Đồng thời . . . . .      | 546        |
| 12.3 Phân phối Gaussian Đa biến và Bình phương Tối thiểu Có trọng số . . . . . | 555        |
| <b>Phân tích Nhân tử Ma trận (Matrix Factorizations)</b>                                    | <b>563</b> |
| <b>Chỉ mục (Index)</b>                                                    | <b>565</b> |
| <b>Sáu Định lý Lớn / Đại số Tuyến tính Tóm lược</b>        | <b>574</b> |

# **Lời tựa (Preface)**

Tôi rất vui khi các bạn đang xem Ấn bản lần thứ Năm của cuốn Giới thiệu về Đại số Tuyến tính này. Đây là tài liệu cho các bài giảng video của tôi trên OpenCourseWare của MIT **(ocw.mit.edu** và cả **YouTube).** Tôi hy vọng những bài giảng đó sẽ hữu ích cho bạn (thậm chí có thể rất thú vị!).

Hàng trăm trường cao đẳng và đại học đã chọn giáo trình này cho khóa học đại số tuyến tính cơ bản của họ. Một kỳ nghỉ phép (sabbatical) đã cho tôi cơ hội chuẩn bị hai chương mới về xác suất và thống kê cùng với việc hiểu dữ liệu. Hàng nghìn cải tiến khác cũng đã được thực hiện, có lẽ chỉ có tác giả mới nhận ra... Dưới đây là một bổ sung mới dành cho sinh viên và tất cả người đọc:

Mỗi phần mở đầu với một tóm tắt ngắn để giải thích nội dung của nó. Khi bạn đọc một phần mới, và khi bạn xem lại một phần để ôn tập và sắp xếp nó trong tâm trí, những dòng đó là một hướng dẫn nhanh và là một công cụ hỗ trợ trí nhớ.

Một thay đổi lớn khác đến từ trang web của cuốn sách này **math.mit.edu/linearalgebra.** Trang web đó hiện chứa các lời giải cho Bài tập trong sách. Với không gian không giới hạn, điều này linh hoạt hơn rất nhiều so với việc in các lời giải ngắn gọn. Có ba trang web chính:

**ocw.mit.edu** Rất nhiều tin nhắn đến từ hàng nghìn sinh viên và giảng viên về đại số tuyến tính trên trang OpenCourseWare này. Các khóa học 18.06 và 18.06 SC bao gồm các bài giảng video của toàn bộ một học kỳ. Những bài giảng đó cung cấp một đánh giá độc lập về toàn bộ chủ đề dựa trên cuốn giáo trình này - thời gian của giáo sư được rảnh rỗi và sinh viên có thể học lúc 2 giờ sáng. (Người đọc hoàn toàn không cần phải ở trong một lớp học.) Sáu triệu người xem trên toàn thế giới đã xem những video này *(thật kinh ngạc).* Tôi hy vọng bạn thấy chúng hữu ích.

**web.mit.edu/18.06** Trang web này có bài tập về nhà và các bài kiểm tra (kèm đáp án) cho khóa học hiện tại đang được giảng dạy, và từ những năm 1996. Ngoài ra còn có các câu hỏi ôn tập, demo Java, mã giảng dạy (Teaching Codes), và các bài luận ngắn *(và các bài giảng video).* Mục tiêu của tôi là làm cho cuốn sách này hữu ích nhất có thể đối với bạn, cùng với tất cả tài liệu khóa học mà chúng tôi có thể cung cấp.

**math.mit.edu/linearalgebra** Trang này đã trở thành một trang web hoạt động tích cực. Nó hiện có Lời giải cho Bài tập - với không gian để giải thích các ý tưởng. Ngoài ra còn có các bài tập mới từ nhiều nguồn khác nhau - các bài tập thực hành, phát triển các ví dụ từ sách giáo khoa, mã trong MATLAB, *Julia* và *Python,* cùng với các bộ sưu tập bài kiểm tra (18.06 và các khóa khác) để ôn tập.

Vui lòng ghé thăm trang đại số tuyến tính này. *Gửi đề xuất tới* **linearalgebrabook@gmail.com** 

#### **Ấn bản lần thứ 5**

Bìa sách cho thấy **Bốn Không gian con Cơ bản (Four Fundamental Subspaces) -** không gian hàng (row space) và không gian null (nullspace) nằm ở phía bên trái, không gian cột (column space) và không gian null của A <sup>T</sup> nằm ở phía bên phải. Không có gì là bất thường khi đưa những ý tưởng trung tâm của môn học lên hiển thị như thế này! Khi bạn gặp bốn không gian đó trong Chương 3, bạn sẽ hiểu tại sao bức tranh đó lại đóng vai trò trung tâm như vậy đối với đại số tuyến tính.

Chúng được đặt tên là Bốn Không gian con Cơ bản trong cuốn sách đầu tiên của tôi, và chúng bắt đầu từ một ma trận *A.* Mỗi hàng của *A* là một vectơ trong không gian n chiều. Khi ma trận có *m* hàng, mỗi cột là một vectơ trong không gian m chiều. Hoạt động quan trọng trong đại số tuyến tính là thực hiện *tổ hợp tuyến tính của các vectơ cột (linear combinations of column vectors).* Đây chính xác là kết quả của một phép nhân ma trận - vectơ. *Ax là một tổ hợp các cột của A.* 

Khi chúng ta lấy *tất cả* các tổ hợp *Ax* của các vectơ cột, chúng ta có được *không gian cột.* Nếu không gian này bao gồm vectơ *b,* chúng ta có thể giải phương trình *Ax* = *b.* 

Tôi xin đặc biệt lưu ý đến Phần 1.3, nơi những ý tưởng này xuất hiện sớm - cùng với hai ví dụ cụ thể. Bạn không được mong đợi sẽ nắm bắt được mọi chi tiết của không gian vectơ trong một ngày! Nhưng bạn sẽ thấy các ma trận đầu tiên trong sách, và một hình ảnh về các không gian cột của chúng. Thậm chí còn có một *ma trận nghịch đảo (inverse matrix)* và mối liên hệ của nó với giải tích. Bạn sẽ học ngôn ngữ của đại số tuyến tính theo cách tốt nhất và hiệu quả nhất: thông qua việc sử dụng nó.

Mỗi phần của khóa học cơ bản đều kết thúc bằng một tập hợp lớn các bài toán ôn tập. Chúng yêu cầu bạn sử dụng các ý tưởng trong phần đó -- số chiều của không gian cột, một cơ sở (basis) cho không gian đó, hạng (rank) và nghịch đảo (inverse) và định thức (determinant) và trị riêng (eigenvalues) của *A.* Nhiều bài toán hướng tới việc tính toán bằng tay trên một ma trận nhỏ, và chúng đã được đánh giá rất cao. Các *Bài toán Thử thách (Challenge Problems)* tiến thêm một bước nữa, và đôi khi sâu hơn. Hãy để tôi đưa ra bốn ví dụ: *Phần* 2.1: Các thao tác hoán vị hàng nào của một ma trận Sudoku sẽ tạo ra một ma trận Sudoku khác?

*Phần* 2.7: Nếu P là một ma trận hoán vị, tại sao có một lũy thừa p <sup>k</sup> nào đó lại bằng *I?* 

*Phần* 3.4: Nếu *Ax=* b và *Cx* = *b* có cùng các nghiệm cho mọi *b,* liệu *A* có bằng *C?* 

*Phần* 4.1: Các điều kiện nào đối với bốn vectơ *r, n, c, l* cho phép chúng là cơ sở cho không gian hàng, không gian null, không gian cột, và không gian null trái của một ma trận 2x2?

#### **Bắt đầu Khóa học**

Phương trình *Ax* = *b* sử dụng ngôn ngữ của tổ hợp tuyến tính ngay lập tức. Vectơ *Ax* là *một tổ hợp của các cột của A.* Phương trình này đang yêu cầu *một tổ hợp tạo ra b.* Vectơ nghiệm *x* xuất hiện ở ba cấp độ và tất cả đều quan trọng:

- 1. *Giải trực tiếp (Direct solution)* để tìm *x* bằng khử tiến (forward elimination) và thế ngược (back substitution).
- **2.** *Nghiệm ma trận (Matrix solution)* sử dụng ma trận nghịch đảo: *x* = *A-<sup>1</sup> b* (nếu *A* có nghịch đảo).
- **3.** *Nghiệm cụ thể (Particular solution)* (cho *Ay* = *b)* cộng với *nghiệm không gian null* (cho *Az* = 0).

Nghiệm không gian vectơ *x* = *y*+ *z* đó được thể hiện trên trang bìa của cuốn sách.

Khử trực tiếp (Direct elimination) là thuật toán được sử dụng thường xuyên nhất trong tính toán khoa học. Ma trận *A* trở thành dạng tam giác - sau đó nghiệm được tìm ra nhanh chóng. Chúng ta cũng sẽ thấy cơ sở cho bốn không gian con. Nhưng đừng dành quá nhiều thời gian chỉ để thực hành phép khử . . . những ý tưởng hay hơn đang đến.

Tốc độ của mọi siêu máy tính mới đều được kiểm tra trên *Ax* = *b* : đại số tuyến tính thuần túy. Nhưng ngay cả một siêu máy tính cũng không muốn tính ma trận nghịch đảo: *quá chậm.* Các ma trận nghịch đảo cho ra công thức đơn giản nhất *x* = $A^{-1}b$ nhưng không phải là tốc độ cao nhất. Và mọi người phải biết rằng định thức (determinants) thậm chí còn chậm hơn - không có lý do gì một khóa học đại số tuyến tính lại nên bắt đầu bằng các công thức tính định thức của một ma trận n x n. Những công thức đó có vị trí của chúng, nhưng không phải là ở vị trí đầu tiên.

#### **Cấu trúc của Giáo trình**

Ngay trong lời tựa này, bạn đã có thể thấy phong cách của cuốn sách và mục tiêu của nó. Mục tiêu đó rất nghiêm túc, nhằm giải thích *phần Toán học* đẹp đẽ và hữu ích này. Bạn sẽ thấy các ứng dụng của đại số tuyến tính củng cố các ý tưởng chính như thế nào. Cuốn sách này tiến triển dần dần và đều đặn từ *các số* đến *các vectơ* rồi đến *các không gian con - mỗi* cấp độ đều đến một cách tự nhiên và ai cũng có thể nắm bắt được.

Dưới đây là 12 điểm về việc học và dạy từ cuốn sách này:

- 1. Chương 1 bắt đầu với vectơ và tích vô hướng. Nếu lớp học đã gặp chúng trước đây, hãy tập trung nhanh vào các tổ hợp tuyến tính. Phần 1.3 cung cấp ba vectơ độc lập mà tổ hợp của chúng lấp đầy toàn bộ không gian 3 chiều, và ba vectơ phụ thuộc trong một mặt phẳng. *Hai ví dụ đó là sự khởi đầu của đại số tuyến tính.*
- **2.** Chương 2 cho thấy bức tranh hàng (row picture) và bức tranh cột (column picture) của *Ax* = *b.* Trái tim của đại số tuyến tính nằm ở mối liên hệ đó giữa các hàng của *A* và các cột của *A* : cùng những con số nhưng những bức tranh rất khác nhau. Sau đó bắt đầu phần đại số của các ma trận: một ma trận khử *E* nhân với *A* để tạo ra một số không. Mục tiêu là nắm bắt toàn bộ quá trình - bắt đầu với *A,* nhân với các ma trận E, kết thúc với *U.*

Phép khử được nhìn thấy ở dạng tuyệt đẹp *A* = *LU.* Ma trận *tam giác dưới L* giữ các bước khử tiến, và *U* là ma trận *tam giác trên* cho phép thế ngược.

- **3.** Chương 3 là đại số tuyến tính ở cấp độ tốt nhất: *các không gian con.* Không gian cột chứa tất cả các tổ hợp tuyến tính của các cột. Câu hỏi quan trọng là: *Cần bao nhiêu cột trong số đó?* Câu trả lời cho chúng ta biết số chiều của không gian cột, và thông tin cốt lõi về *A.* Chúng ta đi đến Định lý Cơ bản của Đại số Tuyến tính (Fundamental Theorem of Linear Algebra).
- **4.** Khi có nhiều phương trình hơn ẩn số, gần như chắc chắn rằng *Ax* = *b* sẽ vô nghiệm. Chúng ta không thể vứt bỏ mọi phép đo mà gần đúng nhưng không hoàn hảo tuyệt đối! Khi chúng ta giải bằng *bình phương tối thiểu (least squares),* chìa khóa sẽ là ma trận A <sup>T</sup>A. Ma trận tuyệt vời này xuất hiện ở mọi nơi trong toán học ứng dụng, khi *A* là ma trận chữ nhật.
- 5. *Định thức* cung cấp công thức cho tất cả những gì đã có trước đó - Quy tắc Cramer, ma trận nghịch đảo, thể tích trong không gian *n* chiều. Chúng ta không cần những công thức đó để tính toán. Chúng làm chúng ta chậm lại. Nhưng det *A* = 0 cho biết khi nào một ma trận bị suy biến (singular): đây là chìa khóa để tìm trị riêng.

- 6. *Phần* 6.1 *giải thích trị riêng cho* các *ma trận* 2x2*.* Nhiều khóa học muốn xem xét trị riêng sớm. Việc đi thẳng đến đây từ Chương 3 là hoàn toàn hợp lý, vì định thức của ma trận 2x2 là rất dễ. *Phương trình quan trọng là Ax = $\lambda$x.* Trị riêng và vectơ riêng là một cách đáng kinh ngạc để hiểu về ma trận vuông. Chúng không dành cho *Ax* = *b,* chúng dành cho các phương trình động như *du/ dt* = *Au.* Ý tưởng luôn giống nhau: *đi theo các vectơ riêng.* Trong những hướng đặc biệt đó, *A* hoạt động giống như một số đơn lẻ (trị riêng $\lambda$) và bài toán trở thành một chiều. Điểm nổi bật quan trọng của Chương 6 là *chéo hóa một ma trận đối xứng.* Khi tất cả các trị riêng đều dương, ma trận đó là "xác định dương" (positive definite). Ý tưởng then chốt này kết nối toàn bộ khóa học - các phần tử chốt (pivots) dương, định thức, trị riêng và năng lượng. Tôi làm việc chăm chỉ để đạt đến điểm này trong cuốn sách và giải thích nó bằng các ví dụ.
- 7. Chương 7 là phần mới. Nó giới thiệu *các giá trị kỳ dị (singular values)* và *các vectơ kỳ dị.* Chúng tách mọi ma trận thành các phần đơn giản, xếp hạng theo thứ tự tầm quan trọng của chúng. Bạn sẽ thấy một cách để nén một hình ảnh. Đặc biệt, bạn có thể phân tích một ma trận đầy dữ liệu.
- 8. Chương 8 giải thích *các biến đổi tuyến tính.* Đây là hình học không có trục tọa độ, đại số không có tọa độ. Khi chúng ta chọn một cơ sở, chúng ta đạt được ma trận tốt nhất có thể.
- 9. Chương 9 chuyển từ các số thực và vectơ thực sang các vectơ và ma trận phức. Ma trận Fourier *F* là ma trận phức quan trọng nhất mà chúng ta từng thấy. Và *Biến đổi Fourier Nhanh (Fast Fourier Transform)* (nhân nhanh bằng *F* và $F^{-1}$ ) mang tính cách mạng.
- 10. Chương 10 chứa đầy các ứng dụng, nhiều hơn những gì bất kỳ khóa học đơn lẻ nào có thể cần: 10.1 *Đồ thị và* Mạng - dẫn đến ma trận cạnh-nút cho các Định luật Kirchhoff **10.2** *Ma trận trong* Kỹ thuật - phương trình vi phân song song với phương trình ma trận **10.3** *Ma trận Markov-* như trong thuật toán *PageRank* của Google 10.4 *Quy hoạch Tuyến tính-* một yêu cầu mới $x \ge 0$ và cực tiểu hóa chi phí **10.5** *Chuỗi Fourier -* đại số tuyến tính cho hàm số và xử lý tín hiệu kỹ thuật số **10.6** *Đồ họa Máy tính -* các ma trận di chuyển, xoay và nén hình ảnh **10.7** *Đại số Tuyến tính trong Mật mã học - phần* mới này rất thú vị khi viết. Mật mã Hill (Hill Cipher) không quá bảo mật. Nó sử dụng số học mô-đun (modular arithmetic): các số nguyên từ 0 đến p - 1. Phép nhân cho 4 x 5 = 1 *(mod* 19). Để giải mã, điều này cho 4-<sup>1</sup> = 5.
- 11. Tính toán nên được đưa vào khóa học đại số tuyến tính như thế nào? Nó có thể mở ra một sự hiểu biết mới về ma trận - mỗi lớp học sẽ tìm thấy một sự cân bằng. MATLAB và *Maple* và *Mathematica* mạnh mẽ theo những cách khác nhau. *Julia* và *Python* đều miễn phí và có thể truy cập trực tiếp trên Web. Những ngôn ngữ mới này cũng rất mạnh mẽ! Các lệnh cơ bản bắt đầu ở Chương 2. Sau đó Chương 11 chuyển sang các thuật toán chuyên nghiệp. Bạn có thể tải lên và tải xuống các mã cho khóa học này trên trang web.
- 12. Chương 12 về Xác suất và Thống kê là phần mới, với những ứng dụng thực sự quan trọng. Khi các biến ngẫu nhiên không độc lập, chúng ta nhận được các ma trận hiệp phương sai. May mắn thay, chúng là các ma trận đối xứng xác định dương. Đại số tuyến tính ở Chương 6 là cần thiết lúc này.

# **Sự đa dạng của Đại số Tuyến tính**

Giải tích chủ yếu xoay quanh một phép toán đặc biệt (đạo hàm) và phép toán ngược của nó (tích phân). Tất nhiên tôi thừa nhận rằng giải tích có thể quan trọng .... Nhưng rất nhiều ứng dụng của toán học lại là rời rạc (discrete) thay vì liên tục (continuous), kỹ thuật số (digital) thay vì tương tự (analog). Thế kỷ của dữ liệu đã bắt đầu! Bạn sẽ tìm thấy một bài luận mang tính giải trí tên là "Quá nhiều Giải tích" (Too Much Calculus) trên trang web của tôi. *Sự thật là vectơ và ma trận đã trở thành ngôn ngữ cần phải biết.* 

Một phần của ngôn ngữ đó là sự đa dạng tuyệt vời của các ma trận. Hãy để tôi đưa ra ba ví dụ:

| Ma trận Đối xứng (Symmetric matrix)                                                                                       | Ma trận Trực giao (Orthogonal matrix)                                                                                                 | Ma trận Tam giác (Triangular matrix)                                                                                |
|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| $\begin{bmatrix} 2 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & -1 & 2 \end{bmatrix}$ | $\frac{1}{2} \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & -1 & 1 & -1 \\ 1 & 1 & -1 & 1 \\ 1 & -1 & 1 & -1 \end{bmatrix}$ | $\begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 \end{bmatrix}$ |

*Mục tiêu then chốt là học cách "đọc" một ma trận.* Bạn cần nhìn thấy ý nghĩa trong các con số. Đây thực sự là cốt lõi của toán học - các khuôn mẫu và ý nghĩa của chúng.

Tôi đã sử dụng chữ *in nghiêng (italics)* và chữ **in đậm (boldface)** để làm nổi bật các từ khóa trên mỗi trang. Tôi biết có những lúc bạn muốn đọc nhanh, tìm kiếm những dòng quan trọng.

Cho phép tôi kết thúc với một vài lời dành cho các giáo sư. Bạn có thể cảm thấy hướng đi này là đúng, và băn khoăn liệu sinh viên của mình đã sẵn sàng hay chưa. *Chỉ cần cho họ một cơ hội!* Thực sự hàng nghìn sinh viên đã viết thư cho tôi, thường xuyên với những gợi ý và thật đáng ngạc nhiên thường xuyên kèm theo lời cảm ơn. Họ biết khóa học này có một mục đích, bởi vì giáo sư và cuốn sách đều đứng về phía họ. Đại số tuyến tính là một môn học tuyệt vời, hãy tận hưởng nó.

### **Sự giúp đỡ với Cuốn sách này**

Sự khích lệ lớn nhất chính là cảm giác rằng bạn đang làm một điều gì đó đáng giá với cuộc đời mình. Hàng trăm độc giả hào phóng đã gửi các ý tưởng, ví dụ, chỉnh sửa (và các ma trận yêu thích) xuất hiện trong cuốn sách này. *Cảm ơn tất cả các bạn.* 

Có một người đã giúp đỡ với từng từ trong cuốn sách này. Anh ấy là Ashley C. Fernandes, người đã chuẩn bị các tệp LaTeX. Bây giờ là sáu cuốn sách anh ấy đã cho phép tôi viết và viết lại, hướng tới sự chính xác và cũng vì cuộc sống. Làm việc với bạn bè là một cách sống hạnh phúc.

Những người bạn bên trong và bên ngoài khoa toán của MIT thật tuyệt vời. Alan Edelman cho *Julia* và nhiều hơn nữa, Alex Townsend cho các ví dụ về lá cờ trong phần 7.1, và Peter Kempthorne cho ví dụ về tài chính trong 7.3: đó là những điều nổi bật. Trang web của Don Spickler về mật mã học thực sự rất xuất sắc. Tôi xin cảm ơn Jon Bloom, Jack Dongarra, Hilary Finucane, Pavel Grinfeld, Randy LeVeque, David Vogan, Liang Wang, và Karen Willcox. Các "khuôn mặt riêng" (eigenfaces) trong 7.3 đến từ Matthew Turk và Jeff Jauregui. Và bước tiến lớn đối với các giá trị kỳ dị được thúc đẩy bởi khóa học tuyệt vời của Raj Rao tại Michigan.

Cuốn sách này mang nợ rất nhiều cho kỳ nghỉ phép vui vẻ của tôi tại Oxford. Cảm ơn Nick Trefethen và mọi người. Đặc biệt là bạn, người đọc! Xin gửi những lời chúc tốt đẹp nhất đến công việc của bạn.

# **Tiểu sử của Tác giả (Background of the Author)**

Đây là cuốn giáo trình thứ 9 của tôi về đại số tuyến tính, và tôi ngần ngại khi viết về bản thân mình. Chính toán học mới là điều quan trọng, và người đọc. Các đoạn tiếp theo thêm vào một chút ngắn gọn và mang tính cá nhân, như một cách để nói rằng các cuốn sách giáo khoa được viết bởi những con người.

Tôi sinh ra ở Chicago và đi học ở Washington, Cincinnati và St. Louis. Trường đại học của tôi là MIT (và khóa học đại số tuyến tính của tôi thì *cực kỳ trừu tượng).* Sau đó là Oxford và UCLA, rồi trở lại MIT trong một khoảng thời gian rất dài. Tôi không biết có bao nhiêu nghìn sinh viên đã tham gia khóa học 18.06 (hơn 6 triệu người nếu bạn tính cả các video trên *ocw.mit.edu).* Đã đến lúc thích hợp cho một cách tiếp cận mới mẻ, bởi vì môn học tuyệt vời này vốn chỉ được tiết lộ cho những sinh viên chuyên toán - chúng ta **cần phải mở đại số tuyến tính ra thế giới.** Tôi vô cùng biết ơn vì một cuộc đời giảng dạy toán học, nhiều hơn những gì tôi có thể diễn tả với bạn.

### Gilbert Strang

Tái bút: Tôi hy vọng cuốn sách tiếp theo (2018 ?) sẽ bao gồm *Học từ Dữ liệu (Learning from Data).* Chủ đề này đang phát triển nhanh chóng, đặc biệt là "học sâu" (deep learning). Bằng cách biết một hàm trên một tập dữ liệu huấn luyện gồm các dữ liệu cũ, chúng ta xấp xỉ hàm đó trên dữ liệu mới. Phép xấp xỉ chỉ sử dụng một hàm phi tuyến tính đơn giản *f(x)* = max(0, *x).* Chúng ta tối ưu hóa phép nhân ma trận *n* lần để làm cho việc học trở nên sâu sắc: X1 = f(A1x + b1), X2 = f(A2x1 + b2), ... , Xn = f(AnXn-1 + b<sup>n</sup> ) Đó là các lớp ẩn (hidden layers) *n* -1 giữa đầu vào *x* và đầu ra Xn - xấp xỉ *F* ( *x)* trên tập huấn luyện.

# **BẢNG CHỮ CÁI MA TRẬN (THE MATRIX ALPHABET)**

| A | Bất kỳ Ma trận nào (Any Matrix)              | p  | Ma trận Hoán vị (Permutation Matrix)      |
|---|-------------------------|----|-------------------------|
| B | Ma trận Cơ sở (Basis Matrix)            | p  | Ma trận Chiếu (Projection Matrix)       |
| C | Ma trận Phần phụ đại số (Cofactor Matrix)         | Q  | Ma trận Trực giao (Orthogonal Matrix)       |
| D | Ma trận Đường chéo (Diagonal Matrix)         | R  | Ma trận Tam giác Trên (Upper Triangular Matrix) |
| E | Ma trận Khử (Elimination Matrix)      | R  | Ma trận Bậc thang Rút gọn (Reduced Echelon Matrix)  |
| F | Ma trận Fourier          | s  | Ma trận Đối xứng (Symmetric Matrix)        |
| H | Ma trận Hadamard         | T  | Biến đổi Tuyến tính (Linear Transformation)   |
| I | Ma trận Đơn vị (Identity Matrix)         | u  | Ma trận Tam giác Trên (Upper Triangular Matrix) |
| J | Ma trận Jordan           | u  | Vectơ Kỳ dị Trái (Left Singular Vectors)   |
| K | Ma trận Độ cứng (Stiffness Matrix)        | V  | Vectơ Kỳ dị Phải (Right Singular Vectors)  |
| L | Ma trận Tam giác Dưới (Lower Triangular Matrix) | X  | Ma trận Vectơ riêng (Eigenvector Matrix)      |
| M | Ma trận Markov           | A  | Ma trận Trị riêng (Eigenvalue Matrix)       |
| N | Ma trận Không gian null (Nullspace Matrix)        | :E | Ma trận Giá trị Kỳ dị (Singular Value Matrix)   |
