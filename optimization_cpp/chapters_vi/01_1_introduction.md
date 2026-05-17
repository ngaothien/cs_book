# 1 Giới thiệu

Tài liệu này dành cho các lập trình viên và nhà phát triển phần mềm nâng cao, những người muốn làm cho phần mềm của họ chạy nhanh hơn. Giả định rằng người đọc đã có kiến thức tốt về ngôn ngữ lập trình C++ và hiểu biết cơ bản về cách hoạt động của các trình biên dịch (compiler). Ngôn ngữ C++ được chọn làm cơ sở cho tài liệu này vì những lý do được giải thích ở trang 8 dưới đây.

Tài liệu này chủ yếu dựa trên nghiên cứu của tôi về cách hoạt động của các trình biên dịch và bộ vi xử lý. Các khuyến nghị dựa trên dòng bộ vi xử lý x86 từ Intel, AMD và VIA, bao gồm cả các phiên bản 64-bit. Các bộ vi xử lý x86 được sử dụng trong các nền tảng phổ biến nhất với hệ điều hành Windows, Linux, BSD và Mac OS X, mặc dù các hệ điều hành này cũng có thể được sử dụng với các bộ vi xử lý khác. Nhiều lời khuyên cũng có thể áp dụng cho các nền tảng khác và các ngôn ngữ lập trình biên dịch khác.

Đây là cuốn đầu tiên trong chuỗi năm tài liệu:

1. Optimizing software in C++: Hướng dẫn tối ưu hóa cho các nền tảng Windows, Linux và Mac.

2. Optimizing subroutines in assembly language: Hướng dẫn tối ưu hóa cho các nền tảng x86.

3. The microarchitecture of Intel, AMD and VIA CPUs: Hướng dẫn tối ưu hóa dành cho lập trình viên hợp ngữ (assembly) và người làm trình biên dịch.

4. Instruction tables: Danh sách độ trễ (latency), thông lượng (throughput) và chi tiết các vi thao tác (micro-operation) của tập lệnh cho CPU Intel, AMD và VIA.

5. Calling conventions for different C++ compilers and operating systems.

Các phiên bản mới nhất của các tài liệu này luôn có sẵn tại www.agner.org/optimize. Các điều kiện bản quyền được liệt kê ở trang 168 bên dưới.

Những ai hài lòng với việc lập trình phần mềm bằng ngôn ngữ bậc cao chỉ cần đọc tài liệu đầu tiên này. Các tài liệu tiếp theo dành cho những ai muốn đi sâu hơn vào các chi tiết kỹ thuật về thời gian thực thi tập lệnh, lập trình bằng hợp ngữ, công nghệ trình biên dịch, và vi kiến trúc của bộ vi xử lý. Mức độ tối ưu hóa cao hơn đôi khi có thể đạt được bằng cách sử dụng hợp ngữ cho các đoạn mã chuyên sâu về CPU, như được mô tả trong các tài liệu sau.

Xin lưu ý rằng các tài liệu hướng dẫn tối ưu hóa của tôi được hàng nghìn người sử dụng. Tôi đơn giản là không có thời gian để trả lời câu hỏi của tất cả mọi người. Vì vậy, xin đừng gửi các câu hỏi lập trình của bạn cho tôi. Bạn sẽ không nhận được bất kỳ câu trả lời nào đâu. Người mới bắt đầu được khuyên nên tìm kiếm thông tin ở nơi khác và tích lũy một lượng kinh nghiệm lập trình nhất định trước khi thử các kỹ thuật trong tài liệu này. Có rất nhiều diễn đàn thảo luận trên Internet nơi bạn có thể nhận được câu trả lời cho các câu hỏi lập trình của mình nếu bạn không thể tìm thấy câu trả lời trong các cuốn sách và tài liệu liên quan.

Tôi muốn cảm ơn rất nhiều người đã gửi cho tôi các bản sửa lỗi và gợi ý cho các tài liệu hướng dẫn tối ưu hóa của mình. Tôi luôn rất vui khi nhận được thông tin mới có liên quan.

## 1.1 Chi phí của việc tối ưu hóa (The costs of optimizing)

Các khóa học đại học về lập trình ngày nay nhấn mạnh tầm quan trọng của lập trình cấu trúc và hướng đối tượng, tính mô-đun, khả năng tái sử dụng và tính hệ thống của quy trình phát triển phần mềm. Những yêu cầu này thường mâu thuẫn với yêu cầu tối ưu hóa phần mềm về tốc độ hoặc kích thước.

Ngày nay, không có gì lạ khi các giáo viên dạy phần mềm khuyên rằng không có hàm hoặc phương thức nào nên dài hơn vài dòng. Vài thập kỷ trước, khuyến nghị lại hoàn toàn ngược lại: Đừng đặt thứ gì đó vào một chương trình con riêng biệt nếu nó chỉ được gọi một lần. Lý do cho sự thay đổi trong phong cách viết phần mềm này là các dự án phần mềm đã trở nên lớn hơn và phức tạp hơn, người ta chú trọng nhiều hơn vào chi phí phát triển phần mềm, và máy tính đã trở nên mạnh mẽ hơn.

Ưu tiên cao của việc phát triển phần mềm có cấu trúc và ưu tiên thấp của tính hiệu quả chương trình được phản ánh, trước hết và quan trọng nhất, trong việc lựa chọn ngôn ngữ lập trình và các framework giao diện. Điều này thường là một bất lợi cho người dùng cuối, những người phải đầu tư vào các máy tính ngày càng mạnh mẽ hơn để theo kịp các gói phần mềm ngày càng lớn hơn và vẫn cảm thấy thất vọng vì thời gian phản hồi quá lâu, thậm chí đối với các tác vụ đơn giản.

Đôi khi cần phải thỏa hiệp với các nguyên tắc phát triển phần mềm tiên tiến để làm cho các gói phần mềm nhanh hơn và nhỏ hơn. Tài liệu này thảo luận về cách tạo ra một sự cân bằng hợp lý giữa các cân nhắc này. Nó thảo luận về cách xác định và cô lập phần quan trọng nhất của một chương trình và tập trung nỗ lực tối ưu hóa vào phần cụ thể đó. Nó thảo luận về cách vượt qua những nguy hiểm của phong cách lập trình tương đối sơ khai mà không tự động kiểm tra vi phạm giới hạn mảng (array bounds violations), con trỏ không hợp lệ (invalid pointers), v.v. Và nó cũng thảo luận xem cấu trúc lập trình tiên tiến nào là tốn kém và cấu trúc nào là rẻ, xét trên khía cạnh thời gian thực thi (execution time).
