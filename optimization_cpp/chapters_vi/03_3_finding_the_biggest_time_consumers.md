# 3 Tìm kiếm những yếu tố tốn thời gian nhất (Finding the biggest time consumers)

Tràn số nguyên (Integer overflow) là một vấn đề bảo mật khác. Tiêu chuẩn C chính thức nói rằng hành vi của số nguyên có dấu (signed integers) trong trường hợp tràn số là "không xác định" (undefined). Điều này cho phép trình biên dịch bỏ qua việc tràn số hoặc giả định rằng nó không xảy ra. Trong trường hợp của trình biên dịch Gnu, giả định rằng tràn số nguyên có dấu không xảy ra có một hậu quả đáng tiếc là nó cho phép trình biên dịch tối ưu hóa (loại bỏ) bước kiểm tra tràn số. Có một số biện pháp khắc phục khả thi cho vấn đề này: (1) kiểm tra tràn số trước khi nó xảy ra, (2) sử dụng số nguyên không dấu (unsigned integers) - chúng được đảm bảo sẽ quay vòng (wrap around), (3) bẫy (trap) hiện tượng tràn số nguyên bằng tùy chọn `-ftrapv`, nhưng điều này cực kỳ kém hiệu quả, (4) nhận cảnh báo từ trình biên dịch cho các tối ưu hóa như vậy với tùy chọn `-Wstrict-overflow=2`, hoặc (5) làm cho hành vi tràn số được xác định rõ ràng với tùy chọn `-fwrapv` hoặc `-fno-strict-overflow`.

Bạn có thể đi chệch khỏi các lời khuyên bảo mật ở trên trong các phần quan trọng của mã nơi tốc độ là yếu tố tiên quyết. Điều này có thể được cho phép nếu mã không an toàn (unsafe code) được giới hạn trong các hàm, lớp, khuôn mẫu (templates) hoặc mô-đun đã được kiểm tra kỹ lưỡng với một giao diện (interface) được xác định rõ ràng với phần còn lại của chương trình.

## 3.1 Một chu kỳ xung nhịp là bao nhiêu? (How much is a clock cycle?)

Trong tài liệu này, tôi sử dụng chu kỳ xung nhịp CPU (CPU clock cycles) thay vì giây hoặc micro giây làm thước đo thời gian. Điều này là do các máy tính có tốc độ rất khác nhau. Nếu tôi viết rằng một cái gì đó mất 10 μs ngày hôm nay, thì nó có thể chỉ mất 5 μs trên thế hệ máy tính tiếp theo và tài liệu của tôi sẽ sớm trở nên lỗi thời. Nhưng nếu tôi viết rằng một cái gì đó mất 10 chu kỳ xung nhịp thì nó sẽ vẫn mất 10 chu kỳ xung nhịp ngay cả khi tần số xung nhịp CPU (CPU clock frequency) tăng gấp đôi.

Độ dài của một chu kỳ xung nhịp là nghịch đảo của tần số xung nhịp. Ví dụ, nếu tần số xung nhịp là 2 GHz thì độ dài của một chu kỳ xung nhịp là 1 / (2 GHz) = 0.5 ns.

Một chu kỳ xung nhịp trên máy tính này không phải lúc nào cũng có thể so sánh được với một chu kỳ xung nhịp trên máy tính khác. CPU Pentium 4 (NetBurst) được thiết kế cho tần số xung nhịp cao hơn các CPU khác, nhưng nó thường sử dụng nhiều chu kỳ xung nhịp hơn các CPU khác để thực thi cùng một đoạn mã.

Giả sử một vòng lặp trong một chương trình lặp lại 1000 lần và có 100 phép toán dấu phẩy động (cộng, nhân, v.v.) bên trong vòng lặp. Nếu mỗi phép toán dấu phẩy động mất 5 chu kỳ xung nhịp, thì chúng ta có thể ước tính sơ bộ rằng vòng lặp sẽ mất 1000 * 100 * 5 * 0.5 ns = 250 μs trên CPU 2 GHz. Chúng ta có nên cố gắng tối ưu hóa vòng lặp này không? Chắc chắn là không! 250 μs ít hơn 1/50 thời gian cần thiết để làm mới màn hình. Người dùng không có cách nào có thể nhìn thấy độ trễ đó. Nhưng nếu vòng lặp nằm bên trong một vòng lặp khác cũng lặp lại 1000 lần thì chúng ta có thời gian tính toán ước tính là 250 ms. Độ trễ này vừa đủ dài để có thể nhận thấy nhưng chưa đủ dài để gây khó chịu. Chúng ta có thể quyết định thực hiện một số phép đo để xem ước tính của mình có đúng hay không hoặc thời gian tính toán thực tế có nhiều hơn 250 ms hay không. Nếu thời gian phản hồi quá lâu đến mức người dùng thực sự phải đợi kết quả thì chúng ta sẽ xem xét xem có điều gì có thể cải thiện được không.

## 3.2 Sử dụng một profiler để tìm các điểm nóng (Use a profiler to find hot spots)

Trước khi bạn bắt đầu tối ưu hóa bất cứ điều gì, bạn phải xác định các phần quan trọng của chương trình. Trong một số chương trình, hơn 99% thời gian được dành cho vòng lặp trong cùng (innermost loop) thực hiện các tính toán toán học. Trong các chương trình khác, 99% thời gian được dành cho việc đọc và ghi các tệp dữ liệu trong khi chưa tới 1% dùng để thực sự làm điều gì đó trên các dữ liệu này. Điều rất quan trọng là tối ưu hóa các phần mã quan trọng chứ không phải là các phần mã chỉ sử dụng một phần nhỏ trong tổng thời gian. Việc tối ưu hóa các phần mã ít quan trọng hơn sẽ không chỉ lãng phí thời gian mà còn làm cho mã kém rõ ràng hơn và khó gỡ lỗi (debug) cũng như bảo trì hơn.

Hầu hết các gói trình biên dịch đều bao gồm một bộ phân tích hiệu năng (profiler) có thể cho biết số lần mỗi hàm được gọi và thời gian nó sử dụng. Cũng có các profiler của bên thứ ba như AQtime, Intel VTune và AMD CodeAnalyst.

Có một số phương pháp profiling khác nhau:

* **Instrumentation (Đo lường bằng mã chèn):** Trình biên dịch chèn thêm mã tại mỗi lệnh gọi hàm để đếm số lần hàm được gọi và mất bao nhiêu thời gian.
* **Debugging (Gỡ lỗi):** Profiler chèn các điểm dừng gỡ lỗi (debug breakpoints) tạm thời tại mỗi hàm hoặc mỗi dòng mã.
* **Time-based sampling (Lấy mẫu dựa trên thời gian):** Profiler yêu cầu hệ điều hành tạo ra một ngắt (interrupt), ví dụ: cứ mỗi mili giây. Profiler đếm số lần ngắt xảy ra trong từng phần của chương trình. Điều này không yêu cầu sửa đổi chương trình đang được kiểm tra, nhưng kém tin cậy hơn.
* **Event-based sampling (Lấy mẫu dựa trên sự kiện):** Profiler yêu cầu CPU tạo ra ngắt tại các sự kiện nhất định, ví dụ như mỗi khi có một nghìn lần trượt bộ đệm (cache misses) xảy ra. Điều này giúp có thể xem phần nào của chương trình có nhiều cache miss nhất, dự đoán nhánh sai (branch mispredictions), ngoại lệ dấu phẩy động (floating point exceptions), v.v. Việc lấy mẫu dựa trên sự kiện yêu cầu một profiler dành riêng cho CPU. Đối với CPU Intel, hãy sử dụng Intel VTune, đối với CPU AMD, hãy sử dụng AMD CodeAnalyst.

Đáng buồn thay, các profiler thường không đáng tin cậy. Đôi khi chúng đưa ra kết quả gây hiểu lầm hoặc thất bại hoàn toàn do các vấn đề kỹ thuật.

Một số vấn đề phổ biến với profiler là:

* **Đo thời gian thô sơ (Coarse time measurement):** Nếu thời gian được đo với độ phân giải mili giây và các hàm quan trọng mất vài micro giây để thực thi thì các phép đo có thể trở nên không chính xác hoặc đơn giản là bằng 0.
* **Thời gian thực thi quá nhỏ hoặc quá dài:** Nếu chương trình đang kiểm tra hoàn thành trong một thời gian ngắn thì việc lấy mẫu tạo ra quá ít dữ liệu để phân tích. Nếu chương trình mất quá nhiều thời gian để thực thi thì profiler có thể lấy mẫu nhiều dữ liệu hơn mức nó có thể xử lý.
* **Chờ người dùng nhập liệu (Waiting for user input):** Nhiều chương trình dành phần lớn thời gian để chờ người dùng nhập liệu hoặc chờ tài nguyên mạng. Thời gian này được tính vào profile. Có thể cần phải sửa đổi chương trình để sử dụng tập dữ liệu thử nghiệm thay vì đầu vào của người dùng để giúp việc profiling khả thi.
* **Nhiễu từ các tiến trình khác (Interference from other processes):** Profiler không chỉ đo thời gian sử dụng trong chương trình đang kiểm tra mà còn đo thời gian được sử dụng bởi tất cả các tiến trình khác đang chạy trên cùng một máy tính, bao gồm cả chính profiler.
* **Địa chỉ hàm bị che khuất trong các chương trình được tối ưu hóa (Function addresses are obscured in optimized programs):** Profiler xác định bất kỳ điểm nóng nào trong chương trình bằng địa chỉ của chúng và cố gắng dịch các địa chỉ này thành tên hàm. Nhưng một chương trình được tối ưu hóa cao thường được tổ chức lại theo cách không có sự tương ứng rõ ràng giữa tên hàm và địa chỉ mã. Tên của các hàm nội tuyến (inlined functions) có thể hoàn toàn không hiển thị với profiler. Kết quả sẽ là các báo cáo gây hiểu lầm về việc hàm nào tốn nhiều thời gian nhất.
* **Sử dụng phiên bản gỡ lỗi của mã (Uses debug version of the code):** Một số profiler yêu cầu mã bạn đang kiểm tra chứa thông tin gỡ lỗi (debug information) để xác định các hàm hoặc dòng mã riêng lẻ. Phiên bản gỡ lỗi của mã không được tối ưu hóa.
* **Nhảy giữa các lõi CPU (Jumps between CPU cores):** Một tiến trình (process) hoặc luồng (thread) không nhất thiết ở lại cùng một lõi bộ xử lý trên các CPU đa lõi, nhưng bộ đếm sự kiện (event-counters) thì có. Điều này dẫn đến số lượng sự kiện vô nghĩa đối với các luồng nhảy giữa nhiều lõi CPU. Bạn có thể cần khóa (lock) một luồng vào một lõi CPU cụ thể bằng cách đặt `thread affinity mask`.
* **Khả năng tái lập kém (Poor reproducibility):** Độ trễ trong quá trình thực thi chương trình có thể do các sự kiện ngẫu nhiên không thể tái lập gây ra. Các sự kiện như chuyển đổi tác vụ (task switches) và thu gom rác (garbage collection) có thể xảy ra vào những thời điểm ngẫu nhiên và làm cho các phần của chương trình dường như mất nhiều thời gian hơn bình thường.

Có nhiều lựa chọn thay thế cho việc sử dụng profiler. Một giải pháp thay thế đơn giản là chạy chương trình trong trình gỡ lỗi (debugger) và nhấn `break` (tạm dừng) trong khi chương trình đang chạy. Nếu có một điểm nóng sử dụng 90% thời gian CPU thì có 90% cơ hội điểm break sẽ xảy ra trong điểm nóng này. Lặp lại quá trình break một vài lần có thể đủ để xác định một điểm nóng. Sử dụng ngăn xếp lệnh gọi (call stack) trong trình gỡ lỗi để xác định các trường hợp xung quanh điểm nóng.

Đôi khi, cách tốt nhất để xác định các nút thắt hiệu năng (performance bottlenecks) là đặt các công cụ đo đạc trực tiếp vào mã thay vì sử dụng một profiler làm sẵn. Điều này không giải quyết tất cả các vấn đề liên quan đến profiling, nhưng nó thường cho kết quả đáng tin cậy hơn. Nếu bạn không hài lòng với cách hoạt động của một profiler thì bạn có thể đưa các công cụ đo đạc mong muốn vào chính chương trình. Bạn có thể thêm các biến đếm để đếm số lần mỗi phần của chương trình được thực thi. Hơn nữa, bạn có thể đọc thời gian trước và sau mỗi phần quan trọng nhất của chương trình để đo xem mỗi phần mất bao nhiêu thời gian. Xem trang 157 để thảo luận thêm về phương pháp này.

Mã đo lường của bạn nên có các chỉ thị `#if` xung quanh nó để có thể vô hiệu hóa nó trong phiên bản cuối cùng của mã. Việc chèn các công cụ profiling của riêng bạn vào mã là một cách rất hữu ích để theo dõi hiệu năng trong quá trình phát triển chương trình.

Các phép đo thời gian có thể yêu cầu độ phân giải rất cao nếu khoảng thời gian ngắn. Trong Windows, bạn có thể sử dụng các hàm `GetTickCount` hoặc `QueryPerformanceCounter` cho độ phân giải mili giây. Có thể đạt được độ phân giải cao hơn nhiều bằng bộ đếm dấu thời gian (time stamp counter) trong CPU, bộ đếm này đếm theo tần số xung nhịp CPU (trong Windows: `__rdtsc()`).

Bộ đếm dấu thời gian trở nên không hợp lệ nếu một luồng nhảy giữa các lõi CPU khác nhau. Bạn có thể phải cố định luồng vào một lõi CPU cụ thể trong quá trình đo thời gian để tránh điều này. (Trong Windows, `SetThreadAffinityMask`, trong Linux, `sched_setaffinity`).

Chương trình nên được kiểm tra bằng một tập dữ liệu thử nghiệm thực tế. Dữ liệu thử nghiệm phải chứa một mức độ ngẫu nhiên điển hình để có được số lượng cache misses và branch mispredictions thực tế.

Khi các phần tốn thời gian nhất của chương trình đã được tìm thấy, thì điều quan trọng là chỉ tập trung nỗ lực tối ưu hóa vào các phần tốn thời gian. Các đoạn mã quan trọng có thể được kiểm tra và điều tra thêm bằng các phương pháp được mô tả ở trang 157.

Một profiler hữu ích nhất để tìm các vấn đề liên quan đến mã chuyên sâu về CPU. Nhưng nhiều chương trình sử dụng nhiều thời gian hơn để tải tệp hoặc truy cập cơ sở dữ liệu, mạng và các tài nguyên khác hơn là thực hiện các phép toán số học. Các yếu tố tốn thời gian phổ biến nhất được thảo luận trong các phần sau.

## 3.3 Cài đặt chương trình (Program installation)

Thời gian cần thiết để cài đặt một gói chương trình theo truyền thống không được coi là một vấn đề tối ưu hóa phần mềm. Nhưng nó chắc chắn là thứ có thể đánh cắp thời gian của người dùng. Không thể bỏ qua thời gian để cài đặt một gói phần mềm và làm cho nó hoạt động nếu mục tiêu của việc tối ưu hóa phần mềm là tiết kiệm thời gian cho người dùng. Với tính phức tạp cao của phần mềm hiện đại, không có gì lạ khi quá trình cài đặt mất hơn một giờ. Cũng không hiếm trường hợp người dùng phải cài đặt lại một gói phần mềm nhiều lần để tìm và giải quyết các vấn đề tương thích.

Các nhà phát triển phần mềm nên tính đến thời gian cài đặt và các vấn đề tương thích khi quyết định xem có nên xây dựng một gói phần mềm dựa trên một framework phức tạp đòi hỏi phải cài đặt nhiều tệp hay không.

Quá trình cài đặt phải luôn sử dụng các công cụ cài đặt được tiêu chuẩn hóa. Người dùng phải có khả năng chọn tất cả các tùy chọn cài đặt ngay lúc bắt đầu để phần còn lại của quá trình cài đặt có thể tiến hành mà không cần giám sát. Việc gỡ cài đặt (Uninstallation) cũng nên tiến hành theo cách chuẩn hóa.

## 3.4 Tự động cập nhật (Automatic updates)

Nhiều chương trình phần mềm tự động tải xuống các bản cập nhật qua Internet theo những khoảng thời gian đều đặn. Một số chương trình tìm kiếm bản cập nhật mỗi khi máy tính khởi động, ngay cả khi chương trình không bao giờ được sử dụng. Một máy tính cài đặt nhiều chương trình như vậy có thể mất vài phút để khởi động, điều này hoàn toàn lãng phí thời gian của người dùng. Các chương trình khác sử dụng thời gian tìm kiếm các bản cập nhật mỗi khi chương trình bắt đầu. Người dùng có thể không cần các bản cập nhật nếu phiên bản hiện tại đáp ứng nhu cầu của họ. Tìm kiếm bản cập nhật nên là tùy chọn và mặc định là tắt trừ khi có lý do bảo mật bắt buộc để cập nhật. Quá trình cập nhật nên chạy trong một luồng ưu tiên thấp (low priority thread) và chỉ khi chương trình thực sự được sử dụng. Không có chương trình nào nên để lại một tiến trình nền (background process) đang chạy khi nó không được sử dụng. Việc cài đặt các bản cập nhật chương trình đã tải xuống nên được hoãn lại cho đến khi chương trình bị tắt và dù sao cũng được khởi động lại.

Các bản cập nhật cho hệ điều hành có thể đặc biệt tốn thời gian. Đôi khi phải mất hàng giờ để cài đặt các bản cập nhật tự động cho hệ điều hành. Điều này rất có vấn đề vì những bản cập nhật tốn thời gian này có thể đến một cách khó lường vào những thời điểm bất tiện. Điều này có thể là một vấn đề rất lớn nếu người dùng phải tắt hoặc đăng xuất máy tính vì lý do bảo mật trước khi rời khỏi nơi làm việc của họ và hệ thống cấm người dùng tắt máy tính trong quá trình cập nhật.

## 3.5 Tải chương trình (Program loading)

Thông thường, tải một chương trình mất nhiều thời gian hơn là thực thi nó. Thời gian tải có thể cao đến mức khó chịu đối với các chương trình dựa trên các runtime frameworks lớn, mã trung gian (intermediate code), trình thông dịch (interpreters), trình biên dịch JIT, v.v., như thường thấy ở các chương trình được viết bằng Java, C#, Visual Basic, v.v.

Nhưng tải chương trình có thể là một yếu tố ngốn thời gian ngay cả đối với các chương trình được triển khai trong C++ đã biên dịch. Điều này thường xảy ra nếu chương trình sử dụng nhiều tệp DLL runtime (dynamically linked libraries hoặc shared objects), tệp tài nguyên, tệp cấu hình, tệp trợ giúp và cơ sở dữ liệu. Hệ điều hành có thể không tải tất cả các mô-đun của một chương trình lớn khi chương trình khởi động. Một số mô-đun có thể chỉ được tải khi cần thiết, hoặc chúng có thể được tráo đổi (swapped) sang đĩa cứng nếu kích thước RAM không đủ.

Người dùng mong đợi phản hồi ngay lập tức cho các hành động đơn giản như nhấn phím hoặc di chuyển chuột. Người dùng không thể chấp nhận được nếu một phản hồi như vậy bị trì hoãn trong vài giây vì hệ thống yêu cầu phải load các module hoặc tệp tài nguyên từ đĩa. Các ứng dụng ngốn bộ nhớ buộc hệ điều hành phải hoán đổi bộ nhớ (swap memory) vào ổ đĩa. Tráo đổi bộ nhớ là nguyên nhân thường xuyên gây ra thời gian phản hồi lâu một cách khó chấp nhận cho những thứ đơn giản như di chuyển chuột hoặc nhấn phím.

Tránh số lượng quá lớn tệp DLL, tệp cấu hình, tệp tài nguyên, tệp trợ giúp, v.v. rải rác trên ổ cứng. Một vài tệp, tốt nhất là trong cùng thư mục với tệp `.exe`, là có thể chấp nhận được.

## 3.6 Liên kết động và mã không phụ thuộc vị trí (Dynamic linking and position-independent code)

Các thư viện hàm có thể được triển khai dưới dạng thư viện liên kết tĩnh (static link libraries `*.lib`, `*.a`) hoặc thư viện liên kết động (dynamic link libraries), còn được gọi là đối tượng chia sẻ (shared objects `*.dll`, `*.so`). Có một số yếu tố có thể làm cho thư viện liên kết động chậm hơn thư viện liên kết tĩnh. Những yếu tố này được giải thích chi tiết ở trang 149 bên dưới.

Mã không phụ thuộc vị trí (Position-independent code) được sử dụng trong các đối tượng chia sẻ trong các hệ thống giống Unix. Các hệ thống Mac thường sử dụng mã không phụ thuộc vị trí ở mọi nơi theo mặc định. Mã không phụ thuộc vị trí kém hiệu quả, đặc biệt là ở chế độ 32-bit, vì những lý do được giải thích ở trang 149 bên dưới.

## 3.7 Truy cập tệp (File access)

Đọc hoặc ghi tệp trên đĩa cứng thường mất nhiều thời gian hơn so với xử lý dữ liệu trong tệp, đặc biệt nếu người dùng có trình quét vi-rút quét tất cả các tệp khi truy cập.

Truy cập tệp tuần tự theo chiều tiến (Sequential forward access) nhanh hơn truy cập ngẫu nhiên (random access). Đọc hoặc ghi khối dữ liệu lớn nhanh hơn đọc hoặc ghi một bit dữ liệu nhỏ tại một thời điểm. Không đọc hoặc ghi ít hơn một vài kilobyte tại một thời điểm.

Bạn có thể tạo bản sao (mirror) của toàn bộ tệp trong bộ đệm bộ nhớ (memory buffer) và đọc hoặc ghi nó trong một thao tác duy nhất thay vì đọc hoặc ghi các bit nhỏ theo cách không tuần tự.

Truy cập một tệp đã được truy cập gần đây thường nhanh hơn nhiều so với việc truy cập nó lần đầu tiên. Điều này là do tệp đã được sao chép vào bộ nhớ đệm của đĩa (disk cache).

Các tệp trên ổ đĩa từ xa hoặc phương tiện lưu trữ rời như đĩa mềm và thẻ nhớ USB có thể không được lưu vào bộ đệm (cached). Điều này có thể gây ra những hậu quả khá nghiêm trọng. Tôi đã từng làm một chương trình Windows tạo một tệp bằng cách gọi `WritePrivateProfileString`, thao tác này mở và đóng tệp cho mỗi dòng được ghi. Điều này hoạt động đủ nhanh trên đĩa cứng nhờ disk caching, nhưng phải mất vài phút để ghi tệp vào đĩa mềm.

Một tệp lớn chứa dữ liệu số sẽ nhỏ gọn và hiệu quả hơn nếu dữ liệu được lưu trữ ở dạng nhị phân (binary) thay vì dạng ASCII. Nhược điểm của lưu trữ dữ liệu nhị phân là con người không thể đọc được và không dễ dàng port (chuyển) sang các hệ thống sử dụng kiểu lưu trữ `big-endian`.

Tối ưu hóa khả năng truy cập tệp quan trọng hơn tối ưu hóa việc sử dụng CPU trong các chương trình có nhiều thao tác nhập/xuất tệp (I/O). Việc đặt truy cập tệp vào một luồng riêng biệt (separate thread) có thể mang lại lợi thế nếu bộ xử lý có việc khác để làm trong khi chờ thao tác đĩa hoàn thành.

## 3.8 Cơ sở dữ liệu hệ thống (System database)

Có thể mất vài giây để truy cập cơ sở dữ liệu hệ thống (system database) trong Windows. Sẽ hiệu quả hơn nếu lưu trữ thông tin dành riêng cho ứng dụng trong một tệp riêng biệt thay vì trong cơ sở dữ liệu đăng ký lớn (registration database) trong hệ thống Windows. Lưu ý rằng dù sao thì hệ thống vẫn có thể lưu trữ thông tin vào cơ sở dữ liệu nếu bạn đang sử dụng các hàm như `GetPrivateProfileString` và `WritePrivateProfileString` để đọc và ghi các tệp cấu hình (tệp `*.ini`).

## 3.9 Các cơ sở dữ liệu khác (Other databases)

Nhiều ứng dụng phần mềm sử dụng cơ sở dữ liệu để lưu trữ dữ liệu người dùng. Một cơ sở dữ liệu có thể tiêu thụ nhiều thời gian CPU, RAM và không gian ổ đĩa. Có thể thay thế cơ sở dữ liệu bằng một tệp dữ liệu cũ thông thường (plain old data file) trong các trường hợp đơn giản. Các truy vấn cơ sở dữ liệu thường có thể được tối ưu hóa bằng cách sử dụng chỉ mục (indexes), thao tác với tập hợp (sets) thay vì vòng lặp, v.v. Tối ưu hóa truy vấn cơ sở dữ liệu nằm ngoài phạm vi của tài liệu này, nhưng bạn nên biết rằng thường có thể đạt được nhiều lợi ích bằng cách tối ưu hóa truy cập cơ sở dữ liệu.

## 3.10 Đồ họa (Graphics)

Giao diện người dùng đồ họa có thể sử dụng nhiều tài nguyên máy tính. Thông thường, một framework đồ họa cụ thể được sử dụng. Hệ điều hành có thể cung cấp framework như vậy trong API của nó. Trong một số trường hợp, có thêm một lớp framework đồ họa của bên thứ ba ở giữa API hệ điều hành và phần mềm ứng dụng. Một framework bổ sung như vậy có thể tiêu thụ rất nhiều tài nguyên phụ.

Mỗi thao tác đồ họa trong phần mềm ứng dụng được thực hiện dưới dạng lệnh gọi hàm tới thư viện đồ họa hoặc hàm API, hàm này sau đó gọi trình điều khiển thiết bị (device driver). Lệnh gọi tới hàm đồ họa tốn thời gian vì nó có thể đi qua nhiều lớp và cần chuyển sang chế độ bảo vệ (protected mode) rồi quay lại. Rõ ràng, việc thực hiện một lệnh gọi duy nhất tới một hàm đồ họa vẽ toàn bộ đa giác hoặc ảnh bitmap sẽ hiệu quả hơn việc vẽ từng điểm ảnh (pixel) hoặc đường thẳng riêng biệt thông qua nhiều lệnh gọi hàm.

Việc tính toán các đối tượng đồ họa trong game máy tính và hoạt hình tất nhiên cũng ngốn thời gian, đặc biệt nếu không có thiết bị xử lý đồ họa (GPU).

Nhiều thư viện hàm đồ họa và driver khác nhau có sự khác biệt rất lớn về hiệu suất. Tôi không có khuyến nghị cụ thể nào về việc cái nào là tốt nhất.

## 3.11 Các tài nguyên hệ thống khác (Other system resources)

Việc ghi vào máy in hoặc thiết bị khác tốt nhất nên được thực hiện theo các khối dữ liệu lớn thay vì từng mảnh nhỏ một vì mỗi lệnh gọi tới trình điều khiển (driver) liên quan đến phần phụ phí (overhead) khi chuyển sang chế độ bảo vệ và quay trở lại.

Truy cập các thiết bị hệ thống và sử dụng các tiện ích nâng cao của hệ điều hành có thể tốn thời gian vì nó có thể bao gồm việc tải nhiều driver, tệp cấu hình và các mô-đun hệ thống.

## 3.12 Truy cập mạng (Network access)

Một số chương trình ứng dụng sử dụng internet hoặc mạng nội bộ để tự động cập nhật, sử dụng tệp trợ giúp từ xa, truy cập cơ sở dữ liệu, v.v. Vấn đề ở đây là không thể kiểm soát được thời gian truy cập. Truy cập mạng có thể nhanh trong một thiết lập thử nghiệm đơn giản nhưng lại chậm hoặc mất hoàn toàn trong tình huống sử dụng mà mạng bị quá tải hoặc người dùng ở xa máy chủ.

Những vấn đề này nên được tính đến khi quyết định lưu trữ tệp trợ giúp và các tài nguyên khác tại máy trạm hay từ xa. Nếu cần cập nhật thường xuyên, tối ưu nhất là tạo bản sao (mirror) dữ liệu từ xa tại máy nội bộ.

Việc truy cập cơ sở dữ liệu từ xa thường yêu cầu đăng nhập bằng mật khẩu. Quá trình đăng nhập được biết đến là một kẻ tiêu tốn thời gian gây phiền nhiễu cho nhiều người dùng phần mềm làm việc chăm chỉ. Trong một số trường hợp, quá trình đăng nhập có thể mất hơn một phút nếu mạng hoặc cơ sở dữ liệu tải quá nặng.

## 3.13 Truy cập bộ nhớ (Memory access)

Việc truy xuất dữ liệu từ bộ nhớ RAM có thể mất một thời gian khá dài so với thời gian để thực hiện các phép tính trên dữ liệu. Đây là lý do tại sao tất cả các máy tính hiện đại đều có bộ đệm bộ nhớ (memory caches). Thông thường, có một bộ đệm dữ liệu (data cache) cấp 1 từ 8 - 64 Kbytes và một bộ đệm cấp 2 từ 256 Kbytes đến 2 Mbytes. Có thể cũng có thêm một bộ đệm cấp 3.

Nếu tổng kích thước của tất cả dữ liệu trong một chương trình lớn hơn cache cấp 2 và dữ liệu bị phân tán khắp nơi trong bộ nhớ hoặc được truy cập theo cách không tuần tự, thì rất có khả năng truy cập bộ nhớ là nguyên nhân làm mất nhiều thời gian nhất trong chương trình. Việc đọc hoặc ghi vào một biến trong bộ nhớ chỉ mất 2-3 chu kỳ xung nhịp (clock cycles) nếu nó được cache, nhưng sẽ tốn vài trăm chu kỳ xung nhịp nếu nó không được cache. Xem trang 26 về lưu trữ dữ liệu và trang 88 về memory caching.

## 3.14 Chuyển đổi ngữ cảnh (Context switches)

Chuyển đổi ngữ cảnh (context switch) là việc chuyển đổi giữa các tác vụ (tasks) khác nhau trong môi trường đa nhiệm (multitasking), giữa các luồng (threads) khác nhau trong một chương trình đa luồng, hoặc giữa các phần khác nhau của một chương trình lớn. Việc chuyển đổi ngữ cảnh thường xuyên có thể làm giảm hiệu suất vì nội dung của bộ nhớ đệm dữ liệu, bộ nhớ đệm mã, bộ đệm đích phân nhánh (branch target buffer), lịch sử mẫu rẽ nhánh (branch pattern history), v.v. có thể phải được làm mới.

Việc chuyển đổi ngữ cảnh diễn ra thường xuyên hơn nếu các lát cắt thời gian (time slices) được phân bổ cho mỗi tác vụ hoặc luồng nhỏ hơn. Độ dài của lát cắt thời gian được xác định bởi hệ điều hành, không phải bởi chương trình ứng dụng.

Số lần chuyển đổi ngữ cảnh nhỏ hơn trong một máy tính có nhiều CPU hoặc CPU có nhiều lõi (multiple cores).

## 3.15 Các chuỗi phụ thuộc (Dependency chains)

Các bộ vi xử lý hiện đại có thể thực hiện thực thi ngoài luồng (out-of-order execution). Điều này có nghĩa là nếu một đoạn phần mềm chỉ định việc tính toán A và sau đó là B, và việc tính toán A bị chậm, thì vi xử lý có thể bắt đầu tính toán B trước khi tính toán A kết thúc. Rõ ràng, điều này chỉ có thể xảy ra nếu giá trị của A không cần thiết cho việc tính toán B.

Để tận dụng việc thực thi out-of-order, bạn phải tránh các chuỗi phụ thuộc dài. Chuỗi phụ thuộc là một chuỗi các tính toán, trong đó mỗi phép tính phụ thuộc vào kết quả của phép tính trước đó. Điều này ngăn cản CPU thực hiện nhiều tính toán đồng thời hoặc không theo thứ tự. Xem trang 105 để biết các ví dụ về cách phá vỡ (break) một chuỗi phụ thuộc.

## 3.16 Thông lượng của khối thực thi (Execution unit throughput)

Có một sự khác biệt quan trọng giữa độ trễ (latency) và thông lượng (throughput) của một khối thực thi. Ví dụ, có thể mất 3 - 5 chu kỳ xung nhịp để thực hiện một phép cộng số thực dấu phẩy động trên một CPU hiện đại. Nhưng bạn có thể bắt đầu một phép cộng dấu phẩy động mới mỗi chu kỳ xung nhịp. Điều này có nghĩa là nếu mỗi phép cộng phụ thuộc vào kết quả của phép cộng trước đó, thì bạn sẽ chỉ có một phép cộng sau mỗi ba chu kỳ xung nhịp. Nhưng nếu tất cả các phép cộng đều độc lập, thì bạn có thể có một phép cộng cho mỗi chu kỳ xung nhịp.

Hiệu năng cao nhất có thể đạt được trong một chương trình chuyên sâu về tính toán đạt được khi không có yếu tố tốn thời gian nào được đề cập trong các phần trên chiếm ưu thế và không có chuỗi phụ thuộc dài nào. Trong trường hợp này, hiệu năng bị giới hạn bởi thông lượng của các khối thực thi chứ không phải bởi độ trễ hoặc khả năng truy cập bộ nhớ.

Lõi thực thi của các bộ vi xử lý hiện đại được phân tách thành một số đơn vị thực thi (execution units). Điển hình như, có hai hoặc nhiều đơn vị số nguyên, một hoặc hai đơn vị cộng dấu phẩy động, và một số đơn vị xử lý bộ nhớ. Các đơn vị thực thi này có thể hoạt động song song với nhau. Do đó, có thể thực hiện một phép cộng số nguyên, một phép nhân số nguyên, một phép cộng dấu phẩy động, và xử lý các phép toán bộ nhớ tại cùng một thời điểm. Mức hiệu suất này là khó đạt được nhưng không phải là không thể.
