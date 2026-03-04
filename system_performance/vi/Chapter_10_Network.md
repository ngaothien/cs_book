# Chương 10: Mạng (Network)

Khi các hệ thống trở nên phân tán hơn, đặc biệt là với các môi trường điện toán đám mây, mạng đóng một vai trò lớn hơn trong hiệu năng. Các tác vụ phổ biến trong hiệu năng mạng bao gồm cải thiện độ trễ và thông lượng mạng, và loại bỏ các giá trị ngoại lai độ trễ, thứ có thể gây ra bởi các gói tin bị đánh rơi hoặc bị trì hoãn.

Phân tích mạng trải dài qua phần cứng và phần mềm. Phần cứng là mạng vật lý, bao gồm các card giao diện mạng, các switch, các router, và các gateways (những thứ này thường cũng có phần mềm). Phần mềm là network stack của kernel bao gồm các trình điều khiển thiết bị mạng, các hàng đợi gói tin, và các trình lập lịch gói tin, và việc triển khai các giao thức mạng. Các giao thức tầng thấp thường là phần mềm kernel (IP, TCP, UDP, v.v.) và các giao thức tầng cao hơn thường là thư viện hoặc phần mềm ứng dụng (ví dụ: HTTP).

Mạng thường bị đổ lỗi cho hiệu năng kém do tiềm năng cho việc tắc nghẽn và sự phức tạp cố hữu của nó (đổ lỗi cho những gì chưa biết). Chương này sẽ chỉ ra cách tìm ra những gì thực sự đang xảy ra, thứ có thể giải oan cho mạng sao cho quá trình phân tích có thể tiếp tục.

Các mục tiêu học tập của chương này là:
- Hiểu các mô hình và khái niệm mạng.
- Hiểu các phép đo độ trễ mạng khác nhau.
- Có kiến thức làm việc về các giao thức mạng phổ biến.
- Trở nên quen thuộc với các thành phần nội bộ phần cứng mạng.
- Trở nên quen thuộc với đường dẫn kernel từ các socket và thiết bị.
- Tuân theo các phương pháp luận khác nhau cho phân tích mạng.
- Đặc tính hóa I/O mạng trên toàn hệ thống và theo từng tiến trình.
- Nhận diện các vấn đề gây ra bởi việc truyền lại TCP (TCP retransmits).
- Điều tra các thành phần nội bộ mạng bằng cách sử dụng các công cụ truy vết.
- Nhận biết các tham số tinh chỉnh mạng.

Chương này bao gồm sáu phần, ba phần đầu cung cấp cơ sở cho việc phân tích mạng và ba phần cuối trình bày ứng dụng thực tế của nó cho các hệ thống dựa trên Linux. Các phần như sau:
- **Nền tảng (Background)** giới thiệu thuật ngữ liên quan đến mạng, các mô hình, và các khái niệm hiệu năng mạng then chốt.
- **Kiến trúc (Architecture)** cung cấp các mô tả chung về các thành phần mạng vật lý và network stack.
- **Phương pháp luận (Methodology)** mô tả các phương pháp luận phân tích hiệu năng, cả quan sát và thực nghiệm.
- **Công cụ Quan trắc (Observability Tools)** trình bày các công cụ quan sát hiệu năng mạng cho các hệ thống dựa trên Linux.
- **Thực nghiệm (Experimentation)** tóm tắt các công cụ benchmark và thực nghiệm mạng.
- **Tinh chỉnh (Tuning)** mô tả các tham số tinh chỉnh ví dụ.

Các kiến thức cơ bản về mạng, chẳng hạn như vai trò của TCP và IP, được coi là kiến thức mặc định cho chương này.

## 10.1 Thuật ngữ (Terminology)
Để tham khảo, thuật ngữ liên quan đến mạng được sử dụng trong chương này bao gồm:
- **Giao diện (Interface):** Thuật ngữ *interface port* đề cập đến đầu nối mạng vật lý. Thuật ngữ *interface* hoặc *link* đề cập đến bản thể logic của một cổng giao diện mạng, như được thấy và cấu hình bởi hệ điều hành. (Không phải tất cả các giao diện OS đều được hỗ trợ bởi phần cứng: một số là ảo.)
- **Gói tin (Packet):** Thuật ngữ *packet* đề cập đến một thông điệp trong một mạng chuyển mạch gói, chẳng hạn như các gói tin IP.
- **Khung hình (Frame):** Một thông điệp cấp mạng vật lý, ví dụ một khung hình Ethernet.
- **Socket:** Một API có nguồn gốc từ BSD cho các endpoint mạng.
- **Băng thông (Bandwidth):** Tốc độ truyền dữ liệu tối đa cho loại mạng, thường được đo bằng bit mỗi giây. "100 GbE" là Ethernet với băng thông 100 Gbits/s. Có thể có các giới hạn băng thông cho mỗi hướng, vì vậy một 100 GbE có thể có khả năng truyền 100 Gbits/s và nhận 100 Gbits/s song song (tổng cộng 200 Gbit/sec).
- **Thông lượng (Throughput):** Tốc độ truyền dữ liệu hiện tại giữa các endpoint mạng, được đo bằng bit mỗi giây hoặc byte mỗi giây.
- **Độ trễ (Latency):** Độ trễ mạng có thể đề cập đến thời gian cần thiết để một thông điệp thực hiện một vòng lặp (round-trip) giữa các endpoint, hoặc thời gian cần thiết để thiết lập một kết nối (ví dụ: TCP handshake), loại trừ thời gian truyền dữ liệu theo sau đó.

Các thuật ngữ khác được giới thiệu xuyên suốt chương này. Bảng thuật ngữ (Glossary) bao gồm thuật ngữ cơ bản để tham khảo, bao gồm *client*, *Ethernet*, *host*, *IP*, *RFC*, *server*, *SYN*, *ACK*. Đồng thời xem các phần thuật ngữ trong Chương 2 và 3.

## 10.2 Mô hình (Models)
Các mô hình đơn giản sau đây minh họa một số nguyên tắc cơ bản của mạng và hiệu năng mạng. Mục 10.4, Kiến trúc, đào sâu hơn nhiều, bao gồm cả các chi tiết triển khai cụ thể.

### 10.2.1 Giao diện Mạng (Network Interface)
Một giao diện mạng là một endpoint hệ điều hành cho các kết nối mạng; nó là một sự trừu tượng hóa được cấu hình và quản lý bởi các quản trị viên hệ thống.

(Hình 10.1 Giao diện mạng)

Một giao diện mạng được mô tả trong Hình 10.1. Các giao diện mạng được ánh xạ tới các cổng mạng vật lý như một phần cấu hình của chúng. Các cổng kết nối tới mạng và thường có các kênh truyền và nhận riêng biệt.

### 10.2.2 Bộ điều khiển (Controller)
Một card giao diện mạng (NIC) cung cấp một hoặc nhiều cổng mạng cho hệ thống và chứa một bộ điều khiển mạng: một bộ vi xử lý để truyền tải các gói tin giữa các cổng và I/O vận chuyển hệ thống. Một ví dụ về bộ điều khiển với bốn cổng được mô tả trong Hình 10.2, trình bày các thành phần vật lý liên quan.

(Hình 10.2 Bộ điều khiển mạng)

Bộ điều khiển thường được cung cấp như một card mở rộng riêng biệt hoặc được tích hợp vào bo mạch hệ thống. (Các tùy chọn khác bao gồm qua USB.)

### 10.2.3 Protocol Stack (Chồng giao thức)
Mạng được thực hiện bởi một chồng các giao thức, mỗi tầng của chúng phục vụ một mục đích cụ thể. Hai mô hình chồng giao thức được trình bày trong Hình 10.3, cùng với các giao thức ví dụ.

(Hình 10.3 Các chồng giao thức mạng)

Các tầng thấp hơn được vẽ rộng hơn để chỉ ra việc đóng gói giao thức (protocol encapsulation). Các thông điệp được gửi di chuyển xuống chồng giao thức từ ứng dụng tới mạng vật lý. Các thông điệp nhận được di chuyển lên.

Lưu ý rằng tiêu chuẩn Ethernet cũng mô tả tầng vật lý, và cách đồng hoặc sợi quang được sử dụng.

Có thể có các tầng bổ sung, ví dụ, nếu Internet Protocol Security (IPsec) hoặc Linux WireGuard đang được sử dụng, chúng nằm trên tầng Internet để cung cấp bảo mật giữa các endpoint IP. Ngoài ra, nếu tunneling đang được sử dụng (ví dụ: Virtual Extensible LAN (VXLAN)), thì một chồng giao thức có thể được đóng gói trong một cái khác.

Trong khi chồng giao thức TCP/IP đã trở thành tiêu chuẩn, tôi nghĩ có thể hữu ích khi xem xét ngắn gọn mô hình OSI, vì nó cho thấy các tầng giao thức bên trong ứng dụng. Thuật ngữ "layer" (tầng) bắt nguồn từ OSI, nơi Layer 3 đề cập đến các giao thức mạng.

Các thông điệp tại các tầng khác nhau cũng sử dụng thuật ngữ khác nhau. Sử dụng mô hình OSI: tại tầng vận chuyển (transport layer) một thông điệp là một *segment* hoặc *datagram*; tại tầng mạng (network layer) một thông điệp là một *packet*; và tại tầng liên kết dữ liệu (data link layer) một thông điệp là một *frame*.

## 10.3 Các khái niệm (Concepts)
Sau đây là một lựa chọn các khái niệm quan trọng trong mạng và hiệu năng mạng.

### 10.3.1 Các mạng và Định tuyến (Networks and Routing)
Một mạng là một nhóm các máy chủ được kết nối, liên quan bởi các địa chỉ giao thức mạng. Việc có nhiều mạng—thay vì một mạng khổng lồ trên toàn thế giới—là mong muốn vì một số lý do, đặc biệt là khả năng mở rộng (scalability). Các thông điệp mạng sẽ được *broadcast* tới tất cả các máy chủ lân cận. Bằng cách tạo ra các mạng con (subnetworks) nhỏ hơn, các thông điệp broadcast như vậy có thể được cô lập cục bộ sao cho chúng không tạo ra một vấn đề tràn ngập (flooding) ở quy mô lớn. Đây cũng là cơ sở để cô lập việc truyền tải các thông điệp thông thường tới chỉ những mạng giữa nguồn và đích, giúp sử dụng hiệu quả hơn hạ tầng mạng.

Định tuyến quản lý việc phân phối các thông điệp, được gọi là *packets*, qua các mạng này. Vai trò của định tuyến được mô tả trong Hình 10.4.

(Hình 10.4 Các mạng được kết nối qua các router)

Từ quan điểm của máy chủ A, *localhost* là chính máy chủ A. Tất cả các máy chủ khác được mô tả là các máy chủ từ xa (*remote hosts*).

Máy chủ A có thể kết nối tới máy chủ B qua mạng cục bộ, thường được điều khiển bởi một network switch (xem Mục 10.4, Kiến trúc). Máy chủ A có thể kết nối tới máy chủ C qua router 1, và tới máy chủ D qua các router 1, 2, và 3. Vì các thành phần mạng này được chia sẻ, sự tranh chấp từ các lưu lượng khác (ví dụ: máy chủ C tới máy chủ E) có thể gây hại cho hiệu năng.

Bên cạnh các router, một mạng điển hình cũng sẽ sử dụng các *firewalls* để cải thiện bảo mật, chặn các kết nối không mong muốn giữa các máy chủ.

Thông tin địa chỉ cần thiết để định tuyến các gói tin được chứa trong một IP header.

### 10.3.2 Các giao thức (Protocols)
Các tiêu chuẩn giao thức mạng, chẳng hạn như cho IP, TCP, và UDP, là một yêu cầu cần thiết cho việc liên lạc giữa các hệ thống và các thiết bị khác nhau. Giao tiếp được thực hiện bằng cách truyền tải các thông điệp có thể định tuyến được gọi là *packets*, thông thường bằng cách đóng gói dữ liệu payload.

Các giao thức mạng có các đặc tính hiệu năng khác nhau, phát sinh từ thiết kế ban đầu, các phần mở rộng, hoặc việc xử lý đặc biệt bởi phần mềm hoặc phần cứng. Ví dụ, các phiên bản khác nhau của giao thức IP, IPv4 và IPv6, có thể được xử lý bởi các đường dẫn mã kernel khác nhau và có thể thể hiện các đặc tính hiệu năng khác nhau. Các giao thức khác thực hiện khác nhau theo thiết kế, và có thể được lựa chọn khi chúng phù hợp với khối lượng công việc: các ví dụ bao gồm Stream Control Transmission Protocol (SCTP), Multipath TCP (MPTCP), và QUIC.

Thường xuyên, có các tham số tinh chỉnh hệ thống có thể ảnh hưởng đến hiệu năng giao thức, bằng cách thay đổi các thiết lập chẳng hạn như kích thước bộ đệm, các thuật toán, và các bộ định thời (timers) khác nhau. Những sự khác biệt này đối với các giao thức cụ thể được mô tả sau này.

Các giao thức thường truyền dữ liệu bằng cách sử dụng đóng gói (encapsulation).

### 10.3.3 Đóng gói (Encapsulation)
Việc đóng gói thêm các metadata vào một payload tại điểm bắt đầu (một *header*), tại điểm kết thúc (một *footer*), hoặc cả hai. Việc này không làm thay đổi dữ liệu payload, mặc dù nó làm tăng kích thước tổng thể của thông điệp một chút, thứ tiêu tốn một số chi phí cho việc truyền tải.

Hình 10.5 trình bày một ví dụ về việc đóng gói cho một chồng TCP/IP với Ethernet.

(Hình 10.5 Đóng gói giao thức mạng)

E.H. là Ethernet header, và E.F. là Ethernet footer tùy chọn.

### 10.3.4 Kích thước Gói tin (Packet Size)
Kích thước của các gói tin và payload của chúng ảnh hưởng đến hiệu năng, với các kích thước lớn hơn giúp cải thiện thông lượng và giảm các chi phí gói tin. Đối với TCP/IP và Ethernet, các gói tin có thể nằm trong khoảng từ 54 đến 9,054 byte, bao gồm 54 byte (hoặc nhiều hơn, tùy thuộc vào các tùy chọn hoặc phiên bản) của các headers giao thức.

Kích thước gói tin thường bị giới hạn bởi giá trị *maximum transmission unit* (MTU) của giao diện mạng, thứ cho nhiều mạng Ethernet được cấu hình là 1,500 byte. Nguồn gốc của kích thước 1,500 MTU là từ các phiên bản đầu tiên của Ethernet, và nhu cầu cân bằng các yếu tố chẳng hạn như chi phí bộ nhớ đệm NIC và độ trễ truyền tải [Nosachev 20]. Các máy chủ tranh chấp để sử dụng một môi trường chia sẻ (cáp đồng trục hoặc một Ethernet hub), và các kích thước lớn hơn làm tăng độ trễ cho các máy chủ phải chờ đợi tới lượt của mình.

Ethernet hiện nay hỗ trợ các gói tin lớn hơn (frames) lên tới xấp xỉ 9,000 byte, được gọi là *jumbo frames*. Những thứ này có thể cải thiện hiệu năng thông lượng mạng, cũng như độ trễ của việc truyền dữ liệu, bằng cách yêu cầu ít gói tin hơn.

Sự hội tụ của hai thành phần đã cản trở việc áp dụng jumbo frames: các phần cứng mạng cũ hơn và các firewall cấu hình sai. Các phần cứng cũ hơn không hỗ trợ jumbo frames và có thể hoặc là phân mảnh gói tin bằng cách sử dụng giao thức IP (gây ra chi phí hiệu năng cho việc lắp ráp lại gói tin) hoặc phản hồi với một lỗi ICMP "can't fragment", báo cho bên gửi biết để giảm kích thước gói tin. Bây giờ các firewall cấu hình sai bắt đầu phát huy tác dụng: đã có các cuộc tấn công dựa trên ICMP trong quá khứ (bao gồm cả "ping of death") mà một số quản trị viên firewall đã phản hồi bằng cách chặn tất cả ICMP. Điều này ngăn cản thông điệp "can't fragment" hữu ích tiếp cận bên gửi và khiến các gói tin mạng bị đánh rơi một cách thầm lặng khi kích thước gói tin của chúng vượt quá 1,500. Nếu thông điệp ICMP được nhận và việc phân mảnh xảy ra, cũng có rủi ro các gói tin bị phân mảnh bị đánh rơi bởi các thiết bị không hỗ trợ chúng. Để tránh những vấn đề này, nhiều hệ thống vẫn giữ nguyên mặc định 1,500 MTU.

Hiệu năng của các khung hình 1,500 MTU đã được cải thiện bởi các tính năng của card giao diện mạng, bao gồm *TCP offload* và *large segment offload*. Những thứ này gửi các bộ đệm lớn hơn tới card mạng, thứ sau đó tự chia chúng thành các khung hình nhỏ hơn bằng cách sử dụng phần cứng chuyên dụng và được tối ưu hóa. Điều này, ở một mức độ nào đó, đã thu hẹp khoảng cách giữa hiệu năng mạng 1,500 và 9,000 MTU.

### 10.3.5 Độ trễ (Latency)
Độ trễ là một chỉ số quan trọng cho hiệu năng mạng và có thể được đo lường theo những cách khác nhau, bao gồm độ trễ phân giải tên (name resolution latency), độ trễ ping, độ trễ kết nối, độ trễ byte đầu tiên (first-byte latency), thời gian vòng lặp (round-trip time), và tuổi thọ kết nối. Những điều này được mô tả như được đo lường bởi một máy khách kết nối tới một máy chủ.

**Độ trễ Phân giải Tên (Name Resolution Latency)**
Khi thiết lập các kết nối tới các máy chủ từ xa, một tên máy chủ thường được phân giải thành một địa chỉ IP, ví dụ, bằng phân giải DNS. Thời gian cho việc này có thể được đo lường riêng biệt dưới dạng độ trễ phân giải tên. Trường hợp tệ nhất cho độ trễ này liên quan đến các lần hết thời gian phân giải tên, thứ có thể mất hàng chục giây.

Các hệ điều hành thường cung cấp một dịch vụ phân giải tên có cung cấp cơ chế đệm ẩn, sao cho các lần tra cứu DNS tiếp theo có thể giải quyết nhanh chóng từ một bộ đệm ẩn. Đôi khi các ứng dụng chỉ sử dụng các địa chỉ IP và không sử dụng tên, và do đó độ trễ DNS được tránh hoàn toàn.

**Độ trễ Ping (Ping Latency)**
Đây là thời gian cho một yêu cầu ICMP echo tới phản hồi echo, như được đo lường bởi lệnh ping(1). Thời gian này được sử dụng để đo độ trễ mạng giữa các máy chủ, bao gồm các bước nhảy (hops) ở giữa, và được đo lường như thời gian cần thiết để một yêu cầu mạng thực hiện một vòng lặp. Nó được sử dụng phổ biến vì nó đơn giản và thường có sẵn: nhiều hệ điều hành sẽ phản hồi ping theo mặc định. Nó có thể không khớp chính xác với thời gian vòng lặp của các yêu cầu ứng dụng, vì ICMP có thể được xử lý với mức ưu tiên khác nhau bởi các router.

Ví dụ các độ trễ ping được trình bày trong Bảng 10.1.

Bảng 10.1 Các độ trễ ping ví dụ
| Từ | Tới | Qua | Độ trễ | Được điều chỉnh |
| --- | --- | --- | --- | --- |
| Localhost | Localhost | Kernel | 0.05 ms | 1 s |
| Host | Host (cùng mạng con) | 10 GbE | 0.2 ms | 4 s |
| Host | Host (cùng mạng con) | 1 GbE | 0.6 ms | 12 s |
| Host | Host (cùng mạng con) | Wi-Fi | 3 ms | 1 phút |
| San Francisco | New York | Internet | 40 ms | 13 phút |
| San Francisco | Vương quốc Anh | Internet | 81 ms | 27 phút |
| San Francisco | Australia | Internet | 183 ms | 1 giờ |

Để minh họa rõ hơn các bậc độ lớn liên quan, cột Scaled hiển thị một sự so sánh dựa trên một độ trễ ping localhost giả định là một giây.

**Độ trễ Kết nối (Connection Latency)**
Độ trễ kết nối là thời gian để thiết lập một kết nối mạng, trước khi bất kỳ dữ liệu nào được truyền tải. Đối với *độ trễ kết nối TCP*, đây là thời gian TCP handshake. Được đo lường từ máy khách, nó là thời gian từ lúc gửi gói tin SYN tới lúc nhận được gói tin SYN-ACK tương ứng. Độ trễ kết nối có thể được gọi tốt hơn là *connection establishment latency* để phân biệt rõ ràng nó với tuổi thọ kết nối (connection life span).

Độ trễ kết nối là tương tự như độ trễ ping, mặc dù nó thực hiện nhiều mã kernel hơn để thiết lập một kết nối và bao gồm thời gian để truyền lại bất kỳ gói tin nào bị đánh rơi. Gói tin TCP SYN, cụ thể, có thể bị đánh rơi bởi máy chủ nếu backlog của nó đầy, khiến máy khách phải gửi một đợt truyền lại dựa trên bộ định thời (timer-based retransmit) của gói tin SYN. Thao tác TCP handshake này, do độ trễ truyền lại, có thể bao gồm độ trễ truyền lại, thêm một hoặc nhiều giây.

Độ trễ kết nối được theo sau bởi độ trễ byte đầu tiên.

**Độ trễ Byte đầu tiên (First-Byte Latency)**
Còn được gọi là *time to first byte* (TTFB), độ trễ byte đầu tiên là thời gian từ khi kết nối đã được thiết lập tới khi byte dữ liệu đầu tiên được nhận. Điều này bao gồm thời gian để máy chủ từ xa chấp nhận một kết nối, lập lịch luồng phục vụ nó, và cho luồng đó thực thi và gửi byte đầu tiên.

Trong khi độ trễ ping và kết nối đo lường độ trễ phát sinh bởi mạng, độ trễ byte đầu tiên bao gồm thời gian suy nghĩ của máy chủ mục tiêu. Điều này có thể bao gồm độ trễ nếu máy chủ bị quá tải và cần thời gian để xử lý yêu cầu (ví dụ: TCP backlog) và để lập lịch máy chủ (độ trễ trình lập lịch CPU).

**Thời gian Vòng lặp (Round-Trip Time)**
Thời gian vòng lặp (RTT) mô tả thời gian cần thiết cho một yêu cầu mạng thực hiện một vòng lặp giữa các endpoint. Điều này bao gồm thời gian lan truyền tín hiệu và thời gian xử lý tại mỗi hop mạng. Mục đích sử dụng là để xác định độ trễ của mạng, vì vậy lý tưởng nhất RTT bị chiếm ưu thế bởi thời gian mà yêu cầu và phản hồi dành cho mạng (và không phải thời gian máy chủ từ xa dành để phục vụ yêu cầu). RTT cho các yêu cầu ICMP echo thường được nghiên cứu, vì thời gian xử lý máy chủ từ xa là tối thiểu.

**Tuổi thọ Kết nối (Connection Life Span)**
Tuổi thọ kết nối là thời gian từ khi một kết nối mạng được khởi tạo cho tới khi nó được đóng lại. Một số giao thức chẳng hạn như HTTP có thể sử dụng một chiến lược *keep-alive*, để lại các kết nối mở và rảnh rỗi cho các yêu cầu trong tương lai, nhằm tránh các chi phí về độ trễ của việc thiết lập kết nối lặp đi lặp lại.

Để biết thêm các phép đo độ trễ mạng, hãy xem Mục 10.5.4, Phân tích độ trễ, thứ mô tả việc sử dụng chúng để chẩn đoán hiệu năng mạng.

### 10.3.6 Buffering (Vùng đệm)
Bất chấp các độ trễ mạng khác nhau có thể gặp phải, thông lượng mạng có thể được duy trì ở tốc độ cao bằng việc sử dụng buffering ở bên gửi và bên nhận. Các bộ đệm lớn hơn có thể giảm thiểu các ảnh hưởng của thời gian vòng lặp cao hơn bằng cách tiếp tục gửi dữ liệu trước khi dừng lại và chờ đợi một xác nhận (acknowledgment).

TCP sử dụng buffering, cùng với một sliding send window, để cải thiện thông lượng. Các socket mạng cũng có các bộ đệm, và các ứng dụng cũng có thể sử dụng các bộ đệm của chính chúng, để tổng hợp dữ liệu trước khi gửi.

Buffering cũng có thể được thực hiện bởi các thành phần mạng bên ngoài, chẳng hạn như các switch và các router, trong một nỗ lực để cải thiện thông lượng của chính chúng. Thật không may, việc sử dụng các bộ đệm lớn trên những thành phần này có thể dẫn đến *bufferbloat*, nơi các gói tin được xếp hàng trong các khoảng thời gian dài. Điều này khiến TCP congestion avoidance (tránh tắc nghẽn TCP) trên các máy chủ dẫn đến các đợt điều tiết (throttles) hiệu năng. Các tính năng đã được thêm vào các kernel Linux 3.x để giải quyết vấn đề này (bao gồm các giới hạn hàng đợi byte, kỷ luật xếp hàng CoDel [Nichols 12], và các hàng đợi TCP nhỏ). Cũng có một trang web để thảo luận về vấn đề này [Bufferbloat 20].

Chức năng của buffering (hoặc buffering lớn) có thể được phục vụ tốt nhất bởi các endpoint—các máy chủ—và không phải là các nút mạng trung gian, tuân theo một nguyên tắc được gọi là *end-to-end arguments* [Saltzer 84].

### 10.3.7 Connection Backlog (Hàng đợi kết nối)
Một loại buffering khác là cho các yêu cầu kết nối ban đầu. TCP triển khai một backlog, nơi các yêu cầu SYN có thể xếp hàng trong kernel trước khi được chấp nhận bởi tiến trình không gian người dùng. Khi có quá nhiều yêu cầu kết nối TCP cho tiến trình chấp nhận kịp thời, backlog đạt tới giới hạn và các gói tin SYN bị đánh rơi, phải được truyền lại bởi máy khách sau đó. Việc truyền lại các gói tin này gây ra độ trễ cho thời gian kết nối của khách hàng. Giới hạn này có thể tinh chỉnh được: nó là một tham số của syscall listen(2), và kernel cũng có thể cung cấp các giới hạn trên toàn hệ thống.

Việc đánh rơi backlog và truyền lại SYN là các chỉ báo của sự quá tải máy chủ.

### 10.3.8 Thương lượng Giao diện (Interface Negotiation)
Các giao diện mạng vận hành với các chế độ khác nhau, được thương lượng tự động giữa các bộ thu phát (transceivers) được kết nối. Một số ví dụ là:
- **Băng thông:** Ví dụ, 10, 100, 1,000, 10,000, 40,000, 100,000 Mbits/s
- **Duplex:** Bán song công (Half) hoặc Toàn song công (Full)

Các ví dụ này là từ Ethernet, thứ có xu hướng sử dụng các con số làm tròn cơ số 10 cho các giới hạn băng thông. Các loại lớp vật lý khác, chẳng hạn như SONET, có một bộ băng thông khả thi khác.

Các giao diện mạng thường được mô tả theo các thuật ngữ về băng thông và giao thức cao nhất của chúng, ví dụ, 1 Gbit/s Ethernet (1 GbE). Giao diện này có thể, tuy nhiên, tự động thương lượng về tốc độ thấp hơn nếu cần thiết. Điều này có thể xảy ra nếu endpoint kia không hỗ trợ tốc độ nhanh hơn, hoặc để điều chỉnh các vấn đề môi trường vật lý (dây dẫn kém).

Chế độ toàn song công (Full-duplex) cho phép truyền tải song song đồng thời, với các đường dẫn riêng biệt để truyền và nhận sao cho mỗi cái có thể vận hành ở băng thông đầy đủ. Chế độ bán song công chỉ cho phép một hướng tại một thời điểm.

### 10.3.9 Tránh Tắc nghẽn (Congestion Avoidance)
Các mạng là các tài nguyên chia sẻ có thể trở nên tắc nghẽn khi tải lưu lượng cao. Điều này có thể gây ra các vấn đề hiệu năng: ví dụ, các router hoặc switch có thể đánh rơi các gói tin, gây ra độ trễ do truyền lại TCP. Các máy chủ cũng có thể trở nên quá tải khi nhận tốc độ gói tin cao, và có thể đánh rơi chính các gói tin đó.

Có nhiều cơ chế để tránh những vấn đề này; các cơ chế này nên được nghiên cứu, và tinh chỉnh nếu cần thiết, để cải thiện khả năng mở rộng dưới mức tải. Ví dụ cho các giao thức khác nhau bao gồm:
- **Ethernet:** Một máy chủ bị quá tải có thể gửi các *pause frames* tới một bên truyền, yêu cầu họ tạm dừng truyền tải (IEEE 802.3x). Cũng có các lớp ưu tiên và *priority pause frames* cho mỗi lớp.
- **IP:** Bao gồm một trường Explicit Congestion Notification (ECN).
- **TCP:** Bao gồm một congestion window, và các thuật toán *congestion control* khác nhau có thể được sử dụng.

Các phần sau này mô tả IP ECN và các thuật toán điều khiển tắc nghẽn TCP chi tiết hơn.

### 10.3.10 Mức sử dụng (Utilization)
Mức sử dụng giao diện mạng có thể được tính toán như thông lượng hiện tại chia cho băng thông tối đa. Với băng thông và duplex thay đổi do tự động thương lượng, việc tính toán này không đơn giản như tên gọi của nó.

Đối với toàn song công, mức sử dụng áp dụng cho mỗi hướng và được đo lường như thông lượng hiện tại cho hướng đó chia cho băng thông đã thương lượng hiện tại. Thường chỉ là một hướng quan trọng nhất, vì các máy chủ thường là không đối xứng: các máy chủ truyền-nặng (transmit-heavy), và các máy khách là nhận-nặng (receive-heavy).

Một khi mức sử dụng giao diện mạng đạt tới 100%, nó trở thành một nút thắt cổ chai, giới hạn hiệu năng.

Một số công cụ báo cáo hoạt động mạng chỉ theo các thuật ngữ gói tin, không phải byte. Vì kích thước gói tin có thể thay đổi rất lớn (như đã đề cập trước đó), không thể liên hệ số lượng gói tin với số byte để tính toán thông lượng hoặc mức sử dụng (dựa trên thông lượng).

### 10.3.11 Các kết nối Cục bộ (Local Connections)
Mạng có thể xảy ra giữa hai ứng dụng trên cùng một hệ thống. Những kết nối *localhost* này và sử dụng một giao diện mạng ảo: *loopback*.

Các môi trường ứng dụng phân tán thường được chia thành các phần logic liên lạc qua mạng. Những phần này có thể bao gồm các máy chủ web, các máy chủ cơ sở dữ liệu, các máy chủ đệm ẩn (caching servers), các máy chủ proxy, và các máy chủ ứng dụng. Nếu chúng đang chạy trên cùng một máy chủ, các kết nối của chúng là tới localhost.

Việc kết nối qua IP tới localhost là kỹ thuật *IP sockets* của giao tiếp liên tiến trình (IPC). Một kỹ thuật khác là Unix domain sockets (UDS), thứ tạo ra một tập tin trên hệ thống tập tin cho việc giao tiếp. Hiệu năng có thể tốt hơn với UDS, vì network stack TCP/IP của kernel có thể được bỏ qua, bỏ qua mã kernel và các chi phí đóng gói gói tin giao thức.

Đối với các TCP/IP sockets, kernel có thể phát hiện kết nối localhost sau handshake, và sau đó đi tắt qua TCP/IP stack cho các lần truyền tải dữ liệu, cải thiện hiệu năng. Điều này đã được phát triển như một tính năng của Linux kernel, được gọi là *TCP friends*, nhưng đã không được sáp nhập [Corbet 12]. BPF hiện nay có thể được sử dụng trên Linux cho mục đích này, như được thực hiện bởi phần mềm Cilium cho hiệu năng và bảo mật mạng container [Cilium 20a].

## 10.4 Kiến trúc (Architecture)
Phần này giới thiệu kiến trúc mạng: các giao thức, phần cứng, và phần mềm. Những thứ này đã được tóm tắt như nền tảng cho phân tích hiệu năng và tinh chỉnh, với trọng tâm là hiệu năng. Để biết thêm chi tiết, bao gồm các chủ đề mạng chung, hãy xem các văn bản mạng [Stevens 93][Hassan 03], RFCs, và tài liệu của nhà cung cấp cho phần cứng mạng. Một số trong số này được liệt kê ở cuối chương.

### 10.4.1 Các giao thức (Protocols)
Trong phần này, các tính năng hiệu năng và đặc tính của IP, TCP, UDP, và QUIC được tóm tắt. Cách các giao thức này được triển khai trong phần cứng và phần mềm (bao gồm các tính năng chẳng hạn như segmentation offload, hàng đợi kết nối, và buffering) được mô tả trong các phần phần cứng và phần mềm sau đó.

**IP**
Internet Protocol (IP) phiên bản 4 và 6 bao gồm một trường để thiết lập hiệu năng mong muốn của một kết nối: trường Type of Service trong IPv4, và trường Traffic Class trong IPv6. Những trường này từ đó đã được định nghĩa lại để chứa một Differentiated Services Code Point (DSCP) (RFC 2474) [Nichols 98] và một trường Explicit Congestion Notification (ECN) (RFC 3168) [Ramakrishnan 01].

DSCP được thiết kế để hỗ trợ các *service classes* khác nhau, mỗi lớp có các đặc tính khác nhau bao gồm xác suất rớt gói tin. Các ví dụ về lớp dịch vụ bao gồm: điện thoại, video phát sóng, dữ liệu độ trễ thấp, thông lượng cao, và dữ liệu ưu tiên thấp.

ECN là một cơ chế cho phép các máy chủ, router, hoặc switch trên đường dẫn truyền tín hiệu rõ ràng về sự hiện diện của tắc nghẽn bằng cách thiết lập một bit trong IP header, thay vì đánh rơi một gói tin. Bên nhận sẽ phản hồi tín hiệu này lại cho bên gửi, người sau đó có thể điều tiết việc truyền tải. Điều này cung cấp các lợi ích của việc tránh tắc nghẽn mà không phải chịu hình phạt về việc đánh rơi gói tin (miễn là bit ECN được sử dụng chính xác trên toàn mạng).

**TCP**
Transmission Control Protocol (TCP) là một tiêu chuẩn Internet thường được sử dụng để tạo ra các kết nối mạng đáng tin cậy. TCP được quy định bởi RFC 793 [Postel 81] và các bổ sung sau này.

Về mặt hiệu năng, TCP có thể cung cấp một tốc độ thông lượng cao ngay cả trên các mạng có độ trễ cao, nhờ việc sử dụng buffering và một *sliding window*. TCP cũng sử dụng congestion control và một *congestion window* được thiết lập bởi bên gửi, sao cho nó có thể duy trì một tốc độ truyền tải cao nhưng cũng đáng tin cậy qua các mạng khác nhau và các mạng đang thay đổi. Congestion control tránh việc gửi đi quá nhiều gói tin, thứ có thể gây ra tắc nghẽn và sụt giảm hiệu năng.

Sau đây là bản tóm tắt các tính năng hiệu năng TCP, bao gồm các sự bổ sung kể từ đặc tả gốc:
- **Sliding window:** Điều này cho phép nhiều gói tin lên tới kích thước của cửa sổ được gửi lên mạng trước khi các xác nhận được nhận về, cung cấp thông lượng cao ngay cả trên các mạng có độ trễ cao. Kích thước của cửa sổ được quảng cáo bởi bên nhận để chỉ ra bao nhiêu gói tin nó sẵn lòng nhận tại thời điểm đó.
- **Congestion avoidance:** Để ngăn chặn việc gửi quá nhiều dữ liệu và gây ra bão hòa, thứ có thể gây ra rớt gói tin và hiệu năng tệ hơn.
- **Slow-start:** Một phần của TCP congestion control, điều này bắt đầu với một congestion window nhỏ và sau đó tăng dần khi các xác nhận (ACKs) được nhận về trong một khoảng thời gian nhất định. Khi chúng không được nhận, congestion window bị giảm xuống.
- **Selective acknowledgments (SACKs):** Cho phép TCP xác nhận các gói tin không liên tục, làm giảm số lượng truyền lại cần thiết.
- **Fast retransmit:** Thay vì chờ đợi một bộ định thời, TCP có thể truyền lại các gói tin bị đánh rơi dựa trên việc đến của các ACKs trùng lặp (duplicate ACKs). Đây là một chức năng của thời gian vòng lặp (round-trip time) chứ không phải là bộ định thời thông thường chậm hơn nhiều.
- **Fast recovery:** Điều này khôi phục hiệu năng TCP sau khi phát hiện các ACKs trùng lặp, bằng cách thiết lập lại kết nối để thực hiện slow-start.
- **TCP fast open:** Cho phép một máy khách bao gồm dữ liệu trong một gói tin SYN, sao cho việc xử lý yêu cầu máy chủ có thể bắt đầu sớm hơn và không phải chờ đợi cho TCP handshake (RFC 7413). Việc này có thể sử dụng một cryptographic cookie để xác thực máy khách.
- **TCP timestamps:** Bao gồm một dấu thời gian cho các gói tin được gửi thứ được trả về trong ACK, sao cho thời gian vòng lặp đó có thể được đo lường (RFC 1323) [Jacobson 92].
- **TCP SYN cookies:** Cung cấp các cookie mật mã cho các máy khách trong các đợt tấn công TCP SYN flood (backlogs đầy) sao cho các máy khách hợp lệ có thể tiếp tục kết nối, mà không cần máy chủ phải lưu trữ thêm dữ liệu cho những nỗ lực kết nối này.

Trong một số trường hợp, các tính năng này được triển khai bằng cách sử dụng các tùy chọn TCP mở rộng được thêm vào giao thức header.

Các chủ đề quan trọng cho hiệu năng TCP bao gồm three-way handshake, phát hiện rớt gói tin, các thuật toán congestion control, Nagle, trì hoãn ACKs, SACK, và FACK.

**Three-Way Handshake**
Các kết nối TCP được thiết lập bằng cách sử dụng một three-way handshake giữa các máy chủ. Một máy chủ thụ động lắng nghe các kết nối; máy chủ kia tích cực khởi tạo kết nối. Để làm rõ thuật ngữ: *passive* và *active* là từ RFC 793 [Postel 81]; tuy nhiên, chúng thường được gọi tương ứng là *listen* và *connect*, sau socket API. Đối với mô hình client/server, máy chủ thực hiện listen và các máy khách thực hiện connect.

Three-way handshake được mô tả trong Hình 10.6.

(Hình 10.6 TCP three-way handshake)

Độ trễ kết nối từ máy khách được chỉ ra, thứ hoàn thành khi ACK cuối cùng được gửi. Sau đó, việc truyền tải dữ liệu có thể bắt đầu.

Hình này cho thấy độ trễ trường hợp tốt nhất cho một handshake. Một gói tin có thể bị đánh rơi, thêm độ trễ khi nó hết thời gian chờ và được truyền lại.

Một khi three-way handshake hoàn thành, phiên TCP được đặt vào trạng thái ESTABLISHED.

**Trạng thái và Bộ định thời (States and Timers)**
Các phiên TCP chuyển đổi giữa các trạng thái TCP dựa trên các gói tin và các sự kiện socket. Các trạng thái là LISTEN, SYN-SENT, SYN-RECEIVED, ESTABLISHED, FIN-WAIT-1, FIN-WAIT-2, CLOSE-WAIT, CLOSING, LAST-ACK, TIME-WAIT, và CLOSED [Postel 80]. Phân tích hiệu năng thường tập trung vào những cái ở trạng thái ESTABLISHED, đó là các kết nối đang hoạt động. Các kết nối như vậy có thể đang truyền tải dữ liệu, hoặc rảnh rỗi chờ đợi sự kiện tiếp theo: một lần truyền tải dữ liệu hoặc đóng kết nối.

Một phiên đã đóng hoàn toàn sẽ đi vào trạng thái TIME_WAIT sao cho các gói tin muộn không bị nhầm lẫn với một kết nối mới trên cùng các cổng. Điều này có thể dẫn đến một vấn đề cạn kiệt tài nguyên hiệu năng, được giải thích trong Mục 10.5.7, Phân tích TCP.

Một số trạng thái có các bộ định thời liên kết với chúng. TIME_WAIT thường là hai phút (một số kernel, chẳng hạn như Windows kernel, cho phép nó được tinh chỉnh). Có thể cũng có một bộ định thời "keep alive" trên ESTABLISHED, được đặt thành một khoảng thời gian dài (ví dụ: hai giờ), để kích hoạt các gói tin thăm dò nhằm kiểm tra xem máy chủ từ xa có còn hoạt động hay không.

**Phát hiện ACK trùng lặp (Duplicate ACK Detection)**
Phát hiện ACK trùng lặp được sử dụng bởi các thuật toán truyền lại nhanh (fast retransmit) và phục hồi nhanh (fast recovery) để nhanh chóng phát hiện khi một gói tin được gửi (hoặc ACK của nó) bị mất. Nó hoạt động như sau:
1. Bên gửi gửi một gói tin với số thứ tự 10.
2. Bên nhận phản hồi bằng một ACK cho số thứ tự 11.
3. Bên gửi gửi 11, 12, và 13.
4. Gói tin 11 bị đánh rơi.
5. Bên nhận phản hồi cho cả 12 và 13 bằng cách gửi một ACK cho 11, thứ nó vẫn đang mong đợi.
6. Bên gửi nhận được các ACKs trùng lặp cho 11.

Phát hiện ACK trùng lặp cũng được sử dụng bởi các thuật toán tránh tắc nghẽn (congestion avoidance) khác nhau.

**Truyền lại (Retransmits)**
Hai cơ chế phổ biến được TCP sử dụng để phát hiện và truyền lại các gói tin bị mất là:
- **Truyền lại dựa trên bộ định thời (Timer-based retransmits):** Những điều này xảy ra khi một thời gian đã trôi qua và một xác nhận gói tin chưa được nhận về. Thời gian này là TCP retransmit timeout, được tính toán động dựa trên thời gian vòng lặp (RTT) của kết nối. Trên Linux, thời gian này ít nhất sẽ là 200 ms (TCP_RTO_MIN) cho lần truyền lại đầu tiên, và các lần truyền lại tiếp theo sẽ chậm hơn nhiều, tuân theo một thuật toán exponential backoff làm gấp đôi thời gian hết hạn (timeout).
- **Truyền lại nhanh (Fast retransmits):** Khi nhận được các ACKs trùng lặp, TCP có thể giả định rằng một gói tin đã bị đánh rơi và truyền lại nó ngay lập tức.

Để cải thiện hơn nữa hiệu năng, các cơ chế bổ sung đã được phát triển để tránh việc truyền lại dựa trên bộ định thời. Một vấn đề xảy ra là khi gói tin được truyền cuối cùng bị mất, và không có các gói tin tiếp theo để kích hoạt phát hiện ACK trùng lặp. (Cân nhắc ví dụ trước đó với việc mất gói tin 13.) Vấn đề này được giải quyết bởi Tail Loss Probe (TLP), thứ gửi một gói tin bổ sung (thăm dò) sau một khoảng thời gian hết hạn ngắn trên lần truyền cuối cùng để giúp phát hiện mất gói tin [Dukkipati 13].

Các thuật toán điều khiển tắc nghẽn (Congestion control algorithms) cũng có thể điều tiết thông lượng khi có sự hiện diện của các lần truyền lại.

**Các kiểm soát Tắc nghẽn (Congestion Controls)**
Các thuật toán điều khiển tắc nghẽn đã được phát triển để duy trì hiệu năng trên các mạng bị tắc nghẽn. Một số hệ thống vận hành (bao gồm dựa trên Linux) cho phép thuật toán được lựa chọn như một phần của việc tinh chỉnh hệ thống. Các thuật toán này bao gồm:
- **Reno:** Kích hoạt ACK trùng lặp ba lần: giảm một nửa congestion window, giảm một nửa ngưỡng slow-start, truyền lại nhanh, và phục hồi nhanh.
- **Tahoe:** Kích hoạt ACK trùng lặp ba lần: truyền lại nhanh, giảm một nửa ngưỡng slow-start, congestion window được đặt thành một kích thước đoạn tối đa (MSS), và slow-start. (Cùng với Reno, Tahoe được phát triển lần đầu tiên cho 4.3BSD.)
- **CUBIC:** Sử dụng một hàm bậc ba (do đó có tên như vậy) để chia tỉ lệ cửa sổ, và một hàm "hybrid start" để thoát slow-start nhanh hơn. CUBIC có xu hướng tích cực hơn Reno, và là mặc định trong Linux.
- **BBR:** Thay vì dựa trên cửa sổ, BBR xây dựng một mô hình rõ ràng về các đặc tính đường dẫn mạng (RTT và băng thông) sử dụng các giai đoạn thăm dò. BBR có thể mang lại hiệu năng tốt hơn đáng kể trên một số đường dẫn mạng, trong khi gây hại cho hiệu năng trên các đường dẫn khác. BBRv2 hiện đang được phát triển và hứa hẹn sẽ khắc phục một số thiếu sót của v1.
- **DCTCP:** DataCenter TCP dựa trên các switch được cấu hình để phát ra Explicit Congestion Notification (ECN) đánh dấu tại một mức chiếm dụng hàng đợi rất nông để nhanh chóng tăng tốc tới băng thông khả dụng. Điều này khiến DCTCP không phù hợp để triển khai qua Internet, nhưng trong một môi trường được điều khiển được cấu hình phù hợp, nó có thể cải thiện hiệu năng đáng kể.

Các thuật toán khác không được liệt kê trước đó bao gồm Vegas, New Reno, và Hybla.

Thuật toán điều khiển tắc nghẽn có thể tạo ra sự khác biệt lớn về hiệu năng mạng. Các dịch vụ đám mây Netflix, ví dụ, sử dụng BBR và thấy rằng nó có thể cải thiện thông lượng gấp ba lần trong các đợt mất gói tin nặng [Ather 17]. Hiểu cách các thuật toán này phản ứng dưới các điều kiện mạng khác nhau là một hoạt động quan trọng khi phân tích hiệu năng TCP.

Linux 5.6, phát hành năm 2020, đã thêm hỗ trợ cho việc phát triển các thuật toán điều khiển tắc nghẽn trong BPF [Corbet 20]. Điều này cho phép chúng được định nghĩa bởi người dùng cuối và được nạp theo yêu cầu.

**Nagle**
Thuật toán này (RFC 896) [Nagle 84] làm giảm số lượng các gói tin nhỏ trên mạng bằng cách trì hoãn việc truyền tải của chúng để cho phép nhiều dữ liệu hơn đến và được kết hợp (coalesced). Việc này chỉ trì hoãn các gói tin nếu có dữ liệu trong pipeline và các độ trễ đã được gặp phải.

Hệ thống có thể cung cấp một tham số có thể tinh chỉnh hoặc tùy chọn socket để vô hiệu hóa Nagle, thứ có thể cần thiết nếu hoạt động của nó xung đột với Delayed ACKs (xem Mục 10.8.2, Tùy chọn Socket).

**Delayed ACKs**
Thuật toán này (RFC 1122) [Braden 89] trì hoãn việc gửi các ACKs lên tới 500 ms, sao cho nhiều ACKs có thể được kết hợp. Các thông điệp điều khiển TCP khác cũng có thể được kết hợp, làm giảm số lượng gói tin trên mạng.

Cũng như với Nagle, hệ thống có thể cung cấp một tham số tinh chỉnh để vô hiệu hóa hành vi này.

**SACK, FACK, và RACK**
Thuật toán TCP selective acknowledgment (SACK) cho phép bên nhận thông báo cho bên gửi rằng nó đã nhận được một khối dữ liệu không liên tục. Nếu không có điều này, một đợt rớt gói tin cuối cùng sẽ khiến toàn bộ cửa sổ phải được truyền lại, nhằm bảo toàn sơ đồ xác nhận tuần tự. Điều này gây hại cho hiệu năng TCP và bị tránh trong hầu hết các hệ điều hành hiện đại có hỗ trợ SACK.

SACK đã được mở rộng bằng forward acknowledgments (FACK), thứ được hỗ trợ trong Linux theo mặc định. FACKs tiến xa hơn một bước và điều tiết tốt hơn lượng dữ liệu nổi bật trong mạng, cải thiện hiệu năng tổng thể [Mathis 96].

Cả SACK và FACK đều được sử dụng để cải thiện việc khôi phục mất gói tin. Một thuật toán mới hơn, Recent ACKnowledgment (RACK; hiện được gọi là RACK-TLP với việc tích hợp TLP) sử dụng thông tin thời gian từ các ACKs cho việc phát hiện và phục hồi mất mát tốt hơn thay vì chỉ dựa trên các số thứ tự ACK đơn thuần. Các IWs lớn hơn, tuy nhiên, có thể gây rủi ro các chuỗi ACK một mình [Cheng 20]. Cho FreeBSD, Netflix đã phát triển một TCP stack được tái cấu trúc mới mang tên RACK dựa trên RACK, TLP, và các tính năng khác [Stewart 18].

**Initial Window**
Initial window (IW) là số lượng gói tin một trình gửi TCP sẽ truyền đi tại thời điểm bắt đầu của một kết nối trước khi chờ đợi xác nhận từ trình nhận. Đối với các kết nối ngắn, chẳng hạn như các kết nối HTTP điển hình, một IW đủ lớn để trải dài toàn bộ dữ liệu được truyền tải có thể giảm đáng kể thời gian hoàn thành, cải thiện hiệu năng. Các IWs lớn hơn, tuy nhiên, có thể gây rủi ro tắc nghẽn và rớt gói tin. Điều này đặc biệt bị thổi phồng khi có nhiều luồng bắt đầu cùng một lúc.

Mặc định của Linux (10 gói tin, hay còn gọi là IW10) có thể quá cao trên các liên kết chậm hoặc khi có quá nhiều kết nối bắt đầu; các hệ điều hành khác mặc định là 2 hoặc 4 gói tin (IW2 hoặc IW4).

**UDP**
User Datagram Protocol (UDP) là một tiêu chuẩn Internet thường được sử dụng để gửi các thông điệp, được gọi là *datagrams*, qua một mạng (RFC 768) [Postel 80]. Xét theo hiệu năng, UDP cung cấp:
- **Sự đơn giản:** Các headers giao thức nhỏ và đơn giản làm giảm các chi phí tính toán và kích thước.
- **Statelessness (Không trạng thái):** Các chi phí thấp cho các kết nối và truyền tải.
- **Không truyền lại:** Những điều này thêm các độ trễ đáng kể cho các kết nối TCP.

Trong khi đơn giản và thường có hiệu năng cao, UDP không được thiết kế để đáng tin cậy, và dữ liệu có thể bị thiếu hoặc nhận được sai thứ tự. Điều này khiến nó không phù hợp cho nhiều loại kết nối. UDP cũng không có congestion avoidance và do đó có thể đóng góp vào tắc nghẽn trên mạng.

Một số dịch vụ, bao gồm các phiên bản của NFS, có thể được cấu hình để vận hành qua TCP hoặc UDP tùy ý. Những dịch vụ khác thực hiện broadcast hoặc multicast dữ liệu có thể chỉ sử dụng UDP.

Một mục đích sử dụng chính cho UDP là DNS. Do tính đơn giản của UDP, việc thiếu kiểm soát tắc nghẽn, và hỗ trợ Internet (nó thường không được bảo vệ bởi tường lửa) hiện có các giao thức mới được xây dựng trên UDP triển khai các tính năng và kiểm soát tắc nghẽn riêng của chúng. Một ví dụ là QUIC.

**QUIC và HTTP/3**
QUIC là một giao thức mạng được thiết kế bởi Jim Roskind tại Google như một giải pháp thay thế hiệu năng cao, độ trễ thấp cho TCP, được tối ưu hóa cho HTTP và TLS [Roskind 12]. QUIC được xây dựng trên UDP, và cung cấp nhiều tính năng ưu việt so với nó, bao gồm:
- Khả năng đa luồng (multiplex) vài dòng truyền phát (streams) được định nghĩa bởi ứng dụng trên cùng một "connection."
- Một vận chuyển dòng truyền phát theo thứ tự đáng tin cậy kiểu TCP có thể được tắt tùy ý cho các dòng truyền phát con (substreams) riêng lẻ.
- Việc tiếp tục kết nối khi một máy khách thay đổi địa chỉ mạng của nó, dựa trên các mã định danh kết nối được mã hóa.
- Mã hóa đầy đủ dữ liệu payload, bao gồm cả các QUIC headers.
- Các handshake kết nối 0-RTT bao gồm mã hóa (cho các bên đã liên lạc trước đó).

QUIC đang được sử dụng nặng nề bởi trình duyệt web Chrome.

Trong khi QUIC ban đầu được phát triển bởi Google, Internet Engineering Task Force (IETF) đang trong quá trình chuẩn hóa cả bản thân QUIC transport, và cấu hình cụ thể của việc sử dụng HTTP qua QUIC (sự kết hợp sau này được đặt tên là HTTP/3).

### 10.4.2 Phần cứng
Phần cứng mạng bao gồm các giao diện, bộ điều khiển, switch, router, và tường lửa. Việc hiểu rõ hoạt động của chúng là hữu ích, ngay cả khi chúng được quản lý bởi các nhân viên khác (các quản trị viên mạng).

**Các giao diện (Interfaces)**
Các giao diện mạng gửi và nhận các thông điệp, được gọi là *frames*, trên mạng được gắn kèm. Chúng quản lý các tín hiệu điện, quang, hoặc không dây liên quan, bao gồm cả việc xử lý các lỗi truyền tải.

Các loại giao diện dựa trên các tiêu chuẩn tầng 2, mỗi loại cung cấp một băng thông tối đa. Các giao diện băng thông cao hơn cung cấp độ trễ truyền dữ liệu thấp hơn, với chi phí cao hơn. Khi thiết kế các máy chủ mới, một quyết định then chốt là mức độ cân bằng thường xuyên giữa giá của máy chủ với hiệu năng mạng mong muốn.

Đối với Ethernet, các lựa chọn bao gồm đồng hoặc quang, với các tốc độ tối đa 1 Gbit/s (1 GbE), 10 GbE, 40 GbE, 100 GbE, 200 GbE, và 400 GbE. Nhiều nhà cung cấp sản xuất các giao diện Ethernet, mặc dù hệ điều hành của bạn có thể không có driver hỗ trợ cho một số trong số chúng.

Mức sử dụng giao diện có thể được kiểm tra như thông lượng hiện tại chia cho băng thông đã thương lượng hiện tại. Hầu hết các giao diện có các kênh truyền và nhận riêng biệt, và khi vận hành trong chế độ toàn song công (full-duplex), mức sử dụng của mỗi kênh phải được nghiên cứu một cách riêng biệt.

Các giao diện không dây có thể chịu các vấn đề hiệu năng do cường độ tín hiệu kém và sự nhiễu loạn.

**Các bộ điều khiển (Controllers)**
Các giao diện mạng vật lý được cung cấp cho hệ thống thông qua các bộ điều khiển, được tích hợp vào bảng mạch hệ thống hoặc được cung cấp qua các card mở rộng.

Các bộ điều khiển được điều khiển bởi các bộ vi xử lý và được gắn tới hệ thống thông qua một vận chuyển I/O (ví dụ: PCI). Bất kỳ thứ nào trong số này cũng có thể trở thành yếu tố giới hạn cho thông lượng mạng hoặc IOPS.

Ví dụ, một card giao diện mạng 10 GbE kép được kết nối tới một khe cắm PCI express (PCIe) Gen 2 bốn làn. Card này có băng thông gửi hoặc nhận tối đa là 2 × 10 GbE = 20 Gbits/s, và hai hướng, 40 Gbit/s. Khe cắm có băng thông tối đa 4 × 4 Gbits/s = 16 Gbits/s. Do đó, thông lượng mạng trên cả hai cổng sẽ bị giới hạn bởi băng thông PCIe Gen 2, và không thể chạy cả hai ở tốc độ đường truyền cùng một lúc (tôi biết điều này từ kinh nghiệm thực tế!).

**Các Switch và Router**
Các Switch cung cấp một đường dẫn liên lạc chuyên dụng giữa bất kỳ hai máy chủ được kết nối nào, cho phép nhiều lần truyền tải giữa các cặp máy chủ mà không có sự nhiễu loạn. Công nghệ này đã thay thế các hubs (và trước đó, các bus vật lý dùng chung: cáp đồng trục dày-Ethernet được sử dụng phổ biến), thứ chia sẻ tất cả các gói tin với tất cả các máy chủ. Việc chia sẻ này dẫn đến tranh chấp khi các máy chủ truyền tải đồng thời, được nhận diện bởi giao diện như một *va chạm* (collision) sử dụng thuật toán "carrier sense multiple access with collision detection" (CSMA/CD). Thuật toán này sẽ tắt và truyền lại theo cấp số nhân cho đến khi thành công, tạo ra hiệu năng kém dưới tải. Với việc sử dụng các switch, điều này đã ở phía sau chúng ta, nhưng một số công cụ quan sát vẫn có các bộ đếm va chạm—mặc dù những thứ này thường chỉ xảy ra do các lỗi (thương lượng hoặc đi dây kém).

Các Router phân phối các gói tin giữa các mạng và sử dụng các giao thức mạng và các bảng định tuyến để xác định các đường dẫn phân phối hiệu quả. Phân phối một gói tin giữa hai thành phố có thể liên quan đến một chục hoặc nhiều router hơn, cùng với các phần cứng mạng khác. Các router và các đường dẫn thường được cấu hình để cập nhật linh động, sao cho mạng có thể tự động phản hồi lại các sự cố mạng và router, và để cân bằng tải. Điều này có nghĩa là tại một thời điểm nhất định, không ai có thể chắc chắn đường dẫn mà một gói tin thực sự đang đi. Với nhiều đường dẫn khả thi, cũng có tiềm năng cho các gói tin được phân phối sai thứ tự, thứ có thể gây ra các vấn đề hiệu năng TCP.

Yếu tố bí ẩn này trên mạng thường bị đổ lỗi cho hiệu năng kém: có lẽ lưu lượng mạng nặng—từ các máy chủ không liên quan khác—đang làm bão hòa một router giữa nguồn và đích? Do đó, các nhóm quản trị mạng thường xuyên được yêu cầu giải oan cho hạ tầng của họ. Họ có thể làm như vậy bằng cách sử dụng các công cụ giám sát thời gian thực nâng cao để kiểm tra tất cả các router và các thành phần mạng liên quan.

Cả router và switch đều bao gồm các bộ đệm và bộ vi xử lý, chính những thứ này có thể trở thành các nút thắt cổ chai hiệu năng dưới tải. Như một ví dụ cực đoan, một switch 10 GbE ban đầu có thể hỗ trợ tổng cộng không quá 11 Gbits/s trên tất cả các cổng, do dung lượng CPU giới hạn của nó.

Lưu ý rằng các switch và router cũng thường là nơi xảy ra các *chuyển đổi tốc độ* (rate transitions) (chuyển đổi từ băng thông này sang băng thông khác, ví dụ: các liên kết 10 Gbps chuyển đổi sang một liên kết 1 Gbps). Khi điều này xảy ra, một số buffering là cần thiết để tránh việc rớt gói tin quá mức, nhưng không phải tất cả các nhà cung cấp thiết bị mạng đều hỗ trợ chúng. Pacing tại nguồn cũng có thể là một cách để giảm bớt các vấn đề với việc chuyển đổi tốc độ bằng cách làm cho lưu lượng ít bị bùng phát hơn.

**Firewalls (Tường lửa)**
Tường lửa thường được sử dụng để chỉ cho phép các giao tiếp được ủy quyền dựa trên một bộ quy tắc được cấu hình, cải thiện tính bảo mật của mạng. Chúng có thể hiện diện dưới dạng cả các thiết bị mạng vật lý và phần mềm kernel.

Tường lửa có thể trở thành một nút thắt cổ chai hiệu năng, đặc biệt khi được cấu hình ở trạng thái (stateful). Tường lửa có trạng thái lưu trữ metadata cho mỗi kết nối được thấy, và tường lửa có thể gặp phải mức sử dụng bộ nhớ quá mức khi xử lý nhiều kết nối. Điều này có thể xảy ra do một cuộc tấn công từ chối dịch vụ (DoS) cố gắng làm tràn ngập một mục tiêu với các kết nối. Nó cũng có thể xảy ra với tốc độ kết nối outbound cao, vì chúng có thể yêu cầu theo dõi kết nối tương tự.

Vì tường lửa là phần cứng hoặc phần mềm tùy chỉnh, các công cụ sẵn có để phân tích chúng phụ thuộc vào từng sản phẩm tường lửa. Xem tài liệu hướng dẫn tương ứng của chúng.

Việc sử dụng BPF mở rộng để triển khai các tường lửa trên phần cứng thương mại đang gia tăng, do hiệu năng, khả năng lập trình, tính dễ sử dụng và chi phí cuối cùng của nó. Các công ty đang áp dụng tường lửa BPF và các giải pháp DDoS bao gồm Facebook [Deepak 18], Cloudflare [Majkowski 18], và Cilium [Cilium 20a].

Tường lửa cũng có thể là một phiền toái trong quá trình kiểm tra hiệu năng: thực hiện một thực nghiệm băng thông mạng khi gỡ lỗi một vấn đề có thể liên quan đến việc sửa đổi các quy tắc tường lửa để cho phép kết nối (và phối hợp điều đó với nhóm bảo mật).

**Các thành phần khác**
Môi trường của bạn có thể bao gồm các thiết bị mạng vật lý khác, chẳng hạn như hubs, bridges, repeaters, và modems. Bất kỳ thứ nào trong số này cũng có thể là một nguồn gây ra các nút thắt cổ chai hiệu năng và các gói tin bị đánh rơi.

### 10.4.3 Phần mềm
Phần mềm mạng bao gồm network stack, TCP, và các trình điều khiển thiết bị. Các chủ đề liên quan đến hiệu năng được thảo luận trong phần này.

**Network Stack**
Các thành phần và các tầng liên quan phụ thuộc vào loại hệ điều hành, phiên bản, các giao thức, và các giao diện đang được sử dụng. Hình 10.7 mô tả một mô hình chung, trình bày các thành phần phần mềm.

(Hình 10.7 Network stack chung)

Trên các kernel hiện đại, stack là đa luồng, và các gói tin inbound có thể được xử lý bởi nhiều CPUs.

**Linux**
Network stack của Linux được trình bày trong Hình 10.8, bao gồm vị trí của các socket send/receive buffers và các hàng đợi gói tin.

Trên các hệ thống Linux, network stack là một thành phần kernel cốt lõi, và các trình điều khiển thiết bị là các mô-đun bổ sung. Các gói tin được truyền qua các thành phần kernel này dưới dạng cấu trúc sk_buff (socket buffer) data type. Lưu ý rằng cũng có thể có việc xếp hàng ở tầng IP (không được vẽ trong hình) cho việc lắp ráp lại gói tin.

Các phần sau đây thảo luận về các chi tiết triển khai Linux liên quan đến hiệu năng: hàng đợi kết nối TCP, TCP buffering, các hàng đợi kỷ luật (queueing disciplines), mở rộng quy mô CPU (CPU scaling), và kernel bypass. Giao thức TCP đã được mô tả trong phần trước.

(Hình 10.8 Linux network stack)

**Hàng đợi kết nối TCP (TCP Connection Queues)**
Các đợt bùng phát kết nối inbound được xử lý bằng cách sử dụng các hàng đợi backlog. Có hai hàng đợi như vậy, một cho các kết nối chưa hoàn thành trong khi TCP handshake hoàn tất (còn được gọi là *SYN backlog*), và một cho các phiên đã thiết lập đang chờ ứng dụng được chấp nhận (còn được gọi là *listen backlog*). Những điều này được mô tả trong Hình 10.9.

Chỉ có một hàng đợi được sử dụng trong các kernel trước đó, và nó dễ bị tấn công SYN floods. Một SYN flood là một loại tấn công DoS liên quan đến việc gửi vô số các gói tin SYN tới cổng lắng nghe từ các địa chỉ IP giả mạo. Điều này làm đầy hàng đợi backlog trong khi TCP chờ đợi để hoàn thành handshake, ngăn cản các máy khách thực sự kết nối.

Với hai hàng đợi, cái đầu tiên có thể đóng vai trò như một khu vực dàn dựng cho các kết nối tiềm năng, thứ chỉ được thăng cấp lên hàng đợi thứ hai khi kết nối đã được thiết lập. Hàng đợi đầu tiên có thể được tạo ra đủ dài để hấp thụ các đợt SYN floods và được tối ưu hóa để chỉ lưu trữ lượng metadata tối thiểu cần thiết.

(Hình 10.9 Các hàng đợi TCP backlog)

Việc sử dụng SYN cookies bỏ qua hàng đợi đầu tiên, vì chúng cho thấy máy khách đã được ủy quyền.

Độ dài của các hàng đợi này có thể được tinh chỉnh độc lập (xem Mục 10.8, Tinh chỉnh). Hàng đợi thứ hai cũng có thể được thiết lập bởi đối số backlog của listen(2).

**TCP Buffering**
Thông lượng dữ liệu được cải thiện bằng cách sử dụng các bộ đệm gửi và nhận liên kết với socket. Những điều này được mô tả trong Hình 10.10.

(Hình 10.10 Gửi và nhận bộ đệm TCP)

Kích thước của cả bộ đệm gửi và nhận đều có thể tinh chỉnh được. Kích thước lớn hơn cải thiện hiệu năng thông lượng, với chi phí là tiêu tốn thêm bộ nhớ chính cho mỗi kết nối. Một bộ đệm có thể được thiết lập lớn hơn bộ đệm kia nếu máy chủ được kỳ vọng sẽ thực hiện nhiều việc gửi hoặc nhận hơn. Kernel Linux cũng sẽ tự động tăng kích thước của các bộ đệm này dựa trên hoạt động kết nối, và cho phép tinh chỉnh các kích thước tối thiểu, mặc định, và tối đa của chúng.

**Segmentation Offload: GSO và TSO**
Các thiết bị mạng và các mạng chấp nhận kích thước gói tin lên tới một giá trị maximum segment size (MSS) nhất định, thứ có thể nhỏ tới mức 1,500 byte. Để tránh các chi phí network stack của việc gửi nhiều gói tin nhỏ, Linux sử dụng generic segmentation offload (GSO) để gửi các gói tin lên tới 64 Kbytes ("super packets"), thứ được chia thành các phân đoạn kích thước MSS ngay trước khi phân phối tới thiết bị mạng. Nếu NIC và trình điều khiển hỗ trợ TCP segmentation offload (TSO), GSO chuyển việc phân chia cho thiết bị, cải thiện thông lượng mạng. Cũng có một giải pháp tương đương nhận chung (generic receive offload - GRO) bổ trợ cho GSO [Linux 20i]. GRO và GSO được triển khai trong phần mềm kernel, và TSO được triển khai bởi phần cứng NIC.

**Queueing Discipline (Kỷ luật Xếp hàng)**
Đây là một tầng tùy chọn cho việc quản lý phân loại lưu lượng (tc), lập lịch, thao tác, lọc, và định hình các gói tin mạng. Linux cung cấp vô số các thuật toán kỷ luật xếp hàng (qdiscs), thứ có thể được cấu hình bằng lệnh tc(8). Khi mỗi cái có một trang man, lệnh man(1) có thể được sử dụng để liệt kê chúng:
```bash
# man -k tc-
tc-actions (8)       - independently defined actions in tc
tc-basic (8)         - basic traffic control filter
tc-bfifo (8)         - Packet limited First In, First Out queue
tc-bpf (8)           - BPF programmable classifier and actions for ingress/egress
queueing disciplines
tc-cbq (8)           - Class Based Queueing
tc-cbq-details (8)   - Class Based Queueing
tc-cbs (8)           - Credit Based Shaper (CBS) Qdisc
tc-cgroup (8)        - control group based traffic control filter
tc-choke (8)         - choose and keep scheduler
tc-codel (8)         - Controlled-Delay Active Queue Management algorithm
tc-connmark (8)      - netfilter connmark retriever action
tc-csum (8)          - checksum update action
tc-drr (8)           - deficit round robin scheduler
tc-ematch (8)        - extended matches for use with "basic" or "flow" filters
tc-flow (8)          - flow based traffic control filter
tc-flower (8)        - flow based traffic control filter
tc-fq (8)            - Fair Queue traffic policing
tc-fq_codel (8)      - Fair Queuing (FQ) with Controlled Delay (CoDel)
[...]
```
Kernel Linux thiết lập pfifo_fast làm qdisc mặc định, trong khi systemd ít bảo thủ hơn và thiết lập nó thành fq_codel để giảm bớt bufferbloat tiềm tàng, với chi phí là độ phức tạp cao hơn một chút trong lớp qdisc.

BPF có thể tăng cường khả năng của tầng này với các chương trình loại BPF_PROG_TYPE_SCHED_CLS và BPF_PROG_TYPE_SCHED_ACT. Những chương trình BPF này có thể được gắn vào kernel ingress và egress points cho việc lọc gói tin, thao tác, và chuyển tiếp, như được sử dụng bởi các trình cân bằng tải (load balancers) và tường lửa.

**Trình điều khiển thiết bị mạng (Network Device Drivers)**
Trình điều khiển thiết bị mạng thường có một bộ đệm bổ sung—một ring buffer—để gửi và nhận các gói tin giữa bộ nhớ kernel và NIC. Điều này đã được mô tả trong Hình 10.8 như trình điều khiển hàng đợi (driver queue).

Một tính năng hiệu năng ngày càng trở nên phổ biến với mạng tốc độ cao là việc sử dụng *interrupt coalescing mode*. Thay vì ngắt quãng kernel cho mỗi gói tin đến, một ngắt chỉ được gửi khi một bộ định thời (polling) hoặc một số lượng gói tin nhất định đã đạt tới. Điều này làm giảm tốc độ kernel bị ngắt quãng với card mạng, cho phép truyền tải lớn hơn để được buffer, dẫn đến thông lượng lớn hơn, mặc dù có một số chi phí về độ trễ.

Kernel Linux sử dụng một framework API (NAPI) mới sử dụng một kỹ thuật giảm thiểu ngắt: đối với tốc độ gói tin thấp, các ngắt được sử dụng (quá trình xử lý được lập lịch qua một softirq); đối với tốc độ gói tin cao, các ngắt được vô hiệu hóa, và việc polling được sử dụng để cho phép kết hợp [Corbet 03][Corbet 06b]. Điều này mang lại độ trễ thấp hoặc thông lượng cao, tùy thuộc vào khối lượng công việc. Các tính năng khác của NAPI bao gồm:
- **Packet throttling:** cho phép rớt gói tin sớm trong card mạng để ngăn chặn hệ thống bị tràn ngập bởi các cơn bão gói tin.
- **Interface scheduling:** nơi một hạn ngạch (quota) được sử dụng để giới hạn các bộ đệm được xử lý trong một chu kỳ polling, nhằm đảm bảo sự công bằng giữa các giao diện mạng bận rộn.
- **Support cho tùy chọn socket SO_BUSY_POLL:** nơi các ứng dụng cấp người dùng có thể giảm bớt độ trễ mạng bằng cách yêu cầu *busy wait* (xoay vòng trên CPU cho đến khi một sự kiện xảy ra) trên một socket [Dumazet 17a].

Kết hợp (Coalescing) có thể đặc biệt quan trọng để cải thiện mạng máy ảo, và được sử dụng bởi trình điều khiển mạng ena được sử dụng bởi AWS EC2.

**NIC Gửi và Nhận**
Đối với các gói tin được gửi, NIC được thông báo và thường đọc gói tin (khung hình) từ bộ nhớ kernel sử dụng truy cập bộ nhớ trực tiếp (DMA) để đạt được hiệu quả. Các NIC cung cấp các transmit descriptors để quản lý các gói tin DMA; nếu NIC không có các descriptors trống, network stack sẽ tạm dừng việc truyền tải để cho phép NIC bắt kịp.

Đối với các gói tin nhận được, các NIC có thể sử dụng DMA để đặt gói tin vào hàng đợi kernel ring-buffer và sau đó thông báo cho kernel bằng một ngắt (thứ có thể bị bỏ qua để cho phép kết hợp). Ngắt kích hoạt một softirq để phân phối gói tin tới network stack để xử lý thêm.

**CPU Scaling**
Tốc độ gói tin cao có thể đạt được bằng cách huy động nhiều CPU để xử lý các gói tin và chồng giao thức TCP/IP. Linux hỗ trợ các phương pháp khác nhau cho việc xử lý gói tin đa CPU (xem Documentation/networking/scaling.txt):
- **RSS: Receive Side Scaling:** Đối với các NIC hiện đại hỗ trợ nhiều hàng đợi và có thể băm các gói tin vào các hàng đợi khác nhau, thứ lần lượt được xử lý bởi các CPU khác nhau, ngắt quãng chúng trực tiếp. Bản băm này có thể dựa trên địa chỉ IP và các số cổng TCP, sao cho các gói tin từ cùng một kết nối cuối cùng được xử lý bởi cùng một CPU.
- **RPS: Receive Packet Steering:** Một triển khai phần mềm của RSS, cho các NIC không hỗ trợ nhiều hàng đợi. Điều này liên quan đến một thói quen dịch vụ ngắt ngắn để ánh xạ gói tin inbound tới một CPU để xử lý. Một bản băm tương tự có thể được sử dụng để ánh xạ các gói tin tới các CPU, dựa trên các trường từ các packet headers.
- **RFS: Receive Flow Steering:** Điều này tương tự như RPS, nhưng có mối quan hệ (affinity) cho nơi socket đã được xử lý lần cuối trên CPU, để cải thiện tỷ lệ trúng bộ đệm CPU và tính cục bộ của bộ nhớ.
- **Accelerated Receive Flow Steering:** Điều này đạt được RFS trong phần cứng, cho các NIC hỗ trợ tính năng này. Nó liên quan đến việc cập nhật NIC với thông tin luồng sao cho nó có thể xác định CPU nào cần ngắt.
- **XPS: Transmit Packet Steering:** Cho các NIC với nhiều hàng đợi truyền tải, điều này hỗ trợ việc truyền tải bởi nhiều CPU tới các hàng đợi.

Không có một chiến lược cân bằng tải CPU cho các gói tin mạng, một NIC có thể chỉ ngắt quãng một CPU duy nhất, thứ có thể đạt mức sử dụng 100% và trở thành một nút thắt cổ chai. Điều này có thể hiển thị như thời gian softirq CPU cao trên một CPU duy nhất (ví dụ: sử dụng Linux mpstat(1): xem Chương 6, CPUs, Mục 6.6.3, mpstat). Điều này có thể đặc biệt xảy ra đối với các trình cân bằng tải (load balancers) hoặc các máy chủ proxy (ví dụ: nginx), khi khối lượng công việc dự kiến của chúng là các gói tin inbound.

Ánh xạ các ngắt tới các CPU dựa trên các yếu tố chẳng hạn như tính nhất quán của bộ đệm ẩn, như được thực hiện bởi RFS, có thể cải thiện đáng kể hiệu năng mạng. Điều này cũng có thể được thực hiện bởi daemon irqbalance, thứ gán các dòng yêu cầu ngắt (IRQ) tới các CPU.

**Kernel Bypass**
Hình 10.8 trình bày đường dẫn được thực hiện phổ biến nhất qua TCP/IP stack. Các ứng dụng có thể bỏ qua network stack kernel bằng cách sử dụng các công nghệ chẳng hạn như Data Plane Development Kit (DPDK) nhằm đạt được tốc độ gói tin cao hơn và hiệu năng tốt hơn. Điều này liên quan đến một ứng dụng tự triển khai các giao thức mạng của chính nó trong không gian người dùng, và thực hiện việc ghi trực tiếp vào card giao diện mạng qua một thư viện DPDK và một trình điều khiển kernel user space I/O (UIO) hoặc virtual function I/O (VFIO). Chi phí của việc sao chép dữ liệu có thể tránh được bằng cách truy cập trực tiếp bộ nhớ trên NIC.

Công nghệ eXpress Data Path (XDP) cung cấp một đường dẫn khác cho các gói tin mạng: một con đường nhanh có thể lập trình được sử dụng BPF mở rộng và tích hợp vào network stack kernel hiện có thay vì bỏ qua nó [Høiland-Jørgensen 18]. (DPDK hiện hỗ trợ XDP cho việc nhận gói tin, di chuyển một số chức năng trở lại kernel [DPDK 20].)

Với network stack bypass của kernel, sự instrumentation sử dụng các công cụ và các chỉ số truyền thống là không khả dụng vì các bộ đếm và các sự kiện truy vết mà chúng sử dụng cũng bị bỏ qua. Điều này làm cho việc phân tích hiệu năng trở nên khó khăn hơn.

Bên cạnh việc bỏ qua toàn bộ stack, còn có các khả năng để tránh chi phí của việc sao chép dữ liệu: cờ `MSG_ZEROCOPY` send(2), và nhận không-sao-chép (zero-copy receive) qua mmap(2) [Linux 20c][Corbet 18b].

**Các tối ưu hóa khác**
Có các thuật toán khác đang được sử dụng xuyên suốt Linux network stack để cải thiện hiệu năng. Hình 10.11 trình bày các thành phần cho đường dẫn gửi TCP (nhiều trong số này được gọi từ hàm kernel tcp_write_xmit()).

(Hình 10.11 Đường dẫn gửi TCP)

Một số thành phần và thuật toán này đã được mô tả trước đó (bộ đệm gửi socket, TSO, các kiểm soát tắc nghẽn, Nagle, và qdiscs); những cái khác bao gồm:
- **Pacing:** Điều này kiểm soát khi nào gửi các gói tin, rải các lần truyền tải (pacing) để tránh các đợt bùng phát có thể gây hại cho hiệu năng (điều này có thể giúp tránh TCP micro-bursts thứ có thể dẫn đến độ trễ xếp hàng, hoặc thậm chí khiến các network switches đánh rơi gói tin. Nó cũng có thể giúp ích với vấn đề *incast*, khi nhiều endpoint truyền tới một endpoint cùng một lúc [Fritchie 12]).
- **TCP Small Queues (TSQ):** Kiểm soát này (làm giảm) lượng dữ liệu được xếp hàng bởi network stack để giải quyết các vấn đề bao gồm bufferbloat [Bufferbloat 20].
- **Byte Queue Limits (BQL):** Những thứ này tự động thay đổi kích thước các hàng đợi trình điều khiển để tránh tình trạng "đói" (starvation), nhưng cũng đủ nhỏ để giảm độ trễ tối đa của các gói tin được xếp hàng, và để tránh làm cạn kiệt các NIC descriptors [Hrubý 12]. Nó hoạt động bằng cách tạm dừng việc thêm các gói tin vào hàng đợi trình điều khiển khi cần thiết, và được thêm vào trong Linux 3.3 [Siemon 13].
- **Earliest Departure Time (EDT):** Điều này sử dụng một vòng quay thời gian (timing wheel) thay vì một hàng đợi để ra lệnh cho các gói tin được gửi tới NIC. Các dấu thời gian được thiết lập trên mỗi gói tin dựa trên chính sách và cấu hình tốc độ. Việc này được thêm vào trong Linux 4.20, và có các khả năng giống như BQL- và TSQ. [Jacobson 18].

Các thuật toán này thường hoạt động kết hợp để cải thiện hiệu năng. Một gói tin gửi TCP có thể được xử lý bởi bất kỳ kiểm soát tắc nghẽn nào, TSO, TSQ, pacing, và các kỷ luật xếp hàng, trước khi nó thực sự đến được NIC [Cheng 16].

---

## 10.5 Phương pháp luận (Methodology)
Phần này mô tả các phương pháp luận và các bài tập cho việc phân tích và tinh chỉnh mạng. Bảng 10.2 tóm tắt các chủ đề.

Bảng 10.2 Các phương pháp luận hiệu năng mạng
| Mục | Phương pháp luận | Các loại |
| --- | --- | --- |
| 10.5.1 | Phương pháp công cụ | Phân tích quan sát |
| 10.5.2 | Phương pháp USE | Phân tích quan sát |
| 10.5.3 | Đặc tính hóa khối lượng công việc | Phân tích quan sát, quy hoạch dung lượng |
| 10.5.4 | Phân tích độ trễ | Phân tích quan sát |
| 10.5.5 | Giám sát hiệu năng | Phân tích quan sát, quy hoạch dung lượng |
| 10.5.6 | Packet sniffing (Ngửi gói tin) | Phân tích quan sát |
| 10.5.7 | Phân tích TCP | Phân tích quan sát |
| 10.5.8 | Tinh chỉnh hiệu năng tĩnh | Phân tích quan sát, quy hoạch dung lượng |
| 10.5.9 | Các kiểm soát tài nguyên | Tinh chỉnh |
| 10.5.10 | Kiểm thử vi mô | Phân tích thực nghiệm |

Xem Chương 2, Các phương pháp luận, cho các chiến lược và phần giới thiệu cho nhiều nội dung trong số này.

Những nội dung này có thể được tuân theo riêng lẻ hoặc được sử dụng kết hợp. Gợi ý của tôi là sử dụng các chiến lược sau để bắt đầu, theo thứ tự này: giám sát hiệu năng, phương pháp USE, tinh chỉnh hiệu năng tĩnh, và đặc tính hóa khối lượng công việc.

Mục 10.6, Các Công cụ Quan trắc, chỉ ra các công cụ hệ điều hành để áp dụng những phương pháp này.

### 10.5.1 Phương pháp Công cụ (Tools Method)
Phương pháp công cụ là một quá trình lặp đi lặp lại qua các công cụ có sẵn, kiểm tra các chỉ số then chốt mà chúng cung cấp. Nó có thể bỏ sót các vấn đề mà các công cụ cung cấp thông tin kém hoặc không có khả năng hiển thị, và nó có thể tiêu tốn nhiều thời gian để thực hiện.

Đối với mạng, phương pháp công cụ có thể bao gồm việc kiểm tra:
- **nstat/netstat -s:** Tìm kiếm tốc độ truyền lại (retransmits) và các gói tin sai thứ tự (out-of-order packets) cao. Những gì cấu thành một tốc độ truyền lại "cao" tùy thuộc vào các máy khách: một hệ thống hướng Internet với các máy khách từ xa không đáng tin cậy nên có tốc độ truyền lại cao hơn một hệ thống nội bộ với các máy khách trong cùng một trung tâm dữ liệu.
- **ip -s link/netstat -i:** Kiểm tra các bộ đếm lỗi giao diện, bao gồm "errors," "dropped," "overruns."
- **ss -tiepm:** Kiểm tra cờ giới hạn cho các socket quan trọng để xem nút thắt cổ chai của chúng là gì, cũng như các thống kê khác hiển thị tình trạng socket.
- **nicstat/ip -s link:** Kiểm tra tốc độ truyền và nhận byte. Thông lượng cao có thể bị giới hạn bởi tốc độ liên kết dữ liệu đã thương lượng, hoặc một đợt điều tiết mạng bên ngoài (external network throttle). Nó cũng có thể gây ra tranh chấp và sự trì hoãn giữa các người dùng mạng trên hệ thống.
- **tcplife:** Ghi nhật ký các phiên TCP với các chi tiết tiến trình, thời lượng (tuổi thọ), và các thống kê thông lượng.
- **tcptop:** Xem trực tiếp các phiên TCP hàng đầu.
- **tcpdump:** Mặc dù điều này có thể tốn kém về CPU và chi phí lưu trữ, việc sử dụng tcpdump(8) trong các khoảng thời gian ngắn có thể giúp bạn nhận diện lưu lượng mạng bất thường hoặc các headers giao thức.
- **perf(1)/BCC/bpftrace:** Kiểm tra các gói tin giữa ứng dụng và đường dây, bao gồm cả việc kiểm tra trạng thái kernel.

Nếu tìm thấy một vấn đề, hãy kiểm tra tất cả các trường từ các công cụ có sẵn để tìm hiểu thêm ngữ cảnh. Xem Mục 10.6, Các Công cụ Quan trắc, để biết thêm về mỗi công cụ. Các phương pháp luận khác cũng có thể nhận diện nhiều loại vấn đề hơn nữa.

### 10.5.2 Phương pháp USE
Phương pháp USE là để nhanh chóng nhận diện các nút thắt cổ chai và các lỗi trên tất cả các thành phần. Đối với mỗi giao diện mạng, và ở mỗi hướng—truyền (TX) và nhận (RX)—hãy kiểm tra:
- **Mức sử dụng (Utilization):** Thời gian giao diện bận rộn gửi hoặc nhận các khung hình.
- **Độ bão hòa (Saturation):** Mức độ của việc xếp hàng, buffering, hoặc bị chặn thêm do một giao diện đã sử dụng hết công suất.
- **Các lỗi (Errors):** Đối với nhận: checksum sai, khung hình quá ngắn (ít hơn header liên kết dữ liệu) hoặc quá dài, các va chạm (không chắc chắn với các mạng chuyển mạch); đối với truyền: các va chạm muộn (late collisions) (đi dây kém).

Các lỗi có thể được kiểm tra trước tiên, vì chúng thường nhanh chóng để kiểm tra và dễ dàng nhất để diễn giải.

Mức sử dụng không được cung cấp phổ biến bởi hệ điều hành hoặc các công cụ giám sát một cách trực tiếp (nicstat(1) là một ngoại lệ). Nó có thể được tính toán như thông lượng hiện tại chia cho tốc độ đã thương lượng hiện tại, cho mỗi hướng. Thông lượng hiện tại nên được đo lường dưới dạng byte mỗi giây trên mạng, bao gồm tất cả các headers giao thức.

Đối với các môi trường triển khai các giới hạn băng thông mạng (các kiểm soát tài nguyên), như xảy ra trong một số môi trường điện toán đám mây, mức sử dụng mạng có thể cần được đo lường theo các thuật ngữ về giới hạn đã áp đặt, bên cạnh giới hạn vật lý.

Độ bão hòa của giao diện mạng là khó đo lường. Một số buffering mạng là bình thường, vì các ứng dụng có thể gửi dữ liệu nhanh hơn nhiều so với việc một giao diện có thể truyền tải nó. Có thể đo lường nó dưới dạng thời gian các luồng ứng dụng dành cho việc bị chặn trên các lần gửi mạng, thứ nên tăng lên khi độ bão hòa tăng lên. Đồng thời kiểm tra xem liệu có các thống kê kernel khác liên quan chặt chẽ hơn tới sự bão hòa của giao diện hay không, ví dụ, "overruns" của Linux. Lưu ý rằng Linux sử dụng BQL để điều tiết kích thước hàng đợi NIC, thứ giúp tránh bão hòa NIC.

Các lần truyền lại (retransmits) tại mức TCP thường có sẵn dưới dạng các thống kê và có thể là một chỉ báo của sự bão hòa mạng. Tuy nhiên, chúng được đo lường qua mạng giữa máy chủ và các máy khách của nó và có thể được gây ra bởi các vấn đề tại bất kỳ bước nhảy nào.

Phương pháp USE cũng có thể được áp dụng cho các bộ điều khiển mạng, và các vận chuyển giữa chúng và các bộ xử lý. Vì các công cụ quan sát cho các thành phần này là thưa thớt, có thể dễ dàng hơn để suy luận các chỉ số dựa trên các thống kê mạng và topo mạng. Ví dụ, nếu bộ điều khiển mạng A chứa các cổng A0 và A1, thông lượng của bộ điều khiển mạng có thể được tính toán như tổng thông lượng của A0 + A1. Với thông lượng tối đa đã biết, mức sử dụng của bộ điều khiển mạng sau đó có thể được tính toán.

### 10.5.3 Đặc tính hóa Khối lượng công việc (Workload Characterization)
Đặc tính hóa tải được áp dụng là một bài tập quan trọng khi quy hoạch dung lượng, benchmarking, và mô phỏng khối lượng công việc. Nó cũng có thể dẫn đến một số cải thiện hiệu năng lớn nhất bằng cách nhận diện các công việc không cần thiết có thể được loại bỏ.

Sau đây là các đặc tính cơ bản nhất để đo lường:
- **Thông lượng giao diện mạng (Network interface throughput):** RX và TX, byte mỗi giây.
- **IOPS giao diện mạng:** RX và TX, khung hình mỗi giây.
- **Tốc độ kết nối TCP:** Hoạt động (active) và thụ động (passive), số kết nối mỗi giây.

Các thuật ngữ *active* và *passive* đã được mô tả trong phần Three-Way Handshake của Mục 10.4.1, Các giao thức.

Các đặc tính này có thể thay đổi theo thời gian, khi các mẫu sử dụng thay đổi trong suốt cả ngày. Việc giám sát theo thời gian được mô tả trong Mục 10.5.5, Giám sát Hiệu năng.

Dưới đây là một mô tả khối lượng công việc ví dụ, để chỉ ra cách các thuộc tính này có thể được diễn đạt cùng nhau:

> Thông lượng mạng thay đổi dựa trên người dùng và thực hiện nhiều lệnh ghi (TX) hơn lệnh đọc (RX). Tốc độ ghi cao điểm là 200 Mbytes/s và 210,000 gói tin/s, và tốc độ đọc cao điểm là 10 Mbytes/s với 70,000 gói tin/s. Tốc độ kết nối TCP inbound (thụ động) đạt tới 3,000 kết nối/s.

Bên cạnh việc mô tả các đặc tính này trên toàn hệ thống, chúng cũng có thể được diễn đạt cho mỗi giao diện. Điều này cho phép xác định các nút thắt cổ chai giao diện. Nếu thông lượng mạng có thể được quan sát được là đạt tới tốc độ đường truyền. Nếu các giới hạn băng thông mạng (các kiểm soát tài nguyên) hiện diện, chúng có thể điều tiết thông lượng mạng trước khi đạt tới tốc độ đường truyền.

**Đặc tính hóa Khối lượng công việc Nâng cao / Checklist**
Các chi tiết bổ sung có thể được bao gồm để đặc tính hóa khối lượng công việc. Những điều này đã được liệt kê ở đây dưới dạng các câu hỏi để cân nhắc, thứ cũng có thể phục vụ như một checklist khi nghiên cứu các vấn đề CPU thấu đáo:
- Kích thước gói tin trung bình là bao nhiêu? RX, TX?
- Sự phân tích giao thức cho mỗi tầng là gì? Cho các giao thức vận chuyển: TCP, UDP (có thể bao gồm QUIC).
- Những cổng TCP/UDP nào đang hoạt động? Byte mỗi giây, kết nối mỗi giây?
- Các tốc độ gói tin broadcast và multicast là gì?
- Những tiến trình nào đang tích cực sử dụng mạng?

Các phần tiếp theo sẽ trả lời một số câu hỏi trong số này. Xem Chương 2, Các phương pháp luận, cho một bản tóm tắt cấp cao hơn về phương pháp luận này và các đặc tính cần đo lường (ai, tại sao, cái gì, như thế nào).

### 10.5.4 Phân tích Độ trễ (Latency Analysis)
Các độ trễ (latencies) khác nhau có thể được nghiên cứu để giúp hiểu và diễn giải hiệu năng mạng. Một số đã được giới thiệu trong Mục 10.3.5, Độ trễ, và một danh sách dài hơn được cung cấp ở Bảng 10.3. Hãy đo lường càng nhiều trong số này càng tốt để có thể thu hẹp nguồn gốc thực sự của độ trễ.

Bảng 10.3 Các độ trễ mạng
| Độ trễ | Mô tả |
| --- | --- |
| Độ trễ phân giải tên | Thời gian cho một máy chủ để được phân giải thành một địa chỉ IP, thường bằng phân giải DNS—một nguồn gốc phổ biến của các vấn đề hiệu năng. |
| Độ trễ ping | Thời gian từ một yêu cầu ICMP echo tới một phản hồi. Điều này đo lường mạng và việc xử lý kernel stack của gói tin trên mỗi máy chủ. |
| Độ trễ khởi tạo kết nối TCP | Thời gian từ khi một gói SYN được gửi cho tới khi nhận được SYN,ACK. Vì không có ứng dụng nào liên quan, điều này đo lường mạng và việc xử lý kernel của gói tin trên mỗi máy chủ, tương tự như độ trễ ping, nhưng với các yêu cầu xử lý kernel bổ sung cho phiên TCP. TCP Fast Open (TFO) có thể được sử dụng để giảm độ trễ này. |
| Độ trễ byte đầu tiên TCP | Còn được gọi là *time to first byte* (TTFB), điều này đo lường thời gian từ khi một kết nối đã được thiết lập tới khi byte dữ liệu đầu tiên được nhận. Điều này bao gồm thời gian cho máy chủ từ xa chấp nhận một kết nối, lập lịch luồng phục vụ nó, và cho luồng đó thực thi và gửi byte đầu tiên. Điều này bao gồm lập lịch CPU và thời gian suy nghĩ của ứng dụng cho máy chủ, làm cho nó trở thành một phép đo hiệu năng ứng dụng và tải hiện tại hơn là độ trễ kết nối TCP. |
| Các lần truyền lại TCP | Nếu hiện diện, có thể thêm hàng nghìn mili giây độ trễ cho I/O mạng. |
| Độ trễ TCP TIME_WAIT | Khoảng thời gian mà các phiên TCP đã đóng cục bộ được để lại chờ đợi cho các gói tin muộn. |
| Tuổi thọ Kết nối/phiên | Thời gian của một kết nối mạng từ lúc khởi tạo tới lúc đóng. Một số giao thức chẳng hạn như HTTP có thể sử dụng một chiến lược keep-alive, để lại các kết nối mở và rảnh rỗi cho các yêu cầu trong tương lai, nhằm tránh các chi phí của việc thiết lập kết nối lặp đi lặp lại. |
| Độ trễ gửi/nhận system call | Thời gian cho các lệnh gọi socket read/write (bất kỳ syscalls nào đọc/ghi tới sockets, bao gồm read(2), write(2), recv(2), send(2), và các biến thể). |
| Độ trễ kết nối system call | Cho việc thiết lập kết nối; lưu ý rằng một số ứng dụng thực hiện việc này như một non-blocking syscall. |
| Thời gian vòng lặp mạng | Thời gian cho một yêu cầu mạng thực hiện một vòng lặp giữa các endpoint. Kernel có thể sử dụng các phép đo như vậy với các thuật toán điều khiển tắc nghẽn. |
| Độ trễ ngắt | Thời gian từ khi card điều khiển mạng ngắt cho một gói tin nhận được cho tới khi nó được phục vụ bởi kernel. |
| Độ trễ inter-stack | Thời gian cho một gói tin di chuyển qua chồng giao thức kernel TCP/IP. |

Độ trễ có thể được trình bày dưới dạng:
- **Trung bình theo khoảng thời gian:** Tốt nhất là cho mỗi cặp client/server, để cô lập các sự khác biệt trong mạng trung gian.
- **Phân phối đầy đủ:** Dưới dạng biểu đồ histogram hoặc bản đồ nhiệt.
- **Độ trễ cho mỗi thao tác:** Liệt kê các chi tiết cho mỗi sự kiện, bao gồm các địa chỉ IP nguồn và đích.

Một nguồn gốc phổ biến của các vấn đề là sự hiện diện của các giá trị ngoại lai độ trễ gây ra bởi các lần truyền lại TCP. Những điều này có thể được nhận diện bằng cách sử dụng các phân phối đầy đủ hoặc truy vết độ trễ cho mỗi thao tác, bao gồm cả việc lọc cho một ngưỡng độ trễ tối thiểu.

Độ trễ có thể được đo lường bằng cách sử dụng các công cụ truy vết và, đối với một số độ trễ, các tùy chọn socket. Trên Linux, các tùy chọn socket bao gồm SO_TIMESTAMP cho thời gian đến của gói tin (và SO_TIMESTAMPNS cho độ phân giải nano giây) và SO_TIMESTAMPING cho các dấu thời gian cho mỗi sự kiện [Linux 20j]. SO_TIMESTAMPING có thể nhận diện các sự trì hoãn truyền tải, các độ trễ mạng, và các độ trễ inter-stack; điều này có thể đặc biệt hữu ích khi phân tích độ trễ gói tin phức tạp liên quan đến tinh chỉnh [Hassas Yeganeh 19].

Lưu ý rằng một số nguồn gốc của độ trễ bổ sung là mang tính nhất thời và chỉ xảy ra trong quá trình hệ thống tải. Đối với các phép đo thực tế về độ trễ mạng, điều quan trọng là phải đo lường không chỉ một hệ thống đang rảnh rỗi, mà còn một hệ thống dưới tải.

### 10.5.5 Giám sát Hiệu năng (Performance Monitoring)
Giám sát hiệu năng có thể nhận diện các vấn đề đang hoạt động và các mẫu hành vi theo thời gian, bao gồm các mẫu hàng ngày của người dùng cuối, và các hoạt động theo lịch trình chẳng hạn như các bản sao lưu mạng.

Các chỉ số then chốt cho giám sát mạng là:
- **Thông lượng (Throughput):** Byte mạng mỗi giây cho cả việc nhận và truyền, lý tưởng nhất là cho mỗi giao diện.
- **Các kết nối (Connections):** Kết nối TCP mỗi giây, như một chỉ báo khác của mạng tải.
- **Các lỗi (Errors):** Bao gồm các bộ đếm gói tin bị đánh rơi.
- **Các lần truyền lại TCP (TCP retransmits):** Cũng hữu ích để ghi lại cho sự tương quan với các vấn đề mạng.
- **Các gói tin TCP sai thứ tự (TCP out-of-order packets):** Cũng có thể gây ra các vấn đề hiệu năng.

Đối với các môi trường triển khai các giới hạn băng thông mạng (các kiểm soát tài nguyên), chẳng hạn như trong một số môi trường điện toán đám mây, các thống kê liên quan đến các giới hạn đã áp đặt cũng có thể được thu thập.

### 10.5.6 Packet Sniffing (Ngửi gói tin)
Packet sniffing (hay gọi là *packet capture*) liên quan đến việc bắt các gói tin từ mạng sao cho các headers giao thức và dữ liệu của chúng có thể được kiểm tra trên cơ sở từng gói tin một. Đối với phân tích quan sát, đây có thể là phương án cuối cùng, vì nó có thể tốn kém về mặt chi phí CPU và lưu trữ. Các đường dẫn mã mạng kernel hiện đại thường được tối ưu hóa theo chu kỳ, vì chúng cần xử lý hàng triệu gói tin mỗi giây và nhạy cảm với bất kỳ chi phí bổ sung nào. Để giảm chi phí này, các buffer ring được sử dụng bởi kernel để truyền dữ liệu gói tin tới trình truy vết cấp người dùng thông qua một bộ nhớ chung—ví dụ, sử dụng BPF với buffer ring kết quả của perf(1), và cũng sử dụng AF_XDP [Linux 20k]. Một cách khác để giải quyết chi phí là sử dụng một "tap" hoặc "mirror" port mạng gắn ngoài của một switch. Các nhà cung cấp dịch vụ đám mây công cộng chẳng hạn như Amazon và Google cung cấp điều này như một dịch vụ [Amazon 19][Google 20b].

Packet sniffing thường bao gồm việc bắt các gói tin vào một tập tin, và sau đó phân tích tập tin đó theo các cách khác nhau. Một cách là tạo ra một bản nhật ký, thứ có thể chứa các thông tin sau đây cho mỗi gói tin:
- Dấu thời gian (Timestamp)
- Toàn bộ gói tin, bao gồm:
  - Tất cả các protocol headers (ví dụ: Ethernet, IP, TCP)
  - Toàn bộ hoặc một phần dữ liệu payload
- Metadata: số lượng gói tin, số lượng đợt rớt
- Tên giao diện

Dưới đây là một ví dụ về kết quả bắt gói tin, phần sau đây cho thấy mặc định của công cụ tcpdump(8) trong Linux:
```bash
# tcpdump -ni eth4
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth4, link-type EN10MB (Ethernet), capture size 65535 bytes
01:20:46.769073 IP 10.2.203.2.22 > 10.2.0.2.33771: Flags [P.], seq
4235343542:4235343734, ack 4053030377, win 132, options [nop,nop,TS val 328647671 ecr
2313764364], length 192
01:20:46.769470 IP 10.2.0.2.33771 > 10.2.203.2.22: Flags [.], ack 192, win 501,
options [nop,nop,TS val 2313764392 ecr 328647671], length 0
01:20:46.787673 IP 10.2.203.2.22 > 10.2.0.2.33771: Flags [P.], seq 192:560, ack 1,
win 132, options [nop,nop,TS val 328647672 ecr 2313764392], length 368
01:20:46.788050 IP 10.2.0.2.33771 > 10.2.203.2.22: Flags [.], ack 560, win 501,
options [nop,nop,TS val 2313764394 ecr 328647672], length 0
01:20:46.808491 IP 10.2.203.2.22 > 10.2.0.2.33771: Flags [P.], seq 560:896, ack 1,
win 132, options [nop,nop,TS val 328647674 ecr 2313764394], length 336
[...]
```
Kết quả này có một dòng tóm tắt từng gói tin, bao gồm các chi tiết về địa chỉ IP, cổng TCP, và các chi tiết header TCP khác. Điều này có thể được sử dụng để gỡ lỗi một loạt các vấn đề bao gồm độ trễ thông điệp và các gói tin bị thiếu.

Bởi vì việc bắt gói tin có thể là một hoạt động tiêu tốn nhiều tài nguyên CPU, hầu hết các triển khai đều bao gồm khả năng rớt các sự kiện bắt gói tin khi bị quá tải. Số lượng gói tin bị đánh rơi có thể được bao gồm trong bản nhật ký.

Bên cạnh việc sử dụng các buffer ring để giảm bớt chi phí, các triển khai bắt gói tin thường cho phép một biểu thức lọc được cung cấp bởi người dùng và thực hiện việc lọc này trong kernel. Biểu thức lọc này thường sử dụng Berkeley Packet Filter (BPF), thứ biên dịch biểu thức thành mã bytecode BPF có thể được biên dịch JIT thành mã máy bởi kernel. Trong những năm gần đây, BPF đã được mở rộng trong Linux để trở thành một môi trường thực thi đa năng, thứ cung cấp sức mạnh cho nhiều công cụ quan sát: xem Chương 3, Hệ điều hành, Mục 3.4.4, BPF mở rộng, và Chương 15, BPF.

### 10.5.7 Phân tích TCP
Bên cạnh những gì đã được bao quát trong Mục 10.5.4, Phân tích độ trễ, các hành vi TCP cụ thể khác có thể được điều tra, bao gồm:
- Sử dụng các bộ đệm gửi/nhận TCP (socket).
- Sử dụng các hàng đợi TCP backlog.
- Việc rớt gói tin kernel do hàng đợi backlog bị đầy.
- Kích thước cửa sổ tắc nghẽn (congestion window size), bao gồm cả các quảng cáo không-kích-thước (zero-size advertisements).
- Các gói tin SYN nhận được trong một khoảng thời gian TCP TIME_WAIT.

Hành vi cuối cùng có thể trở thành một vấn đề về khả năng mở rộng khi một máy chủ đang kết nối thường xuyên tới cùng một máy chủ đích, sử dụng cùng một cặp máy chủ và cổng đích. Thành phần phân biệt duy nhất cho mỗi kết nối là cổng nguồn máy khách—*cổng tạm thời* (ephemeral port)—thứ cho TCP là một giá trị 16-bit và có thể bị hạn chế thêm bởi các tham số hệ thống (tối thiểu và tối đa). Kết hợp với khoảng thời gian TCP TIME_WAIT, có thể kéo dài 60 giây, tốc độ kết nối cao (hơn 65,536 trong 60 giây) có thể gặp phải một sự xung đột cho các kết nối mới. Trong kịch bản này, một gói tin SYN được gửi trong khi cổng tạm thời vẫn còn liên kết với một phiên TCP trước đó đang ở trạng thái TIME_WAIT, và gói tin SYN mới có thể bị xác định sai là một phần của kết nối cũ (một va chạm). Để tránh vấn đề này, kernel Linux cố gắng tái sử dụng hoặc tái chế các kết nối một cách nhanh chóng (thứ thường hoạt động tốt). Việc sử dụng nhiều địa chỉ IP bởi máy chủ là một giải pháp khả thi khác, cũng như tùy chọn socket SO_LINGER với thời gian kéo dài (linger time) thấp.

### 10.5.8 Tinh chỉnh Hiệu năng Tĩnh (Static Performance Tuning)
Tinh chỉnh hiệu năng tĩnh tập trung vào các vấn đề của môi trường đã cấu hình. Cho hiệu năng mạng, hãy kiểm tra các khía cạnh sau của cấu hình tĩnh:
- Có bao nhiêu giao diện mạng khả dụng để sử dụng? Chúng hiện đang được sử dụng chứ?
- Tốc độ tối đa của các giao diện mạng là bao nhiêu?
- Tốc độ đã thương lượng hiện tại của các giao diện mạng là bao nhiêu?
- Các giao diện mạng đã thương lượng là bán song công hay toàn song công?
- MTU nào được cấu hình cho các giao diện mạng?
- Các giao diện mạng có được trunked (nhóm lại) không?
- Những tham số tinh chỉnh nào tồn tại cho trình điều khiển thiết bị? Tầng IP? Tầng TCP?
- Có bất kỳ tham số tinh chỉnh nào đã được thay đổi so với mặc định không?
- Định tuyến được cấu hình như thế nào? Gateway mặc định là gì?
- Thông lượng tối đa của các thành phần mạng trong đường dẫn dữ liệu (tất cả các thành phần, bao gồm cả switch và router backplanes) là bao nhiêu?
- MTU tối đa cho đường dẫn dữ liệu là bao nhiêu và việc phân mảnh có xảy ra không?
- Có bất kỳ kết nối không dây nào trong đường dẫn dữ liệu không? Chúng có đang chịu sự nhiễu loạn không?
- Chuyển tiếp (forwarding) có được bật không? Hệ thống có đang đóng vai trò như một router không?
- DNS được cấu hình như thế nào? Máy chủ cách xa bao nhiêu?
- Có các vấn đề hiệu năng đã biết (lỗi) với phiên bản của firmware giao diện mạng, hoặc bất kỳ phần cứng mạng nào khác không?
- Có các vấn đề hiệu năng đã biết (lỗi) với trình điều khiển thiết bị mạng không? Stack TCP/IP của kernel?
- Những firewalls nào hiện diện?
- Có bất kỳ giới hạn thông lượng mạng nào do phần mềm áp đặt không (các kiểm soát tài nguyên)? Chúng là gì?

Câu trả lời cho những câu hỏi này có thể tiết lộ các lựa chọn cấu hình đã bị bỏ qua. Câu hỏi cuối cùng đặc biệt liên quan đến các môi trường điện toán đám mây, nơi có thể có các giới hạn áp đặt lên thông lượng mạng.

### 10.5.9 Các kiểm soát Tài nguyên
Hệ điều hành có thể cung cấp các kiểm soát để giới hạn tài nguyên mạng cho các loại kết nối, tiến trình, hoặc các nhóm tiến trình. Những điều này có thể bao gồm các loại kiểm soát sau:
- **Network bandwidth limits:** Một băng thông tối đa cho phép (thông lượng tối đa) cho các giao thức hoặc ứng dụng khác nhau, được áp dụng bởi kernel.
- **IP quality of service (QoS):** Việc ưu tiên hóa lưu lượng mạng, được thực hiện bởi các thành phần mạng (ví dụ: các router). Điều này có thể được triển khai theo các cách khác nhau: IP header bao gồm các bit type-of-service (ToS), bao gồm một mức ưu tiên; những bit này từ đó đã được định nghĩa lại cho các sơ đồ QoS mới hơn, bao gồm Differentiated Services (xem Mục 10.4.1, Các giao thức, dưới tiêu đề IP). Có thể có các mức ưu tiên khác được thực hiện bởi các tầng giao thức khác, cho cùng một mục đích.
- **Packet latency:** Độ trễ gói tin bổ sung (ví dụ: sử dụng tc-netem(8) của Linux), thứ có thể được sử dụng để mô phỏng các mạng khác khi kiểm tra hiệu năng.

Mạng của bạn có thể có một sự hỗn hợp của lưu lượng có thể được phân loại là ưu tiên thấp hoặc cao. Lưu lượng ưu tiên thấp có thể bao gồm việc truyền tải các bản sao lưu và các lưu lượng giám sát hiệu năng. Các kiểm soát tài nguyên mạng có thể được sử dụng để điều tiết lưu lượng ưu tiên thấp, mang lại hiệu năng thuận lợi hơn cho lưu lượng ưu tiên cao.

Cách thức thực hiện những điều này là tùy thuộc vào việc triển khai: xem Mục 10.8, Tinh chỉnh.

### 10.5.10 Kiểm thử vi mô (Micro-Benchmarking)
Có nhiều công cụ benchmark cho mạng. Chúng đặc biệt hữu ích khi điều tra thông lượng vượt qua các ứng dụng, để xác nhận rằng mạng có thể ít nhất đạt được thông lượng mạng mong muốn. Những điều này có thể được điều tra qua một công cụ micro-benchmark mạng, thứ thông thường ít phức tạp và nhanh hơn để gỡ lỗi hơn là chính ứng dụng đó. Sau khi mạng đã được tinh chỉnh tới tốc độ mong muốn, sự chú ý có thể quay trở lại ứng dụng.

Các yếu tố điển hình có thể được kiểm tra bao gồm:
- **Hướng:** Gửi hoặc nhận.
- **Giao thức:** TCP hoặc UDP, và cổng.
- **Số lượng luồng (threads).**
- **Kích thước bộ đệm (buffer size).**
- **Kích thước MTU giao diện.**

Các giao diện mạng nhanh hơn, chẳng hạn như 100 Gbits/s, có thể yêu cầu nhiều luồng máy khách để được đẩy tới băng thông tối đa.

Một công cụ micro-benchmark mạng ví dụ, iperf(1), được giới thiệu trong Mục 10.7.4, iperf, và những cái khác được liệt kê trong Mục 10.7, Thực nghiệm.

---

## 10.6 Các Công cụ Quan trắc (Observability Tools)
Phần này giới thiệu các công cụ quan sát hiệu năng mạng cho các hệ điều hành dựa trên Linux. Hãy xem phần trước cho các chiến lược cần tuân theo khi sử dụng chúng.

Các công cụ trong phần này được liệt kê trong Bảng 10.4.

Bảng 10.4 Các công cụ quan sát mạng
| Mục | Công cụ | Mô tả |
| --- | --- | --- |
| 10.6.1 | ss | Các thống kê Socket |
| 10.6.2 | ip | Các thống kê giao diện mạng và định tuyến |
| 10.6.3 | ifconfig | Các thống kê giao diện mạng |
| 10.6.4 | nstat | Các thống kê network stack |
| 10.6.5 | netstat | Các thống kê network stack và giao diện mạng đa dạng |
| 10.6.6 | sar | Các thống kê lịch sử |
| 10.6.7 | nicstat | Thông lượng và mức sử dụng giao diện mạng |
| 10.6.8 | ethtool | Các thống kê trình điều khiển giao diện mạng |
| 10.6.9 | tcplife | Truy vết tuổi thọ phiên TCP với các chi tiết kết nối |
| 10.6.10 | tcptop | Hiển thị thông lượng TCP theo máy chủ và tiến trình |
| 10.6.11 | tcpretrans | Truy vết các lần truyền lại TCP với địa chỉ và trạng thái TCP |
| 10.6.12 | bpftrace | Truy vết TCP/IP stack: các kết nối, các gói tin, các lần đánh rơi, độ trễ |
| 10.6.13 | tcpdump | Trình ngửi gói tin mạng (network packet sniffer) |
| 10.6.14 | Wireshark | Kiểm tra gói tin mạng đồ họa |

Đây là một sự lựa chọn các công cụ và khả năng để hỗ trợ Mục 10.5, Phương pháp luận, bắt đầu với các công cụ thống kê truyền thống, sau đó là các công cụ truy vết, và cuối cùng là các công cụ bắt gói tin. Một số công cụ truyền thống có khả năng khả dụng trên các hệ điều hành dạng Unix khác nơi chúng bắt nguồn, bao gồm: ifconfig(8), netstat(8), và sar(1). Các công cụ truy vết là dựa trên BPF, và sử dụng các frontend BCC và bpftrace (Chương 15); chúng là: socketio(8), tcplife(8), tcptop(8), và tcpretrans(8).

Các công cụ thống kê đầu tiên được đề cập là ss(8), ip(8), và nstat(8), vì đây là từ gói iproute2 được kernel duy trì bởi các kỹ sư mạng. Các công cụ từ gói này có nhiều khả năng nhất hỗ trợ các tính năng kernel Linux mới nhất. Các công cụ tương tự từ gói net-tools, cụ thể là ifconfig(8) và netstat(8), cũng được bao quát vì chúng đang được sử dụng rộng rãi, mặc dù các kỹ sư mạng Linux coi những thứ này là lỗi thời.

### 10.6.1 ss
ss(8) là một công cụ thống kê socket tóm tắt các socket đang mở. Kết quả mặc định cung cấp thông tin cấp cao về các socket, ví dụ:
```bash
# ss
Netid State      Recv-Q Send-Q    Local Address:Port          Peer Address:Port
[...]
tcp   ESTAB      0      0         100.85.142.69:65264       100.82.166.11:6001
tcp   ESTAB      0      0         100.85.142.69:6028        100.82.16.200:6101
[...]
```
Kết quả này là một ảnh chụp nhanh của trạng thái hiện tại. Cột đầu tiên hiển thị giao thức được sử dụng bởi các socket: đây là các socket TCP. Vì kết quả này liệt kê tất cả các kết nối đã được thiết lập với thông tin địa chỉ IP, nó có thể được sử dụng để đặc tính hóa khối lượng công việc hiện tại, và trả lời các câu hỏi bao gồm có bao nhiêu kết nối máy khách đang mở, có bao nhiêu kết nối đồng thời tới một máy chủ phụ thuộc, v.v.

Thông tin tương tự cho mỗi socket có sẵn bằng cách sử dụng công cụ netstat(8) cũ hơn. Tuy nhiên, ss(8) có thể hiển thị nhiều thông tin hơn nữa khi sử dụng các tùy chọn. Ví dụ, hiển thị các socket TCP (-t), với thông tin TCP nội bộ (-i), thông tin socket mở rộng (-e), thông tin tiến trình (-p), và sử dụng bộ nhớ (-m):
```bash
# ss -tiepm
State      Recv-Q Send-Q    Local Address:Port          Peer Address:Port

ESTAB      0      0         100.85.142.69:65264       100.82.166.11:6001
   users:(("java",pid=4195,fd=10865)) uid:33 ino:2009918 sk:78 <->
         skmem:(r0,rb12582912,t0,tb12582912,f266240,w0,b10,d0) ts sack bbr wscale:9,9 rto:204 rtt:0.159/0.009 ato:40 mss:1448 pmtu:1500 rcvmss:1448 advmss:1448 cwnd:152 bytes_acked:347681 bytes_received:1798733 segs_out:582 segs_in:1397 data_segs_out:294 data_segs_in:1318 bbr:(bw:328.6Mbps,mrtt:0.149,pacing_gain:2.88672,cwnd_gain:2.88672) send 11074.0Mbps lastsnd:1696 lastrcv:1660 lastack:1660 pacing_rate 2422.4Mbps delivery_rate 328.6Mbps app_limited busy:16ms rcv_rtt:39.822 rcv_space:84867 rcv_ssthresh:3609062 minrtt:0.139
[...]
```
Được bôi đậm là các địa chỉ endpoint và các chi tiết sau:
- **"java",pid=4195:** Tên tiến trình "java," PID 4195.
- **fd=10865:** File descriptor 10865 (cho PID 4195).
- **rto:204:** TCP retransmission timeout: 204 mili giây.
- **rtt:0.159/0.009:** Thời gian vòng lặp trung bình là 0.159 mili giây, với độ lệch trung bình là 0.009 mili giây.
- **mss:1448:** Kích thước phân đoạn tối đa: 1448 byte.
- **cwnd:152:** Kích thước cửa sổ tắc nghẽn: 152 × MSS.
- **bytes_acked:347681:** 340 Kbytes được truyền tải thành công.
- **bytes_received:1798733:** 1.72 Mbytes được nhận.
- **bbr:...:** Các thống kê điều khiển tắc nghẽn BBR.
- **pacing_rate 2422.4Mbps:** Tốc độ Pacing là 2422.4 Mbps.
- **app_limited:** Cho thấy congestion window không được tận dụng đầy đủ, cho thấy rằng kết nối là bị giới hạn bởi ứng dụng (application-bound).
- **minrtt:0.139:** Thời gian vòng lặp tối thiểu tính theo mili giây. So sánh với độ lệch trung bình (đã liệt kê trước đó) để có một ý tưởng về biến động mạng và tắc nghẽn.

Kết nối cụ thể này được đánh dấu là app-limited (app_limited), với RTT thấp tới máy chủ từ xa, và tổng số byte được truyền tải thấp. Các trạng thái "limited" (bị giới hạn) khả thi mà ss(1) có thể in là:
- **app_limited:** Bị giới hạn bởi ứng dụng.
- **rwnd_limited:Xms:** Bị giới hạn bởi cửa sổ nhận (receive window). Bao gồm thời gian bị giới hạn tính theo mili giây.
- **sndbuf_limited:Xms:** Bị giới hạn bởi bộ đệm gửi (send buffer). Bao gồm thời gian bị giới hạn tính theo mili giây.

Một chi tiết bị thiếu từ kết quả là tuổi thọ của kết nối, thứ cần thiết để tính toán thông lượng trung bình. Một cách giải quyết mà tôi tìm thấy là sử dụng dấu thời gian thay đổi (change timestamp) trên file descriptor file trong /proc: cho kết nối này, tôi sẽ chạy stat(1) trên /proc/4195/fd/10865.

**netlink**
ss(8) đọc các thống kê này từ giao diện netlink(7), thứ vận hành qua các socket thuộc họ AF_NETLINK để lấy thông tin từ kernel. Bạn có thể thấy điều này trong hoạt động khi sử dụng strace(1) (xem Mục 5.5.4, strace, cho các cảnh báo về chi phí của strace(1)):
```bash
# strace -e sendmsg,recvmsg ss -t
sendmsg(3, {msg_name={sa_family=AF_NETLINK, nl_pid=0, nl_groups=00000000},
msg_namelen=12, msg_iov=[{iov_base={{len=72, type=SOCK_DIAG_BY_FAMILY,
flags=NLM_F_REQUEST|NLM_F_DUMP, seq=123456, pid=0}, {sdiag_family=AF_INET,
sdiag_protocol=IPPROTO_TCP, idiag_ext=1<<(INET_DIAG_MEMINFO-1)|...
recvmsg(3, {msg_name={sa_family=AF_NETLINK, nl_pid=0, nl_groups=00000000},...
[...]
```
netstat(8) thay vào đó tìm nguồn từ các tập tin /proc/net:
```bash
# strace -e openat netstat -an
[...]
openat(AT_FDCWD, "/proc/net/tcp", O_RDONLY) = 3
openat(AT_FDCWD, "/proc/net/tcp6", O_RDONLY) = 3
[...]
```
Bởi vì các tập tin /proc/net là văn bản, tôi thấy chúng tiện lợi như một nguồn cho các báo cáo tùy biến (ad hoc), yêu cầu không gì hơn ngoài awk(1) để xử lý. Các công cụ giám sát nghiêm túc nên sử dụng giao diện netlink(7) thay vào đó, thứ truyền thông tin dưới định dạng nhị phân và tránh các chi phí của việc phân tích văn bản.

### 10.6.2 ip
ip(8) là một công cụ để quản lý định tuyến, các thiết bị mạng, các giao diện, và các tunnels. Để có khả năng quan sát, nó có thể được sử dụng để in các thống kê trên link, địa chỉ, định tuyến, v.v. Ví dụ, in các thống kê bổ sung (-s) trên các giao diện (link):
```bash
# ip -s link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT
group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    RX: bytes  packets  errors  dropped overrun mcast
    26550075   273178   0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    26550075   273178   0       0       0       0

2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT
group default qlen 1000
    link/ether 12:c0:0a:b0:21:b8 brd ff:ff:ff:ff:ff:ff
    RX: bytes  packets  errors  dropped overrun mcast
    512473039143 568704184 0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    573510263433 668110321 0       0       0       0
```
Việc kiểm tra cấu hình của tất cả các giao diện có thể hữu ích trong quá trình tinh chỉnh hiệu năng tĩnh, để kiểm tra các cấu hình sai. Các chỉ số lỗi cũng được bao gồm trong kết quả: cho nhận (RX): các lỗi (errors), các lần rớt (drops), và các đợt tràn (overruns); cho truyền (TX): các lỗi truyền, các lần rớt, và các va chạm (collisions). Những điều này có thể là một nguồn gốc của các vấn đề hiệu năng và, tùy thuộc vào hệ điều hành, có thể gây ra bởi phần cứng mạng bị lỗi. Đây là các bộ đếm toàn cầu hiển thị tất cả các lỗi kể từ khi giao diện được kích hoạt (theo thuật ngữ mạng, nó được đưa lên "UP").

Việc chỉ định tùy chọn -s hai lần (-s -s) cung cấp thêm nhiều thống kê hơn nữa cho các loại lỗi.

Mặc dù ip(8) cung cấp các bộ đếm byte RX và TX, nó không cung cấp một tùy chọn để in thông lượng hiện tại qua một khoảng thời gian. Để làm được điều đó, hãy sử dụng sar(1) (Mục 10.6.6, sar).

**Bảng Định tuyến (Route Table)**
ip(1) có khả năng quan sát cho các thành phần mạng khác, ví dụ, đối tượng định tuyến (route) hiển thị bảng định tuyến:
```bash
# ip route
default via 100.85.128.1 dev eth0
default via 100.85.128.1 dev eth0 proto dhcp src 100.85.142.69 metric 100
100.85.128.0/18 dev eth0 proto kernel scope link src 100.85.142.69
100.85.128.1 dev eth0 proto dhcp scope link src 100.85.142.69 metric 100
```
Các định tuyến được cấu hình sai cũng có thể là một nguồn gốc của các vấn đề hiệu năng (ví dụ, khi các mục định tuyến cụ thể được thêm vào bởi một quản trị viên nhưng không còn cần thiết, và bây giờ thực hiện tệ hơn định tuyến mặc định).

**Giám sát (Monitoring)**
Sử dụng lệnh phụ monitoring ip monitor để quan sát các thông điệp netlink.

### 10.6.3 ifconfig
Lệnh ifconfig(8) là công cụ truyền thống cho việc quản trị giao diện, và cũng có thể liệt kê cấu hình của tất cả các giao diện. Phiên bản Linux bao gồm các thống kê với kết quả [Linux 20l]:
```bash
$ ifconfig
eth0      Link encap:Ethernet  HWaddr 00:21:9b:97:a9:bf
          inet addr:10.2.0.2  Bcast:10.2.0.255  Mask:255.255.255.0
          inet6 addr: fe80::221:9bff:fe97:a9bf/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:933874764 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1090431029 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:584622361619 (584.6 GB)  TX bytes:537745836640 (537.7 GB)
          Interrupt:36 Memory:d6000000-d6012800
eth3      Link encap:Ethernet  HWaddr 00:21:9b:97:a9:c5
[...]
```
Các bộ đếm là giống như những bộ đếm đã được mô tả cho lệnh ip(8). Trên Linux, ifconfig(8) được coi là lỗi thời, được thay thế bằng ip(8).

### 10.6.4 nstat
nstat(8) in các chỉ số mạng khác nhau được kernel duy trì, cùng với tên SNMP của chúng. Ví dụ, sử dụng -s để tránh việc reset các bộ đếm:
```bash
# nstat -s
#kernel
IpInReceives                    462657733          0.0
IpInDelivers                    462657733          0.0
IpOutRequests                   497050986          0.0
IpOutDiscards                   42                 0.0
IpFragOKs                       2298               0.0
IpFragCreates                   13788              0.0
IcmpInMsgs                      91                 0.0
[...]
TcpActiveOpens                  362997             0.0
TcpPassiveOpens                 9663983            0.0
TcpAttemptFails                 12718              0.0
TcpEstabResets                  14591              0.0
TcpInSegs                       462181482          0.0
TcpOutSegs                      938958577          0.0
TcpRetransSegs                  129212             0.0
TcpOutRsts                      52362              0.0
UdpInDatagrams                  476072             0.0
UdpNoPorts                      88                 0.0
UdpOutDatagrams                 476197             0.0
UdpIgnoredMulti                 2                  0.0
Ip6OutRequests                  29                 0.0
[...]
```
Các chỉ số then chốt bao gồm:
- **IpInReceives:** Các gói tin IP inbound.
- **IpOutRequests:** Các gói tin IP outbound.
- **TcpActiveOpens:** Các kết nối TCP hoạt động (lệnh gọi socket connect(2)).
- **TcpPassiveOpens:** Các kết nối TCP thụ động (lệnh gọi socket accept(2)).
- **TcpInSegs:** Các phân đoạn TCP inbound.
- **TcpOutSegs:** Các phân đoạn TCP outbound.
- **TcpRetransSegs:** Các phân đoạn TCP được truyền lại. So sánh với TcpOutSegs cho tỷ lệ truyền lại.

Nếu tùy chọn -s không được sử dụng, hành vi mặc định của nstat(8) là reset các bộ đếm kernel. Điều này có thể hữu ích, vì sau đó bạn có thể chạy nstat(8) lần thứ hai và xem các số lượng đã trải dài qua khoảng thời gian đó, thay vì các tổng số kể từ khi boot. Nếu bạn muốn kiểm tra xem một mạng tải có thể được tái hiện bằng một lệnh hay không, nstat(8) có thể được chạy trước và sau lệnh để xem các bộ đếm đã thay đổi như thế nào.

Nếu bạn quên sử dụng -s và đã reset các bộ đếm một cách vô ý, bạn có thể sử dụng -rs để thiết lập chúng trở lại tóm tắt của chúng kể từ các giá trị khi boot.

nstat(8) cũng có một chế độ daemon (-d) để thu thập các thống kê theo khoảng thời gian, thứ khi được sử dụng sẽ được hiển thị ở cột cuối cùng.

### 10.6.5 netstat
Lệnh netstat(8) báo cáo các loại thống kê mạng khác nhau, dựa trên các tùy chọn được sử dụng. Nó giống như một công cụ đa năng với nhiều chức năng khác nhau. Những thứ này bao gồm:
- **(mặc định):** Liệt kê các socket đã kết nối
- **-a:** Liệt kê thông tin cho tất cả các socket
- **-s:** Các thống kê network stack
- **-i:** Các thống kê giao diện mạng
- **-r:** Liệt kê bảng định tuyến

Các tùy chọn khác có thể sửa đổi kết quả, bao gồm -n để không phân giải các địa chỉ IP thành tên máy chủ, và -v cho các chi tiết dài dòng khi có sẵn.

Dưới đây là một ví dụ về các thống kê giao diện netstat(8):
```bash
$ netstat -i
Kernel Interface table
Iface   MTU Met   RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
eth0   1500   0 933760207      0      0 0      1090211545      0      0      0 BMRU
eth3   1500   0 718900017      0      0 0      587534567      0      0      0 BMRU
lo    16436   0 21126497      0      0 0      21126497      0      0      0 LRU
ppp5   1496   0     4225      0      0 0          3736      0      0      0 MOPRU
ppp6   1496   0     1183      0      0 0          1143      0      0      0 MOPRU
tun0   1500   0   695581      0      0 0        692378      0      0      0 MOPRU
tun1   1462   0        0      0      0 0             4      0      0      0 PRU
```
Các cột bao gồm giao diện mạng (Iface), MTU, và một loạt các chỉ số cho nhận (RX-) và truyền (TX-):
- **-OK:** Các gói tin được truyền tải thành công
- **-ERR:** Các lỗi gói tin
- **-DRP:** Các lần rớt gói tin
- **-OVR:** Các đợt tràn gói tin

Các lần rớt gói tin và tràn gói tin là các chỉ báo của giao diện mạng *bão hòa* (saturation) và có thể được kiểm tra cùng với các lỗi như một phần của phương pháp USE.

Tùy chọn -c liên tục có thể được sử dụng với -i, thứ in các bộ đếm tích lũy này mỗi giây. Điều này cung cấp dữ liệu cho việc tính toán tốc độ của các gói tin.

Dưới đây là một ví dụ về các thống kê network stack netstat(8) (đã bị lược bớt):
```bash
$ netstat -s
Ip:
    Forwarding: 2
    454143446 total packets received
    0 forwarded
    0 incoming packets discarded
    454143446 incoming packets delivered
    487760885 requests sent out
    42 outgoing packets dropped
    2260 fragments received ok
    13560 fragments created
Icmp:
    91 ICMP messages received
[...]
Tcp:
    359286 active connection openings
    9463980 passive connection openings
    12527 failed connection attempts
    14323 connection resets received
    13545 connections established
    453673963 segments received
    922299281 segments sent out
    127247 segments retransmitted
    0 bad segments received
    51660 resets sent
Udp:
    469302 packets received
    88 packets to unknown port received
    0 packet receive errors
    469427 packets sent
    0 receive buffer errors
    0 send buffer errors
    IgnoredMulti: 2
TcpExt:
    21 resets received for embryonic SYN_RECV sockets
    12252 packets pruned from receive queue because of socket buffer overrun
    201219 TCP sockets finished time wait in fast timer
    11727438 delayed acks sent
    1445 delayed acks further delayed because of locked socket
    Quick ack mode was activated 17624 times
    169257582 packets received
    76058392 acknowledgments not containing data payload received
    111925821 predicted acknowledgments
    TCPSackRecovery: 1703
    Detected reordering 876 times using SACK
    Detected reordering 19 times using time stamp
    2 congestion windows fully recovered without slow start
    19 congestion windows partially recovered using Hoe heuristic
    TCPDSACKUndo: 164
    88 congestion windows recovered without slow start after partial ack
    TCPLostRetransmit: 901
    TCPSackFailures: 31
    28248 fast retransmits
    709 retransmits in slow start
    TCPTimeouts: 12684
    TCPLossProbes: 73383
    TCPLossProbeRecovery: 132
    TCPSackRecoveryFail: 24
    805315 packets collapsed in receive queue due to low socket buffer
[...]
    TCPAutoCorking: 13520259
    TCPFromZeroWindowAdv: 257
    TCPToZeroWindowAdv: 257
    TCPWantZeroWindowAdv: 18941
    TCPSynRetrans: 24816
[...]
```
Kết quả liệt kê các thống kê mạng khác nhau, chủ yếu từ TCP, được nhóm theo giao thức của chúng. May mắn thay, nhiều trong số những thống kê này có các cái tên mô tả dài, sao cho ý nghĩa của chúng có thể rõ ràng. Một số thống kê đã được bôi đậm, để chỉ ra loại hành vi hiệu năng cần tìm kiếm. Nhiều trong số này yêu cầu một sự hiểu biết nâng cao về hành vi TCP, bao gồm các tính năng và thuật toán mới đã được đưa vào trong những năm gần đây. Một số ví dụ thống kê cần tìm kiếm:
- Tốc độ cao các gói tin nhận được so với gói tin chuyển tiếp: kiểm tra xem máy chủ có được cho là chuyển tiếp (định tuyến) các gói tin hay không.
- Các kết nối thụ động mở: cái này có thể được giám sát để chỉ ra mức tải xét theo các kết nối máy khách.
- Tốc độ cao của các phân đoạn được truyền lại so với các phân đoạn được gửi ra: có thể cho thấy một mạng không đáng tin cậy. Điều này có thể được kỳ vọng (các máy khách Internet).
- TCPSynRetrans: hiển thị các SYNs được truyền lại, thứ có thể gây ra bởi endpoint từ xa đánh rơi SYNs từ hàng đợi listen backlog do tải.
- Gói tin bị cắt tỉa từ hàng đợi nhận do bộ đệm socket bị tràn: đây là một dấu hiệu của sự bão hòa mạng và có thể sửa chữa được bằng cách tăng các bộ đệm socket, miễn là có đủ tài nguyên hệ thống cho ứng dụng để theo kịp.

Một số tên chỉ số thống kê bao gồm các lỗi đánh máy (ví dụ: *packetes_rejected*). Những thứ này có thể là vấn đề để sửa chữa đơn giản, nếu các công cụ giám sát khác đã được xây dựng dựa trên cùng kết quả đó. Các công cụ như vậy nên tốt hơn là được phục vụ bằng cách xử lý nstat(8) output, thứ sử dụng các tên SNMP tiêu chuẩn, hoặc thậm chí tốt hơn, bằng cách trực tiếp đọc các nguồn /proc cho các thống kê này, đó là /proc/net/snmp và /proc/net/netstat. Ví dụ:
```bash
$ grep ^Tcp /proc/net/snmp
Tcp: RtoAlgorithm RtoMin RtoMax MaxConn ActiveOpens PassiveOpens AttemptFails
EstabResets CurrEstab InSegs OutSegs RetransSegs InErrs OutRsts InCSumErrors
Tcp: 1 200 120000 -1 102378 126946 11940 19495 24 627115849 325815063 346455 5 24183
0
```
Những thống kê /proc/net/snmp này cũng bao gồm các SNMP management information bases (MIBs). Tài liệu MIB mô tả ý nghĩa của mỗi thống kê (nếu kernel đã triển khai chính xác). Các thống kê mở rộng nằm trong /proc/net/netstat.

Một khoảng thời gian, tính bằng giây, có thể được sử dụng với netstat(8) sao cho nó liên tục in các bộ đếm tích lũy sau mỗi khoảng thời gian. Kết quả này sau đó có thể được xử lý hậu kỳ để tính toán tốc độ của mỗi bộ đếm.

### 10.6.6 sar
Trình báo cáo hoạt động hệ thống, sar(1), có thể được sử dụng để quan sát hoạt động hiện tại và có thể được cấu hình để lưu trữ và báo cáo các thống kê lịch sử. Nó được giới thiệu trong Chương 4, Các Công cụ Quan trắc, và đã được đề cập trong các chương khác nhau khi phù hợp.

Phiên bản Linux cung cấp các thống kê mạng qua các tùy chọn sau:
- **-n DEV:** Các thống kê giao diện mạng
- **-n EDEV:** Các lỗi giao diện mạng
- **-n IP:** Các thống kê datagram IP
- **-n EIP:** Các thống kê lỗi IP
- **-n TCP:** Các thống kê TCP
- **-n ETCP:** Các thống kê lỗi TCP
- **-n SOCK:** Sử dụng socket

Các thống kê được cung cấp bao gồm những thống kê được trình bày trong Bảng 10.5.

Bảng 10.5 Các thống kê mạng Linux sar
| Tùy chọn | Chỉ số | Mô tả | Đơn vị |
| --- | --- | --- | --- |
| -n DEV | rxpkt/s | Các gói tin nhận được | Gói tin/s |
| -n DEV | txpkt/s | Các gói tin truyền đi | Gói tin/s |
| -n DEV | rxkB/s | Các kilobyte nhận được | Kilobyte/s |
| -n DEV | txkB/s | Các kilobyte truyền đi | Kilobyte/s |
| -n DEV | rxpck/s | Các gói tin nén nhận được | Gói tin/s |
| -n DEV | txpck/s | Các gói tin nén truyền đi | Gói tin/s |
| -n DEV | rxmcst/s | Các gói tin multicast nhận được | Gói tin/s |
| -n DEV | %ifutil | Mức sử dụng giao diện: cho toàn song công, giá trị lớn hơn của rx hoặc tx | Phần trăm |
| -n EDEV | rxerr/s | Các lỗi gói tin nhận được | Gói tin/s |
| -n EDEV | txerr/s | Các lỗi gói tin truyền đi | Gói tin/s |
| -n EDEV | coll/s | Các va chạm | Gói tin/s |
| -n EDEV | rxdrop/s | Các gói tin nhận được bị đánh rơi (bộ đệm đầy) | Gói tin/s |
| -n EDEV | txdrop/s | Các gói tin truyền đi bị đánh rơi (bộ đệm đầy) | Gói tin/s |
| -n EDEV | txcarr/s | Các lỗi truyền sóng (transmission carrier errors) | Lỗi/s |
| -n EDEV | rxfram/s | Các lỗi canh lề nhận được | Lỗi/s |
| -n EDEV | rxfifo/s | Các lỗi tràn FIFO cho gói tin nhận được | Gói tin/s |
| -n EDEV | txfifo/s | Các lỗi tràn FIFO cho gói tin truyền đi | Gói tin/s |
| -n IP | irec/s | Các datagram đầu vào (nhận được) | Datagram/s |
| -n IP | fwddgm/s | Các datagram được chuyển tiếp | Datagram/s |
| -n IP | idel/s | Các datagram IP đầu vào (bao gồm ICMP) | Datagram/s |
| -n IP | orq/s | Các yêu cầu datagram đầu ra (truyền đi) | Datagram/s |
| -n IP | asmrq/s | Các phân đoạn IP nhận được | Phân đoạn/s |
| -n IP | asmok/s | Các datagram IP được lắp ráp lại | Datagram/s |
| -n IP | fragok/s | Các datagram IP được phân mảnh | Datagram/s |
| -n IP | fragcrt/s | Các phân đoạn datagram IP được tạo ra | Phân đoạn/s |
| -n EIP | ihdrerr/s | Các lỗi IP header | Datagram/s |
| -n EIP | iadrerr/s | Các lỗi địa chỉ IP đích không hợp lệ | Datagram/s |
| -n EIP | iukwnpr/s | Các lỗi giao thức không xác định | Datagram/s |
| -n EIP | idisc/s | Các lần rớt IP đầu vào (ví dụ: bộ đệm đầy) | Datagram/s |
| -n EIP | odisc/s | Các lần rớt IP đầu ra (ví dụ: bộ đệm đầy) | Datagram/s |
| -n EIP | onort/s | Các lỗi không có định tuyến cho datagram đầu ra | Datagram/s |
| -n EIP | asmf/s | Các thất bại khi lắp ráp lại IP | Thất bại/s |
| -n EIP | fragf/s | Các lần rớt phân mảnh IP | Datagram/s |
| -n TCP | active/s | Các kết nối TCP hoạt động mới (connect(2)) | Kết nối/s |
| -n TCP | passive/s | Các kết nối TCP thụ động mới (accept(2)) | Kết nối/s |
| -n TCP | iseg/s | Các phân đoạn đầu vào (nhận được) | Phân đoạn/s |
| -n TCP | oseg/s | Các phân đoạn đầu ra (truyền đi) | Phân đoạn/s |
| -n ETCP | atmptf/s | Các lần thất bại kết nối TCP hoạt động | Kết nối/s |
| -n ETCP | estres/s | Các lần reset được thiết lập | Resets/s |
| -n ETCP | retrans/s | Các phân đoạn TCP được truyền lại | Phân đoạn/s |
| -n ETCP | isegerr/s | Các lỗi phân đoạn | Phân đoạn/s |
| -n ETCP | orsts/s | Các lần gửi reset | Phân đoạn/s |
| -n SOCK | totsck | Tổng số socket đang sử dụng | Sockets |
| -n SOCK | tcpsck | Tổng số socket TCP đang sử dụng | Sockets |
| -n SOCK | udpsck | Tổng số socket UDP đang sử dụng | Sockets |
| -n SOCK | rawsck | Tổng số socket RAW đang sử dụng | Sockets |
| -n SOCK | ip-frag | Các phân đoạn IP hiện đang được xếp hàng | Phân đoạn |
| -n SOCK | tcp-tw | Các socket TCP trong trạng thái TIME_WAIT | Sockets |

Không được liệt kê là các nhóm ICMP, NFS, và SOFT (xử lý mạng bằng phần mềm), và các biến thể IPv6: IP6, EIP6, SOCK6, và UDP6. Xem trang man để biết danh sách đầy đủ các thống kê, thứ cũng lưu ý một số tên SNMP tương đương (ví dụ: IpInReceives cho irec/s). Nhiều thống kê sar(1) có các tên dễ nhớ trong thực tế, vì chúng bao gồm hướng và các đơn vị được đo lường: rx cho "received" (nhận được), i cho "input," seg cho "segments," v.v.

Ví dụ này in các thống kê TCP mỗi giây:
```bash
$ sar -n TCP 1
Linux 5.3.0-1010-aws (ip-10-1-239-218)    02/27/20    _x86_64_    (2 CPU)

07:32:45      active/s passive/s    iseg/s    oseg/s
07:32:46          0.00     12.00    186.00  28837.00
07:32:47          0.00     13.00    203.00  33584.00
07:32:48          0.00     11.00   1999.00  24441.00
07:32:49          0.00      7.00     92.00   8908.00
07:32:50          0.00     10.00    114.00  13795.00
[...]
```
Kết quả cho thấy một tốc độ kết nối thụ động (inbound) khoảng 10 mỗi giây.

Khi kiểm tra các thiết bị mạng (DEV), cột thống kê giao diện mạng (IFACE) liệt kê tất cả các giao diện; tuy nhiên, thường chỉ có một cái là đáng quan tâm. Ví dụ sau đây sử dụng một chút awk(1) để lọc kết quả:
```bash
$ sar -n DEV 1 | awk 'NR == 3 || $2 == "ens5"'
07:35:41  IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s %ifutil
07:35:42   ens5    134.00  11483.00     10.22   6328.72      0.00      0.00      0.00      0.00
07:35:43   ens5    170.00  20354.00     13.62   6925.27      0.00      0.00      0.00      0.00
07:35:44   ens5    185.00  28228.00     14.33   8586.79      0.00      0.00      0.00      0.00
07:35:45   ens5    180.00  23093.00     14.59   7452.49      0.00      0.00      0.00      0.00
07:35:46   ens5   1525.00  19594.00    137.48   7044.81      0.00      0.00      0.00      0.00
07:35:47   ens5    146.00  10282.00     12.05   6876.80      0.00      0.00      0.00      0.00
[...]
```
Điều này hiển thị thông lượng mạng cho truyền và nhận, và các thống kê khác.

Công cụ atop(1) cũng có khả năng lưu trữ các thống kê.

### 10.6.7 nicstat
nicstat(1) in các thống kê giao diện mạng, bao gồm thông lượng và mức sử dụng. Nó tuân theo phong cách của các công cụ thống kê tài nguyên truyền thống, iostat(1) và mpstat(1).

Dưới đây là kết quả cho phiên bản 1.92 trên Linux:
```bash
# nicstat -z 1
    Time      Int   rkB/s   wkB/s   rpK/s   wpK/s    rAvs    wAvs %Util    Sat
01:20:58     eth0    0.07    0.00    0.95    0.02   79.43   64.81  0.00   0.00
01:20:58     eth4    0.28    0.01    0.20    0.10 1451.3   80.11  0.00   0.00
01:20:58  vlan123    0.00    0.00    0.00    0.02   42.00   64.81  0.00   0.00
01:20:58      br0    0.00    0.00    0.00    0.00   42.00   42.07  0.00   0.00
    Time      Int   rkB/s   wkB/s   rpK/s   wpK/s    rAvs    wAvs %Util    Sat
01:20:59     eth4 42376.0   974.5 28589.4 14002.1  1517.8   71.27  35.5   0.00
    Time      Int   rkB/s   wkB/s   rpK/s   wpK/s    rAvs    wAvs %Util    Sat
01:21:00     eth0    0.05    0.00    1.00    0.00   56.00   42.07  0.00   0.00
01:21:00     eth4 41834.7   977.9 28221.5 14058.3  1517.9   71.23  35.1   0.00
    Time      Int   rkB/s   wkB/s   rpK/s   wpK/s    rAvs    wAvs %Util    Sat
01:21:01     eth0    0.05    0.00    1.00    0.00   56.00   42.07  0.00   0.00
01:21:01     eth4 42017.9   979.0 28345.0 14073.0  1517.9   71.24  35.2   0.00
```
Kết quả đầu tiên là bản tóm tắt kể từ khi boot, theo sau là các bản tóm tắt theo khoảng thời gian. Bản tóm tắt theo khoảng thời gian cho thấy giao diện eth4 đang chạy ở mức 35% sử dụng (giá trị này đang báo cáo mức sử dụng hiện tại cao nhất từ hướng RX hoặc TX) và đang đọc ở mức 42 Mbytes/s.

Các trường bao gồm tên giao diện (Int), mức sử dụng tối đa (%Util), một giá trị phản ánh các số lượng lỗi bão hòa giao diện (Sat), và một loạt các thống kê được tiền tố với r cho "read" (nhận) và w cho "write" (truyền):
- **kB/s:** Kbytes mỗi giây
- **Pk/s:** Gói tin mỗi giây
- **Avs:** Kích thước gói tin trung bình, byte

Các tùy chọn được hỗ trợ trong phiên bản này bao gồm -z để bỏ qua các dòng toàn số không (các giao diện rảnh rỗi) và -t cho các thống kê TCP.

nicstat(1) đặc biệt hữu ích cho phương pháp USE, vì nó cung cấp các giá trị mức sử dụng và độ bão hòa.

### 10.6.8 ethtool
ethtool(8) có thể được sử dụng để kiểm tra cấu hình tĩnh của các giao diện mạng với các tùy chọn -i và -k, và cũng in các thống kê trình điều khiển với -S. Ví dụ:
```bash
# ethtool -S eth0
NIC statistics:
     tx_timeout: 0
     suspend: 0
     resume: 0
     wd_expired: 0
     interface_up: 1
     interface_down: 0
     admin_q_pause: 0
     queue_0_tx_cnt: 100219217
     queue_0_tx_bytes: 84830086234
     queue_0_tx_queue_stop: 0
     queue_0_tx_queue_wakeup: 0
     queue_0_tx_dma_mapping_err: 0
     queue_0_tx_linearize: 0
     queue_0_tx_linearize_failed: 0
     queue_0_tx_napi_comp: 112514572
     queue_0_tx_tx_poll: 112514649
     queue_0_tx_doorbells: 52759561
[...]
```
Việc này lấy các thống kê từ kernel ethtool framework, thứ mà nhiều trình điều khiển thiết bị mạng hỗ trợ. Các trình điều khiển thiết bị có thể định nghĩa các thống kê ethtool của riêng chúng.

Tùy chọn -i hiển thị các chi tiết trình điều khiển, và -k hiển thị các tunables giao diện. Ví dụ:
```bash
# ethtool -k eth0
Features for eth0:
rx-checksumming: on
[...]
tcp-segmentation-offload: off
    tx-tcp-segmentation: off [fixed]
    tx-tcp-ecn-segmentation: off [fixed]
    tx-tcp-mangleid-segmentation: off [fixed]
    tx-tcp6-segmentation: off [fixed]
udp-fragmentation-offload: off
generic-segmentation-offload: on
generic-receive-offload: on
large-receive-offload: off [fixed]
rx-vlan-offload: off [fixed]
tx-vlan-offload: off [fixed]
ntuple-filters: off [fixed]
receive-hashing: on
highdma: on
[...]
```
Ví dụ này là một thực thể đám mây với trình điều khiển ena, với tcp-segmentation-offload đã bị tắt. Tùy chọn -K có thể được sử dụng để thay đổi những tunables này.

### 10.6.9 tcplife
tcplife(8) là một công cụ BCC và bpftrace để truy vết tuổi thọ của các phiên TCP, hiển thị thời lượng, các chi tiết địa chỉ, thông lượng, và khi có thể, ID cùng tên tiến trình chịu trách nhiệm.

Phần sau đây cho thấy tcplife(8) từ BCC, trên một thực thể sản xuất 48-CPU:
```bash
# tcplife
PID   COMM      LADDR           LPORT RADDR           RPORT TX_KB RX_KB MS
4169  java      100.1.111.231   32648 100.2.0.48      6001      0     0 3.99
4169  java      100.1.111.231   32650 100.2.0.48      6001      0     0 4.10
4169  java      100.1.111.231   32644 100.2.0.48      6001      0     0 8.41
4169  java      100.1.111.231   40158 100.2.116.192   6001      7    33 3590.91
4169  java      100.1.111.231   56940 100.5.177.31    6101      0     0 2.48
4169  java      100.1.111.231   6001  100.2.176.45    49482     0     0 17.94
4169  java      100.1.111.231   18926 100.5.102.250   6101      0     0 0.90
4169  java      100.1.111.231   44530 100.2.31.140    6001      0     0 2.64
4169  java      100.1.111.231   44406 100.2.8.109     6001     11    28 3982.11
34781 sshd      100.1.111.231   22    100.17.121      41566     5     7 2317.30
4169  java      100.1.111.231   49726 100.2.9.217     6001     11    28 3938.47
4169  java      100.1.111.231   58858 100.2.173.248   6001      9    30 2820.51
[...]
```
Kết quả này cho thấy một loạt các kết nối hoặc tồn tại ngắn ngủi (dưới 20 mili giây) hoặc tồn tại lâu dài (trên ba giây), như được hiển thị trong cột thời lượng (MS cho mili giây). Đây là một pool máy chủ ứng dụng lắng nghe trên cổng 6001. Hầu hết các phiên trong ảnh chụp màn hình này cho thấy các kết nối tới cổng 6001 trên các máy chủ ứng dụng từ xa, với chỉ một kết nối tới cổng 6001 cục bộ. Một phiên ssh cũng đã được nhìn thấy, được sở hữu bởi sshd và cổng cục bộ 22—một phiên inbound.

Phiên bản BCC của tcplife(8) hỗ trợ các tùy chọn bao gồm:
- **-t:** Bao gồm cột thời gian (HH:MM:SS)
- **-w:** Các cột rộng hơn (để khớp tốt hơn các địa chỉ IPv6)
- **-p PID:** Chỉ truy vết tiến trình này
- **-L PORT[,PORT,...]:** Chỉ truy vết các phiên với những cổng cục bộ này
- **-D PORT[,PORT,...]:** Chỉ truy vết các phiên với những cổng từ xa này

Công cụ này hoạt động bằng cách truy vết các sự kiện thay đổi trạng thái socket TCP, và in các chi tiết tóm tắt khi trạng thái chuyển sang TCP_CLOSE. Những sự kiện thay đổi trạng thái này ít thường xuyên hơn nhiều so với các gói tin, làm cho cách tiếp cận này ít tốn kém hơn nhiều về chi phí so với các trình ngửi gói tin cho mỗi gói tin (per-packet sniffers). Điều này khiến tcplife(8) có thể chấp nhận được để chạy liên tục như một trình ghi nhật ký luồng TCP trên các máy chủ sản xuất Netflix.

Việc tạo ra udplife(8) cho việc truy vết các phiên UDP là một bài tập Chương 10 trong cuốn sách *BPF Performance Tools* [Gregg 19]; tôi đã đăng tải một giải pháp ban đầu [Gregg 19d].

### 10.6.10 tcptop
tcptop(8) là một công cụ BCC hiển thị các tiến trình hàng đầu sử dụng TCP. Ví dụ, từ một thực thể Hadoop 36-CPU sản xuất:
```bash
# tcptop
09:01:13 loadavg: 33.32 36.11 38.63 26/4021 123015

PID    COMM      LADDR                 RADDR                 RX_KB  TX_KB
118119 java      100.1.58.46:36246     100.2.52.79:50010     16840      0
122833 java      100.1.58.46:52426     100.2.6.98:50010          0   3112
122833 java      100.1.58.46:50010     100.2.50.176:55396     3112      0
120711 java      100.1.58.46:50010     100.2.7.75:23358       2922      0
121635 java      100.1.58.46:50010     100.2.5.101:56426      2922      0
121219 java      100.1.58.46:50010     100.2.62.83:40570      2858      0
121219 java      100.1.58.46:42324     100.2.4.58:50010          0   2858
122927 java      100.1.58.46:50010     100.2.2.191:29338      2351      0
[...]
```
Kết quả này cho thấy một kết nối tại vị trí trên cùng đang nhận được hơn 16 Mbytes trong khoảng thời gian này. Theo mặc định, màn hình được cập nhật mỗi giây.

Việc này hoạt động bằng cách truy vết các đường dẫn mã gửi và nhận TCP, và tóm tắt dữ liệu trong một BPF map cho hiệu quả. Ngay cả khi đó, những sự kiện này có thể diễn ra thường xuyên, và trên các hệ thống có thông lượng mạng cao, chi phí này có thể trở nên đáng kể.

Các tùy chọn bao gồm:
- **-C:** Không xóa màn hình.
- **-p PID:** Chỉ đo lường tiến trình này.

tcptop(8) cũng chấp nhận một khoảng thời gian và số lượng tùy chọn.

### 10.6.11 tcpretrans
tcpretrans(8) là một công cụ BCC và bpftrace để truy vết các lần truyền lại TCP, hiển thị địa chỉ IP và các chi tiết cổng cùng trạng thái TCP. Phần sau đây cho thấy tcpretrans(8) từ BCC, trên một thực thể sản xuất:
```bash
# tcpretrans
Tracing retransmits ... Hit Ctrl-C to end
TIME     PID  IP LADDR:LPORT          T> RADDR:RPORT          STATE
00:20:11 72475 4  100.1.58.46:35908    R> 100.2.0.167:50010    ESTABLISHED
00:20:11 72475 4  100.1.58.46:35908    R> 100.2.0.167:50010    ESTABLISHED
00:20:11 72475 4  100.1.58.46:35908    R> 100.2.0.167:50010    ESTABLISHED
00:20:12 60695 4  100.1.58.46:52346    R> 100.2.6.189:50010    ESTABLISHED
00:20:12 60695 4  100.1.58.46:52346    R> 100.2.6.189:50010    ESTABLISHED
00:20:12 60695 4  100.1.58.46:52346    R> 100.2.6.189:50010    ESTABLISHED
00:20:13 60695 6  ::ffff:100.1.58.46:13562 R> ::ffff:100.2.51.209:47356 FIN_WAIT1
00:20:13 60695 6  ::ffff:100.1.58.46:13562 R> ::ffff:100.2.51.209:47356 FIN_WAIT1
[...]
```
Kết quả này cho thấy một tỷ lệ thấp các lần truyền lại, một vài lần mỗi giây (cột TIME), hầu hết là cho các phiên ở trạng thái ESTABLISHED. Một tỷ lệ cao ở trạng thái ESTABLISHED có thể chỉ ra một vấn đề mạng bên ngoài. Một tỷ lệ cao trong trạng thái SYN_SENT có thể chỉ ra một ứng dụng máy chủ bị quá tải thứ không tiêu thụ listen backlog của nó đủ nhanh.

Việc này hoạt động bằng cách truy vết các sự kiện truyền lại trong kernel. Vì những sự kiện này thường không thường xuyên, chi phí nên là không đáng kể. So sánh điều này với việc các lần truyền lại được phân tích một cách lịch sử như thế nào bằng cách sử dụng một trình ngửi gói tin để bắt tất cả các gói tin, và sau đó xử lý hậu kỳ để tìm các lần truyền lại—cả hai bước đều có thể tiêu tốn chi phí CPU đáng kể. Bắt gói tin chỉ có thể thấy các chi tiết trên đường truyền, trong khi tcpretrans(8) in trạng thái TCP trực tiếp từ kernel, và có thể được tăng cường để in thêm các trạng thái kernel nếu cần.

Các tùy chọn cho phiên bản BCC bao gồm:
- **-l:** Bao gồm các lần thử thăm dò mất gói tin đuôi (tail loss probe attempts) (thêm một kprobe cho tcp_send_loss_probe())
- **-c:** Đếm các lần truyền lại cho mỗi luồng

Tùy chọn -c thay đổi hành vi của tcpretrans(8), khiến nó in một bản tóm tắt các số lượng thay vì các chi tiết cho mỗi sự kiện.

### 10.6.12 bpftrace
bpftrace là một trình truy vết dựa trên BPF cung cấp một ngôn ngữ lập trình cấp cao, cho phép tạo ra các lệnh một dòng mạnh mẽ và các script ngắn. Nó rất phù hợp cho việc phân tích mạng tùy chỉnh dựa trên các manh mối từ các công cụ khác. Nó có thể kiểm tra các sự kiện mạng từ bên trong kernel và các ứng dụng, bao gồm các kết nối socket, socket I/O, truyền tải TCP, rớt backlog, các lần truyền lại TCP, và các chi tiết khác. Những khả năng này hỗ trợ việc đặc tính hóa khối lượng công việc và phân tích độ trễ.

bpftrace được giải thích trong Chương 15. Phần này trình bày một số ví dụ cho phân tích mạng: các lệnh một dòng, truy vết socket, và truy vết TCP.

**Các lệnh Một-Dòng**
Các lệnh một dòng sau đây rất hữu ích và trình diễn các khả năng khác nhau của bpftrace.

Đếm socket accept(2) theo PID và tên tiến trình:
```bash
bpftrace -e 't:syscalls:sys_enter_accept* { @[pid, comm] = count(); }'
```
Đếm socket connect(2) theo PID và tên tiến trình:
```bash
bpftrace -e 't:syscalls:sys_enter_connect* { @[pid, comm] = count(); }'
```
Đếm socket connect(2) theo user stack trace:
```bash
bpftrace -e 't:syscalls:sys_enter_connect* { @[ustack, comm] = count(); }'
```
Đếm số byte gửi/nhận theo hướng, PID on-CPU, và tên tiến trình:
```bash
bpftrace -e 'kr:sock_sendmsg,kr:sock_recvmsg { @[func, pid, comm] =
    sum((int32)retval); }'
```
Đếm các kết nối TCP theo PID on-CPU và tên tiến trình:
```bash
bpftrace -e 'k:tcp_v*_connect { @[pid, comm] = count(); }'
```
Đếm các lệnh accept TCP theo PID on-CPU và tên tiến trình:
```bash
bpftrace -e 'k:inet_csk_accept { @[pid, comm] = count(); }'
```
Đếm số byte TCP gửi/nhận theo PID on-CPU và tên tiến trình:
```bash
bpftrace -e 'k:tcp_sendmsg,k:tcp_recvmsg { @[func, pid, comm] = count(); }'
```
Gửi byte TCP dưới dạng biểu đồ histogram:
```bash
bpftrace -e 'k:tcp_sendmsg { @send_bytes = hist(arg2); }'
```
Nhận byte TCP dưới dạng biểu đồ histogram:
```bash
bpftrace -e 'kr:tcp_recvmsg /retval >= 0/ { @recv_bytes = hist(retval); }'
```
Đếm các lần truyền lại TCP theo loại và máy chủ từ xa (giả định IPv4):
```bash
bpftrace -e 't:tcp:tcp_retransmit_* { @[probe, ntop(2, args->saddr)] = count(); }'
```
Đếm tất cả các chức năng TCP (thêm chi phí cao cho TCP):
```bash
bpftrace -e 'k:tcp_* { @[func] = count(); }'
```
Đếm số byte UDP gửi/nhận theo PID on-CPU và tên tiến trình:
```bash
bpftrace -e 'k:udp_sendmsg,k:udp_recvmsg { @[func, pid, comm] = count(); }'
```
Gửi byte UDP dưới dạng biểu đồ histogram:
```bash
bpftrace -e 'k:udp_sendmsg { @send_bytes = hist(arg2); }'
```
Nhận byte UDP dưới dạng biểu đồ histogram:
```bash
bpftrace -e 'kr:udp_recvmsg /retval >= 0/ { @recv_bytes = hist(retval); }'
```
Đếm vết kernel stack truyền tải:
```bash
bpftrace -e 't:net:net_dev_xmit { @[kstack] = count(); }'
```
Hiển thị histogram nhận CPU cho mỗi thiết bị:
```bash
bpftrace -e 't:net:netif_receive_skb { @[str(args->name)] = lhist(cpu, 0, 128, 1); }'
```
Đếm các chức năng tầng ieee80211 (thêm chi phí cao cho gói tin):
```bash
bpftrace -e 'k:ieee80211_* { @[func] = count(); }'
```
Đếm tất cả các chức năng trình điều khiển thiết bị ixgbevf (thêm chi phí cao cho ixgbevf):
```bash
bpftrace -e 'k:ixgbevf_* { @[func] = count(); }'
```
Đếm tất cả các tracepoints trình điều khiển iwl (thêm chi phí cao cho iwl):
```bash
bpftrace -e 't:iwlwifi:*,t:iwlwifi_io:* { @[probe] = count(); }'
```

**Truy vết Socket (Socket Tracing)**
Truy vết các sự kiện mạng tại tầng socket có ưu điểm là tiến trình chịu trách nhiệm vẫn on-CPU, giúp việc xác định ứng dụng và đường dẫn mã trở nên đơn giản. Ví dụ, đếm các ứng dụng gọi syscall accept(2):
```bash
# bpftrace -e 't:syscalls:sys_enter_accept* { @[pid, comm] = count(); }'
Attaching 1 probe...
^C

@[573, sshd]: 2
@[1948, mysqld]: 41
```
Kết quả cho thấy trong khi truy vết, mysqld đã gọi accept(2) 41 lần, và sshd đã gọi accept(2) 2 lần.

User-level stack trace có thể được bao gồm để chỉ ra đường dẫn mã dẫn tới accept(2). Ví dụ, đếm theo user-level stack trace và tên tiến trình:
```bash
# bpftrace -e 't:syscalls:sys_enter_accept* { @[ustack, comm] = count(); }'
Attaching 1 probe...
^C

@[
    accept+79
    Mysqld_socket_listener::listen_for_connection_event()+283
    mysqld_main(int, char**)+15577
    __libc_start_main+243
    0x49564100fe8c4b3d
, mysqld]: 22
```
Kết quả này cho thấy mysqld đã chấp nhận các kết nối thông qua một đường dẫn mã bao gồm Mysqld_socket_listener::listen_for_connection_event(). Bằng cách thay đổi "accept" thành "connect", lệnh một dòng này sẽ xác định các đường dẫn mã dẫn tới việc tạo ra các kết nối từ xa. Tôi đã sử dụng các lệnh một dòng như vậy để giải thích các kết nối mạng bí ẩn, cho biết mã nào đang gọi chúng.

**Các Tracepoints Socket**
Ngoài các syscall socket, còn có các socket tracepoints. Từ một kernel 5.3:
```bash
# bpftrace -l 't:sock:*'
tracepoint:sock:sock_rcvqueue_full
tracepoint:sock:sock_exceed_buf_limit
tracepoint:sock:inet_sock_set_state
```
Tracepoint sock:inet_sock_set_state được sử dụng bởi công cụ tcplife(8) đã mô tả trước đó. Dưới đây là một ví dụ sử dụng nó để đếm số lượng địa chỉ IPv4 nguồn và đích cho các kết nối mới:
```bash
# bpftrace -e 't:sock:inet_sock_set_state
    /args->newstate == 1 && args->family == 2/ {
    @[ntop(args->saddr), ntop(args->daddr)] = count() }'
Attaching 1 probe...
^C
@[127.0.0.1, 127.0.0.1]: 2
@[10.1.239.218, 10.29.225.81]: 18
```
Lệnh một dòng này đang trở nên dài dòng, và sẽ dễ dàng hơn để lưu vào một tập tin chương trình bpftrace (.bt) để chỉnh sửa và thực thi. Như một ví dụ, tập tin có thể bao gồm các kernel headers thích hợp sao cho dòng lọc có thể được viết lại bằng cách sử dụng các tên hằng số thay vì các số được viết cứng (thứ không đáng tin cậy), như thế này:
```c
/args->newstate == TCP_ESTABLISHED && args->family == AF_INET/ {
```
Ví dụ tiếp theo là về một tập tin chương trình: socketio.bt.

**socketio.bt**
Như một ví dụ phức tạp hơn, công cụ socketio(8) hiển thị socket I/O với các chi tiết tiến trình, hướng, giao thức, và cổng. Kết quả ví dụ:
```bash
# ./socketio.bt
Attaching 2 probes...
^C
[...]
@io[sshd, 21925, read, UNIX, 0]: 40
@io[sshd, 21925, read, TCP, 37408]: 41
@io[systemd, 1, write, UNIX, 0]: 51
@io[systemd, 1, read, UNIX, 0]: 57
@io[systemd-udevd, 241, write, NETLINK, 0]: 65
@io[systemd-udevd, 241, read, NETLINK, 0]: 105
@io[dbus-daemon, 525, write, UNIX, 0]: 98
@io[systemd-logind, 526, read, UNIX, 0]: 105
@io[systemd-udevd, 241, read, UNIX, 0]: 127
@io[snapd, 31927, read, NETLINK, 0]: 150
@io[dbus-daemon, 525, read, UNIX, 0]: 160
@io[mysqld, 1948, write, TCP, 55010]: 8147
@io[mysqld, 1948, read, TCP, 55010]: 24466
```
Điều này cho thấy hầu hết socket I/O là của mysqld, với các lệnh đọc và ghi tới cổng TCP 55010, cổng tạm thời mà một máy khách đang sử dụng.

Nguồn cho socketio(8) là:
```c
#!/usr/local/bin/bpftrace

#include <net/sock.h>

kprobe:sock_recvmsg
{
          $sock = (struct socket *)arg0;
          $dport = $sock->sk->____sk_common.skc_dport;
          $dport = ($dport >> 8) | (($dport << 8) & 0xff00);
          @io[comm, pid, "read", $sock->sk->____sk_common.skc_prot->name, $dport] =
              count();
}

kprobe:sock_sendmsg
{
          $sock = (struct socket *)arg0;
          $dport = $sock->sk->____sk_common.skc_dport;
          $dport = ($dport >> 8) | (($dport << 8) & 0xff00);
          @io[comm, pid, "write", $sock->sk->____sk_common.skc_prot->name, $dport] =
              count();
}
```
Đây là một ví dụ về việc lấy các chi tiết từ một cấu trúc kernel, trong trường hợp này là struct socket, thứ cung cấp tên giao thức và cổng đích. Cổng đích là dạng big endian, và được chuyển đổi sang little endian (cho bộ xử lý x86) trước khi được đưa vào bản đồ @io. Script này có thể được sửa đổi để hiển thị các byte được truyền tải thay vì số lượng I/O.

**Truy vết TCP (TCP Tracing)**
Truy vết tại mức TCP cung cấp cái nhìn sâu sắc về các sự kiện và thành phần nội bộ giao thức TCP, cũng như các sự kiện không liên quan đến một socket (ví dụ: quét cổng TCP).

**TCP Tracepoints**
Instrumenting các thành phần nội bộ TCP thường yêu cầu sử dụng kprobes, nhưng có một số TCP tracepoints có sẵn. Từ một kernel 5.3:
```bash
# bpftrace -l 't:tcp:*'
tracepoint:tcp:tcp_retransmit_skb
tracepoint:tcp:tcp_send_reset
tracepoint:tcp:tcp_receive_reset
tracepoint:tcp:tcp_destroy_sock
tracepoint:tcp:tcp_rcv_space_adjust
tracepoint:tcp:tcp_retransmit_synack
tracepoint:tcp:tcp_probe
```
Tracepoint tcp:tcp_retransmit_skb được sử dụng bởi công cụ tcpretrans(8) trước đó. Tracepoints được ưa chuộng hơn cho tính ổn định, nhưng khi chúng không thể giải quyết vấn đề của bạn, bạn có thể sử dụng kprobes trên các chức năng TCP của kernel. Đếm chúng:
```bash
# bpftrace -e 'k:tcp_* { @[func] = count(); }'
Attaching 336 probes...
^C
[...]
@[tcp_try_keep_open]: 1
@[tcp_ooo_try_coalesce]: 1
@[tcp_reset]: 1
[...]
@[tcp_push]: 3191
@[tcp_established_options]: 3584
@[tcp_wfree]: 4408
@[tcp_small_queue_check.isra.0]: 4617
@[tcp_rate_check_app_limited]: 7022
@[tcp_poll]: 8898
@[tcp_release_cb]: 18330
@[tcp_send_msg]: 28168
@[tcp_sendmsg]: 31450
@[tcp_sendmsg_locked]: 31949
@[tcp_write_xmit]: 33276
@[tcp_tx_timestamp]: 33485
```
Điều này cho thấy chức năng được gọi thường xuyên nhất mang tên tcp_tx_timestamp(), được gọi 33,485 lần trong khi truy vết. Các chức năng đếm có thể xác định các mục tiêu để truy vết chi tiết hơn. Lưu ý rằng hầu hết các chức năng TCP đều có chi phí bổ sung đáng kể do số lượng và tần suất của các hàm được truy vết. Đối với tác vụ cụ thể này, tôi muốn sử dụng hồ sơ chức năng Ftrace thay thế qua công cụ funccount(8) perf-tools, vì chi phí và thời gian khởi tạo của nó thấp hơn nhiều. Xem Chương 14, Ftrace.

**tcpsynbl.bt**
Công cụ tcpsynbl(8) là một ví dụ về việc instrument TCP sử dụng kprobes. Nó hiển thị độ dài của hàng đợi backlog listen(2) được chia nhỏ theo độ dài hàng đợi sao cho bạn có thể biết hàng đợi đang gần đạt mức tràn như thế nào (thứ gây ra các lần rớt các gói tin TCP SYN). Kết quả ví dụ:
```bash
# tcpsynbl.bt
Attaching 4 probes...
Tracing SYN backlog size. Ctrl-C to end.
04:44:31 dropping a SYN.
04:44:31 dropping a SYN.
04:44:31 dropping a SYN.
04:44:31 dropping a SYN.
04:44:31 dropping a SYN.
^C

@backlog[backlog limit]: histogram of backlog size

@backlog[128]:
[0]                    473 |@                                                   |
[1]                    502 |@                                                   |
[2, 4)                1001 |@@@                                                 |
[4, 8)                1996 |@@@@@@                                              |
[8, 16)               3943 |@@@@@@@@@@@@                                        |
[16, 32)              7718 |@@@@@@@@@@@@@@@@@@@@@@@                             |
[32, 64)             14460 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        |
[64, 128)            17246 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[128, 256)            1844 |@@@@@                                               |
```
Trong khi đang chạy, tcpsynbl.bt in các dấu thời gian và rớt gói SYN nếu chúng xảy ra khi truy vết. Khi kết thúc (bằng cách nhấn Ctrl-C), một histogram về kích thước backlog được in cho mỗi giới hạn backlog trong kernel. Kết quả này cho thấy một giới hạn 128 và một phân phối nơi giới hạn đó đã đạt tới 1844 lần (thanh 128 tới 256). Phân phối này cho thấy sự bão hòa backlog khi các SYN mới đến.

Bằng việc giám sát độ dài backlog, bạn có thể kiểm tra xem nó có đang phát triển theo thời gian hay không, đưa ra cảnh báo sớm rằng các SYN drops sắp xảy ra. Đây là một phần quan trọng của quy hoạch dung lượng.

Nguồn cho tcpsynbl(8) là:
```c
#!/usr/local/bin/bpftrace

#include <net/sock.h>

BEGIN
{
          printf("Tracing SYN backlog size. Ctrl-C to end.
");
}

kprobe:tcp_v4_syn_recv_sock,
kprobe:tcp_v6_syn_recv_sock
{
          $sock = (struct sock *)arg0;
          @backlog[$sock->sk_max_ack_backlog & 0xffffffff] =
              hist($sock->sk_ack_backlog);
          if ($sock->sk_ack_backlog > $sock->sk_max_ack_backlog) {
              time("%H:%M:%S dropping a SYN.
");
          }
}

END
{
          printf("
@backlog[backlog limit]: histogram of backlog size
");
}
```
Hình dạng của phân phối in ra trước đó liên quan nhiều đến thang log2 được sử dụng bởi hist(), nơi các xô (buckets) sau này trải dài qua các phạm vi lớn hơn. Bạn có thể thay đổi hist() thành lhist() sử dụng:
```c
lhist($sock->sk_ack_backlog, 0, 1000, 10);
```
Điều này sẽ in ra một histogram tuyến tính với các phạm vi bằng nhau cho từng xô: trong trường hợp này, cho phạm vi từ 0 tới 1000 với kích thước xô là 10. Để biết thêm về lập trình bpftrace, xem Chương 15, BPF.

**Các nguồn Sự kiện (Event Sources)**
bpftrace có thể làm được nhiều việc hơn thế; Bảng 10.6 trình bày các nguồn sự kiện cho việc instrument các sự kiện mạng khác nhau.

Bảng 10.6 Các sự kiện mạng và các nguồn
| Sự kiện Mạng | Nguồn Sự kiện |
| --- | --- |
| Các giao thức ứng dụng | uprobes |
| Sockets | syscalls tracepoints |
| TCP | tcp tracepoints, kprobes |
| UDP | kprobes |
| IP và ICMP | kprobes |
| Gói tin (Packets) | skb tracepoints, kprobes |
| QDiscs và các hàng đợi trình điều khiển | qdisc và net tracepoints, kprobes |
| XDP | xdp tracepoints |
| Trình điều khiển thiết bị mạng | kprobes, một số có tracepoints |

Sử dụng tracepoints bất cứ khi nào có thể, vì chúng là một giao diện ổn định.

### 10.6.13 tcpdump
Các gói tin mạng có thể được bắt và kiểm tra trên Linux bằng tiện ích tcpdump(8). Điều này có thể in các bản tóm tắt gói tin ra STDOUT hoặc ghi dữ liệu gói tin thô vào một tập tin để phân tích sau này. Cách sau thường thực tế hơn: tốc độ gói tin có thể quá cao để theo kịp các bản tóm tắt theo thời gian thực của chúng.

Đổ (dumping) các gói tin từ giao diện eth4 vào một tập tin trong /tmp:
```bash
# tcpdump -i eth4 -w /tmp/out.tcpdump
tcpdump: listening on eth4, link-type EN10MB (Ethernet), capture size 65535 bytes
^C273893 packets captured
275752 packets received by filter
1859 packets dropped by kernel
```
Ghi chú kết quả lưu ý rằng bao nhiêu gói tin đã bị đánh rơi bởi kernel thay vì được chuyển tới tcpdump(8), vì tốc độ gói tin quá cao. Lưu ý rằng bạn có thể sử dụng -i any để bắt các gói tin từ tất cả các giao diện.

Kiểm tra các gói tin từ một tập tin dump:
```bash
# tcpdump -nr /tmp/out.tcpdump
reading from file /tmp/out.tcpdump, link-type EN10MB (Ethernet)
02:24:46.160754 IP 10.2.124.2.32863 > 10.2.203.2.5001: Flags [.], seq
3612664461:3612667357, ack 180214943, win 64436, options [nop,nop,TS val 322339741
ecr 346311608], length 2896
```
Mỗi dòng kết quả hiển thị thời gian của gói tin (với độ phân giải micro giây), các địa chỉ IP nguồn và đích, và các giá trị header TCP. Bằng việc nghiên cứu những thứ này, hoạt động của TCP có thể được hiểu chi tiết, bao gồm cả việc các tính năng nâng cao đang hoạt động tốt như thế nào cho khối lượng công việc của bạn.

Tùy chọn -n được sử dụng để không phân giải các địa chỉ IP thành tên máy chủ. Các tùy chọn khác bao gồm in các chi tiết rườm rà (verbose) khi có sẵn (-v), các headers liên kết dữ liệu (-e), và các bản dump địa chỉ hex (-x hoặc -X). Ví dụ:
```bash
# tcpdump -enr /tmp/out.tcpdump -vvv -X
reading from file /tmp/out.tcpdump, link-type EN10MB (Ethernet)
02:24:46.160754 80:71:1f:ad:50:48 > 84:2b:2b:61:b6:ed, ethertype IPv4 (0x0800),
length 2962: (tos 0x0, ttl 63, id 46508, offset 0, flags [DF], proto TCP (6), length
2948)
    10.2.124.2.32863 > 10.2.203.2.5001: Flags [.], cksum 0x667f (incorrect ->
0xc4da), seq 3612664461:3612667357, ack 180214943, win 64436, options [nop,nop,TS val
692339741 ecr 346311608], length 289
6
        0x0000:  4500 0b84 b5ac 4000 3f06 1fbf 0a02 7c02  E.....@.?...|..
        0x0010:  0a02 cb02 805f 1389 d754 e28d 0abc dc9f  ....._...T......
        0x0020:  8010 fbb4 667f 0000 0101 080a 2944 441d  ....f.......)DD.
        0x0030:  14a4 4bb8 3233 3435 3637 3839 3031 3233  ..K.234567890123
        0x0040:  3435 3637 3839 3031 3233 3435 3637 3839  4567890123456789
[...]
```
Trong quá trình phân tích hiệu năng, việc thay đổi cột dấu thời gian để hiển thị các thời gian delta giữa các gói tin (-ttt), hoặc thời gian đã trôi qua kể từ gói tin đầu tiên (-ttttt) có thể hữu ích.

Một biểu thức cũng có thể được cung cấp để mô tả cách lọc các gói tin (xem pcap-filter(7)) để tập trung vào các gói tin quan tâm. Điều này được thực hiện trong kernel để đạt hiệu quả (ngoại trừ trên Linux 2.0 và cũ hơn) bằng cách sử dụng BPF.

Việc bắt gói tin là tốn kém về CPU và bộ nhớ. Nếu có thể, hãy sử dụng tcpdump(8) chỉ trong các khoảng thời gian ngắn để giới hạn chi phí hiệu năng, và tìm kiếm các cách sử dụng các công cụ dựa trên BPF hiệu quả hơn chẳng hạn như bpftrace thay thế.

tshark(1) là một công cụ bắt gói tin dòng lệnh tương tự cung cấp khả năng lọc tốt hơn và các tùy chọn kết quả. Nó là phiên bản CLI của Wireshark.

### 10.6.14 Wireshark
Trong khi tcpdump(8) hoạt động tốt cho các cuộc điều tra thông thường, việc phân tích sâu hơn có thể tiêu tốn nhiều thời gian ở dòng lệnh. Công cụ Wireshark (trước đây là Ethereal) cung cấp một giao diện đồ họa cho việc bắt gói tin và kiểm tra và cũng có thể nhập các tệp dump từ tcpdump(8) [Wireshark 20]. Các tính năng hữu ích bao gồm nhận diện các kết nối mạng và các gói tin liên quan của chúng sao cho chúng có thể được nghiên cứu riêng biệt, và cả việc dịch hàng trăm protocol headers.

(Hình 10.12 Ảnh chụp màn hình Wireshark)

Hình 10.12 cho thấy một ảnh chụp màn hình ví dụ của Wireshark. Cửa sổ được chia theo chiều ngang thành ba phần. Ở phía trên là một bảng hiển thị các gói tin dưới dạng các hàng và các chi tiết dưới dạng các cột. Phần giữa hiển thị các chi tiết giao thức: trong ví dụ này, giao thức TCP đã được mở rộng và đích đến được chọn. Phần dưới cùng hiển thị gói tin thô dưới dạng thập lục phân ở bên trái và văn bản ở bên phải: vị trí của cổng đích TCP được tô sáng.

### 10.6.15 Các công cụ Khác (Other Tools)
Các công cụ phân tích mạng có trong các chương khác của cuốn sách này, và trong *BPF Performance Tools* [Gregg 19], được liệt kê trong Bảng 10.7.

Bảng 10.7 Các công cụ phân tích mạng khác
| Mục | Công cụ | Mô tả |
| --- | --- | --- |
| 5.5.3 | offcputime | Off-CPU profiling cho I/O mạng |
| [Gregg 19] | sockstat | Các thống kê socket cấp cao |
| [Gregg 19] | sofamily | Đếm các họ địa chỉ cho các socket mới, theo tiến trình |
| [Gregg 19] | soprotocol | Đếm các giao thức vận chuyển cho các socket mới, theo tiến trình |
| [Gregg 19] | soconnect | Truy vết các kết nối IP socket với các chi tiết I/O |
| [Gregg 19] | soaccept | Truy vết các socket IP chấp nhận kết nối với các chi tiết |
| [Gregg 19] | socketio | Tóm tắt các chi tiết socket với số lượng I/O |
| [Gregg 19] | socksize | Hiển thị kích thước I/O socket theo biểu đồ histogram theo từng tiến trình |
| [Gregg 19] | sormem | Hiển thị mức sử dụng bộ đệm nhận socket và các đợt tràn |
| [Gregg 19] | soconnlat | Tóm tắt độ trễ kết nối socket IP với các stacks |
| [Gregg 19] | so1stbyte | Tóm tắt độ trễ byte đầu tiên của socket IP |
| [Gregg 19] | tcpconnect | Truy vết các kết nối TCP hoạt động (connect()) |
| [Gregg 19] | tcpaccept | Truy vết các kết nối TCP thụ động (accept()) |
| [Gregg 19] | tcpwin | Truy vết các tham số cửa sổ tắc nghẽn TCP |
| [Gregg 19] | tcpnagle | Truy vết sử dụng TCP Nagle và các độ trễ truyền tải |
| [Gregg 19] | udpconnect | Truy vết các kết nối UDP mới từ localhost |
| [Gregg 19] | gethostlatency | Truy vết độ trễ DNS tra cứu qua các thư viện libc |
| [Gregg 19] | ipecn | Truy vết thông báo tắc nghẽn rõ ràng IP inbound |
| [Gregg 19] | superping | Đo lường thời gian ICMP echo từ network stack |
| [Gregg 19] | qdisc-fq (...) | Hiển thị độ trễ hàng đợi FQ qdisc |
| [Gregg 19] | netsize | Hiển thị các kích thước I/O thiết bị mạng |
| [Gregg 19] | nettxlat | Hiển thị độ trễ truyền thiết bị mạng |
| [Gregg 19] | skbdrop | Truy vết các lần rớt sk_buff với kernel stack traces |
| [Gregg 19] | skblife | Tuổi thọ của sk_buff dưới dạng độ trễ inter-stack |
| [Gregg 19] | ieee80211scan | Truy vết quyét Wi-Fi IEEE 802.11 |

Các công cụ và nguồn quan sát mạng Linux khác bao gồm:
- **strace(1):** Truy vết các syscall liên quan đến socket và kiểm tra các tùy chọn được sử dụng (lưu ý rằng strace(1) có chi phí cao)
- **lsof(8):** Liệt kê các tập tin được mở theo ID tiến trình, bao gồm cả các chi tiết socket
- **nfsstat(8):** Các thống kê máy chủ và máy khách NFS
- **ifpps(8):** Các thống kê mạng hàng đầu và trên toàn hệ thống
- **iftop(8):** Tóm tắt thông lượng giao diện mạng theo máy chủ (sniffer)
- **perf(1):** Đếm và ghi lại các tracepoints và các chức năng kernel
- **/proc/net:** Chứa nhiều tập tin thống kê mạng
- **BPF iterator:** Cho phép các chương trình BPF xuất các thống kê tùy chỉnh trong /sys/fs/bpf

Cũng có nhiều giải pháp giám sát mạng, dựa trên SNMP hoặc chạy các tác vụ agent tùy chỉnh của riêng họ.

---

## 10.7 Thực nghiệm (Experimentation)
Hiệu năng mạng thường được kiểm tra bằng các công cụ thực hiện một thực nghiệm hơn là chỉ quan sát trạng thái của hệ thống. Các công cụ thực nghiệm bao gồm ping(8), traceroute(8), và các micro-benchmarks mạng chẳng hạn như iperf(8). Những thứ này có thể được sử dụng để xác định liệu thông lượng mạng đầu-cuối có phải là một vấn đề hay không khi gỡ lỗi các vấn đề hiệu năng ứng dụng.

### 10.7.1 ping
Lệnh ping(8) kiểm tra kết nối mạng bằng cách gửi các gói tin yêu cầu ICMP echo. Ví dụ:
```bash
# ping www.netflix.com
PING www.netflix.com(2620:108:700f::3423:46a1 (2620:108:700f::3423:46a1)) 56 data
bytes
64 bytes from 2620:108:700f::3423:46a1 (2620:108:700f::3423:46a1): icmp_seq=1 ttl=43
time=32.3 ms
64 bytes from 2620:108:700f::3423:46a1 (2620:108:700f::3423:46a1): icmp_seq=2 ttl=43
time=34.3 ms
64 bytes from 2620:108:700f::3423:46a1 (2620:108:700f::3423:46a1): icmp_seq=3 ttl=43
time=34.0 ms
^C
--- www.netflix.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 32.341/33.579/34.389/0.889 ms
```
Kết quả bao gồm thời gian vòng lặp (time) cho mỗi gói tin và một bản tóm tắt hiển thị các thống kê khác nhau.

Các phiên bản cũ hơn của ping(8) đo lường thời gian vòng lặp từ không gian người dùng, làm thổi phồng nhẹ các thời gian do thực thi kernel và độ trễ trình lập lịch. Các kernel và phiên bản ping(8) mới hơn sử dụng kernel timestamp support (SIOCGSTAMP hoặc SO_TIMESTAMP) để cải thiện độ chính xác của các thời gian ping được báo cáo.

Các gói tin ICMP được sử dụng có thể được xử lý bởi các router ở mức ưu tiên thấp hơn so với các giao thức ứng dụng, và độ trễ có thể cho thấy biến động cao hơn bình thường [Gregg 19b].

### 10.7.2 traceroute
Lệnh traceroute(8) gửi một loạt các gói tin kiểm tra để xác định theo thực nghiệm tuyến đường hiện tại tới một máy chủ. Điều này được thực hiện bằng cách tăng giá trị IP protocol time to live (TTL) mỗi lần một đơn vị cho mỗi gói tin, khiến cho chuỗi các gateways tới đích tự để lộ chúng bằng cách gửi các thông điệp phản hồi vượt quá thời gian ICMP (miễn là tường lửa không chặn chúng).

Ví dụ, kiểm tra tuyến đường hiện tại từ một máy chủ California tới trang web của tôi:
```bash
# traceroute www.brendangregg.com
traceroute to www.brendangregg.com (184.168.188.1), 30 hops max, 60 byte packets
 1  _gateway (10.0.0.1)  3.453 ms  3.379 ms  4.769 ms
 2  196.120.89.153 (196.120.89.153)  19.239 ms  19.217 ms  13.507 ms
 3  be-10006-rur01.sanjose.ca.sfba.comcast.net (162.151.1.145)  19.141 ms  19.102 ms
19.050 ms
 4  be-231-rar01.santaclara.ca.sfba.comcast.net (162.151.78.249)  19.018 ms  18.987
ms  18.941 ms
 5  be-299-ar01.santaclara.ca.sfba.comcast.net (68.86.143.93)  21.184 ms  18.849 ms
21.053 ms
 6  lag-14.ear3.SanJose1.Level3.net (4.68.72.105)  18.717 ms  11.950 ms  16.471 ms
 7  4.69.216.162 (4.69.216.162)  24.905 ms 4.69.216.158 (4.69.216.158)  21.705 ms
28.043 ms
 8  4.53.228.238 (4.53.228.238)  35.802 ms  37.202 ms  37.137 ms
 9  ae0.ibrsa0107-01.lax1.bb.godaddy.com (148.72.34.5)  24.640 ms  24.610 ms  24.579
ms
10  148.72.32.16 (148.72.32.16)  33.747 ms  35.537 ms  33.598 ms
11  be38.trmc0215-01.ars.mgmt.phx3.gdg (184.168.0.69)  33.646 ms  33.590 ms  35.220
ms
12  * * *
13  * * *
[...]
```
Mỗi bước nhảy (hop) hiển thị một chuỗi gồm ba RTTs, thứ có thể được sử dụng như một nguồn thô của các thống kê độ trễ mạng. Như với ping(8), các gói tin được sử dụng là ưu tiên thấp và có thể cho thấy độ trễ cao hơn so với các giao thức ứng dụng khác. Một số bài kiểm tra hiển thị "*": một thông điệp hết thời gian ICMP đã không được trả về. Cả ba bài kiểm tra hiển thị "*" có thể là do một hop không trả về ICMP hoàn toàn, hoặc ICMP bị chặn bởi một tường lửa. Một cách khắc phục có thể là chuyển sang TCP thay vì ICMP, sử dụng tùy chọn -T (cũng được cung cấp như là lệnh tcptraceroute(1); một phiên bản tiên tiến hơn là mtr(8), thứ có thể tùy chỉnh các cờ).

Đường dẫn được thực hiện cũng có thể được nghiên cứu như một phần của việc tinh chỉnh hiệu năng tĩnh. Các mạng được thiết kế để năng động và phản hồi lại các sự cố, và hiệu năng có thể bị suy giảm khi đường dẫn thay đổi. Lưu ý rằng đường dẫn có thể thay đổi trong quá trình chạy traceroute(8): hop 7 trong kết quả trước đó đầu tiên trả về từ 4.69.216.162, và sau đó là 4.69.216.158. Nếu địa chỉ thay đổi, nó được in; nếu không thì chỉ RTT được in cho các bài kiểm tra tiếp theo.

Để biết các chi tiết nâng cao về việc diễn giải traceroute(8), xem [Steenbergen 09].

### 10.7.3 pathchar
pathchar tương tự như traceroute(8) nhưng bao gồm băng thông giữa các bước nhảy. Điều này được xác định bằng cách gửi một loạt các gói tin mạng ở các kích thước khác nhau nhiều lần và thực hiện phân tích thống kê. Dưới đây là kết quả ví dụ:
```bash
# pathchar 192.168.1.10
pathchar to 192.168.1.1 (192.168.1.1)
doing 32 probes at each of 64 to 1500 by 32
0 localhost
|    30 Mb/s,    79 us (562 us)
1 neptune.test.com (192.168.2.1)
|    44 Mb/s,   195 us (1.23 ms)
2 mars.test.com (192.168.1.1)
2 hops, rtt 547 us (1.23 ms), bottleneck  30 Mb/s, pipe 7555 bytes
```
Thật không may, pathchar bằng cách nào đó đã bị bỏ lỡ khi trở nên phổ biến (có lẽ vì mã nguồn không được phát hành, theo như tôi biết), và rất khó để chạy phiên bản gốc (nhị phân Linux mới nhất trên trang web pathchar là cho Linux 2.0.30 phát hành năm 1997 [Jacobson 97]). Một phiên bản mới bởi Bruce A. Mah, mang tên pchar(8), sẵn có rộng rãi hơn. pathchar cũng tiêu tốn rất nhiều thời gian để chạy, mất hàng chục phút tùy thuộc vào số lượng các bước nhảy, mặc dù các phương pháp đã được đề xuất để giảm thời gian này [Downey 99].

### 10.7.4 iperf
iperf(1) là một công cụ mã nguồn mở để kiểm tra thông lượng tối đa của TCP và UDP. Nó hỗ trợ nhiều tùy chọn, bao gồm chế độ song song nơi nhiều luồng máy khách được sử dụng, thứ có thể cần thiết để đẩy một mạng tới giới hạn của nó. iperf(1) phải được thực thi trên cả máy chủ và máy khách.

Ví dụ, thực thi iperf(1) trên máy chủ:
`$ iperf -s -l 128k`
```bash
------------------------------------------------------------
Server listening on TCP port 5001
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
```
Điều này làm tăng kích thước bộ đệm socket lên 128 Kbytes (-l 128k), từ mặc định là 8 Kbytes.

Tiếp theo được thực thi trên máy khách:
`# iperf -c 10.2.203.2 -l 128k -P 2 -i 1 -t 60`
```bash
------------------------------------------------------------
Client connecting to 10.2.203.2, TCP port 5001
TCP window size: 48.0 KByte (default)
------------------------------------------------------------
[  4] local 10.2.124.2 port 41407 connected with 10.2.203.2 port 5001
[  3] local 10.2.124.2 port 35830 connected with 10.2.203.2 port 5001
[ ID] Interval       Transfer     Bandwidth
[  4]  0.0- 1.0 sec  6.00 MBytes  50.3 Mbits/sec
[  3]  0.0- 1.0 sec  22.5 MBytes   189 Mbits/sec
[SUM]  0.0- 1.0 sec  28.5 MBytes   239 Mbits/sec
[  4]  1.0- 2.0 sec  16.1 MBytes   135 Mbits/sec
[  3]  1.0- 2.0 sec  12.6 MBytes   106 Mbits/sec
[SUM]  1.0- 2.0 sec  28.8 MBytes   241 Mbits/sec
[...]
[  4]  0.0-60.0 sec   748 MBytes   105 Mbits/sec
[  3]  0.0-60.0 sec   996 MBytes   139 Mbits/sec
[SUM]  0.0-60.0 sec  1.70 GBytes   244 Mbits/sec
```
Việc này sử dụng các tùy chọn sau:
- **-c host:** Kết nối tới host name hoặc địa chỉ IP
- **-l 128k:** Sử dụng bộ đệm socket 128 Kbyte
- **-P 2:** Chạy trong chế độ song song với hai luồng máy khách
- **-i 1:** In các bản tóm tắt theo từng giây
- **-t 60:** Tổng thời lượng bài kiểm tra: 60 giây

Dòng cuối cùng hiển thị thông lượng trung bình trong quá trình kiểm tra, tổng hợp trên tất cả các luồng song song: 244 Mbits/s.

Các bản tóm tắt cho mỗi khoảng thời gian có thể được kiểm tra để thấy sự biến động theo thời gian. Tùy chọn --reportstyle c có thể được sử dụng để xuất ra CSV, sao cho nó có thể được nhập bởi các công cụ khác, chẳng hạn như phần mềm vẽ đồ thị.

### 10.7.5 netperf
netperf(1) là một công cụ micro-benchmark tiên tiến có thể kiểm tra hiệu năng yêu cầu/phản hồi [HP 18]. Tôi sử dụng netperf(1) để đo độ trễ vòng lặp TCP; dưới đây là một số kết quả ví dụ:
```bash
server$ netserver -D -p 7001
Starting netserver with host 'IN(6)ADDR_ANY' port '7001' and family AF_UNSPEC
[...]

client$ netperf -v 100 -H 100.66.63.99 -t TCP_RR -p 7001
MIGRATED TCP REQUEST/RESPONSE TEST from 0.0.0.0 (0.0.0.0) port 0 AF_INET to
100.66.63.99 () port 0 AF_INET : demo : first burst 0
Alignment      Offset         RoundTrip  Trans    Throughput
Local  Remote  Local  Remote  Latency    Rate     10^6bits/s
Send   Recv    Send   Recv    usec/Tran  per sec  Outbound   Inbound
    8      0      0      0    98699.102    10.132 0.000      0.000
```
Kết quả này cho thấy một độ trễ vòng lặp TCP là 98.7 ms.

### 10.7.6 tc
Tiện ích quản lý lưu lượng, tc(8), cho phép nhiều kỷ luật xếp hàng (qdiscs) được lựa chọn để cải thiện hoặc quản lý hiệu năng. Đối với thực nghiệm, có các qdiscs có thể điều tiết hoặc làm nhiễu loạn hiệu năng, thứ có thể hữu ích cho việc kiểm tra và mô phỏng. Qdisc mô phỏng mạng (netem) trình diễn điều này.

Để bắt đầu, lệnh sau đây liệt kê cấu hình qdisc hiện tại cho giao diện eth0:
```bash
# tc qdisc show dev eth0
qdisc noqueue 0: root refcnt 2
```
Bây giờ qdisc netem sẽ được thêm vào. Mỗi qdisc hỗ trợ các tham số tinh chỉnh khác nhau. Đối với ví dụ này, tôi sẽ sử dụng các tham số mất gói tin cho netem, và thiết lập mất gói tin thành 1%:
```bash
# tc qdisc add dev eth0 root netem loss 1%
# tc qdisc show dev eth0
qdisc netem 8001: root refcnt 2 limit 1000 loss 1%
```
I/O mạng tiếp theo trên eth0 bây giờ sẽ chịu mức mất gói tin 1%. Tùy chọn -s cho tc(8) hiển thị các thống kê:
```bash
# tc -s qdisc show dev eth0
qdisc netem 8001: root refcnt 2 limit 1000 loss 1%
  Sent 75926119 bytes 89538 pkt (dropped 917, overlimits 0 requeues 0)
  backlog 0b 0p requeues 0
```
Kết quả này hiển thị số lượng gói tin bị đánh rơi.

Để loại bỏ qdisc:
```bash
# tc qdisc del dev eth0 root
# tc qdisc show dev eth0
qdisc noqueue 0: root refcnt 2
```
Xem trang man cho mỗi qdisc để biết danh sách đầy đủ các tùy chọn (cho netem, trang man là tc-netem(8)).

### 10.7.7 Các công cụ Khác (Other Tools)
Các công cụ thực nghiệm khác đáng được đề cập:
- **pktgen:** Một trình tạo gói tin được tích hợp trong Linux kernel [Linux 20m].
- **Flent:** FLExible Network Tester khởi chạy nhiều micro-benchmarks và vẽ đồ thị các kết quả [Høiland-Jørgensen 20].
- **mtr(8):** Một công cụ giống như traceroute bao gồm các thống kê ping.
- **tcpreplay(1):** Một công cụ phát lại lưu lượng mạng đã được bắt trước đó (từ tcpdump(8)), bao gồm việc mô phỏng định thời gói tin. Trong khi hữu ích cho việc gỡ lỗi hiệu năng nói chung, việc truyền tải, ở đó có thể bị giới hạn bởi một chuỗi gói tin hoặc mẫu bit nhất định, và công cụ này có thể có khả năng tái hiện chúng.

---

## 10.8 Tinh chỉnh (Tuning)
Các tham số tinh chỉnh mạng thường đã được tinh chỉnh sẵn để cung cấp hiệu năng cao. Network stack cũng thường được thiết kế để phản hồi linh động với các khối lượng công việc khác nhau, mang lại hiệu năng tối ưu.

Trước khi thử các tham số tinh chỉnh, có thể đáng giá để trước tiên hiểu mức sử dụng mạng. Điều này có thể nhận diện các công việc không cần thiết có thể được loại bỏ, dẫn đến thắng lợi hiệu năng lớn hơn nhiều. Hãy thử các phương pháp luận đặc tính hóa khối lượng công việc và tinh chỉnh hiệu năng tĩnh bằng cách sử dụng các công cụ trong phần trước.

Các tham số tinh chỉnh có sẵn khác nhau giữa các phiên bản hệ điều hành. Hãy xem tài liệu hướng dẫn của chúng. Các phần tiếp theo cung cấp một ý tưởng về những gì có thể khả dụng và cách chúng được tinh chỉnh; chúng nên được coi là một điểm khởi đầu để sửa đổi dựa trên khối lượng công việc và môi trường của bạn.

### 10.8.1 Toàn hệ thống (System-Wide)
Trên Linux, các tham số tinh chỉnh trên toàn hệ thống có thể được xem và thiết lập bằng lệnh sysctl(8) và được ghi vào /etc/sysctl.conf. Chúng cũng có thể được đọc và ghi từ hệ thống tập tin /proc, dưới /proc/sys/net.

Ví dụ, để xem những gì hiện có cho TCP, các tham số có thể được tìm kiếm cho văn bản "tcp" từ sysctl(8):
```bash
# sysctl -a | grep tcp
net.ipv4.tcp_abort_on_overflow = 0
net.ipv4.tcp_adv_win_scale = 1
net.ipv4.tcp_allowed_congestion_control = reno cubic
net.ipv4.tcp_app_win = 31
net.ipv4.tcp_autocorking = 1
net.ipv4.tcp_available_congestion_control = reno cubic
net.ipv4.tcp_available_ulp =
net.ipv4.tcp_base_mss = 1024
net.ipv4.tcp_challenge_ack_limit = 1000
net.ipv4.tcp_comp_sack_delay_ns = 1000000
net.ipv4.tcp_comp_sack_nr = 44
net.ipv4.tcp_congestion_control = cubic
net.ipv4.tcp_dsack = 1
[...]
```
Trên kernel này (5.3) có 70 tham số chứa "tcp" và nhiều hơn nữa dưới "net" bao gồm các tham số cho IP, Ethernet, định tuyến, và các giao diện mạng.

Một số thiết lập này có thể được tinh chỉnh trên cơ sở mỗi socket. Ví dụ, net.ipv4.tcp_congestion_control là thiết lập điều khiển tắc nghẽn mặc định trên toàn hệ thống, thứ có thể được thiết lập bởi từng socket bằng cách sử dụng tùy chọn socket TCP_CONGESTION (xem Mục 10.8.2, Tùy chọn Socket).

**Ví dụ Sản xuất (Production Example)**
Dưới đây là cách Netflix tinh chỉnh các thực thể đám mây của họ [Gregg 19c]; nó được áp dụng trong một script khởi động trong quá trình boot:
```bash
net.core.default_qdisc = fq
net.core.netdev_max_backlog = 5000
net.core.rmem_max = 16777216
net.core.somaxconn = 1024
net.core.wmem_max = 16777216
net.ipv4.ip_local_port_range = 10240 65535
net.ipv4.tcp_abort_on_overflow = 1
net.ipv4.tcp_congestion_control = bbr
net.ipv4.tcp_max_syn_backlog = 8192
net.ipv4.tcp_rmem = 4096 12582912 16777216
net.ipv4.tcp_slow_start_after_idle = 0
net.ipv4.tcp_syn_retries = 2
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_wmem = 4096 12582912 16777216
```
Bộ quy tắc này chỉ thiết lập 14 tunables trong số hàng trăm cái khả thi, và được cung cấp như một ví dụ tại một thời điểm nhất định, không phải là một công thức. Netflix đang xem xét cập nhật hai trong số những nội dung này trong năm 2020 (thiết lập net.core.netdev_max_backlog thành 1000, và net.core.somaxconn thành 4096) đang chờ các bài kiểm tra không hồi quy (non-regression testing).

Các phần sau đây thảo luận về các tunables riêng lẻ.

**Socket và TCP Buffers**
Kích thước bộ đệm socket tối đa cho tất cả các loại giao thức, cho cả đọc (rmem_max) và ghi (wmem_max), có thể được thiết lập bằng cách sử dụng:
```bash
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
```
Giá trị là tính theo byte. Điều này có thể cần được thiết lập thành 16 Mbytes hoặc cao hơn để hỗ trợ các kết nối 10 GbE tốc độ đầy đủ.

Bật tính năng tự động tinh chỉnh của bộ đệm nhận TCP:
`net.ipv4.tcp_moderate_rcvbuf = 1`

Thiết lập các tham số tự động tinh chỉnh cho các bộ đệm đọc và ghi TCP:
```bash
net.ipv4.tcp_rmem = 4096 87380 16777216
net.ipv4.tcp_wmem = 4096 65536 16777216
```
Mỗi cái có ba giá trị: tối thiểu, mặc định, và số byte tối đa để sử dụng. Kích thước được sử dụng là tự động tinh chỉnh từ mặc định. Để cải thiện thông lượng TCP, hãy tăng giá trị tối đa. Việc tăng tối thiểu và mặc định sẽ tiêu tốn nhiều bộ nhớ hơn cho mỗi kết nối, thứ có thể không cần thiết.

**TCP Backlog**
Hàng đợi backlog đầu tiên, cho các kết nối nửa mở (half-open):
`net.ipv4.tcp_max_syn_backlog = 4096`

Hàng đợi backlog thứ hai, hàng đợi listen backlog, cho việc chuyển các kết nối tới accept(2):
`net.core.somaxconn = 1024`

Cả hai giá trị này đều có thể cần được tăng lên so với mặc định của chúng, ví dụ, lên 4,096 và 1,024, hoặc cao hơn, để xử lý tốt hơn các đợt bùng phát tải.

**Device Backlog (Hàng đợi thiết bị)**
Tăng chiều dài của hàng đợi backlog thiết bị mạng, cho mỗi CPU:
`net.core.netdev_max_backlog = 10000`
Giá trị này có thể cần được tăng lên, chẳng hạn như tới 10,000, cho các NIC 10 GbE.

**TCP Congestion Control (Điều khiển tắc nghẽn TCP)**
Linux hỗ trợ các thuật toán điều khiển tắc nghẽn có thể cắm vào (pluggable). Liệt kê những thuật toán hiện có:
```bash
# sysctl net.ipv4.tcp_available_congestion_control
net.ipv4.tcp_available_congestion_control = reno cubic
```
Một số cái có thể khả dụng nhưng hiện chưa được nạp. Ví dụ, thêm htcp:
```bash
# modprobe tcp_htcp
# sysctl net.ipv4.tcp_available_congestion_control
net.ipv4.tcp_available_congestion_control = reno cubic htcp
```
Thuật toán hiện tại có thể được lựa chọn bằng cách sử dụng:
`net.ipv4.tcp_congestion_control = cubic`

**TCP Options (Tùy chọn TCP)**
Các tham số TCP khác có thể được thiết lập bao gồm:
```bash
net.ipv4.tcp_sack = 1
net.ipv4.tcp_fack = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 0
```
Phần mở rộng SACK và FACK có thể cải thiện hiệu năng thông qua các mạng có độ trễ cao, mặc dù có một số chi phí tải CPU.

Tunable tcp_tw_reuse cho phép một phiên TIME_WAIT được tái sử dụng khi nó xuất hiện an toàn để làm như vậy. Điều này có thể cho phép tốc độ kết nối cao hơn giữa hai host, chẳng hạn như giữa một máy chủ web và một máy chủ cơ sở dữ liệu, mà không chạm tới giới hạn cổng tạm thời 16-bit trong TIME_WAIT.

tcp_tw_recycle là một cách khác để tái sử dụng các phiên TIME_WAIT, mặc dù không an toàn bằng tcp_tw_reuse.

**ECN**
Explicit Congestion Notification có thể được kiểm soát bằng:
`net.ipv4.tcp_ecn = 1`
Các giá trị là 0 để vô hiệu hóa ECN, 1 để cho phép cho các kết nối inbound và yêu cầu ECN trên các kết nối outbound, và 2 để cho phép cho các kết nối inbound và không yêu cầu ECN trên các kết nối outbound. Mặc định là 2.

Cũng có net.ipv4.tcp_ecn_fallback, được thiết lập thành 1 (true) theo mặc định, thứ sẽ vô hiệu hóa ECN cho một kết nối nếu kernel phát hiện rằng nó hoạt động không đúng.

**Byte Queue Limits (Giới hạn Hàng đợi Byte)**
Điều này có thể được tinh chỉnh qua /sys. Hiển thị nội dung của các file điều khiển cho các giới hạn này (đường dẫn, đã bị lược bớt trong kết quả này, sẽ khác nhau cho hệ thống và giao diện của bạn):
```bash
# grep . /sys/devices/pci.../net/ens5/queues/tx-0/byte_queue_limits/limit*
/sys/devices/pci.../net/ens5/queues/tx-0/byte_queue_limits/limit:16654
/sys/devices/pci.../net/ens5/queues/tx-0/byte_queue_limits/limit_max:1879048192
/sys/devices/pci.../net/ens5/queues/tx-0/byte_queue_limits/limit_min:0
```
Giới hạn cho giao diện này là 16,654 byte, được thiết lập bởi tự động tinh chỉnh. Để kiểm soát giá trị này, hãy thiết lập limit_min và limit_max để kẹp phạm vi được chấp nhận.

**Kiểm soát Tài nguyên (Resource Controls)**
Hệ thống con network priority (net_pri) của container groups (cgroups) có thể được sử dụng để áp dụng một độ ưu tiên cho lưu lượng mạng của tiến trình, cho các tiến trình hoặc các nhóm tiến trình. Điều này có thể được sử dụng để ưu tiên lưu lượng mạng ưu tiên cao, chẳng hạn như lưu lượng sản xuất, hơn lưu lượng ưu tiên thấp, chẳng hạn như các bản sao lưu hoặc giám sát. Những thứ này có thể được sử dụng để tinh chỉnh I/O mạng từ các ứng dụng được cấu hình sai. Các máy chủ cũng có thể được giới hạn thông lượng mạng cho các tiến trình thuộc về một cgroup với một class ID: những ID này sau đó có thể được sử dụng bởi một kỷ luật xếp hàng để áp dụng các giới hạn băng thông gói tin, và cũng bởi các chương trình BPF. Các chương trình BPF cũng có thể sử dụng các thông tin khác chẳng hạn như cgroup v2 ID cho việc nhận thức container, và có thể cải thiện khả năng mở rộng bằng cách di chuyển việc phân loại, đo lường, và đánh dấu lại (remarking) tới tc egress hook, giải tỏa áp lực trên root qdisc lock [Fomichev 20].

Để biết thêm thông tin về các kiểm soát tài nguyên, xem tiêu đề Network I/O trong Chương 11, Điện toán đám mây, Mục 11.3.3, Kiểm soát tài nguyên.

**Queueing Disciplines (Kỷ luật xếp hàng)**
Đã được mô tả trong Mục 10.4.3, Phần mềm, và hình ảnh hóa trong Hình 10.8, các kỷ luật xếp hàng (qdiscs) là các thuật toán để lập lịch, thao tác, lọc, và định hình các gói tin mạng. Mục 10.7.6, tc, đã chỉ ra việc sử dụng qdisc netem để tạo ra rớt gói tin. Cũng có nhiều qdiscs khác nhau có thể cải thiện hiệu năng cho các khối lượng công việc khác nhau. Bạn có thể liệt kê các qdiscs sử dụng hệ thống của mình:
`# man -k tc-`

Mỗi qdisc có trang man riêng của nó. Qdiscs có thể được sử dụng để thiết lập các chính sách tốc độ gói tin hoặc băng thông, thiết lập các cờ IP ECN, và nhiều hơn nữa.

qdisc mặc định có thể được xem và thiết lập bằng cách sử dụng:
```bash
# sysctl net.core.default_qdisc
net.core.default_qdisc = fq_codel
```
Nhiều bản phân phối Linux đã chuyển sang fq_codel làm mặc định vì nó cung cấp hiệu năng tốt trong hầu hết các trường hợp.

**Dự án Tuned (The Tuned Project)**
Với rất nhiều tunables có sẵn, việc tinh chỉnh chúng một cách thủ công có thể rất tốn công sức. Dự án Tuned cung cấp khả năng tự động tinh chỉnh cho một số tunables này dựa trên các cấu hình có thể lựa chọn, và hỗ trợ các bản phân phối Linux bao gồm RHEL, Fedora, Ubuntu, và CentOS [Tuned Project 20]. Sau khi cài đặt tuned, các cấu hình khả dụng có thể được liệt kê bằng cách sử dụng:
```bash
# tuned-adm list
Available profiles:
[...]
- balanced                    - General non-specialized tuned profile
[...]
- network-latency             - Optimize for deterministic performance at the cost of
increased power consumption, focused on low latency network performance
- network-throughput          - Optimize for streaming network throughput, generally
only necessary on older CPUs or 40G+ networks
[...]
```
Kết quả này đã bị lược bớt: danh sách đầy đủ hiển thị 28 cấu hình. Để kích hoạt cấu hình network-latency:
`# tuned-adm profile network-latency`

Để xem những tunables nào cấu hình này thiết lập, tập tin cấu hình của nó có thể được đọc từ tuned source [Škarvada 20]:
```bash
$ more tuned/profiles/network-latency/tuned.conf
[...]
[main]
summary=Optimize for deterministic performance at the cost of increased power
consumption, focused on low latency network performance
include=latency-performance

[vm]
transparent_hugepages=never

[sysctl]
net.core.busy_read=50
net.core.busy_poll=50
net.ipv4.tcp_fastopen=3
kernel.numa_balancing=0

[bootloader]
cmdline_network_latency=skew_tick=1
```
Lưu ý rằng cái này có một chỉ thị include bao gồm cả các tunables trong cấu hình latency-performance.

### 10.8.2 Tùy chọn Socket
Các socket có thể được tinh chỉnh riêng lẻ bởi các ứng dụng thông qua syscall setsockopt(2). Điều này có thể khả thi nếu bạn đang phát triển hoặc biên dịch lại phần mềm, và có thể thực hiện các sửa đổi đối với mã nguồn.

setsockopt(2) cho phép các tầng khác nhau được tinh chỉnh (ví dụ: socket, TCP). Bảng 10.8 trình bày một số khả năng tinh chỉnh trên Linux.

Bảng 10.8 Các tùy chọn socket ví dụ
| Tên Tùy chọn | Mô tả |
| --- | --- |
| SO_SNDBUF, SO_RCVBUF | Thiết lập kích thước bộ đệm gửi và nhận (những thứ này có thể được tinh chỉnh lên tới các giới hạn hệ thống được mô tả trước đó; cũng có các tùy chọn SO_SNDBUFFORCE để ghi đè giới hạn gửi). |
| SO_REUSEPORT | Cho phép nhiều tiến trình hoặc luồng liên kết tới cùng một cổng, cho phép kernel phân phối tải qua chúng để đạt khả năng mở rộng (kể từ Linux 3.9). |
| SO_MAX_PACING_RATE | Thiết lập tốc độ pacing tối đa, tính theo byte mỗi giây (xem tc-fq(8)). |
| SO_LINGER | Có thể được sử dụng để giảm độ trễ TIME_WAIT. |
| SO_TXTIME | Yêu cầu truyền gói tin dựa trên thời gian, nơi các thời hạn cuối (deadlines) có thể được cung cấp (kể từ Linux 4.19) [Corbet 18c] (được sử dụng cho pacing UDP [Bruijn 18]). |
| TCP_NODELAY | Vô hiệu hóa Nagle, gửi các phân đoạn ngay khi có thể. Điều này có thể cải thiện độ trễ với chi phí sử dụng mạng cao hơn (nhiều gói tin hơn). |
| TCP_CORK | Tạm dừng truyền tải cho đến khi các gói tin đầy có thể được gửi đi, cải thiện thông lượng. (Đây cũng là một thiết lập trên toàn hệ thống cho kernel để tự động thử corking: net.ipv4.tcp_autocorking.) |
| TCP_QUICKACK | Gửi các ACKs ngay lập tức (có thể tăng băng thông gửi). |
| TCP_CONGESTION | Thuật toán điều khiển tắc nghẽn cho socket. |

Đối với các tùy chọn socket có sẵn, hãy xem các trang man cho socket(7), tcp(7), udp(7), v.v.

Cũng có một số cờ syscall I/O socket có thể ảnh hưởng đến hiệu năng. Ví dụ, Linux 4.14 đã thêm cờ `MSG_ZEROCOPY` cho các syscall send(2): nó cho phép bộ đệm không gian người dùng được sử dụng trong quá trình truyền tải, tránh chi phí sao chép nó vào không gian kernel [Linux 20c][Corbet 18b].

### 10.8.3 Cấu hình
Các cấu hình sau đây cũng có sẵn cho việc tinh chỉnh hiệu năng mạng:
- **Ethernet jumbo frames:** Tăng MTU mặc định từ 1,500 lên ~9,000 có thể cải thiện thông lượng mạng, nếu các router mạng hỗ trợ jumbo frames.
- **Link aggregation:** Nhiều giao diện mạng có thể được nhóm lại sao cho chúng đóng vai trò như một giao diện duy nhất với băng thông kết hợp. Điều này yêu cầu sự hỗ trợ và cấu hình của switch để hoạt động chính xác.
- **Firewall configuration:** Ví dụ, iptables hoặc các chương trình BPF trên egress hook có thể được sử dụng để thiết lập mức IP ToS (DSCP) trong các IP headers dựa trên một quy tắc tường lửa. Điều này có thể được sử dụng để ưu tiên lưu lượng dựa trên cổng, cũng như các trường hợp sử dụng khác.

---

## 10.9 Các bài tập (Exercises)
1. Trả lời các câu hỏi sau về thuật ngữ mạng:
   - Sự khác biệt giữa băng thông và thông lượng là gì?
   - Độ trễ kết nối TCP là gì?
   - Độ trễ byte đầu tiên là gì?
   - Thời gian vòng lặp (round-trip time) là gì?

2. Trả lời các câu hỏi khái niệm sau:
   - Mô tả mức sử dụng và độ bão hòa giao diện mạng.
   - TCP listen backlog là gì, và nó được sử dụng như thế nào?
   - Mô tả các điểm mạnh và điểm yếu của interrupt coalescing.

3. Trả lời các câu hỏi sâu hơn sau:
   - Đối với một kết nối TCP, giải thích cách thức một lỗi khung hình (hoặc gói tin) mạng có thể gây hại cho hiệu năng.
   - Mô tả những gì xảy ra khi một giao diện mạng bị quá tải với công việc, bao gồm cả ảnh hưởng đến hiệu năng ứng dụng.

4. Phát triển các quy trình sau cho hệ điều hành của bạn:
   - Một checklist phương pháp USE cho các tài nguyên mạng (các giao diện và các bộ điều khiển). Bao gồm cách lấy mỗi chỉ số (ví dụ, lệnh nào để thực thi) và cách diễn giải kết quả. Thử sử dụng các công cụ quan sát hệ điều hành hiện có trước khi cài đặt các sản phẩm phần mềm bổ sung.

5. Một checklist đặc tính hóa khối lượng công việc cho các tài nguyên mạng. Bao gồm cách thực hiện các tác vụ này (có thể yêu cầu sử dụng instrumentation động):
   - Đo lường độ trễ byte đầu tiên cho các kết nối TCP outbound (active).
   - Đo lường độ trễ kết nối TCP. Script nên xử lý các lệnh gọi connect(2) không chặn (non-blocking).

6. (tùy chọn, nâng cao) Đo lường độ trễ inter-stack TCP/IP cho RX và TX. Cho RX, việc này đo lường thời gian từ ngắt mạng tới socket read; cho TX, thời gian từ socket write tới truyền tải thiết bị. Kiểm tra dưới mức tải. Cân nhắc thông tin bổ sung nào cần được bao gồm để giải thích nguồn gốc của bất kỳ giá trị ngoại lai độ trễ nào?

---

## 10.10 Các tài liệu tham khảo (References)
- [Postel 80] Postel, J., “RFC 768: User Datagram Protocol,” *Information Sciences Institute*, https://tools.ietf.org/html/rfc768, 1980.
- [Postel 81] Postel, J., “RFC 793: Transmission Control Protocol,” *Information Sciences Institute*, https://tools.ietf.org/html/rfc793, 1981.
- [Nagle 84] Nagle, J., “RFC 896: Congestion Control in IP/TCP Internetworks,” https://tools.ietf.org/html/rfc896, 1984.
- [Saltzer 84] Saltzer, J., Reed, D., and Clark, D., “End-to-End Arguments in System Design,” *ACM TOCS*, November 1984.
- [Braden 89] Braden, R., “RFC 1122: Requirements for Internet Hosts—Communication Layers,” https://tools.ietf.org/html/rfc1122, 1989.
- [Jacobson 92] Jacobson, V., et al., “TCP Extensions for High Performance,” *Network Working Group*, https://tools.ietf.org/html/rfc1323, 1992.
- [Stevens 93] Stevens, W. R., *TCP/IP Illustrated, Volume 1*, Addison-Wesley, 1993.
- [Mathis 96] Mathis, M., and Mahdavi, J., “Forward Acknowledgement: Refining TCP Congestion Control,” *ACM SIGCOMM*, 1996.
- [Jacobson 97] Jacobson, V., “pathchar-a1-linux-2.0.30.tar.gz,” ftp://ftp.ee.lbl.gov/pathchar, 1997.
- [Nichols 98] Nichols, K., Blake, S., Baker, F., and Black, D., “Definition of the Differentiated Services Field (DS Field) in the IPv4 and IPv6 Headers,” *Network Working Group*, https://tools.ietf.org/html/rfc2474, 1998.
- [Downey 99] Downey, A., “Using pathchar to Estimate Internet Link Characteristics,” *ACM SIGCOMM*, October 1999.
- [Ramakrishnan 01] Ramakrishnan, K., Floyd, S., and Black, D., “The Addition of Explicit Congestion Notification (ECN) to IP,” *Network Working Group*, https://tools.ietf.org/html/rfc3168, 2001.
- [Corbet 03] Corbet, J., “Driver porting: Network drivers,” *LWN.net*, https://lwn.net/Articles/30107, 2003.
- [Hassan 03] Hassan, M., and R. Jain., *High Performance TCP/IP Networking*, Prentice Hall, 2003.
- [Deri 04] Deri, L., “Improving Passive Packet Capture: Beyond Device Polling,” *Proceedings of SANE*, 2004.
- [Corbet 06b] Corbet, J., “Reworking NAPI,” *LWN.net*, https://lwn.net/Articles/214457, 2006.
- [Cook 09] Cook, T., “nicstat - the Solaris and Linux Network Monitoring Tool You Did Not Know You Needed,” https://blogs.oracle.com/timc/entry/nicstat_the_solaris_and_linux, 2009.
- [Steenbergen 09] Steenbergen, R., “A Practical Guide to (Correctly) Troubleshooting with Traceroute,” https://archive.nanog.org/meetings/nanog47/presentations/Sunday/RAS_Traceroute_N47_Sun.pdf, 2009.
- [Paxson 11] Paxson, V., Allman, M., Chu, J., and Sargent, M., “RFC 6298: Computing TCP’s Retransmission Timer,” *Internet Engineering Task Force (IETF)*, https://tools.ietf.org/html/rfc6298, 2011.
- [Corbet 12] “TCP friends,” *LWN.net*, https://lwn.net/Articles/511254, 2012.
- [Fritchie 12] Fritchie, S. L., “quoted,” https://web.archive.org/web/20120119110658/http://www.snookles.com/slf-blog/2012/01/05/tcp-incast-what-is-it, 2012.
- [Hrubý 12] Hrubý, T., “Byte Queue Limits,” *Linux Plumber’s Conference*, https://blog.linuxplumbersconf.org/2012/wp-content/uploads/2012/08/bql_slide.pdf, 2012.
- [Nichols 12] Nichols, K., and Jacobson, V., “Controlling Queue Delay,” *Communications of the ACM*, July 2012.
- [Roskind 12] Roskind, J., “QUIC: Quick UDP Internet Connections,” https://docs.google.com/document/d/1RNHkx_VvKWyWg6L8SZ-saqsQx7rfV-ev2jrFUoVD34/edit#, 2012.
- [Dukkipati 13] Dukkipati, N., Cardwell, N., Cheng, Y., and Mathis, M., “Tail Loss Probe (TLP): An Algorithm for Fast Recovery of Tail Losses,” *TCP Maintenance Working Group*, https://tools.ietf.org/html/draft-dukkipati-tcpm-tcp-loss-probe-01, 2013.
- [Siemon 13] Siemon, D., “Queueing in the Linux Network Stack,” https://www.coverfire.com/articles/queueing-in-the-linux-network-stack, 2013.
- [Cheng 16] Cheng, Y., and Cardwell, N., “Making Linux TCP Fast,” *netdev 1.2*, https://netdevconf.org/1.2/papers/bbr-netdev-1.2.new.new.pdf, 2016.
- [Linux 16] “TCP Offload Engine (TOE),” https://wiki.linuxfoundation.org/networking/toe, 2016.
- [Ather 17] Ather, A., “BBR TCP congestion control offers higher network utilization and throughput during network congestion (packet loss, latencies),” https://twitter.com/amernetflix/status/892787364598132736, 2017.
- [Bensley 17] Bensley, S., et al., “TCP DCTCP: TCP Congestion Control for Data Centers,” *Internet Engineering Task Force (IETF)*, https://tools.ietf.org/html/rfc8257, 2017.
- [Dumazet 17a] Dumazet, E., “Busy Polling: Past, Present, Future,” *netdev 2.1*, https://netdevconf.info/2.1/slides/apr6/dumazet-BUSY-POLLING-Netdev-2.1.pdf, 2017.
- [Dumazet 17b] Dumazet, E., “Re: Something hitting my total number of connections to the server,” *netdev mailing list*, https://lore.kernel.org/netdev/1503423863.2499.39.camel@edumazet-glaptop3.roam.corp.google.com, 2017.
- [Gallatin 17] Gallatin, D., “Serving 100 Gbps from an Open Connect Appliance,” *Netflix Technology Blog*, https://netflixtechblog.com/serving-100-gbps-from-an-open-connect-appliance-cdb51dda3b99, 2017.
- [Bruijn 18] Bruijn, W., and Dumazet, E., “Optimizing UDP for Content Delivery: GSO, Pacing and Zerocopy,” *Linux Plumber’s Conference*, http://vger.kernel.org/lpc_net2018_talks/willembruijn-lpc2018-udpgso-paper-DRAFT-1.pdf, 2018.
- [Corbet 18b] Corbet, J., “Zero-copy TCP receive,” *LWN.net*, https://lwn.net/Articles/752188, 2018.
- [Corbet 18c] Corbet, J., “Time-based packet transmission,” *LWN.net*, https://lwn.net/Articles/752188, 2018.
- [Deepak 18] Deepak, A., “eBPF / XDP firewall and packet filtering,” *Linux Plumber’s Conference*, http://vger.kernel.org/lpc_net2018_talks/ebpf-firewall-LPC.pdf, 2018.
- [Høiland-Jørgensen 18] Høiland-Jørgensen, T., et al., “The eXpress Data Path: Fast Programmable Packet Processing in the Operating System Kernel,” *Proceedings of the 14th International Conference on emerging Networking EXperiments and Technologies*, 2018.
- [HP 18] “Netperf,” https://github.com/HewlettPackard/netperf, 2018.
- [Majkowski 18] Majkowski, M., “How to Drop 10 Million Packets per Second,” https://blog.cloudflare.com/how-to-drop-10-million-packets-per-second, 2018.
- [Stewart 18] Stewart, R., “This commit brings in a new refactored TCP stack called Rack,” https://reviews.freebsd.org/rS334804, 2018.
- [Amazon 19] “Announcing Amazon VPC Traffic Mirroring for Amazon EC2 Instances,” https://aws.amazon.com/about-aws/whats-new/2019/06/announcing-amazon-vpc-traffic-mirroring-for-amazon-ec2-instances, 2019.
- [Dumazet 19] Dumazet, E., “Re: [LKP] [net] 19f92a030c: apachebench.requests_per_second -37.9% regression,” *netdev mailing list*, https://lore.kernel.org/lkml/20191113172102.GA23306@1wt.eu, 2019.
- [Gregg 19] Gregg, B., *BPF Performance Tools: Linux System and Application Observability*, Addison-Wesley, 2019.
- [Gregg 19b] Gregg, B., “BPF Theremin, Tetris, and Typewriters,” http://www.brendangregg.com/blog/2019-12-22/bpf-theremin.html, 2019.
- [Gregg 19c] Gregg, B., “LISA2019 Linux Systems Performance,” *USENIX LISA*, http://www.brendangregg.com/blog/2020-03-08/lisa2019-linux-systems-performance.html, 2019.
- [Gregg 19d] Gregg, B., “udplife.bt,” https://github.com/brendangregg/bpf-perf-tools-book/blob/master/exercises/Ch10_Networking/udplife.bt, 2019.
- [Hassas Yeganeh 19] Hassas Yeganeh, S., and Cheng, Y., “TCP SO_TIMESTAMPING with OPT_STATS for Performance Analytics,” *netdev 0x13*, https://netdevconf.info/0x13/session.html?talk-tcp-timestamping, 2019.
- [Bufferbloat 20] “Bufferbloat,” https://www.bufferbloat.net, 2020.
- [Cheng 20] Cheng, Y., Cardwell, N., Dukkipati, N., and Jha, P., “RACK-TLP: A Time-Based Efficient Loss Detection for TCP,” *TCP Maintenance Working Group*, draft-ietf-tcpm-rack-09, 2020.
- [Cilium 20a] “API-aware Networking and Security,” https://cilium.io, accessed 2020.
- [Corbet 20] Corbet, J., “Kernel operations structures in BPF,” *LWN.net*, https://lwn.net/Articles/811631, 2020.
- [DPDK 20] “AF_XDP Poll Mode Driver,” *DPDK documentation*, http://doc.dpdk.org/guides/index.html, accessed 2020.
- [Fomichev 20] Fomichev, S., et al., “Replacing HTB with EDT and BPF,” *netdev 0x14*, https://netdevconf.info/0x14/session.html?talk-replacing-HTB-with-EDT-and-BPF, 2020.
- [Google 20b] “Packet Mirroring Overview,” https://cloud.google.com/vpc/docs/packet-mirroring, accessed 2020.
- [Høiland-Jørgensen 20] Høiland-Jørgensen, T., “The FLExible Network Tester,” https://flent.org, accessed 2020.
- [Linux 20i] “Segmentation Offloads,” *Linux documentation*, https://www.kernel.org/doc/Documentation/networking/segmentation-offloads.rst, accessed 2020.
- [Linux 20c] “MSG_ZEROCOPY,” *Linux documentation*, https://www.kernel.org/doc/html/latest/networking/msg_zerocopy.html, accessed 2020.
- [Linux 20j] “timestamping.txt,” *Linux documentation*, https://www.kernel.org/doc/Documentation/networking/timestamping.txt, accessed 2020.
- [Linux 20k] “AF_XDP,” *Linux documentation*, https://www.kernel.org/doc/html/latest/networking/af_xdp.html, accessed 2020.
- [Linux 20l] “HOWTO for the Linux Packet Generator,” *Linux documentation*, https://www.kernel.org/doc/Documentation/networking/pktgen.html, accessed 2020.
- [Nosachev 20] Nosachev, D., “How 1500 Bytes Became the MTU of the Internet,” https://blog.benjojo.co.uk/post/why-is-ethernet-mtu-1500, 2020.
- [Škarvada 20] Škarvada, J., “network-latency/tuned.conf,” https://github.com/redhat-performance/tuned/blob/master/profiles/network-latency/tuned.conf, last updated 2020.
- [Tuned Project 20] “The Tuned Project,” https://tuned-project.org, accessed 2020.
- [Wireshark 20] “Wireshark,” https://www.wireshark.org, accessed 2020.
