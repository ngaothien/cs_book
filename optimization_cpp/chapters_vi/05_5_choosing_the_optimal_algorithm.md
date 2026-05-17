# 5 Chọn thuật toán tối ưu (Choosing the optimal algorithm)

*(Tiếp theo)* phần mềm của họ. Điều này gây khó chịu cho người dùng.

* **Các vấn đề tương thích (Compatibility problems):** Tất cả phần mềm nên được kiểm tra trên các nền tảng khác nhau, độ phân giải màn hình khác nhau, cài đặt màu sắc hệ thống khác nhau và quyền truy cập của người dùng khác nhau. Phần mềm nên sử dụng các lời gọi API tiêu chuẩn thay vì các bản hack tự chế và truy cập phần cứng trực tiếp (direct hardware access). Nên sử dụng các giao thức có sẵn và định dạng tệp chuẩn hóa. Các hệ thống Web nên được kiểm tra trên các trình duyệt khác nhau, nền tảng khác nhau, độ phân giải màn hình khác nhau, v.v. Các nguyên tắc về khả năng truy cập (accessibility guidelines) nên được tuân thủ.

* **Bảo vệ sao chép (Copy protection):** Một số cơ chế bảo vệ chống sao chép dựa trên các bản hack vi phạm hoặc phá vỡ các tiêu chuẩn của hệ điều hành. Các cơ chế như vậy thường là nguồn gốc của các vấn đề tương thích và sự cố hệ thống. Nhiều cơ chế bảo vệ sao chép dựa trên nhận dạng phần cứng. Những cơ chế như vậy gây ra vấn đề khi phần cứng được cập nhật. Hầu hết các cơ chế bảo vệ sao chép đều gây phiền toái cho người dùng và ngăn cản việc sao lưu hợp pháp mà không ngăn chặn hiệu quả việc sao chép bất hợp pháp. Lợi ích của một cơ chế bảo vệ sao chép cần được cân nhắc cẩn thận với chi phí phải trả liên quan đến các vấn đề sử dụng và hỗ trợ kỹ thuật cần thiết.

* **Cập nhật phần cứng (Hardware updating):** Việc thay đổi đĩa cứng hoặc phần cứng khác thường yêu cầu phải cài đặt lại tất cả phần mềm và các cài đặt của người dùng sẽ bị mất. Không có gì lạ khi công việc cài đặt lại mất trọn một ngày làm việc hoặc hơn. Nhiều ứng dụng phần mềm cần các tính năng sao lưu (backup) tốt hơn, và các hệ điều hành hiện tại cần hỗ trợ tốt hơn cho việc sao chép đĩa cứng (hard disk copying).

* **Bảo mật (Security):** Tính dễ bị tổn thương của phần mềm có truy cập mạng trước các cuộc tấn công của vi-rút và các hành vi lạm dụng khác là cực kỳ tốn kém đối với nhiều người dùng. Tường lửa (Firewalls), trình quét vi-rút và các phương tiện bảo vệ khác là một trong những nguyên nhân thường xuyên nhất gây ra lỗi tương thích và sập hệ thống (system crash). Hơn nữa, không có gì lạ khi các trình quét vi-rút ngốn nhiều thời gian hơn bất kỳ thứ gì khác trên máy tính. Phần mềm bảo mật là một phần của hệ điều hành thường đáng tin cậy hơn phần mềm bảo mật của bên thứ ba.

* **Dịch vụ nền (Background services):** Nhiều dịch vụ chạy ngầm là không cần thiết đối với người dùng và gây lãng phí tài nguyên. Hãy cân nhắc chỉ chạy các dịch vụ này khi được người dùng kích hoạt.

* **Phình to tính năng (Feature bloat):** Thường thì phần mềm sẽ thêm các tính năng mới vào mỗi phiên bản mới vì lý do tiếp thị. Điều này có thể khiến phần mềm trở nên chậm hơn hoặc yêu cầu nhiều tài nguyên hơn, ngay cả khi người dùng không bao giờ sử dụng đến các tính năng mới đó.

* **Xem xét nghiêm túc phản hồi của người dùng (Take user feedback seriously):** Các phàn nàn của người dùng nên được coi là một nguồn thông tin quý giá về các lỗi (bugs), vấn đề tương thích, vấn đề về khả năng sử dụng và các tính năng mới được mong muốn. Phản hồi của người dùng nên được xử lý một cách có hệ thống để đảm bảo thông tin được sử dụng một cách hợp lý. Người dùng nên nhận được phản hồi về việc điều tra các vấn đề và các giải pháp dự kiến. Các bản vá lỗi (Patches) nên dễ dàng tải xuống từ một trang web.

## 5 Chọn thuật toán tối ưu (Choosing the optimal algorithm)

Điều đầu tiên cần làm khi bạn muốn tối ưu hóa một phần mềm tiêu tốn nhiều tài nguyên CPU là tìm ra thuật toán tốt nhất (the best algorithm). Việc lựa chọn thuật toán rất quan trọng đối với các tác vụ như sắp xếp (sorting), tìm kiếm (searching), và tính toán toán học (mathematical calculations). Trong những trường hợp như vậy, bạn có thể đạt được nhiều lợi ích hơn bằng cách chọn thuật toán tốt nhất thay vì cố gắng tối ưu hóa thuật toán đầu tiên xuất hiện trong đầu. Trong một số trường hợp, bạn có thể phải kiểm tra một vài thuật toán khác nhau để tìm ra thuật toán hoạt động tốt nhất trên một tập dữ liệu thử nghiệm điển hình.

Mặc dù vậy, tôi phải cảnh báo việc làm quá tay (overkill). Đừng sử dụng một thuật toán tiên tiến và phức tạp nếu một thuật toán đơn giản có thể thực hiện công việc đủ nhanh. Ví dụ, một số lập trình viên sử dụng bảng băm (hash table) cho cả danh sách dữ liệu nhỏ nhất. Bảng băm có thể cải thiện thời gian tìm kiếm một cách
