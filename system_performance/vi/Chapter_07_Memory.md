# Chương 7: Bộ nhớ (Memory)

Bộ nhớ chính của hệ thống lưu trữ các chỉ thị của ứng dụng và nhân, dữ liệu làm việc của chúng, và các bộ đệm ẩn hệ thống tập tin. Bộ lưu trữ thứ cấp cho dữ liệu này thường là các thiết bị lưu trữ—các đĩa—thứ hoạt động chậm hơn nhiều bậc. Một khi bộ nhớ chính đã đầy, hệ thống có thể bắt đầu chuyển đổi dữ liệu giữa bộ nhớ chính và các thiết bị lưu trữ. Đây là một quá trình chậm mà thường sẽ trở thành nút thắt cổ chai của hệ thống, làm giảm hiệu năng đáng kể. Hệ thống cũng có thể kết thúc tiến trình tiêu thụ bộ nhớ lớn nhất, gây ra các gián đoạn ứng dụng.

Các yếu tố hiệu năng khác cần xem xét bao gồm chi phí CPU của việc cấp phát và giải phóng bộ nhớ, sao chép bộ nhớ, và quản lý các ánh xạ không gian địa chỉ bộ nhớ. Trên các kiến trúc đa socket, tính cục bộ bộ nhớ có thể trở thành một yếu tố, vì bộ nhớ gắn với các socket cục bộ có độ trễ truy cập thấp hơn so với các socket từ xa.

Các mục tiêu học tập của chương này là:
- Hiểu các khái niệm bộ nhớ.
- Làm quen với các chi tiết bên trong phần cứng bộ nhớ.
- Làm quen với các chi tiết bên trong của trình cấp phát nhân và người dùng.
- Có kiến thức làm việc về MMU và TLB.
- Theo dõi các phương pháp luận khác nhau cho phân tích bộ nhớ.
- Đặc tính hóa việc sử dụng bộ nhớ trên toàn hệ thống và theo từng tiến trình.
- Xác định các vấn đề gây ra bởi bộ nhớ khả dụng thấp.
- Định vị việc sử dụng bộ nhớ trong không gian địa chỉ tiến trình và các slab nhân.
- Khảo sát việc sử dụng bộ nhớ bằng cách sử dụng các công cụ lập hồ sơ, truy vết, và biểu đồ ngọn lửa.
- Nhận biết các tham số có thể tinh chỉnh cho bộ nhớ.

Chương này có năm phần, ba phần đầu cung cấp nền tảng cho phân tích bộ nhớ, và hai phần cuối cho thấy ứng dụng thực tế của nó trên các hệ thống dựa trên Linux. Các phần bao gồm:
- **Background** giới thiệu thuật ngữ liên quan đến bộ nhớ và các khái niệm hiệu năng bộ nhớ quan trọng.
- **Architecture** cung cấp các mô tả tổng quát về kiến trúc bộ nhớ phần cứng và phần mềm.
- **Methodology** giải thích phương pháp luận phân tích hiệu năng.
- **Observability Tools** mô tả các công cụ hiệu năng cho phân tích bộ nhớ.
- **Tuning** giải thích việc tinh chỉnh và các ví dụ về tham số có thể tinh chỉnh.

Các bộ đệm ẩn bộ nhớ trên CPU (Level 1/2/3, TLB) được bao quát trong Chương 6, CPUs.

## 7.1 Thuật ngữ (Terminology)

Để tham khảo, thuật ngữ liên quan đến bộ nhớ được sử dụng trong chương này bao gồm:

- **Bộ nhớ chính (Main memory):** Còn được gọi là bộ nhớ vật lý, mô tả vùng lưu trữ dữ liệu nhanh của máy tính, thường được cung cấp dưới dạng DRAM.
- **Bộ nhớ ảo (Virtual memory):** Một sự trừu tượng hóa bộ nhớ chính mà (gần như) vô hạn và không tranh chấp. Bộ nhớ ảo không phải là bộ nhớ thật.
- **Bộ nhớ thường trú (Resident memory):** Bộ nhớ hiện đang nằm trong bộ nhớ chính.
- **Bộ nhớ vô danh (Anonymous memory):** Bộ nhớ không có vị trí hệ thống tập tin hoặc tên đường dẫn. Nó bao gồm dữ liệu làm việc của không gian địa chỉ tiến trình, được gọi là heap.
- **Không gian địa chỉ (Address space):** Một ngữ cảnh bộ nhớ. Có các không gian địa chỉ ảo cho mỗi tiến trình, và cho nhân.
- **Phân đoạn (Segment):** Một vùng bộ nhớ ảo được đánh dấu cho một mục đích cụ thể, chẳng hạn như để lưu trữ các trang thực thi hoặc có thể ghi.
- **Văn bản chỉ thị (Instruction text):** Đề cập đến các chỉ thị CPU trong bộ nhớ, thường trong một phân đoạn.
- **OOM:** Hết bộ nhớ (Out of memory), khi nhân phát hiện bộ nhớ khả dụng thấp.
- **Trang (Page):** Một đơn vị bộ nhớ, được sử dụng bởi hệ điều hành và CPUs. Về mặt lịch sử nó là 4 hoặc 8 Kbyte. Các bộ xử lý hiện đại hỗ trợ nhiều kích thước trang cho các kích thước lớn hơn.
- **Lỗi trang (Page fault):** Một truy cập bộ nhớ không hợp lệ. Đây là các sự kiện bình thường khi sử dụng bộ nhớ ảo theo nhu cầu.
- **Phân trang (Paging):** Sự chuyển giao các trang giữa bộ nhớ chính và các thiết bị lưu trữ.
- **Hoán đổi (Swapping):** Linux sử dụng thuật ngữ hoán đổi để chỉ việc phân trang vô danh tới thiết bị hoán đổi (sự chuyển giao các trang hoán đổi). Trong Unix và các hệ điều hành khác, hoán đổi là sự chuyển giao toàn bộ tiến trình giữa bộ nhớ chính và các thiết bị hoán đổi. Cuốn sách này sử dụng phiên bản Linux của thuật ngữ.
- **Swap:** Một vùng trên đĩa dành cho dữ liệu vô danh đã được phân trang. Nó có thể là một vùng trên một thiết bị lưu trữ, còn được gọi là thiết bị hoán đổi vật lý, hoặc một tệp hệ thống tập tin, được gọi là tệp hoán đổi. Một số công cụ sử dụng thuật ngữ swap để chỉ bộ nhớ ảo (điều này gây nhầm lẫn và không chính xác).

Các thuật ngữ khác được giới thiệu xuyên suốt chương này. Bảng thuật ngữ bao gồm thuật ngữ cơ bản để tham khảo nếu cần, bao gồm address, buffer, và DRAM. Cũng xem các phần thuật ngữ trong Chương 2 và 3.

## 7.2 Các khái niệm (Concepts)

Sau đây là một số khái niệm quan trọng được lựa chọn liên quan đến bộ nhớ và hiệu năng bộ nhớ.

### 7.2.1 Bộ nhớ ảo (Virtual Memory)
Bộ nhớ ảo là một sự trừu tượng hóa cung cấp cho mỗi tiến trình và nhân không gian địa chỉ riêng, lớn, tuyến tính và riêng tư của riêng nó. Nó đơn giản hóa việc phát triển phần mềm, để việc sắp xếp bộ nhớ vật lý cho hệ điều hành quản lý. Nó cũng hỗ trợ đa nhiệm (các không gian địa chỉ ảo được phân tách theo thiết kế) và đăng ký vượt mức (bộ nhớ đang sử dụng có thể mở rộng vượt quá bộ nhớ chính). Bộ nhớ ảo đã được giới thiệu trong Chương 3, Hệ điều hành, Mục 3.2.8, Bộ nhớ ảo. Về bối cảnh lịch sử, xem [Denning 70].

Hình 7.1 cho thấy vai trò của bộ nhớ ảo cho một tiến trình, trên một hệ thống có thiết bị hoán đổi (bộ lưu trữ thứ cấp). Một trang bộ nhớ được hiển thị, vì hầu hết các triển khai bộ nhớ ảo đều dựa trên trang.

(Hình 7.1 Bộ nhớ ảo tiến trình)

Không gian địa chỉ tiến trình được ánh xạ bởi hệ thống con bộ nhớ ảo tới bộ nhớ chính và thiết bị hoán đổi vật lý. Các trang bộ nhớ có thể được nhân di chuyển giữa chúng khi cần thiết, một quá trình mà Linux gọi là hoán đổi (và các hệ điều hành khác gọi là phân trang vô danh). Điều này cho phép nhân đăng ký vượt mức bộ nhớ chính.

Nhân có thể áp đặt giới hạn cho việc đăng ký vượt mức. Một giới hạn thường được sử dụng là kích thước bộ nhớ chính cộng với các thiết bị hoán đổi vật lý. Nhân có thể từ chối các đợt cấp phát cố gắng vượt quá giới hạn này. Các lỗi "hết bộ nhớ ảo" như vậy có thể gây nhầm lẫn thoạt nhìn, vì bộ nhớ ảo tự nó là một tài nguyên trừu tượng.

Linux cũng cho phép các hành vi khác, bao gồm việc không đặt giới hạn nào cho cấp phát bộ nhớ. Điều này được gọi là cấp phát vượt mức (overcommit) và được mô tả sau các phần tiếp theo về phân trang và phân trang theo nhu cầu, những thứ cần thiết để overcommit hoạt động.

### 7.2.2 Phân trang (Paging)
Phân trang là sự di chuyển các trang vào và ra khỏi bộ nhớ chính, được gọi lần lượt là page-in và page-out. Nó lần đầu tiên được giới thiệu bởi Atlas Computer vào năm 1962 [Corbató 68], cho phép:
- Các chương trình được tải một phần có thể thực thi
- Các chương trình lớn hơn bộ nhớ chính có thể thực thi
- Di chuyển hiệu quả các chương trình giữa bộ nhớ chính và các thiết bị lưu trữ

Các khả năng này vẫn đúng ngày nay. Không giống kỹ thuật trước đó là hoán đổi ra toàn bộ chương trình, phân trang là một cách tiếp cận chi tiết để quản lý và giải phóng bộ nhớ chính, vì đơn vị kích thước trang tương đối nhỏ (ví dụ: 4 Kbyte).

Phân trang với bộ nhớ ảo (bộ nhớ ảo phân trang) đã được giới thiệu vào Unix qua BSD [Babaoglu 79] và trở thành tiêu chuẩn.

Với sự bổ sung sau này của bộ đệm trang (page cache) để chia sẻ các trang hệ thống tập tin (xem Chương 8, Hệ thống tập tin), hai loại phân trang khác nhau trở nên khả dụng: phân trang hệ thống tập tin và phân trang vô danh.

**Phân trang Hệ thống Tập tin (File System Paging)**
Phân trang hệ thống tập tin được gây ra bởi việc đọc và ghi các trang trong các tệp được ánh xạ bộ nhớ. Đây là hành vi bình thường cho các ứng dụng sử dụng ánh xạ bộ nhớ tệp (mmap(2)) và trên các hệ thống tập tin sử dụng bộ đệm trang (hầu hết đều làm; xem Chương 8, Hệ thống tập tin). Nó đã được gọi là phân trang "tốt" [McDougall 06a].

Khi cần thiết, nhân có thể giải phóng bộ nhớ bằng cách phân trang ra một phần. Đây là nơi thuật ngữ trở nên hơi phức tạp: nếu một trang hệ thống tập tin đã được sửa đổi trong bộ nhớ chính (gọi là dirty), việc page-out sẽ yêu cầu nó được ghi ra đĩa. Nếu thay vào đó, trang hệ thống tập tin chưa được sửa đổi (gọi là clean), việc page-out chỉ đơn giản giải phóng bộ nhớ để tái sử dụng ngay lập tức, vì một bản sao đã tồn tại trên đĩa.

**Phân trang Vô danh (Anonymous Paging / Swapping)**
Phân trang vô danh liên quan đến dữ liệu riêng tư của các tiến trình: heap và ngăn xếp của tiến trình. Nó được gọi là vô danh vì nó không có vị trí được đặt tên trong hệ điều hành (nghĩa là, không có tên đường dẫn hệ thống tập tin). Các page-out vô danh yêu cầu di chuyển dữ liệu tới các thiết bị hoán đổi vật lý hoặc các tệp hoán đổi. Linux sử dụng thuật ngữ hoán đổi (swapping) để chỉ loại phân trang này.

Phân trang vô danh làm giảm hiệu năng và do đó đã được gọi là phân trang "xấu" [McDougall 06a]. Khi các ứng dụng truy cập các trang bộ nhớ đã được phân trang ra ngoài, chúng bị chặn trên I/O đĩa cần thiết để đọc chúng trở lại bộ nhớ chính. Đây là một page-in vô danh, giới thiệu độ trễ đồng bộ cho ứng dụng. Các page-out vô danh có thể không ảnh hưởng trực tiếp đến hiệu năng ứng dụng, vì chúng có thể được thực hiện bất đồng bộ bởi nhân.

Hiệu năng là tốt nhất khi không có phân trang vô danh (hoán đổi). Điều này có thể đạt được bằng cách cấu hình các ứng dụng để nằm trong bộ nhớ chính khả dụng và bằng cách giám sát quét trang, mức sử dụng bộ nhớ, và phân trang vô danh, để đảm bảo không có dấu hiệu thiếu hụt bộ nhớ.

### 7.2.3 Phân trang theo Nhu cầu (Demand Paging)
Các hệ điều hành hỗ trợ phân trang theo nhu cầu (hầu hết đều hỗ trợ) ánh xạ các trang bộ nhớ ảo tới bộ nhớ vật lý theo nhu cầu, như minh họa trong Hình 7.2. Điều này trì hoãn chi phí CPU của việc tạo các ánh xạ cho đến khi chúng thực sự cần thiết và được truy cập, thay vì tại thời điểm một vùng bộ nhớ được cấp phát lần đầu.

(Hình 7.2 Ví dụ về lỗi trang)

Trình tự trong Hình 7.2 bắt đầu với một malloc() (bước 1) cung cấp bộ nhớ đã được cấp phát, và sau đó một chỉ thị store (bước 2) tới bộ nhớ mới được cấp phát đó. Để MMU xác định vị trí bộ nhớ chính của store, nó thực hiện tra cứu ảo sang vật lý (bước 3), thứ thất bại vì chưa có ánh xạ. Sự thất bại này được gọi là lỗi trang (bước 4), kích hoạt nhân tạo một ánh xạ theo nhu cầu (bước 5). Sau đó, trang bộ nhớ có thể được phân trang ra các thiết bị hoán đổi để giải phóng bộ nhớ (bước 6).

Nếu ánh xạ có thể được thỏa mãn từ một trang khác trong bộ nhớ, nó được gọi là **lỗi nhỏ (minor fault)**. Điều này có thể xảy ra khi ánh xạ một trang mới từ bộ nhớ khả dụng, trong quá trình tăng trưởng bộ nhớ của tiến trình. Các lỗi trang yêu cầu truy cập thiết bị lưu trữ được gọi là **lỗi lớn (major fault)**.

Kết quả mà mô hình bộ nhớ ảo và cấp phát theo nhu cầu mang lại là bất kỳ trang bộ nhớ ảo nào cũng có thể ở một trong các trạng thái sau:
- A. Chưa được cấp phát
- B. Đã cấp phát, nhưng chưa được ánh xạ (chưa được điền và chưa bị lỗi)
- C. Đã cấp phát, và ánh xạ tới bộ nhớ chính (RAM)
- D. Đã cấp phát, và ánh xạ tới thiết bị hoán đổi vật lý (đĩa)

Từ các trạng thái này, hai thuật ngữ sử dụng bộ nhớ cũng có thể được định nghĩa:
- **Kích thước tập thường trú (RSS - Resident set size):** Kích thước các trang bộ nhớ chính đã được cấp phát (C)
- **Kích thước bộ nhớ ảo (Virtual memory size):** Kích thước của tất cả các vùng đã được cấp phát (B + C + D)

### 7.2.4 Cấp phát Vượt mức (Overcommit)
Linux hỗ trợ khái niệm cấp phát vượt mức, cho phép cấp phát nhiều bộ nhớ hơn hệ thống có thể lưu trữ—nhiều hơn bộ nhớ vật lý và các thiết bị hoán đổi cộng lại. Nó dựa vào phân trang theo nhu cầu và xu hướng của các ứng dụng không sử dụng nhiều bộ nhớ mà chúng đã cấp phát.

Với overcommit, các yêu cầu bộ nhớ ứng dụng (ví dụ: malloc(3)) sẽ thành công khi chúng lẽ ra đã thất bại. Trên Linux, hành vi của overcommit có thể được cấu hình với một tham số có thể tinh chỉnh. Xem Mục 7.6, Tinh chỉnh, để biết chi tiết.

### 7.2.5 Hoán đổi Tiến trình (Process Swapping)
Hoán đổi tiến trình là sự di chuyển toàn bộ tiến trình giữa bộ nhớ chính và thiết bị hoán đổi vật lý hoặc tệp hoán đổi. Đây là kỹ thuật Unix gốc để quản lý bộ nhớ chính và là nguồn gốc của thuật ngữ swap [Thompson 78].

Hoán đổi tiến trình gây hại nghiêm trọng cho hiệu năng, vì một tiến trình đã được hoán đổi ra yêu cầu nhiều I/O đĩa để chạy lại. Mô tả này được cung cấp cho bối cảnh lịch sử. Các hệ thống Linux hoàn toàn không hoán đổi tiến trình và chỉ dựa vào phân trang.

### 7.2.6 Sử dụng Bộ đệm ẩn Hệ thống Tập tin (File System Cache Usage)
Việc sử dụng bộ nhớ tăng lên sau khi khởi động hệ thống là bình thường khi hệ điều hành sử dụng bộ nhớ khả dụng để đệm ẩn hệ thống tập tin, cải thiện hiệu năng. Nguyên tắc là: Nếu có bộ nhớ chính dư, hãy sử dụng nó cho điều gì đó hữu ích. Điều này có thể khiến những người dùng thiếu kinh nghiệm lo lắng khi thấy bộ nhớ tự do khả dụng co lại gần về không sau khi khởi động. Nhưng nó không gây ra vấn đề cho các ứng dụng, vì nhân có thể nhanh chóng giải phóng bộ nhớ từ bộ đệm ẩn hệ thống tập tin khi ứng dụng cần.

### 7.2.7 Mức sử dụng và Độ bão hòa (Utilization and Saturation)
Mức sử dụng bộ nhớ chính có thể được tính bằng bộ nhớ đã sử dụng so với tổng bộ nhớ. Bộ nhớ được sử dụng bởi bộ đệm ẩn hệ thống tập tin có thể được coi là chưa sử dụng, vì nó khả dụng để tái sử dụng bởi các ứng dụng.

Nếu nhu cầu bộ nhớ vượt quá lượng bộ nhớ chính, bộ nhớ chính trở nên bão hòa. Hệ điều hành sau đó có thể giải phóng bộ nhớ bằng cách sử dụng phân trang, hoán đổi tiến trình (nếu được hỗ trợ), và trên Linux, trình giết OOM. Bất kỳ hoạt động nào trong số này là một chỉ báo của sự bão hòa bộ nhớ chính.

### 7.2.8 Các Trình cấp phát (Allocators)
Trong khi bộ nhớ ảo xử lý đa nhiệm của bộ nhớ vật lý, việc cấp phát và sắp xếp thực tế trong một không gian địa chỉ ảo thường được xử lý bởi các trình cấp phát. Đây là các thư viện cấp người dùng hoặc các thủ tục dựa trên nhân, cung cấp cho lập trình viên phần mềm một giao diện dễ dàng cho việc sử dụng bộ nhớ (ví dụ: malloc(3), free(3)).

Các trình cấp phát có thể có ảnh hưởng đáng kể đến hiệu năng. Chúng có thể cải thiện hiệu năng bằng cách sử dụng các kỹ thuật bao gồm đệm ẩn đối tượng theo từng luồng, nhưng chúng cũng có thể làm giảm hiệu năng nếu cấp phát trở nên phân mảnh và lãng phí.

### 7.2.9 Bộ nhớ Chia sẻ (Shared Memory)
Bộ nhớ có thể được chia sẻ giữa các tiến trình. Điều này thường được sử dụng cho các thư viện hệ thống để tiết kiệm bộ nhớ bằng cách chia sẻ một bản sao văn bản chỉ thị chỉ đọc của chúng với tất cả các tiến trình sử dụng nó.

Điều này gây ra khó khăn cho các công cụ quan sát hiển thị mức sử dụng bộ nhớ chính theo từng tiến trình. Bộ nhớ chia sẻ có nên được bao gồm khi báo cáo tổng kích thước bộ nhớ của một tiến trình không? Một kỹ thuật được sử dụng bởi Linux là cung cấp một thước đo bổ sung, kích thước tập tỉ lệ (PSS - proportional set size), bao gồm bộ nhớ riêng (không chia sẻ) cộng với bộ nhớ chia sẻ chia cho số người dùng.

### 7.2.10 Kích thước Tập Làm việc (Working Set Size)
Kích thước tập làm việc (WSS) là lượng bộ nhớ chính mà một tiến trình thường xuyên sử dụng để thực hiện công việc. Nó là một khái niệm hữu ích cho việc tinh chỉnh hiệu năng bộ nhớ: hiệu năng sẽ được cải thiện rất nhiều nếu WSS có thể nằm gọn trong các bộ đệm ẩn CPU, thay vì bộ nhớ chính. Ngoài ra, hiệu năng sẽ giảm rất nhiều nếu WSS vượt quá kích thước bộ nhớ chính, và ứng dụng phải hoán đổi để thực hiện công việc.

Mặc dù hữu ích như một khái niệm, nó khó đo lường trong thực tế: không có thống kê WSS trong các công cụ quan sát (chúng thường báo cáo RSS, không phải WSS).

### 7.2.11 Kích thước Từ (Word Size)
Như đã giới thiệu trong Chương 6, CPUs, các bộ xử lý có thể hỗ trợ nhiều kích thước từ, chẳng hạn như 32-bit và 64-bit, cho phép phần mềm cho một trong hai chạy. Vì kích thước không gian địa chỉ bị giới hạn bởi phạm vi có thể đánh địa chỉ từ kích thước từ, các ứng dụng yêu cầu hơn 4 Gbytes bộ nhớ quá lớn cho một không gian địa chỉ 32-bit và cần được biên dịch cho 64 bit trở lên.
## 7.3 Kiến trúc (Architecture)

Kiến trúc bộ nhớ thay đổi tùy theo bộ xử lý và kiến trúc hệ thống, bao gồm bộ nhớ chung (UMA) so với kiến trúc đa nút (NUMA), cũng như hệ điều hành với cách nó triển khai bộ nhớ ảo, phân trang và truy cập bộ nhớ. Cả phần cứng và phần mềm đều được bao quát trong phần này.

### 7.3.1 Phần cứng (Hardware)
Nhiều máy tính bao quát một CPU socket duy nhất—có thể là một thiết bị di động, một bo mạch nhúng, một máy tính xách tay với CPU được hàn chết, một máy chủ phiến nhỏ, hoặc một phiên bản đám mây. Đã có một cuộc đua hướng tới số lượng lõi (core) ngày càng tăng trên mỗi socket thay vì mở rộng quy mô hệ thống đa bộ xử lý với nhiều socket. Số lượng lõi có thể dễ dàng vượt quá băng thông do bộ nhớ chính cung cấp, trừ khi bộ xử lý triển khai một thiết kế liên kết hệ thống tốc độ cao sang DRAM để mở rộng quy mô với số lượng lõi. Ngoài ra còn có các bộ đệm ẩn CPU kích thước lớn—hoạt động nhanh hơn nhiều so với DRAM—bù đắp phần nào nhu cầu tăng băng thông DRAM, vì chúng có thể thỏa mãn một phần lớn các truy cập bộ nhớ. Các bộ đệm ẩn CPU được thảo luận thêm trong Chương 6, CPUs.

**Kiến trúc UMA (UMA Architecture)**
Trước khi UMA và NUMA được nói tới, phần này bắt đầu bằng việc giải thích kiến trúc UMA là gì: truy cập bộ nhớ đồng nhất (uniform memory access) hoặc "không-NUMA". Trong UMA, tất cả bộ nhớ được truy cập có độ trễ bằng nhau, như trong sơ đồ đơn giản hóa ở Hình 7.3.

(Hình 7.3 Kiến trúc truy cập bộ nhớ đồng nhất/UMA)

Bộ nhớ thường bao gồm một tập các mô-đun bộ nhớ nội tuyến kép (DIMM) chia sẻ cùng một bus bộ nhớ giao tiếp với CPU. Trong UMA, bus (hoặc các bus bộ nhớ song song) phải mở rộng để đáp ứng nhu cầu gia tăng của nhiều CPU (và nhiều lõi hơn), một cách tiếp cận cuối cùng sẽ chạm đến giới hạn điện và khả năng định tuyến trên bo mạch chủ.

Hệ thống có thể có thiết bị truy cập bộ nhớ trực tiếp (DMA - direct memory access) cho phép các thành phần khác, như thiết bị lưu trữ, ghi trực tiếp vào bộ nhớ. Hình dạng này có thể không nhất quán từ góc độ các thiết bị khác, chẳng hạn như một thẻ giao diện mạng được gắn trực tiếp vào một bus CPU nhưng không thuộc bus CPU bên cạnh.

Hệ thống của bạn có thể sử dụng UMA, nếu phần cứng chỉ có duy nhất một bộ xử lý được gắn vào một tập hợp RAM cục bộ chung.

**Kiến trúc NUMA (NUMA Architecture)**
Kiến trúc truy cập bộ nhớ không đồng nhất (non-uniform memory access) bao gồm nhiều cụm CPU riêng biệt, thường là các socket xử lý đa lõi với các mô-đun bộ nhớ riêng được gắn cục bộ trên mỗi node, được kết nối với nhau thông qua một liên kết liên thông (interconnect). Các bus định tuyến được thiết kế qua nhiều cụm như vậy. Thiết kế NUMA làm giảm độ phức tạp cho các thiết kế đa xử lý cũng như tối đa hóa sử dụng băng thông cho bộ đệm ẩn cục bộ. Về mặt lý thuyết, nó cũng cung cấp cho phần mềm khả năng mở rộng bộ nhớ khi nhiều mô-đun bộ nhớ có sẵn, tuy vậy trong một hệ thống quá khổ nó có thể tăng thêm một chút độ trễ tùy thuộc vào vị trí mô-đun (xem bài báo cũ nhưng vẫn liên quan của Andi Kleen [Kleen 05]). Hình 7.4 minh họa NUMA hai nút đơn giản.

(Hình 7.4 Kiến trúc truy cập bộ nhớ không đồng nhất)

Thời gian truy cập cho I/O bộ nhớ phụ thuộc vào vị trí dữ liệu so với bộ xử lý thực hiện I/O ("không đồng nhất"): chi phí bộ nhớ cục bộ sẽ thấp hơn truy cập bộ nhớ từ xa thông qua liên kết (ví dụ: Intel QPI dọc các NUMA node), thứ phải chuyển qua các bộ xử lý từ xa.

Tùy thuộc vào ứng dụng xử lý của bạn, hệ điều hành có thể liên kết (bind/pin) các quy trình ứng dụng với RAM gắn cục bộ (nhất quán về NUMA) nếu chúng ít phải chia sẻ bộ nhớ hoặc chuyển các tác vụ giữa các CPU. Đối với các ứng dụng xử lý lượng dữ liệu khổng lồ (bộ đệm quá khổ đối với nút gắn cục bộ của chúng), chúng có thể gặp hiệu năng thấp hơn. Hệ điều hành cung cấp các chính sách để hỗ trợ tối ưu NUMA và cung cấp tài nguyên, và có sẵn các công cụ (ví dụ numastat(8), numactl(8)) để xác định hiệu quả, tinh chỉnh (Hình 7.5). Hệ điều hành với cấu hình kiến trúc đa socket đôi khi thiếu quản lý NUMA hợp lý do đó cản trở lợi ích phần cứng thiết kế.

(Hình 7.5 Hiệu năng NUMA)

Bất kỳ độ trễ bổ sung nào sinh ra khi truy cập bộ nhớ cho ứng dụng vượt qua khả năng cục bộ sẽ khiến bộ nhớ cache bị lỗi và truy cập tới RAM qua CPU thứ 2 (hoặc cao hơn).

**MMU**
Đơn vị quản lý bộ nhớ (MMU - memory management unit) chịu trách nhiệm dịch địa chỉ ảo sang địa chỉ vật lý (có thể được tìm thấy trong nhân). Các vi xử lý trước đây với cấu trúc nhỏ từng cho các dịch vụ truy cập thẳng thay vì đi qua MMU. Hầu hết kiến trúc hiện đại cung cấp ánh xạ đa lớp để dịch trong MMU, thường hỗ trợ các thanh ghi TLB để chuyển đổi hiệu quả hơn, với việc chuyển đổi có thể chậm nếu bộ đệm bộ nhớ bị miss (đòi hỏi dò tìm trong MMU, gọi là page walk).

**TLB**
Translation lookaside buffer (TLB) trong hầu hết các vi xử lý là bộ nhớ cache chuyên dụng trên trong CPU (thực ra phần lớn có nhiều bộ nhớ TLB riêng) sử dụng thông tin ánh xạ tương đối được sử dụng gần đây giữa các trang bộ nhớ vật lý và kích thước trang. Khi mã máy cố gắng truy cập địa chỉ ảo bộ nhớ, TLB có thể cung cấp truy xuất ngay phần bù, làm cho sự chuyển đổi siêu nhanh. Khi thiếu TLB (miss), một nỗ lực bộ nhớ chính đắt tiền (truy cập bảng trang bộ nhớ chính/MMU) có thể cản trở vòng lặp hoặc làm giảm IPC. Điều này đòi hỏi phần cứng tăng nhiều trang bộ nhớ bổ sung hơn. Để tăng cường khả năng của TLB, phần cứng và mô-đun quản lý hệ thống có xu hướng hỗ trợ thay đổi cấp phát từ các khối kích thước thông thường (4 Kbyte trên x86) lên kích thước siêu lớn (như 2 Mbyte hoặc 1 Gbyte). Hệ điều hành đóng một vai trò lớn. Linux cấu hình "Transparent Huge Pages - THP" để tăng số lượng và tỷ lệ hit cho TLB tự động.

### 7.3.2 Phần mềm (Software)
Phần này mô tả kiến trúc bộ nhớ phần mềm của hệ điều hành, từ cấp phát nhân đến cấp phát không gian người dùng. Trình bày tổng thể các thành phần về bộ nhớ trên Linux ở mục 7.6.

(Hình 7.6 Kiến trúc bộ nhớ ảo trên Linux)

Hình 7.6 biểu thị phân cấp Linux đối với giao thức bộ quản lý bộ nhớ (VM). Giao thức của hệ điều hành bao gồm những hệ thống để điều phối các nhu cầu cấp thoát bộ nhớ. Kernel sẽ chuyển trực tiếp lên phần cứng với thông tin để thao tác cấu trúc bộ nhớ cache / RAM một cách thông minh (những API đó là Linux memory allocators). Ở cấp ứng dụng người dùng sẽ cấp thẻ thông qua glibc khi muốn sử dụng MMU cho dịch địa chỉ phần cứng/tạo page caches.

**Quản lý bộ nhớ với cấu trúc phần mềm VM**
Memory managers hoặc hệ điều hành xây dựng MMU nhằm giúp cho: cấp phát tiến trình bộ nhớ vật lý/kéo hoán đổi nếu thiếu (swap/paging); giám sát TLB, theo dõi các lần hit; dọn/thu hoạch dữ liệu RAM sạch/dơ. Overcommit (cấp phát vượt mức), nếu được cho, sẽ làm ngơ giới hạn cứng của toàn bộ dung lượng trống. Tiến trình cấp thẻ bộ nhớ với dung lượng chưa chạm tới có thể bị trì hoãn bởi theo nhu cầu (demand paging), tuy nhiên, khi đạt giới hạn giới nghiêm bộ nhớ của Linux VM (hoặc hệ điều hành), quá trình có thể phải ngừng với 'Bị OOM Giết - Out of Memory killer'. Ở dạng thức OOM này quá tải (hết dung lượng thực/ảo/không có page cache đủ lớn), Linux hy sinh bằng cách tắt một quy trình có cấp điểm cao (ví dụ: kích cỡ lớn, hoặc mức oom_score). Bỏ đi hoán đổi hệ thống (không kích hoạt page/file system), Linux sử dụng OOM nếu tiến trình dùng hết bộ nhớ.

Trong các đám mây Netflix, các nhóm dùng thông thường không nên kích hoạt tính năng chạy swap và thường sẽ chọn thiết bị OOM killed nếu có một ứng dụng có trục trặc bộ nhớ.

Khi tiến hành sử dụng cho memory cgroups (giới hạn bộ nhớ/ảo của các tác vụ được chỉ định ảo), nó có một bộ thu hoạch riêng và có thể đối mặt với OOM ở mức thấp mà không can thiệp bộ nhớ VM lớn (sẽ rõ trong Chương 11 Mô hình Điện toán Đám mây).

**Các danh sách trống (Free List(s))**
Khi BSD giới thiệu việc dùng phân trang (page mapping) nó cũng sử dụng trình phân trang daemon (page out). Các khung danh sách trang tự do có trong hệ Linux thường có chức năng: cập nhật liên tục bộ khung những địa chỉ cho tiến trình dễ dãi định hướng việc tìm kiếm một khối RAM có sẵn. Lịch sử của nó khá đồ sộ, có kiểu sắp xếp "người bạn đồng hành - buddy allocator", theo phân bổ trang Linux. Số lượng đơn vị kết hợp tương đương lũy thừa hệ cơ số hai. Để tối ưu với NUMA, quá trình giữ phân loại theo cấp memory node:
- **Nodes:** Vùng ngân hàng dành cho kích cỡ bộ nhớ gắn bó NUMA node.
- **Zones:** Mục đích sử dụng loại DMA hoặc bình thường hoặc Highmem.
- **Migration types:** Unmovable (không dời), Reclaimable (có thể thu hoạch), vv.

Slab cho hạt nhân/tiến trình hoạt động song song.

**Reaping (Thu hoạch)**
Nhân hoặc các luồng có thao tác giải phóng không gian theo slab. Reaping thường là hành động thu hoạch giải phóng bộ đệm (bộ nhớ chưa xài cho vùng RAM hạt nhân sau một vòng luân chuyển ngắn). Linux đăng ký qua `register_shrinker()`.

**Quét trang (Page Scanning)**
Quét và dịch chuyển các trang, với mục đích có thêm Free Lists, được xử lý bởi Page Out daemon. Nó không chạy thường xuyên nếu hệ thống tĩnh, tuy nhiên với daemon phân trang Linux (kswapd, viết tắt của kernel swap daemon), kswapd theo dõi ngưỡng cao/thấp cho giới hạn phục hồi memory/dọn bộ đệm tập tin, cũng như chuyển đổi các danh sách LRU active và inactive:
- Nếu dưới mức kswapd watermarks (High/Low/Min), việc dọn/thu hoạch theo mức thấp, sẽ đẩy nhanh việc giải phóng trang ở Inactive cache list để tăng bộ trống (kSwapd wake-ups and modes: Hình 7.8, 7.9). Kswapd duyệt (với các trang 'sạch') qua danh sách, hoặc viết trả / trích xuất ra vị trí hoán đổi ẩn. Trong Linux, các tham số có thay thế được đề cập với vm.watermark_*.

### 7.3.3 Không gian Địa chỉ Ảo Tiến trình (Process Virtual Address Space)
Phạm vi của quá trình chuyển bộ nhớ không gian phụ thuộc phần cứng (cách thức MMU định hướng) nhưng về cấp người dùng, quy luật chia thành "Phân đoạn ảo - Virtual pages": Text, Data, Heap và Stack và liên kết Thư viện động:
- **Executable text:** Lưu lệnh cấp người dùng với thuộc tính chỉ đọc và có quyền run.
- **Executable data:** Dữ liệu có thể được truy xuất và bị ghi đè, và nó gắn cơ chế ghi riêng nên quá trình không thay được bản trên bộ nhớ cứng.
- **Heap:** Phân cực dành cho biến thể theo cơ chế RAM vô danh khi có sự gia tăng/ứng dụng cung cấp qua vùng được xin quyền và gọi API tạo malloc().
- **Stack:** Chứa cấu trúc cấp phát đa dạng.

Cấu trúc Linux ở x86 bộ nhớ nhân bị đảo (0xffff...).

**Sự phát triển của Heap (Heap Growth)**
Mọi người dùng hay lầm tưởng tiến trình thường xuyên tăng dung lượng RSS với Memory leak. Khi trình gọi free(), những nhà cung cấp giải phóng đôi khi có thói quen "thu hồi cho những thẻ kế tiếp", và ứng dụng "nhìn như không bao giờ kết thúc mảng tiêu thụ RSS". Việc không thay đổi hệ thống có hai tính tái yêu cầu hoặc tạo MAP. Nhưng với thư viện như glibc hỗ trợ với trình thu hoạch malloc_trim() thứ làm nhỏ heap (sbrk).

**Trình cấp phát (Allocators)**
Như đề cập từ trước mục đích trình quản lý cấp phát (Hình 7.11):
- **Slab/SLUB:** Phục vụ hạt nhân, theo quy mô size, không cần liên tục xin trang ảo cấp cứng. SLUB thay thế độ phức tạp (bỏ đối tượng danh sách cho nhân). Solarist / J. Bonwick đã hoàn thiện cấu trúc trước.
- **glibc:** Người sử dụng, thay đổi dlmalloc/Doug Lea, với cấp thẻ bộ nhớ "buddy-like" nếu dư hay dùng qua các cây (trees)/ mmap.
- **TCMalloc:** Của Google, tránh bị lock threads khi có ứng dụng đa luồng (multi-task allocation), có gc chu kỳ cho bộ xử lý thu dọn tự động.
- **jemalloc:** Khởi nguồn từ FreeBSD và dùng tại Facebook, tránh sự phân mảnh memory fragmentation và điều chỉnh mở rộng hiệu suất, mmap.
## 7.4 Phương pháp luận (Methodology)

Phần này mô tả các phương pháp luận và bài tập khác nhau cho việc phân tích và tinh chỉnh bộ nhớ. Các chủ đề được tóm tắt trong Bảng 7.3.

**Bảng 7.3 Phương pháp hiệu năng bộ nhớ**
| Mục | Phương pháp luận | Các loại |
| --- | --- | --- |
| 7.4.1 | Phương pháp công cụ (Tools method) | Phân tích quan sát |
| 7.4.2 | Phương pháp USE (USE method) | Phân tích quan sát |
| 7.4.3 | Đặc tả việc sử dụng (Characterizing usage) | Phân tích quan sát, Hoạch định công suất |
| 7.4.4 | Phân tích chu kỳ (Cycle analysis) | Phân tích quan sát |
| 7.4.5 | Giám sát hiệu năng (Performance monitoring) | Phân tích quan sát, Hoạch định công suất |
| 7.4.6 | Phát hiện rò rỉ (Leak detection) | Phân tích quan sát |
| 7.4.7 | Tinh chỉnh hiệu năng tĩnh (Static performance tuning) | Phân tích quan sát, Hoạch định công suất |
| 7.4.8 | Kiểm soát tài nguyên (Resource controls) | Tinh chỉnh |
| 7.4.9 | Đo kiểm chuẩn vi mô (Micro-benchmarking) | Phân tích thực nghiệm |
| 7.4.10 | Thu hẹp bộ nhớ (Memory shrinking) | Phân tích thực nghiệm |

Xem Chương 2, Phương pháp luận, để biết thêm các chiến lược và lời giới thiệu về nhiều phương pháp trong số này.

Các phương pháp này có thể được theo dõi riêng lẻ hoặc được sử dụng kết hợp với nhau. Khi khắc phục sự cố về bộ nhớ, gợi ý của tôi là bắt đầu với các chiến lược sau theo thứ tự này: Giám sát hiệu năng, phương pháp USE, và đặc tả việc sử dụng.

Mục 7.5, Công cụ Quan sát (Observability Tools), hiển thị các công cụ hệ điều hành để áp dụng các phương pháp này.

### 7.4.1 Phương pháp Công cụ (Tools Method)
Phương pháp công cụ là một quá trình lặp lặp đi lặp lại nhiều lần qua các công cụ có sẵn, kiểm tra các số liệu chính mà chúng cung cấp. Đây là một phương pháp luận đơn giản có thể bỏ qua các sự cố mà trong đó các công cụ bạn tình cờ có không cung cấp và khiến tầm nhìn kém đi và tốn thêm thời gian.

Đối với bộ nhớ, quy trình công cụ Linux bao gồm:
- **Quét trang (Page scanning):** Quét những đợt phân trang giật trang liên tục (trên 10 giây). Lượng sức ép cần quan sát trong sar -B.
- **Áp lực thông tin PSI:** (Linux 4.20+) thông tin áp suất memory tại /proc/pressure/memory.
- **Hoán đổi (Swapping):** Phân trang vô danh tại cột si và so của vmstat(8).
- **vmstat:** Chạy và theo dõi vmstat 1 ở cột `free` cho bộ nhớ khả dụng.
- **OOM killer:** Trong `/var/log/messages` / `dmesg`, với thông báo "Out of memory."
- **top:** Tiến trình có `%MEM` và `VIRT` `RES` dùng lượng thẻ nhớ RAM.
- **perf(1)/BCC/bpftrace:** Truy vết các hàm gọi phân bộ nhớ stack tracing. Ghi nhận là nó rất nặng trịch (overhead).

### 7.4.2 Phương pháp USE (USE Method)
Phương pháp USE dùng cho việc xác định điểm thắt cổ chai và kiểm tra lỗi của các thành phần trước.

Kiểm tra toàn hệ thống cho:
- **Mức Sử dụng (Utilization):** Mức được dùng, mức còn khả dụng / Physical vs Virtual.
- **Bão hòa (Saturation):** Từng đợt OOM, đợt Page scan liên tục, Swap out.
- **Lỗi (Errors):** Những báo lỗi cấp phát/phần cứng.

Hãy kiểm tra OOM Kill sacrifice và swapping qua `dmesg`, hoặc thiết lập đĩa với iostat(1). Sử dụng PSI để xem nghẽn do bộ nhớ. Chú ý khái niệm Page cache của VM. Overcommit nếu không dùng hệ thống chối cấp phát. Các thanh RAM lỗi dính phần cứng ECC - error checking có thể tra `dmidecode`, `edac-utils`, `ipmitool sel` cho hệ điều hành phát lỗi uncorrectable dẫn đến Segmentation fault (crashes bất thường). Trong Cloud bạn có cấu hình Resource Controls/giới hạn memory ở Limit.

### 7.4.3 Đặc tả việc sử dụng (Characterizing Usage)
Nắm được cách hệ thống được xài (hoạch định/năng lực/benchmark/mô phỏng). Nếu database cấu hình cache thấp, bộ nhớ xài chưa tốt; cao sẽ vấp hoán đổi.

- Utilization cho Physical và virtual
- Bão hòa (Saturation) ở Swapping / OOM list.
- RAM Page cache/Filesystem đang chiếm
- Virtual / RAM ở cấp tiến trình.
- Quy chuẩn về control quota memory limit.

Ví dụ: "RAM có 256GB - trong đó có 1% ứng dụng chạy (utilized) và 30% bộ ẩn tập tin. DBMS là lớn nhất lấy khoảng 2G." Một số memory leak dính lỗi lập trình/lỗi thiết lập.

**Bảng check danh sách phân tích (Checklist)**
- Kích thước Working Set Size (WSS) của các tiến trình?
- Dành bao nhiêu cho slab của nhân (kernel)?
- Số lượng active/inactive file cache?
- Dành bao nhiêu bộ nhớ trong phân đoạn text/data/heap/stack đối với ứng dụng?
- Vệt vết (Call paths) báo cho allocation memory? (Kernel và người dùng/User).
- Số liệu Swap của quá khứ.
- Có bộ nhớ lỗi / memory leaks ở cấp module/OS tiến trình?
- Trạng thái NUMA local/foreign (Sự phân phối có đều?).
- Thống kê chênh lệch IPC / bộ nhớ rớt Stall cycles. Tính tương qua giao tiếp bộ nhớ IO (Local vs Remote bus).

### 7.4.4 Phân tích chu kỳ (Cycle Analysis)
Xác định mức tải Bus Memory nhờ PMCs CPU. Instructions Per Cycle (IPC).

### 7.4.5 Giám sát Hiệu năng (Performance Monitoring)
Theo dấu vệt lịch sử thông qua:
- **Utilization:** Percent used.
- **Saturation:** Swapping, OOM.
- Tài nguyên giới hạn limits / quota đối với ảo hóa. Memory grow kiểm kê về rò rỉ tăng dài hạn theo quy trình rò rỉ (memory leak rate).

### 7.4.6 Phát hiện rò rỉ (Leak Detection)
Xả lấp RAM (hết tài nguyên bộ phân trang) có thể diễn tiến khi module mọc thêm rễ. OOM sẽ tiến đến. Thường bị gọi là "Rò rỉ - leak". Thật ra do:
- **Rò rỉ (Memory leak):** Quên báo cho bộ dọn hoặc lỗi dọn (Bug memory leak frees). Patching phần mềm hoặc biên dịch sửa mã code.
- **Gia tăng (Memory growth):** Tiêu thụ của mô-đun cấp phát quá đáng sinh ra tăng trưởng. Chỉnh đổi config phần mềm (không phải do leak).

Có nên như vậy không (is it supposed to do that?). Warming cache. Cách track leak bao gồm debug allocator, stack traces. BCC hỗ trợ memleak(8) cấp Linux nhưng có overhead. Coi kỹ ở mục số 15 của BPF BCC.

### 7.4.7 Tinh chỉnh Hiệu năng Tĩnh (Static Performance Tuning)
Bao quát hệ thống tài nguyên tĩnh:
- Tổng kích cỡ bao nhiêu?
- Ứng dụng phân bao nhiêu theo cấu trúc? (Config size)
- Việc xin cấp phát allocators loại nào? (Glibc hay tcmalloc)
- Tốc độ bus (DDR5).
- Bài test qua (memtester).
- Hệ kiến trúc: CPU UMA? NUMA?
- OS hỗ trợ NUMA, nhận liên kết RAM-to-socket, đa kênh nhiều memory buses? Tách hay tập trung? Size cache CPU (L2 L3 TLB). Bios?
- Trang siêu cỡ lớn - Large pages/Huge pages? Hệ Overcommit? Tham số sysctl VM. Giới hạn Resource control?

### 7.4.8 Kiểm soát Tài nguyên (Resource Controls)
Memory control groups - cgroups được xây làm quota/giới hạn phân phát. Phần này mô tả sâu ở Mục 11 Điện toán Đám mây / 7.6 Tuning.

### 7.4.9 Đo kiểm chuẩn vi mô (Micro-Benchmarking)
Sức mạnh / tốc độ qua cache (Cache line) để thử tốc độ thay vì chỉ tốc độ clock CPU. Các chương trình dùng đo kiểm hiệu năng latency ở chương 6.

### 7.4.10 Thu hẹp bộ nhớ (Memory Shrinking)
Đây là cách tiêu cực khi giả định WSS tiến trình, cấu hình tắt bớt bộ vùng cho ứng dụng trên OS rồi canh hiệu năng ngã ngựa tại mốc nào cho OOM/hoạt động bị thắt lại. Tham khảo thêm công cụ wss(8).
## 7.5 Công cụ Quan sát (Observability Tools)

Phần này giới thiệu các công cụ quan sát bộ nhớ cho các hệ điều hành dựa trên Linux. Xem phần trước cho các phương pháp luận để tuân theo khi sử dụng chúng.
Các công cụ trong phần này được thể hiện trong Bảng 7.4.

**Bảng 7.4 Các công cụ quan sát bộ nhớ Linux**
| Mục | Công cụ | Mô tả |
| --- | --- | --- |
| 7.5.1 | vmstat | Thống kê bộ nhớ vật lý và ảo |
| 7.5.2 | PSI | Thông tin ngưng trệ áp lực bộ nhớ (Memory pressure stall information) |
| 7.5.3 | swapon | Sử dụng thiết bị hoán đổi (Swap device) |
| 7.5.4 | sar | Thống kê lịch sử |
| 7.5.5 | slabtop | Thống kê trình cấp phát slab của nhân |
| 7.5.6 | numastat | Thống kê NUMA |
| 7.5.7 | ps | Trạng thái tiến trình |
| 7.5.8 | top | Giám sát sử dụng bộ nhớ theo từng tiến trình |
| 7.5.9 | pmap | Thống kê không gian địa chỉ tiến trình |
| 7.5.10| perf | Phân tích PMC bộ nhớ và điểm truy vết (tracepoint) |
| 7.5.11| drsnoop | Truy vết thu hồi trực tiếp (Direct reclaim) |
| 7.5.12| wss | Ước tính kích thước tập làm việc (Working set size) |
| 7.5.13| bpftrace | Chương trình truy vết cho phân tích bộ nhớ |

Đây là một danh sách chọn lọc các công cụ thao tác theo nguyên tắc kiểm thử Mục 7.4 (Methodology). Chúng ta bắt đầu với giám sát cấp cao (`vmstat`, `sar`), `slabtop`, theo các cấp tiến trình (`ps`, `top`), `pmap`, và cấp trace với `drsnoop` từ thư viện `BCC`.

### 7.5.1 vmstat
Lệnh lấy số liệu bộ nhớ ảo `vmstat` cung cấp tầm nhìn cao tần, cùng với CPU/paging, đã giới thiệu trước đó từ BSD 1979 bởi Bill Joy, Ozalp Babaoglu với ghi chú: "BUGS: Print ra quá nhiều, hơi khó đọc." Một bản của Linux:
```bash
$ vmstat 1
procs -----------memory---------- ---swap-- -----io---- -system-- ----cpu----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa
 4  0      0 34454064 111516 13438596 0   0     0     5    2    0  0  0 100  0
 4  0      0 34455208 111516 13438596 0   0     0    16   12   73  0  2   0  0
[...]
```

Phiên bản `vmstat(8)` này cung cấp:
- **swpd:** Dung lượng swap.
- **free:** Bộ nhớ tự do (chưa dùng).
- **buff/cache:** Buffer và page cache hệ thống tập tin (File system cache - giải thích ở Chương 8). Giải phóng được.
- **si / so:** Swapped in/out (áp lực phân trang).

Lệnh có hệ quy chuẩn theo kilobytes. Đợt theo si/so liên tục thì đang thiếu bộ nhớ áp lực cao (xem swapon(8) dmesg). Khi cần chia đơn vị lớn Mbytes thì thêm -Sm, khi muốn kiểm tra chi tiết inactive / active memory thì dùng cờ `-a`. Các inout tham chiếu thống kê dồn dập list bằng option -s.

### 7.5.2 PSI
PSI của Linux (được thêm từ 4.20) chứa áp lực cho bộ nhớ, biểu diễn mức delay và đợt tăng vọt. Dạng 10 giây/60 giây/5 phút. Output % thời gian thread bị nghẽn (stall): full và some (một vài) qua file `cat /proc/pressure/memory`.

### 7.5.3 swapon
`swapon(1)` có thể hiển thị nếu dung lượng bị xài của page-out device.
```bash
$ swapon
NAME       TYPE      SIZE USED PRIO
/dev/dm-2 partition  980M 611.6M -2
/swap1    file       30G  10.9M -3
```
Nhiều hệ thống không hiện gì vì tắt thiết bị swap block. Nhưng có thể xem ở `iostat` (Chương 9).

### 7.5.4 sar
Giám sát lịch sử `sar(1)` (System Activity Reporter). Option:
- **-B:** Phân trang.
- **-H:** Cảnh Huge pages.
- **-r:** Số lượng ảo/vật lý.
- **-S:** Tình trạng Swap space.
- **-W:** Swap paging (Linux swapping/si so).

Ví dụ số liệu của Bảng 7.5 liên quan tới memory: pgpgin/pgpgout (kb/s paging), majflt, pgscank/pgscand (số page scan - kswapd/hệ thống trực tiếp), kbmemused, kbcommit, %vmeff (chỉ số hiệu quả page reclaim), ...

Mức %vmeff 100 là cao - lấy rác inactive tốt; thấp 30 thì chật vật. Trace pgscand cho app bị chặn gọi trực tiếp.

### 7.5.5 slabtop
`slabtop(1)` trình bày của Kernel Slab Cache allocator. In realtime danh sách (OBJS ACTIVE USE SLABS size). Cầm đầu dung lượng cấp nhân như (ext4_inode_cache, dentry, buffer_head, v.v.). Dữ liệu này từ `/proc/slabinfo`.

### 7.5.6 numastat
Lệnh `numastat(8)` liệt kê hiệu năng NUMA (như 2 socket memory). Nếu có số `numa_hit` cao, quá trình gọi cục bộ/local tốt. Khi `numa_miss` hoặc `numa_foreign` và `other_node` cao, máy đang bị lỗi luân chuyển xa dẫn đến Miss/Foreign, phải gọi sysctl (hoặc NUMA cpubind). Lấy cờ -m hoặc numactl xem cấu hình.

### 7.5.7 ps
Lệnh `ps(1)` xem chỉ số memory size `ps aux`. Output phần `%MEM` (tổng % RSS), `RSS` (Kbytes), `VSZ` (Kbytes ảo).
Do chia sẻ library nhiều process, nên nếu đo RSS dồn lại sẽ bị ảo vượt tổng bộ nhớ (chia sẻ). Option -o pid,pmem,vsz,rss,comm xuất format riêng.

### 7.5.8 top
Trình giám sát top tương tác theo cột. (e.g., top -o %MEM). Chỉ rõ \%MEM, VIRT, RES có chung ý nghĩa `ps(1)`. Để biết thêm nhấn `?`. Kéo xuống có SHR để tham chiếu shared.

### 7.5.9 pmap
Lệnh ánh xạ phân giải (address map process). `pmap -x PID`. Ví dụ cho Database Mysqld, sẽ thấy các segment vùng (Offset Address, Kbyte ảo, RSS vật lý, Mode truy cập - r, rw, r-x) do anon (vô danh/heap) hay các thư viện libc chia sẻ.
Mức `pmap -XX` có báo số liệu `Pss` (Proportional set size) tính phân số rạch ròi bằng bộ chia sẻ được tách sòng phẳng giữa process nhằm cho RSS chính xác hơn.

### 7.5.10 perf
Lệnh profiler nhân, trình diễn 7.5:
- Mẫu page fault lỗi trang: `perf record -e page-faults -a -g`.
- Hàm cấp heap sbrk: `perf record -e syscalls:sys_enter_brk -a -g`.
- Count kmem/vmscan: `perf stat -e 'kmem:*' -a -I 1000`.

Biểu đồ "Ngọn lửa Page Faults" Flame Graphs mô phỏng sự kiện cấp phát lỗi trang khi tiến trình nở bung. Sử dụng mảng gộp của Stack collapses scripts `-count=pages`.

### 7.5.11 drsnoop
`drsnoop(8)` là tool `BCC` mô phỏng độ trễ lấy reclaim direct cho OOM (Direct reclaim). Phơi lệnh qua tham chiếu vmscan `mm_vmscan_direct_reclaim_begin` với độ trễ theo ms (LAT). Trễ càng rườm rà thì app đang đói thắt memory VM.

### 7.5.12 wss
Công cụ `wss(8)` tính toán ước lượng bộ WSS - Working Set Size bằng cách xoá sạch theo cờ PTE accessed. Theo dõi trong một số giây đo PSS và Ref. Đây là thực nghiệm trên `/proc/PID/clear_refs`, cẩn thận tốn CPU ngắt.

### 7.5.13 bpftrace
`bpftrace` tạo ra kịch bản tuỳ chỉnh. VD: theo dấu u-stack với malloc/sum(high overhead):
`bpftrace -e 'uprobe:/lib/x86_64-linux-gnu/libc.so.6:malloc { @[ustack] = hist(arg0); }'` (dành cho malloc PID dạng Histogram Flamegraph).
Nó còn có thể thăm dò (probe) qua USDT tracepoints. Mức call triệu/s có thể có overhead cao. Có thể theo dò memory watchpoints trực tiếp.

### 7.5.14 Các công cụ khác (Other Tools)
Các tool tham dự bảng 7.6: `pmcarch` , `tlbstat`, `free`, `cachestat` (xem hệ tập tin), tool từ quyển BCC BPF [Gregg 19] như `oomkill`, `memleak`, `mmapsnoop`, `brkstack` ...
Lệnh phụ như `/proc/buddyinfo` cho list mảnh vỡ kernel Buddy allocator hoặc SysRq trigger `echo m > /proc/sysrq-trigger` xuất trạng thái.

## 7.6 Tinh chỉnh (Tuning)

Việc tinh chỉnh bộ nhớ quan trọng nhất mà bạn có thể thực hiện là đảm bảo rằng các ứng dụng vẫn nằm trong bộ nhớ chính, và việc phân trang (paging) và hoán đổi (swapping) không xảy ra thường xuyên. Việc xác định vấn đề này đã được bao quát trong Mục 7.4, Phương pháp luận, và Mục 7.5, Công cụ Quan sát. Phần này thảo luận về các tinh chỉnh bộ nhớ khác: các tham số có thể tinh chỉnh của nhân, cấu hình các trang lớn (large pages), các trình cấp phát, và kiểm soát tài nguyên.

Các đặc điểm cụ thể của việc tinh chỉnh—các tùy chọn có sẵn và những gì cần thiết lập cho chúng—phụ thuộc vào phiên bản hệ điều hành và khối lượng công việc dự kiến. Các phần sau đây, được tổ chức theo loại tinh chỉnh, cung cấp các ví dụ về các tham số có thể tinh chỉnh nào có sẵn, và tại sao chúng có thể cần được tinh chỉnh.

### 7.6.1 Các Tham số Có thể Tinh chỉnh (Tunable Parameters)

Phần này mô tả các ví dụ về tham số có thể tinh chỉnh cho các nhân Linux gần đây.
Các tham số tinh chỉnh bộ nhớ khác nhau được mô tả trong tài liệu nguồn của nhân trong Documentation/sysctl/vm.txt và có thể được thiết lập bằng sysctl(8). Các ví dụ trong Bảng 7.7 là từ một nhân 5.3, với các mặc định từ Ubuntu 19.10 (phần liệt kê trong phiên bản đầu tiên của cuốn sách này vẫn giữ nguyên không đổi từ lúc đó).

**Bảng 7.7 Ví dụ về các tham số tinh chỉnh bộ nhớ Linux**

| Tùy chọn (Option) | Mặc định (Default) | Mô tả (Description) |
| --- | --- | --- |
| vm.dirty_background_bytes | 0 | Lượng bộ nhớ dơ để kích hoạt tiến trình xả ngầm pdflush (write-back) |
| vm.dirty_background_ratio | 10 | Tỷ lệ phần trăm bộ nhớ hệ thống dơ để kích hoạt tiến trình xả ngầm pdflush |
| vm.dirty_bytes | 0 | Lượng bộ nhớ dơ khiến một tiến trình đang ghi bắt đầu xả ghi (write-back) |
| vm.dirty_ratio | 20 | Tỷ lệ bộ nhớ hệ thống dơ khiến một tiến trình đang ghi bắt đầu thực hiện xả (write-back) |
| vm.dirty_expire_centisecs | 3,000 | Thời gian tối thiểu để bộ nhớ dơ trở nên đủ điều kiện cho pdflush (thúc đẩy việc hủy ghi) |
| vm.dirty_writeback_centisecs | 500 | Khoảng thời gian đánh thức pdflush (0 để vô hiệu hóa) |
| vm.min_free_kbytes | động (dynamic) | thiết lập lượng bộ nhớ tự do mong muốn (một số cấp phát nguyên tử của nhân có thể tiêu thụ cái này) |
| vm.watermark_scale_factor | 10 | Khoảng cách giữa các mốc dung lượng kswapd watermarks (min, low, high) kiểm soát việc thức dậy và ngủ (đơn vị là phân số của 10000, sao cho 10 có nghĩa là 0.1% của bộ nhớ hệ thống) |
| vm.watermark_boost_factor | 5000 | Khoảng cách mà kswapd quét vượt qua high watermark khi bộ nhớ bị phân mảnh (các sự kiện phân mảnh gần đây đã xảy ra); đơn vị là phân số của 10000, vì vậy 5000 có nghĩa là kswapd có thể tăng cường lên tới 150% của high watermark; 0 để vô hiệu hóa |
| vm.percpu_pagelist_fraction | 0 | Có thể ghi đè phân số tối đa mặc định của các trang có thể được phân bổ cho các danh sách trang của từng CPU (một giá trị 10 giới hạn ở 1/10 số trang) |
| vm.overcommit_memory | 0 | 0 = Sử dụng một suy nghiệm (heuristic) để cho phép các đợt cấp phát vượt mức hợp lý; 1 = luôn luôn cấp phát vượt mức; 2 = không cấp phát vượt mức |
| vm.swappiness | 60 | Mức độ ưu tiên hoán đổi (phân trang) cho việc giải phóng bộ nhớ so với việc thu hồi nó từ bộ đệm trang |
| vm.vfs_cache_pressure | 100 | Mức độ thu hồi các đối tượng thư mục và inode được đệm ẩn; các giá trị thấp hơn sẽ giữ lại chúng nhiều hơn; 0 có nghĩa là không bao giờ thu hồi—có thể dễ dàng dẫn đến các tình trạng hết bộ nhớ |
| kernel.numa_balancing | 1 | Bật cân bằng trang NUMA tự động |
| kernel.numa_balancing_scan_size_mb | 256 | Bao nhiêu Mbytes trang được quét cho mỗi đợt quét cân bằng NUMA |

Các tham số tinh chỉnh sử dụng một sơ đồ đặt tên nhất quán bao gồm các đơn vị. Lưu ý rằng dirty_background_bytes và dirty_background_ratio là loại trừ lẫn nhau, cũng như dirty_bytes và dirty_ratio (khi một cái được thiết lập nó sẽ ghi đè cái kia).

Kích thước của vm.min_free_kbytes được thiết lập động như một phân số của bộ nhớ chính. Thuật ngữ để chọn cái này là không tuyến tính, vì nhu cầu cho bộ nhớ tự do không tăng tỉ lệ tuyến tính với kích thước bộ nhớ chính. (Để tham khảo, việc này được tài liệu hóa trong mã nguồn Linux tại mm/page_alloc.c.) vm.min_free_kbytes có thể được giảm bớt để giải phóng một phần bộ nhớ cho các ứng dụng, nhưng điều đó cũng có thể khiến nhân bị quá tải trong quá trình áp lực bộ nhớ và viện đến việc sử dụng OOM sớm hơn. Việc tăng nó có thể giúp tránh các đợt giết OOM.

Một tham số khác để tránh OOM là vm.overcommit_memory, thứ có thể được thiết lập thành 2 để vô hiệu hóa cấp phát vượt mức và tránh các trường hợp nơi việc này dẫn tới OOM. Nếu bạn muốn kiểm soát trình giết OOM trên cơ sở mỗi tiến trình, hãy kiểm tra phiên bản nhân của bạn cho các tham số tinh chỉnh /proc chẳng hạn như oom_adj hoặc oom_score_adj. Những thứ này được mô tả trong Documentation/filesystems/proc.txt.

Tham số tinh chỉnh vm.swappiness có thể ảnh hưởng đáng kể đến hiệu năng nếu nó bắt đầu hoán đổi bộ nhớ ứng dụng sớm hơn mong muốn. Giá trị của tham số tinh chỉnh này có thể nằm giữa 0 và 100, với các giá trị cao ưu tiên việc hoán đổi các ứng dụng và do đó giữ lại bộ đệm trang. Có thể là mong muốn khi thiết lập cái này về không, sao cho bộ nhớ ứng dụng được giữ lại lâu nhất có thể với chi phí là bộ đệm trang. Khi vẫn còn tình trạng thiếu hụt bộ nhớ, nhân vẫn có thể sử dụng hoán đổi.

Tại Netflix, kernel.numa_balancing đã được thiết lập về không cho các kernels sớm hơn (khoảng Linux 3.13) bởi vì việc quét NUMA quá tích cực đã tiêu thụ quá nhiều CPU [Gregg 17d]. Việc này đã được sửa chữa trong các kernels sau này, và có các tham số tinh chỉnh khác bao gồm kernel.numa_balancing_scan_size_mb cho việc điều chỉnh tính tích cực của việc quét NUMA.

### 7.6.2 Nhiều Kích thước Trang (Multiple Page Sizes)
Các kích thước trang lớn có thể cải thiện hiệu năng I/O bộ nhớ bằng cách cải thiện tỷ lệ hit của bộ đệm ẩn TLB (tăng tầm với của nó). Hầu hết các bộ xử lý hiện đại hỗ trợ nhiều kích thước trang, chẳng hạn như mặc định 4 Kbyte và một trang lớn 2 Mbyte.

Trên Linux, các trang lớn (được gọi là các trang khổng lồ - huge pages) có thể được cấu hình theo một số cách. Để tham khảo, xem Documentation/vm/hugetlbpage.txt.

Những việc này thường bắt đầu với việc tạo ra các trang khổng lồ:
```bash
# echo 50 > /proc/sys/vm/nr_hugepages
# grep Huge /proc/meminfo
AnonHugePages:         0 kB
HugePages_Total:      50
HugePages_Free:       50
HugePages_Rsvd:       0
HugePages_Surp:       0
Hugepagesize:       2048 kB
```

Một cách để một ứng dụng tiêu thụ các trang khổng lồ là qua các phân đoạn bộ nhớ chia sẻ, và cờ SHM_HUGETLBS cho shmget(2). Một cách khác liên quan đến việc tạo ra một hệ thống tập tin dựa trên trang khổng lồ cho các ứng dụng ánh xạ bộ nhớ từ đó:
```bash
# mkdir /mnt/hugetlbfs
# mount -t hugetlbfs none /mnt/hugetlbfs -o pagesize=2048K
```

Các cách khác bao gồm các cờ MAP_ANONYMOUS|MAP_HUGETLB cho mmap(2) và việc sử dụng API libhugetlbfs [Gorman 10].

Cuối cùng, các trang khổng lồ trong suốt (transparent huge pages - THP) là một cơ chế khác sử dụng các trang khổng lồ bằng cách tự động thăng cấp và hạ cấp các trang bình thường sang khổng lồ, mà một ứng dụng không cần chỉ định các trang khổng lồ [Corbet 11]. Trong mã nguồn Linux xem Documentation/vm/transhuge.txt và admin-guide/mm/transhuge.rst.¹¹

---
¹¹ Lưu ý rằng trong lịch sử đã có các vấn đề hiệu năng với các trang khổng lồ trong suốt, làm cản trở việc sử dụng nó. Những vấn đề này hy vọng đã được sửa chữa.

---

### 7.6.3 Các trình cấp phát (Allocators)
Các trình cấp phát cấp người dùng khác nhau có thể có sẵn, cung cấp hiệu năng được cải thiện cho các ứng dụng đa luồng. Những thứ này có thể được lựa chọn tại thời điểm biên dịch, hoặc tại thời điểm thực thi bằng cách thiết lập biến môi trường LD_PRELOAD.

Ví dụ, trình cấp phát libtcmalloc có thể được lựa chọn bằng cách sử dụng:
`export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4`

Việc này có thể được đặt trong script khởi động của nó.

### 7.6.4 Liên kết NUMA (NUMA Binding)
Trên các hệ thống NUMA, lệnh numactl(8) có thể được sử dụng để liên kết các tiến trình với các nút NUMA. Điều này có thể cải thiện hiệu năng cho các ứng dụng không cần nhiều hơn một nút NUMA duy nhất của bộ nhớ chính. Ví dụ sử dụng:
`# numactl --membind=0 3161`

Lệnh này liên kết PID 3161 với nút NUMA 0. Các đợt cấp phát bộ nhớ trong tương lai cho tiến trình này sẽ thất bại nếu chúng không thể được thỏa mãn từ nút này. Khi sử dụng tùy chọn này, bạn cũng nên điều tra việc sử dụng tùy chọn --physcpubind để cũng hạn chế việc sử dụng CPU vào các CPUs được kết nối tới nút NUMA đó. Tôi thường xuyên sử dụng cả hai liên kết NUMA và CPU để hạn chế một tiến trình vào một socket duy nhất, nhằm tránh hình phạt hiệu năng của việc truy cập kết nối CPU.

Sử dụng numastat(8) (Mục 7.5.6) để liệt kê các nút NUMA khả dụng.

### 7.6.5 Kiểm soát Tài nguyên (Resource Controls)
Các kiểm soát tài nguyên cơ bản, bao gồm thiết lập một giới hạn bộ nhớ chính và một giới hạn bộ nhớ ảo, có thể khả dụng khi sử dụng ulimit(1).

Đối với Linux, hệ thống con bộ nhớ của các nhóm container (cgroups) cung cấp các kiểm soát bổ sung khác nhau. Những thứ này bao gồm:
- **memory.limit_in_bytes:** Bộ nhớ người dùng tối đa được phép, bao gồm cả việc sử dụng bộ đệm ẩn tệp, tính theo byte
- **memory.memsw.limit_in_bytes:** Bộ nhớ tối đa được phép và không gian hoán đổi, tính theo byte (khi hoán đổi đang được sử dụng)
- **memory.kmem.limit_in_bytes:** Bộ nhớ nhân tối đa được phép, tính theo byte
- **memory.tcp.limit_in_bytes:** Bộ nhớ đệm TCP tối đa, tính theo byte.
- **memory.swappiness:** Tương tự như vm.swappiness đã mô tả trước đó nhưng có thể được thiết lập cho một cgroup
- **memory.oom_control:** Có thể được thiết lập thành 0, để cho phép trình giết OOM cho cgroup này, hoặc 1, để vô hiệu hóa nó

Linux cũng cho phép cấu hình trên toàn hệ thống trong /etc/security/limits.conf.

Để biết thêm về các kiểm soát tài nguyên, xem Chương 11, Điện toán đám mây.

## 7.7 Các bài tập (Exercises)
1. Trả lời các câu hỏi sau đây về thuật ngữ bộ nhớ:
   - Một trang bộ nhớ (page) là gì?
   - Bộ nhớ thường trú là gì?
   - Bộ nhớ ảo là gì?
   - Sử dụng thuật ngữ Linux, sự khác biệt giữa phân trang và hoán đổi là gì?

2. Trả lời các câu hỏi khái niệm sau đây:
   - Mục đích của phân trang theo nhu cầu là gì?
   - Mô tả mức sử dụng bộ nhớ và độ bão hòa.
   - Mục đích của MMU và TLB là gì?
   - Vai trò của daemon phân trang ra ngoài là gì?
   - Vai trò của trình giết OOM là gì?

3. Trả lời các câu hỏi sâu hơn sau đây:
   - Phân trang vô danh là gì, và tại sao việc phân tích nó lại quan trọng hơn phân trang hệ thống tập tin?
   - Mô tả các bước mà nhân thực hiện để giải phóng thêm bộ nhớ khi bộ nhớ tự do bị cạn kiệt trên các hệ thống dựa trên Linux.
   - Mô tả các ưu điểm hiệu năng của việc cấp phát dựa trên slab.

4. Phát triển các quy trình sau cho hệ điều hành của bạn:
   - Một checklist phương pháp USE cho các tài nguyên bộ nhớ. Bao gồm cách lấy từng chỉ số (ví dụ: lệnh nào để thực thi) và cách diễn giải kết quả. Thử sử dụng các công cụ quan sát OS hiện có trước khi cài đặt hoặc sử dụng các sản phẩm phần mềm bổ sung.
   - Tạo một checklist đặc tính hóa khối lượng công việc cho các tài nguyên bộ nhớ. Bao gồm cách lấy từng chỉ số, và thử sử dụng các công cụ quan sát OS hiện có trước tiên.

5. Thực hiện các tác vụ này:
   - Chọn một ứng dụng, và tóm tắt các đường dẫn mã dẫn tới việc cấp phát bộ nhớ (malloc(3)).
   - Chọn một ứng dụng có một mức độ tăng trưởng bộ nhớ nhất định (gọi brk(2) hoặc sbrk(2)), và tóm tắt các đường dẫn mã dẫn tới sự tăng trưởng này.
   - Mô tả hoạt động bộ nhớ hiển thị chỉ riêng trong kết quả Linux sau đây:
```bash
# vmstat 1
procs -----------memory-------- ---swap-- -----io---- --system-- -----cpu----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 2  0 413344  62284     72   6972    0    0    17    12    1    1  0  0 100  0  0
 2  0 418036  68172     68   3808    0 4692  4520  4692 1060 1939 61 38  0  1  0
 2  0 418232  71272     68   1696    0  196 23924   196 1288 2464 51 38  0 11  0
 2  0 418308  68792     76   2456    0   76  3408    96 1028 1873 58 39  0  3  0
 1  0 418308  67296     76   3936    0    0  1060     0 1020 1843 53 47  0  0  0
 1  0 418308  64948     76   3936    0    0     0     0 1005 1808 36 64  0  0  0
 1  0 418308  62724     76   6120    0    0  2208     0 1030 1870 62 38  0  0  0
 1  0 422320  62772     76   6112    0 4012     0  4016 1052 1900 49 51  0  0  0
 1  0 422320  62772     76   6144    0    0     0     0 1007 1826 62 38  0  0  0
 1  0 422320  60796     76   6144    0    0     0     0 1008 1817 53 47  0  0  0
 1  0 422320  60788     76   6144    0    0     0     0 1006 1812 49 51  0  0  0
 3  0 430792  65584     64   5216    0 8472  4912  8472 1030 1846 54 40  0  6  0
 1  0 430792  64220     72   6496    0    0  1124    16 1024 1857 62 38  0  0  0
 2  0 434252  68188     64   3704    0 3460  5112  3460 1070 1964 60 40  0  0  0
 2  0 434252  71540     64   1436    0    0 21856     0 1300 2478 55 41  0  4  0
 1  0 434252  66072     64   3912    0    0  2020     0 1022 1817 60 40  0  0  0
[...]
```

6. (tùy chọn, nâng cao) Tìm hoặc phát triển các chỉ số để chỉ ra các chính sách tính cục bộ bộ nhớ NUMA của nhân đang hoạt động tốt như thế nào trong thực tế. Phát triển các khối lượng công việc “đã biết” có tính cục bộ bộ nhớ tốt hoặc kém để kiểm tra các chỉ số.

## 7.8 Tài liệu tham khảo (References)
- [Corbató 68] Corbató, F. J., *A Paging Experiment with the Multics System*, MIT Project MAC Report MAC-M-384, 1968.
- [Denning 70] Denning, P., “Virtual Memory,” *ACM Computing Surveys (CSUR)* 2, no. 3, 1970.
- [Peterson 77] Peterson, J., and Norman, T., “Buddy Systems,” *Communications of the ACM*, 1977.
- [Thompson 78] Thompson, K., *UNIX Implementation*, Bell Laboratories, 1978.
- [Babaoglu 79] Babaoglu, O., Joy, W., and Porcar, J., *Design and Implementation of the Berkeley Virtual Memory Extensions to the UNIX Operating System*, Computer Science Division, Deptartment of Electrical Engineering and Computer Science, University of California, Berkeley, 1979.
- [Bach 86] Bach, M. J., *The Design of the UNIX Operating System*, Prentice Hall, 1986.
- [Bonwick 94] Bonwick, J., “The Slab Allocator: An Object-Caching Kernel Memory Allocator,” *USENIX*, 1994.
- [Bonwick 01] Bonwick, J., and Adams, J., “Magazines and Vmem: Extending the Slab Allocator to Many CPUs and Arbitrary Resources,” *USENIX*, 2001.
- [Corbet 04] Corbet, J., “2.6 swapping behavior,” *LWN.net*, http://lwn.net/Articles/83588, 2004.
- [Gorman 04] Gorman, M., *Understanding the Linux Virtual Memory Manager*, Prentice Hall, 2004.
- [McDougall 06a] McDougall, R., Mauro, J., and Gregg, B., *Solaris Performance and Tools: DTrace and MDB Techniques for Solaris 10 and OpenSolaris*, Prentice Hall, 2006.
- [Ghemawat 07] Ghemawat, S., “TCMalloc : Thread-Caching Malloc,” https://gperftools.github.io/gperftools/tcmalloc.html, 2007.
- [Lameter 07] Lameter, C., “SLUB: The unqueued slab allocator V6,” *Linux kernel mailing list*, http://lwn.net/Articles/229096, 2007.
- [Hall 09] Hall, A., “Thanks for the Memory, Linux,” Andrew Hall, https://www.ibm.com/developerworks/library/j-nativememory-linux, 2009.
- [Gorman 10] Gorman, M., “Huge pages part 2: Interfaces,” *LWN.net*, http://lwn.net/Articles/375096, 2010.
- [Corbet 11] Corbet, J., “Transparent huge pages in 2.6.38,” *LWN.net*, http://lwn.net/Articles/423584, 2011.
- [Facebook 11] “Scalable memory allocation using jemalloc,” *Facebook Engineering*, https://www.facebook.com/notes/facebook-engineering/scalable-memory-allocationusing-jemalloc/480222803919, 2011.
- [Evans 17] Evans, J., “Swapping, memory limits, and cgroups,” https://jvns.ca/blog/2017/02/17/mystery-swap, 2017.
- [Gregg 17d] Gregg, B., “AWS re:Invent 2017: How Netflix Tunes EC2,” http://www.brendangregg.com/blog/2017-12-31/reinvent-netflix-ec2-tuning.html, 2017.
- [Corbet 18a] Corbet, J., “Is it time to remove ZONE_DMA?” *LWN.net*, https://lwn.net/Articles/753273, 2018.
- [Crucial 18] “The Difference between RAM Speed and CAS Latency,” https://www.crucial.com/articles/about-memory/difference-between-speed-and-latency, 2018.
- [Gregg 18c] Gregg, B., “Working Set Size Estimation,” http://www.brendangregg.com/wss.html, 2018.
- [Facebook 19] “Getting Started with PSI,” *Facebook Engineering*, https://facebookmicrosites.github.io/psi/docs/overview, 2019.
- [Gregg 19] Gregg, B., *BPF Performance Tools: Linux System and Application Observability*, Addison-Wesley, 2019.
- [Intel 19a] *Intel 64 and IA-32 Architectures Software Developer’s Manual, Combined Volumes: 1, 2A, 2B, 2C, 3A, 3B and 3C*, Intel, 2019.
- [Amazon 20] “Amazon EC2 High Memory Instances,” https://aws.amazon.com/ec2/instance-types/high-memory, accessed 2020.
- [Linux 20g] “Linux Magic System Request Key Hacks,” *Linux documentation*, https://www.kernel.org/doc/html/latest/admin-guide/sysrq.html, accessed 2020.
- [Robertson 20] Robertson, A., “bpftrace,” https://github.com/iovisor/bpftrace, last updated 2020.
- [Valgrind 20] “Valgrind Documentation,” http://valgrind.org/docs/manual, May 2020.
