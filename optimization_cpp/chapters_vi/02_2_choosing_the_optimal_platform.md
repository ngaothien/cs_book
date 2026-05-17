# 2 Chọn nền tảng tối ưu (Choosing the optimal platform)

## 2.1 Chọn nền tảng phần cứng (Choice of hardware platform)

Việc chọn lựa nền tảng phần cứng không còn quan trọng như trước đây. Sự khác biệt giữa bộ vi xử lý RISC và CISC, giữa máy tính cá nhân (PC) và máy tính lớn (mainframe), và giữa bộ vi xử lý đơn giản và bộ vi xử lý vector (vector processors) đang ngày càng trở nên mờ nhạt khi các bộ vi xử lý PC tiêu chuẩn với tập lệnh CISC đã có lõi RISC, các lệnh xử lý vector, kiến trúc đa lõi (multiple cores) và tốc độ xử lý vượt xa các máy tính lớn của ngày hôm qua.

Ngày nay, việc lựa chọn nền tảng phần cứng cho một tác vụ nhất định thường được quyết định bởi các cân nhắc như giá cả, khả năng tương thích, nguồn thay thế, và tính sẵn có của các công cụ phát triển tốt, chứ không chỉ dựa vào sức mạnh xử lý. Kết nối nhiều PC tiêu chuẩn trong một mạng có thể vừa rẻ hơn vừa hiệu quả hơn so với việc đầu tư vào một máy tính lớn. Các siêu máy tính (supercomputers) lớn với khả năng xử lý vector song song hàng loạt vẫn có chỗ đứng trong điện toán khoa học, nhưng với hầu hết các mục đích, bộ vi xử lý PC tiêu chuẩn được ưa chuộng hơn nhờ tỷ lệ hiệu năng/giá thành vượt trội.

Tập lệnh CISC (được gọi là x86) của các bộ vi xử lý PC tiêu chuẩn không phải là tối ưu từ góc độ công nghệ. Tập lệnh này được duy trì vì lý do tương thích ngược với một dòng phần mềm có từ khoảng năm 1980, khi bộ nhớ RAM và không gian đĩa là những tài nguyên khan hiếm. Tuy nhiên, tập lệnh CISC thực sự tốt hơn so với danh tiếng của nó. Sự nhỏ gọn của mã (code) làm cho việc lưu đệm (caching) trở nên hiệu quả hơn trong thời đại ngày nay khi kích thước bộ nhớ đệm (cache) là một tài nguyên giới hạn. Tập lệnh CISC trên thực tế có thể tốt hơn RISC trong các tình huống mà việc lưu đệm mã (code caching) là cực kỳ quan trọng. Vấn đề tồi tệ nhất của tập lệnh x86 là sự khan hiếm thanh ghi (registers). Vấn đề này đã được giảm bớt trong phần mở rộng 64-bit của tập lệnh x86, nơi số lượng thanh ghi đã được tăng gấp đôi.

Các máy khách mỏng (thin clients) phụ thuộc vào tài nguyên mạng không được khuyến nghị cho các ứng dụng quan trọng vì thời gian phản hồi của tài nguyên mạng không thể kiểm soát được.

Các thiết bị cầm tay nhỏ đang trở nên phổ biến hơn và được sử dụng cho ngày càng nhiều mục đích như email và duyệt web vốn trước đây cần đến PC. Tương tự, chúng ta đang thấy ngày càng nhiều thiết bị và máy móc có chứa vi điều khiển nhúng (embedded microcontrollers). Tôi không đưa ra khuyến nghị cụ thể nào về nền tảng và hệ điều hành nào là hiệu quả nhất cho các ứng dụng đó, nhưng điều quan trọng cần nhận ra là các thiết bị như vậy thường có ít bộ nhớ và sức mạnh tính toán hơn nhiều so với PC. Do đó, việc tiết kiệm tài nguyên trên các hệ thống như vậy thậm chí còn quan trọng hơn so với trên nền tảng PC. Tuy nhiên, với một thiết kế phần mềm được tối ưu hóa tốt, bạn có thể đạt được hiệu năng tốt cho nhiều ứng dụng ngay cả trên các thiết bị nhỏ như vậy, như được thảo luận ở trang 162.

Tài liệu này dựa trên nền tảng PC tiêu chuẩn với bộ vi xử lý Intel, AMD hoặc VIA và hệ điều hành Windows, Linux, BSD hoặc Mac chạy ở chế độ 32-bit hoặc 64-bit. Phần lớn lời khuyên được đưa ra ở đây cũng có thể áp dụng cho các nền tảng khác, nhưng các ví dụ mới chỉ được thử nghiệm trên nền tảng PC.

**Bộ tăng tốc đồ họa (Graphics accelerators)**

Việc lựa chọn nền tảng rõ ràng bị ảnh hưởng bởi yêu cầu của tác vụ hiện tại. Ví dụ, một ứng dụng đồ họa nặng tốt nhất nên được triển khai trên nền tảng có bộ đồng xử lý đồ họa (graphics coprocessor) hoặc card tăng tốc đồ họa (graphics accelerator card). Một số hệ thống cũng có bộ xử lý vật lý chuyên dụng (physics processor) để tính toán chuyển động vật lý của các đối tượng trong một trò chơi máy tính hoặc hoạt hình.

Trong một số trường hợp, có thể sử dụng sức mạnh xử lý cao của các bộ vi xử lý trên card tăng tốc đồ họa cho các mục đích khác ngoài việc kết xuất đồ họa (rendering graphics) trên màn hình. Tuy nhiên, các ứng dụng như vậy phụ thuộc rất nhiều vào hệ thống và do đó không được khuyến khích nếu tính di động (portability) là quan trọng. Tài liệu này không đề cập đến bộ xử lý đồ họa.

**Thiết bị logic lập trình được (Programmable logic devices)**

Thiết bị logic lập trình được là một con chip có thể được lập trình bằng một ngôn ngữ định nghĩa phần cứng (hardware definition language), chẳng hạn như VHDL hoặc Verilog. Các thiết bị phổ biến là CPLD và FPGA. Điểm khác biệt giữa ngôn ngữ lập trình phần mềm, ví dụ như C++, và ngôn ngữ định nghĩa phần cứng là ngôn ngữ lập trình phần mềm định nghĩa một thuật toán gồm các lệnh tuần tự, trong khi ngôn ngữ định nghĩa phần cứng định nghĩa các mạch phần cứng bao gồm các khối xây dựng kỹ thuật số như cổng (gates), flip-flop, bộ dồn kênh (multiplexers), khối số học (arithmetic units), v.v. và các dây kết nối chúng. Ngôn ngữ định nghĩa phần cứng vốn mang tính song song (inherently parallel) vì nó định nghĩa các kết nối điện chứ không phải là chuỗi các thao tác.

Một thao tác kỹ thuật số phức tạp thường có thể được thực thi nhanh hơn trong một thiết bị logic lập trình được so với trong bộ vi xử lý, vì phần cứng có thể được nối dây cho một mục đích cụ thể.

Có thể triển khai một bộ vi xử lý trong FPGA dưới dạng cái gọi là bộ xử lý mềm (soft processor). Một bộ xử lý mềm như vậy chậm hơn nhiều so với bộ vi xử lý chuyên dụng và do đó tự bản thân nó không có nhiều lợi thế. Nhưng một giải pháp trong đó bộ xử lý mềm kích hoạt các lệnh dành riêng cho ứng dụng (application-specific instructions) quan trọng được viết bằng ngôn ngữ định nghĩa phần cứng trong cùng một con chip có thể là một giải pháp rất hiệu quả trong một số trường hợp. Một giải pháp mạnh mẽ hơn nữa là sự kết hợp của lõi vi xử lý chuyên dụng và FPGA trong cùng một con chip. Những giải pháp lai (hybrid solutions) như vậy hiện đang được sử dụng trong một số hệ thống nhúng.

Một cái nhìn vào quả cầu pha lê của tôi tiết lộ rằng các giải pháp tương tự có thể một ngày nào đó sẽ được áp dụng cho các bộ vi xử lý PC. Chương trình ứng dụng sẽ có khả năng định nghĩa các lệnh chuyên biệt cho ứng dụng có thể được code bằng ngôn ngữ định nghĩa phần cứng. Một bộ xử lý như vậy sẽ có thêm một bộ nhớ đệm (cache) cho mã định nghĩa phần cứng, bên cạnh bộ nhớ đệm mã (code cache) và bộ nhớ đệm dữ liệu (data cache).

## 2.2 Lựa chọn bộ vi xử lý (Choice of microprocessor)

Hiệu năng đo lường (benchmark performance) của các thương hiệu vi xử lý cạnh tranh rất giống nhau nhờ sự cạnh tranh khốc liệt. Các bộ vi xử lý đa lõi (multiple cores) có lợi thế cho các ứng dụng có thể chia thành nhiều luồng (threads) chạy song song. Các vi xử lý hạng nhẹ nhỏ với mức tiêu thụ điện năng thấp thực ra khá mạnh mẽ và có thể đủ dùng cho các ứng dụng ít chuyên sâu hơn.

Một số hệ thống có thiết bị xử lý đồ họa (graphics processing unit - GPU), nằm trên card đồ họa hoặc tích hợp trong chip CPU. Các thiết bị như vậy có thể được sử dụng làm bộ đồng xử lý (coprocessors) để đảm nhận một số tính toán đồ họa nặng. Trong một số trường hợp, có thể tận dụng sức mạnh tính toán của GPU cho các mục đích khác ngoài dự định ban đầu. Một số hệ thống cũng có thiết bị xử lý vật lý (physics processing unit) dùng để tính toán chuyển động của đối tượng trong game. Bộ đồng xử lý như vậy cũng có thể được dùng cho các mục đích khác. Việc sử dụng các bộ đồng xử lý nằm ngoài phạm vi của tài liệu này.

## 2.3 Lựa chọn hệ điều hành (Choice of operating system)

Tất cả các bộ vi xử lý mới hơn trong họ x86 đều có thể chạy ở cả chế độ 16-bit, 32-bit và 64-bit.

Chế độ 16-bit được dùng trong các hệ điều hành cũ DOS và Windows 3.x. Những hệ thống này sử dụng phân đoạn bộ nhớ (segmentation) nếu dung lượng chương trình hoặc dữ liệu vượt quá 64 kbytes. Điều này khá kém hiệu quả. Các bộ vi xử lý hiện đại không được tối ưu hóa cho chế độ 16-bit và một số hệ điều hành không tương thích ngược với các chương trình 16-bit. Không khuyến nghị làm các chương trình 16-bit, ngoại trừ các hệ thống nhúng nhỏ.

Ngày nay (2013), cả hệ điều hành 32-bit và 64-bit đều phổ biến, và không có sự khác biệt lớn về hiệu năng giữa hai hệ thống. Không có chiến dịch marketing rầm rộ nào cho phần mềm 64-bit, nhưng khá chắc chắn rằng các hệ thống 64-bit sẽ thống trị trong tương lai.

Các hệ thống 64-bit có thể cải thiện hiệu năng 5-10% cho một số ứng dụng tốn nhiều CPU với nhiều lời gọi hàm. Nếu nút thắt cổ chai (bottleneck) nằm ở chỗ khác thì không có sự khác biệt về hiệu năng giữa hệ thống 32-bit và 64-bit. Các ứng dụng sử dụng lượng bộ nhớ lớn sẽ được hưởng lợi từ không gian địa chỉ lớn hơn của hệ thống 64-bit.

Một nhà phát triển phần mềm có thể chọn tạo phần mềm ngốn bộ nhớ bằng hai phiên bản. Một phiên bản 32-bit vì mục đích tương thích với các hệ thống hiện tại và một phiên bản 64-bit để có hiệu năng tốt nhất.

Các hệ điều hành Windows và Linux mang lại hiệu năng gần như giống hệt nhau cho phần mềm 32-bit vì hai hệ điều hành sử dụng cùng một quy ước gọi hàm (calling conventions). FreeBSD và Open BSD giống với Linux trong hầu hết các khía cạnh liên quan đến tối ưu hóa phần mềm. Mọi thứ nói ở đây về Linux cũng áp dụng cho hệ thống BSD.

Hệ điều hành Mac OS X nền tảng Intel dựa trên BSD, nhưng trình biên dịch mặc định sử dụng mã không phụ thuộc vị trí (position-independent code) và liên kết trễ (lazy binding), điều này làm cho nó kém hiệu quả hơn. Hiệu năng có thể được cải thiện bằng cách sử dụng liên kết tĩnh (static linking) và không sử dụng mã không phụ thuộc vị trí (tùy chọn `-fno-pic`).

Hệ thống 64 bit có một số ưu điểm so với hệ thống 32 bit:

* Số lượng thanh ghi tăng gấp đôi. Điều này giúp có thể lưu trữ dữ liệu trung gian và biến cục bộ trong thanh ghi thay vì trong bộ nhớ.
* Tham số hàm được chuyển qua thanh ghi thay vì qua ngăn xếp (stack). Điều này làm cho lời gọi hàm hiệu quả hơn.
* Kích thước thanh ghi số nguyên được mở rộng lên 64 bit. Đây chỉ là một lợi thế trong các ứng dụng có thể tận dụng số nguyên 64-bit.
* Việc cấp phát (allocation) và thu hồi (deallocation) các khối bộ nhớ lớn sẽ hiệu quả hơn.
* Tập lệnh SSE2 được hỗ trợ trên tất cả các CPU và hệ điều hành 64-bit.
* Tập lệnh 64 bit hỗ trợ định địa chỉ tương đối tự thân (self-relative addressing) của dữ liệu. Điều này làm cho mã không phụ thuộc vị trí trở nên hiệu quả hơn.

Hệ thống 64 bit có những nhược điểm sau so với hệ thống 32 bit:

* Con trỏ, tham chiếu và các entry trên ngăn xếp sử dụng 64 bit thay vì 32 bit. Điều này làm cho việc lưu đệm dữ liệu (data caching) kém hiệu quả hơn.
* Truy cập vào các mảng tĩnh (static) hoặc toàn cục (global arrays) yêu cầu thêm vài lệnh để tính toán địa chỉ trong chế độ 64 bit nếu `image base` không được đảm bảo nhỏ hơn 2^31. Chi phí tăng thêm này thấy rõ trong các chương trình 64 bit của Windows và Mac nhưng hiếm khi có trong Linux.
* Việc tính toán địa chỉ phức tạp hơn trong mô hình bộ nhớ lớn, nơi kích thước kết hợp của mã và dữ liệu có thể vượt quá 2 Gbytes. Tuy nhiên, mô hình bộ nhớ lớn này hầu như không bao giờ được sử dụng.
* Một số lệnh dài hơn một byte trong chế độ 64 bit so với chế độ 32 bit.
* Một số trình biên dịch 64-bit kém hơn so với phiên bản 32-bit tương ứng.

Nhìn chung, bạn có thể kỳ vọng các chương trình 64-bit chạy nhanh hơn một chút so với các chương trình 32-bit nếu có nhiều lời gọi hàm, nếu có nhiều cấp phát khối bộ nhớ lớn, hoặc nếu chương trình có thể tận dụng các tính toán số nguyên 64-bit. Cần phải sử dụng hệ thống 64-bit nếu chương trình sử dụng hơn 2 gigabyte dữ liệu.

Sự tương đồng giữa các hệ điều hành biến mất khi chạy ở chế độ 64-bit vì các quy ước gọi hàm khác nhau. Windows 64-bit chỉ cho phép truyền bốn tham số hàm qua thanh ghi, trong khi Linux, BSD và Mac 64-bit cho phép truyền tối đa mười bốn tham số qua thanh ghi (6 số nguyên và 8 số thực dấu phẩy động).
Ngoài ra còn có các chi tiết khác giúp cho việc gọi hàm hiệu quả hơn trên Linux 64-bit so với Windows 64-bit (Xem trang 50 và tài liệu 5: "Calling conventions for different C++ compilers and operating systems"). Một ứng dụng với nhiều lời gọi hàm có thể chạy nhanh hơn một chút trên Linux 64-bit so với Windows 64-bit. Bất lợi của Windows 64-bit có thể được giảm nhẹ bằng cách sử dụng `inline` hoặc `static` cho các hàm quan trọng hoặc bằng cách dùng một trình biên dịch có thể thực hiện toàn bộ tối ưu hóa chương trình (whole program optimization).

## 2.4 Lựa chọn ngôn ngữ lập trình (Choice of programming language)

Trước khi bắt đầu một dự án phần mềm mới, việc quyết định ngôn ngữ lập trình nào phù hợp nhất cho dự án là điều quan trọng. Ngôn ngữ bậc thấp (Low-level languages) rất tốt để tối ưu hóa tốc độ thực thi hoặc kích thước chương trình, trong khi ngôn ngữ bậc cao (high-level languages) thì tốt để tạo ra code rõ ràng, có cấu trúc tốt và giúp phát triển nhanh chóng, dễ dàng giao diện người dùng và giao tiếp với mạng, cơ sở dữ liệu, v.v.

Hiệu quả của ứng dụng cuối cùng phụ thuộc vào cách thức triển khai của ngôn ngữ lập trình. Hiệu quả cao nhất đạt được khi mã được biên dịch (compiled) và phân phối dưới dạng mã nhị phân thực thi (binary executable code). Hầu hết các triển khai của C++, Pascal và Fortran đều dựa trên trình biên dịch (compilers).

Một số ngôn ngữ lập trình khác được triển khai dưới dạng thông dịch (interpretation). Mã chương trình được phân phối y nguyên và thông dịch từng dòng khi nó được chạy. Các ví dụ bao gồm JavaScript, PHP, ASP và UNIX shell script. Mã thông dịch rất kém hiệu quả vì phần thân của vòng lặp bị thông dịch đi thông dịch lại cho mỗi lần lặp của vòng lặp.

Một số triển khai sử dụng biên dịch đúng lúc (just-in-time compilation). Mã chương trình được phân phối và lưu trữ dưới dạng ban đầu, và được biên dịch vào thời điểm nó được thực thi. Một ví dụ là Perl.

Nhiều ngôn ngữ lập trình hiện đại sử dụng mã trung gian (intermediate code / byte code). Mã nguồn (source code) được biên dịch thành một mã trung gian, mã này chính là thứ được phân phối. Mã trung gian không thể thực thi y nguyên, mà phải trải qua bước thứ hai là thông dịch hoặc biên dịch trước khi có thể chạy. Một số cách triển khai của Java dựa trên một trình thông dịch (interpreter) để thông dịch mã trung gian bằng cách giả lập cái gọi là máy ảo Java (Java virtual machine). Các máy Java tốt nhất sử dụng biên dịch `just-in-time` (JIT) đối với những phần được dùng nhiều nhất trong mã. C#, managed C++ và các ngôn ngữ khác trong framework .NET của Microsoft dựa trên quá trình biên dịch JIT của một mã trung gian.

Lý do sử dụng mã trung gian là vì nó nhằm mục đích độc lập với nền tảng (platform-independent) và nhỏ gọn. Nhược điểm lớn nhất của việc sử dụng mã trung gian là người dùng phải cài đặt một khung runtime lớn (runtime framework) để thông dịch hoặc biên dịch mã trung gian. Framework này thường tiêu tốn nhiều tài nguyên hơn bản thân mã code.

Một nhược điểm khác của mã trung gian là nó thêm một mức trừu tượng (abstraction) khiến việc tối ưu hóa chi tiết trở nên khó khăn hơn. Mặt khác, một trình biên dịch JIT có thể tối ưu hóa đặc biệt cho CPU mà nó đang chạy, trong khi việc tối ưu hóa cụ thể theo CPU lại phức tạp hơn nhiều đối với mã đã được biên dịch trước (precompiled code).

Lịch sử của các ngôn ngữ lập trình và các triển khai của chúng cho thấy một đường ngoằn ngoèo phản ánh những cân nhắc mâu thuẫn giữa tính hiệu quả, tính di động (portability) và thời gian phát triển. Ví dụ, những PC đầu tiên có trình thông dịch cho Basic. Trình biên dịch cho Basic sớm ra mắt vì phiên bản Basic thông dịch quá chậm. Ngày nay, phiên bản Basic phổ biến nhất là Visual Basic .NET, được triển khai bằng mã trung gian và biên dịch JIT. Một số phiên bản Pascal đời đầu sử dụng mã trung gian giống với cách Java đang dùng ngày nay. Nhưng ngôn ngữ này đã trở nên đặc biệt phổ biến khi có một trình biên dịch đích thực ra mắt.

Qua cuộc thảo luận này, có thể thấy rõ rằng việc lựa chọn ngôn ngữ lập trình là một sự thỏa hiệp giữa tính hiệu quả, tính di động và thời gian phát triển. Các ngôn ngữ thông dịch là hoàn toàn không được cân nhắc khi hiệu suất là yếu tố quan trọng. Một ngôn ngữ dựa trên mã trung gian và biên dịch JIT có thể là một sự thỏa hiệp khả thi khi tính di động và tính dễ phát triển quan trọng hơn tốc độ. Điều này bao gồm các ngôn ngữ như C#, Visual Basic .NET và các phiên bản Java tốt nhất. Tuy nhiên, các ngôn ngữ này có nhược điểm là khung runtime quá lớn phải được tải mỗi khi chương trình chạy. Thời gian tải framework và biên dịch chương trình thường dài hơn nhiều so với thời gian chạy chương trình, và runtime framework có thể sử dụng nhiều tài nguyên hơn chính chương trình khi nó chạy. Các chương trình sử dụng loại framework như vậy đôi khi có thời gian phản hồi chậm chạp đến mức khó chấp nhận cho cả những tác vụ đơn giản như bấm nút hay di chuột. Framework .NET chắc chắn nên bị tránh né khi tốc độ là yếu tố then chốt.

Sự thực thi nhanh nhất không còn nghi ngờ gì nữa thuộc về một mã đã được biên dịch hoàn toàn (fully compiled code). Các ngôn ngữ biên dịch bao gồm C, C++, D, Pascal, Fortran và một số ngôn ngữ ít phổ biến khác. Tôi ưu tiên C++ vì một số lý do. C++ được hỗ trợ bởi một số trình biên dịch rất tốt và các thư viện hàm đã được tối ưu hóa. C++ là một ngôn ngữ bậc cao tiên tiến với vô vàn tính năng hiện đại hiếm có ở các ngôn ngữ khác. Nhưng ngôn ngữ C++ cũng bao gồm một tập hợp con là ngôn ngữ C bậc thấp, cho phép can thiệp vào các tối ưu hóa bậc thấp. Hầu hết các trình biên dịch C++ đều có thể tạo ra output bằng hợp ngữ (assembly), điều này hữu ích để kiểm tra xem trình biên dịch đã tối ưu hóa đoạn code đó tốt đến mức nào. Hơn nữa, phần lớn trình biên dịch C++ cho phép các hàm intrinsic (hàm được compiler thay thế trực tiếp bằng lệnh máy) dạng hợp ngữ, inline assembly (hợp ngữ nội tuyến) hoặc dễ dàng liên kết đến các module hợp ngữ khi cần mức tối ưu hóa cao nhất. Ngôn ngữ C++ có tính di động ở chỗ các trình biên dịch C++ tồn tại trên mọi nền tảng lớn. Pascal có nhiều lợi thế của C++ nhưng lại không đa năng bằng. Fortran cũng khá hiệu quả, nhưng cú pháp đã rất cũ kỹ.

Phát triển bằng C++ khá hiệu quả nhờ có sự hỗ trợ của các công cụ phát triển mạnh mẽ. Một công cụ phát triển phổ biến là Microsoft Visual Studio. Công cụ này có thể tạo ra hai cách triển khai C++ khác nhau: mã được biên dịch trực tiếp (directly compiled code) và mã trung gian cho common language runtime (CLR) của framework .NET. Rõ ràng, phiên bản được biên dịch trực tiếp được ưu tiên hơn khi tốc độ là yếu tố quan trọng.

Một nhược điểm quan trọng của C++ liên quan đến bảo mật (security). Không có kiểm tra vi phạm giới hạn mảng (array bounds violation), tràn số nguyên (integer overflow), và con trỏ không hợp lệ (invalid pointers). Sự vắng mặt của các kiểm tra này làm cho mã thực thi nhanh hơn các ngôn ngữ có kiểm tra. Nhưng đó là trách nhiệm của lập trình viên phải thực hiện kiểm tra thủ công cho những lỗi như vậy trong trường hợp chúng không bị logic chương trình loại bỏ. Vài hướng dẫn sẽ được cung cấp bên dưới, ở trang 15.

C++ chắc chắn là ngôn ngữ lập trình được ưa thích khi việc tối ưu hóa hiệu năng được đặt lên hàng đầu. Sự tăng cường hiệu năng so với các ngôn ngữ lập trình khác có thể rất đáng kể. Việc tăng hiệu năng này có thể dễ dàng bù đắp cho sự gia tăng nhỏ về thời gian phát triển nếu hiệu năng là điều quan trọng với người dùng cuối.

Có thể có những tình huống mà một framework cấp cao dựa trên mã trung gian là cần thiết vì các lý do khác, nhưng một phần mã code vẫn cần tối ưu hóa cẩn thận. Việc triển khai kết hợp (mixed implementation) có thể là giải pháp khả thi trong những trường hợp này. Phần quan trọng nhất của mã có thể được lập trình bằng C++ biên dịch hoặc hợp ngữ, và phần còn lại, bao gồm giao diện người dùng, có thể được lập trình bằng framework cấp cao. Phần mã được tối ưu hóa có thể biên dịch dưới dạng thư viện liên kết động (DLL) và được gọi bởi phần code còn lại. Đây không phải là giải pháp tối ưu vì framework cấp cao vẫn ngốn nhiều tài nguyên, và sự chuyển đổi giữa 2 dạng code gây ra overhead làm tốn thời gian CPU. Nhưng giải pháp này vẫn có thể cho một sự cải thiện đáng kể về hiệu suất nếu phần code tối quan trọng về thời gian (time-critical) có thể gói gọn hoàn toàn trong DLL.

Một lựa chọn khác đáng cân nhắc là ngôn ngữ D. D có nhiều tính năng của Java và C# nhưng né được nhiều hạn chế của C++. Tuy vậy, D được biên dịch thành mã nhị phân và có thể được liên kết với mã C hoặc C++. Trình biên dịch và IDE cho D vẫn chưa được phát triển tốt như các trình biên dịch C++.

## 2.5 Lựa chọn trình biên dịch (Choice of compiler)

Có khá nhiều trình biên dịch C++ khác nhau để lựa chọn. Rất khó dự đoán trình biên dịch nào sẽ tối ưu tốt nhất cho một đoạn code cụ thể. Mỗi trình biên dịch lại làm một số việc rất thông minh và một số việc khác rất ngu ngốc. Một số trình biên dịch phổ biến được đề cập dưới đây.

**Microsoft Visual Studio**
Đây là một trình biên dịch rất thân thiện với người dùng với nhiều tính năng, nhưng cũng rất đắt đỏ. Phiên bản "express" bị giới hạn tính năng được cung cấp miễn phí. Visual Studio có thể build code cho framework .NET cũng như mã biên dịch trực tiếp. (Biên dịch không có Common Language Runtime, CLR, để tạo mã nhị phân). Hỗ trợ Windows 32-bit và 64-bit. Môi trường phát triển tích hợp (IDE) hỗ trợ đa ngôn ngữ lập trình, profiling và debugging. Phiên bản dòng lệnh của trình biên dịch C++ có sẵn miễn phí trong phần mềm phát triển nền tảng của Microsoft (SDK hoặc PSDK). Hỗ trợ các chỉ thị OpenMP cho tính toán đa lõi (multi-core processing). Visual Studio tối ưu hóa tương đối tốt, nhưng không phải là bộ tối ưu hóa tốt nhất.

**Borland/CodeGear/Embarcadero C++ builder**
Có một IDE với nhiều tính năng tương tự trình biên dịch Microsoft. Chỉ hỗ trợ Windows 32-bit. Không hỗ trợ tập lệnh SSE và các thế hệ sau. Khả năng tối ưu hóa kém hơn so với trình biên dịch Microsoft, Intel, Gnu và PathScale.

**Trình biên dịch Intel C++ (parallel composer)**
Trình biên dịch này không có IDE riêng. Nó được thiết kế làm một plug-in cho Microsoft Visual Studio khi biên dịch trên Windows, và cho Eclipse khi trên Linux. Nó cũng có thể được dùng độc lập qua dòng lệnh hoặc công cụ make. Nó hỗ trợ Windows 32-bit/64-bit và Linux 32-bit/64-bit, cũng như Mac OS nền Intel và các hệ thống Itanium.

Trình biên dịch Intel hỗ trợ các vector intrinsics, tự động vector hóa (xem trang 110), OpenMP và tự động song song hóa mã thành nhiều luồng (threads). Trình biên dịch này hỗ trợ CPU dispatching (phân phối CPU) để tạo nhiều phiên bản mã cho các CPU khác nhau. (Xem trang 133 để biết cách hoạt động trên vi xử lý không phải của Intel). Nó hỗ trợ tuyệt vời cho inline assembly (hợp ngữ nội tuyến) trên mọi nền tảng, với khả năng sử dụng cùng một cú pháp trong cả Windows và Linux. Đi kèm trình biên dịch này là một số thư viện hàm toán học tối ưu nhất trên thị trường.

Nhược điểm quan trọng nhất của trình biên dịch Intel là đoạn mã được biên dịch có thể chạy với tốc độ giảm đi hoặc không chạy chút nào trên vi xử lý AMD và VIA. Có thể khắc phục vấn đề này bằng cách bỏ qua cái gọi là `CPU-dispatcher` làm nhiệm vụ kiểm tra xem code có đang chạy trên CPU Intel hay không. (Xem trang 133 để biết chi tiết).

Trình biên dịch Intel là một lựa chọn tốt cho những phần mã có thể hưởng lợi từ vô số tính năng tối ưu của nó, cũng như cho code sẽ được port lên đa hệ điều hành.

**Gnu**
Đây là một trong những trình biên dịch tối ưu hóa tốt nhất, mặc dù ít thân thiện với người dùng hơn. Nó miễn phí và mã nguồn mở (open source). Nó đi kèm với hầu hết các bản phân phối Linux, BSD và Mac OS X, 32-bit và 64-bit. Hỗ trợ OpenMP và tự động song song hóa. Hỗ trợ vector intrinsics và tự động vector hóa (xem trang 110). Các thư viện hàm Gnu hiện vẫn chưa được tối ưu hóa hoàn toàn. Hỗ trợ các thư viện toán học vector của cả AMD và Intel. Trình biên dịch Gnu C++ có sẵn cho nhiều nền tảng, bao gồm Linux, BSD, Windows và Mac 32/64-bit. Đây là một sự lựa chọn rất tốt cho tất cả các nền tảng giống Unix (Unix-like).

**Clang**
Trình biên dịch Clang kết hợp với LLVM là một trình biên dịch mới khá giống Gnu trên nhiều khía cạnh và tương thích cao với Gnu. Nó được mong đợi sẽ thay thế Gnu trên nền tảng Mac, nhưng nó cũng hỗ trợ nền tảng Linux và Windows. Trình biên dịch Clang là lựa chọn tốt cho mọi nền tảng.

**PathScale**
Trình biên dịch C++ cho Linux 32/64-bit. Có nhiều tùy chọn tối ưu hóa tốt. Hỗ trợ xử lý song song, OpenMP và tự động vector hóa. Có thể chèn các gợi ý tối ưu hóa dưới dạng pragmas trong code để báo cho trình biên dịch biết đoạn code đó được thực thi thường xuyên ra sao. Khả năng tối ưu hóa rất tốt. Đây là lựa chọn tốt cho nền tảng Linux nếu sự thiên vị CPU Intel của trình biên dịch Intel không được chấp nhận.

**PGI**
Trình biên dịch C++ cho Windows, Linux, Mac 32/64-bit. Hỗ trợ xử lý song song, OpenMP và tự động vector hóa. Tối ưu hóa tương đối. Hiệu năng rất kém đối với vector intrinsics.

**Digital Mars**
Đây là một trình biên dịch giá rẻ cho Windows 32-bit, bao gồm cả IDE. Tối ưu hóa kém.

**Open Watcom**
Thêm một trình biên dịch mã nguồn mở cho Windows 32-bit. Theo mặc định, nó không tuân thủ các quy ước gọi hàm chuẩn (standard calling conventions). Khả năng tối ưu hóa tương đối tốt.

**Codeplay VectorC**
Một trình biên dịch thương mại cho Windows 32-bit. Tích hợp vào IDE Microsoft Visual Studio. Đã không được cập nhật từ năm 2004. Có khả năng tự động vector hóa. Tối ưu hóa ở mức độ vừa phải. Hỗ trợ 3 định dạng object file (file đối tượng) khác nhau.

**Bình luận**
Tất cả các trình biên dịch trên đều có thể dùng bản dòng lệnh mà không cần IDE. Các bản trial miễn phí thường có sẵn với trình biên dịch thương mại.

Việc trộn các object files từ các trình biên dịch khác nhau thường là khả thi trên nền tảng Linux, và đôi khi là trên Windows. Trình biên dịch Microsoft và Intel cho Windows tương thích hoàn toàn ở cấp độ object file, và trình biên dịch Digital Mars hầu hết là tương thích. Các trình biên dịch CodeGear, Codeplay và Watcom không tương thích với trình biên dịch khác ở cấp độ này.

Khuyến nghị của tôi để có hiệu năng code tốt là sử dụng trình biên dịch Gnu, Clang, Intel hoặc PathScale cho các ứng dụng Unix và Gnu, Clang, Intel hoặc Microsoft cho ứng dụng Windows.

Lựa chọn trình biên dịch trong một số trường hợp có thể được quyết định bởi yêu cầu tương thích với phần mã cũ (legacy code), các ưu tiên cụ thể về IDE, về các tiện ích gỡ lỗi (debugging facilities), việc dễ dàng phát triển GUI, tích hợp cơ sở dữ liệu, ứng dụng web, lập trình đa ngôn ngữ, v.v. Nếu trình biên dịch đã chọn không mang lại khả năng tối ưu hóa tốt nhất, ta có thể xây dựng các module quan trọng nhất bằng một trình biên dịch khác. Các object file tạo bởi Intel và PathScale phần lớn có thể được liên kết (linked) vào dự án làm bằng trình biên dịch Microsoft hoặc Gnu mà không gặp rắc rối, nếu các file thư viện cần thiết đã được thêm vào. Việc kết hợp trình biên dịch Borland với trình biên dịch khác khó khăn hơn nhiều. Các hàm phải được khai báo dạng `extern "C"` và các object files cần được chuyển đổi sang định dạng OMF. Cách thay thế là hãy tạo ra DLL bằng trình biên dịch xịn nhất rồi gọi nó từ trong một project được build bằng trình biên dịch khác.

## 2.6 Lựa chọn thư viện hàm (Choice of function libraries)

Một số ứng dụng dành phần lớn thời gian thực thi cho việc thực thi các hàm thư viện (library functions). Các hàm thư viện tốn thời gian thường thuộc một trong những danh mục sau:

* Cổng nhập/xuất (Input/output) của file
* Xử lý hình ảnh và âm thanh
* Thao tác trên bộ nhớ (memory) và chuỗi (string)
* Hàm toán học
* Mã hóa (Encryption), giải mã (decryption), nén dữ liệu (data compression)

Hầu hết các trình biên dịch đều đi kèm các thư viện tiêu chuẩn (standard libraries) cho nhiều mục đích này. Thật không may, các thư viện tiêu chuẩn không phải lúc nào cũng được tối ưu hóa hoàn toàn.

Các hàm thư viện thường là những mẩu code nhỏ được rất nhiều người dùng sử dụng trong rất nhiều ứng dụng khác nhau. Do đó, việc đầu tư nỗ lực vào việc tối ưu hóa hàm thư viện thường đáng giá hơn là tối ưu hóa cho các đoạn code cụ thể của một ứng dụng (application-specific code). Các thư viện hàm tốt nhất thường được tối ưu hóa ở mức độ cực cao, sử dụng hợp ngữ (assembly) và tự động phân phối CPU (automatic CPU-dispatching - xem trang 125) để hỗ trợ các thế hệ tập lệnh mới nhất.

Nếu việc định cỡ (profiling - xem trang 16) chỉ ra rằng một ứng dụng dành quá nhiều thời gian CPU trong một hàm thư viện, hoặc nếu nó quá rõ ràng, thì ta có thể cải thiện đáng kể hiệu suất chỉ bằng cách đổi sang thư viện hàm khác. Nếu ứng dụng dành phần lớn thời gian trong hàm thư viện, có thể bạn sẽ không cần phải tối ưu hóa bất kỳ thứ gì ngoài việc tìm một thư viện hiệu quả nhất và tiết kiệm các lời gọi hàm thư viện. Bạn nên thử nhiều thư viện khác nhau xem cái nào chạy mượt nhất.

Một vài thư viện hàm phổ biến được bàn tới dưới đây. Nhiều thư viện dành cho mục đích chuyên biệt cũng có sẵn.

**Microsoft**
Đi kèm trình biên dịch Microsoft. Vài hàm được tối ưu tốt, vài hàm thì không. Hỗ trợ Windows 32/64-bit.

**Borland / CodeGear / Embarcadero**
Đi kèm trình biên dịch Borland C++ builder. Không được tối ưu hóa cho SSE2 hay thế hệ tập lệnh sau này. Chỉ hỗ trợ Windows 32-bit.

**Gnu**
Đi kèm với trình biên dịch Gnu. Chưa được tối ưu hóa tốt bằng chính trình biên dịch. Phiên bản 64-bit thì ngon hơn phiên bản 32-bit. Trình biên dịch Gnu thường chèn `built-in code` thay vì sử dụng các lệnh bộ nhớ và lệnh chuỗi thông thường nhất. Code `built-in` này lại không được tối ưu. Có thể dùng flag `-fno-builtin` để lấy ra phiên bản từ thư viện. Thư viện Gnu hỗ trợ Linux và BSD 32/64-bit. Phiên bản cho Windows hiện chưa được cập nhật.

**Mac**
Các thư viện đi kèm trình biên dịch Gnu cho Mac OS X (Darwin) là một phần của dự án Xnu. Một số hàm quan trọng nhất được tích hợp hẳn vào trong nhân hệ điều hành (kernel) trong một thứ gọi là `commpage`. Những hàm này cực kì tối ưu cho vi xử lý Intel Core hoặc mới hơn. Dòng vi xử lý của AMD và Intel đời cũ thì không được hỗ trợ chút nào. Tất nhiên chỉ chạy trên hệ sinh thái Mac.

**Intel**
Trình biên dịch Intel bao gồm các thư viện hàm tiêu chuẩn. Một số thư viện chuyên biệt cũng có sẵn, điển hình như "Intel Math Kernel Library" và "Integrated Performance Primitives". Những thư viện này cực kì tối ưu đối với bộ dữ liệu (data sets) cỡ lớn. Trớ trêu thay, thư viện Intel lại đôi khi hoạt động không trơn tru cho lắm trên chip AMD và VIA. Xin xem trang 133 để được giải thích và cách lách luật. Hỗ trợ mọi hệ máy x86 và x86-64.

**AMD**
Thư viện AMD Math core cung cấp các hàm toán học tối ưu. Và nó chạy tốt trên cả vi xử lý Intel. Tuy nhiên, hiệu năng có phần lép vế so với thư viện Intel. Hỗ trợ Windows và Linux 32/64-bit.

**Asmlib**
Đây là thư viện hàm của chính tác giả (tôi) viết cho mục đích minh họa. Có sẵn tại www.agner.org/optimize/asmlib.zip. Hiện tại bao gồm các phiên bản đã được tối ưu hóa của các hàm memory, string và vài hàm hiếm khó tìm khác. Code chạy nhanh hơn hầu hết các thư viện khác trên nền vi xử lý đời mới nhất. Hỗ trợ mọi nền tảng x86 và x86-64.

*Bảng 2.1. So sánh hiệu năng của các thư viện hàm khác nhau.* (Bạn đọc có thể tham khảo bản tiếng Anh để xem chi tiết tốc độ từng thư viện).

## 2.7 Lựa chọn framework giao diện người dùng (Choice of user interface framework)

Phần lớn khối lượng code trong các dự án phần mềm điển hình đổ dồn về mặt giao diện người dùng (user interface). Những ứng dụng nào ít đòi hỏi tính toán chuyên sâu hoàn toàn có thể tiêu thụ thời gian CPU cho cái giao diện người dùng còn nhiều hơn cả nhiệm vụ cốt lõi của chương trình.

Lập trình viên ứng dụng hiếm khi tự mình lập trình giao diện người dùng đồ họa (GUI) từ đầu (from scratch). Điều này không chỉ lãng phí thời gian của họ mà còn gây khó dễ cho người dùng cuối. Các menu, nút bấm (buttons), hộp thoại (dialog boxes) nên được tiêu chuẩn hóa tối đa vì tính thân thiện với người dùng. Người lập trình có thể dùng các giao diện đồ họa tiêu chuẩn gắn kèm với hệ điều hành hoặc các thư viện nằm trong trình biên dịch và bộ công cụ phát triển.

Thư viện giao diện nổi cộm cho Windows và C++ chính là Microsoft Foundation Classes (MFC). Một sản phẩm cạnh tranh nhưng nay đã lụi tàn là Borland Object Windows Library (OWL). Vài framework giao diện đồ họa hiện hữu trên hệ thống Linux. Thư viện giao diện người dùng này có thể được liên kết dưới dạng DLL runtime hoặc một thư viện tĩnh (static library). Một DLL runtime cắn nhiều RAM hơn thư viện tĩnh, ngoại trừ khi nhiều ứng dụng chia sẻ chung 1 DLL tại cùng một thời điểm.

Thư viện giao diện thậm chí có kích thước phình to hơn bản thân ứng dụng và mất nhiều thời gian load hơn. Lựa chọn hạng nhẹ đáng xem xét là Windows Template Library (WTL). Một ứng dụng WTL thường chạy nhanh và nhẹ nhàng hơn ứng dụng MFC. Thời gian phát triển cho các ứng dụng WTL thường lâu hơn do tài liệu kém (poor documentation) và thiếu các công cụ phát triển tiên tiến.

Giao diện người dùng ở mức tối giản nhất đạt được bằng cách vứt đi giao diện đồ họa và chuyển sang dùng chương trình dạng bảng điều khiển (console mode program). Giá trị đầu vào (inputs) cho chương trình giao diện dòng lệnh thường được khai báo qua giao diện command line hoặc input file. Output sẽ đổ ra cửa sổ dòng lệnh hoặc output file. Chương trình console thì nhanh, gọn và dễ dàng code. Việc mang nó (port) sang nền tảng khác cũng cực kỳ dễ dàng vì nó chẳng dựa dẫm vào cái hàm giao diện đồ họa đặc trưng nào của hệ điều hành. Nhưng trải nghiệm người dùng có thể nghèo nàn do thiếu đi các menu có khả năng tự giải thích như ở giao diện đồ họa. Nhưng console mode program cực kỳ hữu ích khi bị gọi bởi một ứng dụng khác như công cụ `make`.

Kết luận lại, chọn cái framework cho giao diện người dùng chính là đánh đổi giữa thời gian phát triển, tính dễ dùng, sự nhỏ gọn và thời gian thực thi của chương trình. Không có giải pháp vạn năng nào tốt cho mọi người, mọi nhà.

## 2.8 Vượt qua các hạn chế của ngôn ngữ C++ (Overcoming the drawbacks of the C++ language)

Dù C++ ôm đồm muôn vàn cái hay khi nhắc về việc tối ưu hóa, nó vẫn mang một số cái dở khiến dân code phải xách dép đi chọn ngôn ngữ khác. Phần này sẽ luận bàn về việc khắc phục những điểm yếu đó khi đã lỡ chọn C++ vì mục đích tối ưu hóa.

**Tính di động (Portability)**
C++ hoàn toàn mang tính di động nếu ta xét đến cú pháp của nó được tiêu chuẩn hóa đầy đủ và mọi nền tảng lớn đều hỗ trợ. Dù vậy, C++ lại là cái ngôn ngữ cho phép chọc ngoáy trực tiếp vào phần cứng và thực hiện lời gọi hệ thống (system calls). Rõ ràng thì những món này cực kỳ mang tính đặc trưng của từng hệ thống (system-specific). Để việc porting giữa đa nền tảng trở nên khả thi, tôi khuyên bạn nên nhét phần giao diện người dùng (user interface) cũng như mọi phần code dính dáng trực tiếp tới hệ thống (system-specific) vào một module riêng, đồng thời tống nốt phần mã cốt lõi (task-specific, đáng lẽ độc lập với hệ thống) sang một module riêng biệt.

Kích thước của kiểu số nguyên và vô vàn các chi tiết gắn liền với phần cứng thì phụ thuộc nặng vào nền tảng phần cứng và hệ điều hành. Xin tham khảo trang 29 để biết thêm chi tiết.

**Thời gian phát triển (Development time)**
Một số lập trình viên cảm thấy rằng ngôn ngữ nọ công cụ kia xài lẹ hơn cái khác. Dẫu phần lớn chỉ là thói quen, nhưng công nhận có một số công cụ xịn sò sở hữu vài tiện ích xịn có thể gánh phụ phần việc cỏn con tự động. Thời gian phát triển và tính dễ bảo trì cho code C++ có thể cải thiện bằng cách duy trì tính module hóa xuyên suốt và các class có khả năng tái sử dụng (reusable classes).

**Bảo mật (Security)**
Điểm tồi tệ nhất của ngôn ngữ C++ liên quan mật thiết tới vấn đề bảo mật. C++ chuẩn không có sẵn hệ thống check lỗi vi phạm giới hạn mảng (array bounds violations) cũng như con trỏ sai (invalid pointers). Đây là cội rễ cho tỉ lỗi trong các chương trình C++ và cũng là điểm yếu cho hacker khoét vào. Phải cực kì tuân thủ các nguyên tắc viết code nhất định hòng chặn đứng những lỗi tày đình trong các ứng dụng mà vấn đề bảo mật được đặt lên hàng đầu.

Các lỗi con trỏ sai có thể được lách qua bằng cách xài tham chiếu (references) thay vì con trỏ (pointers), bằng việc khởi tạo con trỏ về số 0, hoặc chỉnh con trỏ về 0 mỗi khi object mà nó trỏ tới không còn hợp lệ, và nên né trò toán số học con trỏ (pointer arithmetics) lẫn ép kiểu con trỏ (pointer type casting). Linked lists và hàng tá cấu trúc dữ liệu xài con trỏ có thể thay bằng các mẫu lớp chứa (container class templates) hiệu quả hơn, như đã trình bày ở trang 94. Tuyệt đối tránh xa cái hàm `scanf`.

Vi phạm giới hạn mảng (viết tràn vùng nhớ) có lẽ là cha đẻ của mọi thể loại lỗi trên C++. Viết vào vùng quá giới hạn cuối cùng của một mảng sẽ tống cổ biến khác ra ngoài, hoặc chí mạng hơn, nó chèn luôn vào return address của cái hàm định nghĩa cái mảng đó. Nó sinh ra vô vàn hành vi kỳ lạ ố ồ không ai ngờ. Mảng thường được xài làm vùng đệm chứa text (buffer) hay input data. Cái lỗi bỏ qua kiểm tra buffer overflow khi nhập input chính là cái mỏ vàng quen thuộc để các anh hacker khai thác.

Lối thoát hoàn hảo nhất để diệt những lỗi kiểu này chính là đổi mảng (array) sang các class chứa đã được kiểm thử chán chê. Cái thư viện chuẩn (STL) chính là kho tàng tuyệt vời cho đồ chơi kiểu này. Tiếc cái là, vô vàn standard container class lại sử dụng cấp phát bộ nhớ động (dynamic memory allocation) một cách khá phế. Xin xem các trang ví dụ để học lách cái vụ cấp phát bộ nhớ động rườm rà. Lật trang 94 để tham gia cuộc thảo luận về các class chứa (container classes) hiệu năng cao. Có một cái phụ lục gắn ở trang web www.agner.org/optimize/cppexamples.zip dính kèm vài mẫu arrays được gắn cả bounds checking và mớ efficient container classes khác.

Text strings (chuỗi văn bản) là mỏ gai điển hình vì có khi chúng chả bị giới hạn bởi cái chiều dài cụ thể nào. Cái phong cách xài mảng character cũ mèm hồi C thì nhanh, mượt đó, nhưng chả bao giờ an toàn trừ phi bạn luôn đi đo đạc cẩn thận chiều dài chuỗi trước khi store. Chân ái tiêu chuẩn cho mớ hỗn độn này là xài các class cho chuỗi (string classes), điển hình là `string` hoặc `CString`. Quá an toàn, quá linh hoạt, nhưng cũng siêu phế cho các app lớn. Cái string classes sẽ tự cướp lấy một block bộ nhớ mới mỗi khi chuỗi của nó được nặn ra hoặc được độ lại. Nó sẽ nghiền vụn bộ nhớ, gây ra sự đứt gãy phân mảnh (fragmented), đồng thời kéo theo hóa đơn thanh toán chi phí `overhead` cực chát cho trình quản lý heap (heap management) và dọn rác (garbage collection). Có một giải pháp bá đạo hơn, không ảnh hưởng tí bảo mật nào, là tống cổ mọi chuỗi vào một cái memory pool duy nhất. Đọc nốt các ví dụ đính kèm để biết cách làm phép với memory pool nhé.
