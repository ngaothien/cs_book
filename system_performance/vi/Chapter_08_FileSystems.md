# Chương 8: Hệ thống Tập tin (File Systems)

Hiệu năng hệ thống tập tin thường quan trọng đối với ứng dụng hơn là hiệu năng đĩa hoặc thiết bị lưu trữ, bởi vì chính hệ thống tập tin là thứ mà các ứng dụng tương tác và chờ đợi. Các hệ thống tập tin có thể sử dụng cơ chế cache, buffering và I/O bất đồng bộ để tránh việc khiến các ứng dụng phải chịu độ trễ ở mức đĩa (hoặc hệ thống lưu trữ từ xa).

Các công cụ phân tích và giám sát hiệu năng hệ thống trong lịch sử thường tập trung vào hiệu năng đĩa, để lại hiệu năng hệ thống tập tin như một điểm mù. Chương này làm sáng tỏ các hệ thống tập tin, chỉ ra cách chúng hoạt động và cách đo lường độ trễ cùng các chi tiết khác của chúng. Điều này thường giúp loại trừ hệ thống tập tin và các thiết bị đĩa cơ sở của chúng như là nguồn gây ra hiệu năng kém, cho phép quá trình điều tra chuyển sang các lĩnh vực khác.

Các mục tiêu học tập của chương này là:
- Hiểu các mô hình và khái niệm hệ thống tập tin.
- Hiểu cách khối lượng công việc (workloads) hệ thống tập tin ảnh hưởng đến hiệu năng.
- Trở nên quen thuộc với các bộ đệm (caches) hệ thống tập tin.
- Trở nên quen thuộc với các thành phần nội bộ và các tính năng hiệu năng của hệ thống tập tin.
- Thực hiện theo các phương pháp luận khác nhau để phân tích hệ thống tập tin.
- Đo lường độ trễ hệ thống tập tin để xác định các chế độ (modes) và các giá trị ngoại lai (outliers).
- Điều tra việc sử dụng hệ thống tập tin bằng các công cụ truy vết (tracing).
- Kiểm tra hiệu năng hệ thống tập tin bằng các phép thử vi mô (microbenchmarks).
- Nhận biết các tham số có thể tinh chỉnh (tunable parameters) của hệ thống tập tin.

Chương này bao gồm sáu phần, ba phần đầu cung cấp cơ sở cho việc phân tích hệ thống tập tin và ba phần cuối trình bày ứng dụng thực tế của nó đối với các hệ thống dựa trên Linux. Các phần như sau:
- **Nền tảng (Background)** giới thiệu thuật ngữ liên quan đến hệ thống tập tin và các mô hình cơ bản, minh họa các nguyên tắc hệ thống tập tin và các khái niệm hiệu năng hệ thống tập tin then chốt.
- **Kiến trúc (Architecture)** giới thiệu kiến trúc hệ thống tập tin chung và cụ thể.
- **Phương pháp luận (Methodology)** mô tả các phương pháp phân tích hiệu năng, cả quan sát và thực nghiệm.
- **Công cụ Quan trắc (Observability Tools)** trình bày các công cụ quan sát hệ thống tập tin cho các hệ thống dựa trên Linux, bao gồm instrumentation tĩnh và động.
- **Thực nghiệm (Experimentation)** tóm tắt các công cụ benchmark hệ thống tập tin.
- **Tinh chỉnh (Tuning)** mô tả các tham số có thể tinh chỉnh của hệ thống tập tin.

## 8.1 Thuật ngữ (Terminology)
Để tham khảo, thuật ngữ liên quan đến hệ thống tập tin được sử dụng trong chương này bao gồm:
- **Hệ thống tập tin (File system):** Một sự tổ chức dữ liệu dưới dạng các tập tin và thư mục, với một giao diện dựa trên tập tin để truy cập chúng, và các quyền hạn tập tin để kiểm soát truy cập. Nội dung bổ sung có thể bao gồm các loại tập tin đặc biệt cho các thiết bị, socket, và pipe, và siêu dữ liệu (metadata) bao gồm các dấu thời gian truy cập tập tin.
- **Bộ đệm hệ thống tập tin (File system cache):** Một vùng của bộ nhớ chính (thường là DRAM) được sử dụng để đệm nội dung hệ thống tập tin, có thể bao gồm các bộ đệm khác nhau cho các loại dữ liệu và siêu dữ liệu khác nhau.
- **Các thao tác (Operations):** Các thao tác hệ thống tập tin là các yêu cầu của hệ thống tập tin, bao gồm read(2), write(2), open(2), close(2), stat(2), mkdir(2), và các thao tác khác.
- **I/O:** Input/output. I/O hệ thống tập tin có thể được định nghĩa theo nhiều cách; ở đây nó được dùng để chỉ các thao tác đọc và ghi trực tiếp (thực hiện I/O), bao gồm read(2), write(2), stat(2) (đọc thống kê), và mkdir(2) (ghi một mục thư mục mới). I/O không bao gồm open(2) và close(2) (mặc dù các lệnh gọi đó cập nhật metadata và có thể gây ra I/O đĩa gián tiếp).
- **I/O Logic (Logical I/O):** I/O được phát ra bởi ứng dụng tới hệ thống tập tin.
- **I/O Vật lý (Physical I/O):** I/O được phát trực tiếp tới các đĩa bởi hệ thống tập tin (hoặc thông qua raw I/O).
- **Kích thước khối (Block size):** Còn được gọi là record size, là kích thước của các nhóm dữ liệu trên đĩa của hệ thống tập tin. Xem Block vs. Extent trong Mục 8.4.4, Các tính năng hệ thống tập tin.
- **Thông lượng (Throughput):** Tốc độ truyền dữ liệu hiện tại giữa các ứng dụng và hệ thống tập tin, được đo bằng byte mỗi giây.
- **inode:** Một nút chỉ mục (index node - inode) là một cấu trúc dữ liệu chứa metadata cho một đối tượng hệ thống tập tin, bao gồm các quyền hạn, dấu thời gian, và các con trỏ dữ liệu.
- **VFS:** Virtual file system (hệ thống tập tin ảo), một giao diện kernel để trừu tượng hóa và hỗ trợ các loại hệ thống tập tin khác nhau.
- **Volume (Phân vùng):** Một bản thể lưu trữ cung cấp tính linh hoạt cao hơn so với việc sử dụng toàn bộ một thiết bị lưu trữ. Một volume có thể là một phần của một thiết bị, hoặc nhiều thiết bị.
- **Volume manager:** Phần mềm để quản lý các thiết bị lưu trữ vật lý một cách linh hoạt, tạo ra các virtual volumes để hệ điều hành sử dụng.

Các thuật ngữ khác được giới thiệu xuyên suốt chương này. Bảng thuật ngữ (Glossary) bao gồm các thuật ngữ cơ bản để tham khảo, bao gồm fsck, IOPS, operation rate, và POSIX. Đồng thời hãy xem các phần thuật ngữ trong Chương 2 và 3.

## 8.2 Mô hình (Models)
Các mô hình đơn giản sau đây minh họa một số nguyên tắc cơ bản của hệ thống tập tin và hiệu năng của chúng.

### 8.2.1 Giao diện Hệ thống Tập tin (File System Interfaces)
Một mô hình cơ bản của một hệ thống tập tin được trình bày trong Hình 8.1, xét theo các giao diện của nó.

(Hình 8.1 Các giao diện hệ thống tập tin)

Các vị trí nơi các thao tác logic và vật lý diễn ra cũng được dán nhãn trong hình. Xem Mục 8.3.12, I/O Logic so với Vật lý, để biết thêm về các nội dung này.

Hình 8.1 trình bày các thao tác đối tượng chung. Các kernel có thể triển khai thêm các biến thể bổ sung: ví dụ, Linux cung cấp readv(2), writev(2), openat(2), và nhiều hơn nữa.

Một cách tiếp cận để nghiên cứu hiệu năng hệ thống tập tin là coi nó như một hộp đen, tập trung vào độ trễ của các thao tác đối tượng. Điều này được giải thích chi tiết hơn trong Mục 8.5.2, Phân tích độ trễ (Latency Analysis).

### 8.2.2 Bộ đệm Hệ thống Tập tin (File System Cache)
Một bộ đệm hệ thống tập tin chung được lưu trữ trong bộ nhớ chính được hình ảnh hóa trong Hình 8.2, đang phục vụ một thao tác đọc.

Thao tác đọc trả về dữ liệu hoặc từ bộ đệm (cache hit) hoặc từ đĩa (cache miss). Các trường hợp trượt cache (cache misses) được lưu trữ trong bộ đệm, làm đầy bộ đệm (warming it up).

Bộ đệm hệ thống tập tin cũng có thể đệm các thao tác ghi để được ghi (flushed) sau đó. Các cơ chế để thực hiện việc này khác nhau đối với các loại hệ thống tập tin khác nhau, và được mô tả trong Mục 8.4, Kiến trúc.

Các kernel thường cung cấp một cách để bỏ qua bộ đệm nếu muốn. Xem Mục 8.3.8, Raw and Direct I/O.

(Hình 8.2 Bộ đệm bộ nhớ chính của hệ thống tập tin)

### 8.2.3 Bộ đệm Tầng thứ hai (Second-Level Cache)
Bộ đệm tầng thứ hai có thể là bất kỳ loại bộ nhớ nào; Hình 8.3 trình bày nó dưới dạng bộ nhớ flash. Loại bộ đệm này lần đầu tiên được phát triển bởi chính tác giả vào năm 2007, cho ZFS.

(Hình 8.3 Bộ đệm tầng thứ hai của hệ thống tập tin)

## 8.3 Các khái niệm (Concepts)
Sau đây là một lựa chọn các khái niệm hiệu năng hệ thống tập tin quan trọng.

### 8.3.1 Độ trễ Hệ thống Tập tin (File System Latency)
Độ trễ hệ thống tập tin là chỉ số chính của hiệu năng hệ thống tập tin, được đo bằng thời gian từ một yêu cầu hệ thống tập tin logic đến khi nó hoàn thành. Nó bao gồm thời gian dành cho hệ thống tập tin và hệ thống con I/O đĩa, và việc chờ đợi trên các thiết bị đĩa—I/O vật lý. Các luồng ứng dụng thường bị chặn trong một yêu cầu của ứng dụng để chờ các yêu cầu hệ thống tập tin hoàn thành—theo cách này, độ trễ hệ thống tập tin ảnh hưởng trực tiếp và tỷ lệ thuận đến hiệu năng ứng dụng.

Các trường hợp mà ứng dụng có thể không bị ảnh hưởng trực tiếp bao gồm việc sử dụng non-blocking I/O, prefetch (Mục 8.3.4), và khi I/O được phát ra từ một luồng bất đồng bộ (ví dụ: một luồng flush chạy nền). Có thể xác định các trường hợp này từ ứng dụng, nếu nó cung cấp các chỉ số chi tiết cho việc sử dụng hệ thống tập tin của nó. Nếu không, một cách tiếp cận chung là sử dụng một công cụ truy vết kernel có thể hiển thị stack trace mức người dùng dẫn đến một I/O hệ thống tập tin logic. Stack trace này sau đó có thể được nghiên cứu để xem các thủ tục ứng dụng nào đã phát ra nó.

Các hệ điều hành trong lịch sử đã không làm cho độ trễ hệ thống tập tin có thể quan sát dễ dàng, thay vào đó cung cấp các thống kê mức thiết bị đĩa. Nhưng có nhiều trường hợp mà các thống kê như vậy không liên quan đến hiệu năng ứng dụng, và cũng có khi chúng gây nhầm lẫn. Một ví dụ về điều này là nơi các hệ thống tập tin thực hiện việc flush chạy nền các dữ liệu đã ghi, thứ có thể xuất hiện như các đợt bùng phát I/O đĩa độ trễ cao. Từ các thống kê mức thiết bị đĩa, điều này trông có vẻ đáng báo động; tuy nhiên, không có ứng dụng nào đang chờ chúng hoàn thành. Xem Mục 8.3.12, I/O Logic so với Vật lý, để biết thêm các trường hợp.

### 8.3.2 Caching (Lưu đệm)
Hệ thống tập tin thông thường sẽ sử dụng bộ nhớ chính (RAM) như một bộ đệm để cải thiện hiệu năng. Đối với các ứng dụng, quá trình này là minh bạch: độ trễ I/O logic của ứng dụng trở nên thấp hơn nhiều (tốt hơn), vì nó có thể được phục vụ từ bộ nhớ chính thay vì các thiết bị đĩa chậm hơn nhiều.

Theo thời gian, bộ đệm phát triển, trong khi bộ nhớ trống cho hệ điều hành thu hẹp lại. Điều này có thể gây lo ngại cho những người dùng mới, nhưng là hoàn toàn bình thường. Nguyên tắc là: Nếu có bộ nhớ chính dư thừa, hãy làm điều gì đó hữu ích với nó. Khi các ứng dụng cần thêm bộ nhớ, kernel nên nhanh chóng giải phóng nó từ bộ đệm hệ thống tập tin để sử dụng.

Các hệ thống tập tin sử dụng caching để cải thiện hiệu năng đọc, và buffering (trong bộ đệm) để cải thiện hiệu năng ghi. Nhiều loại bộ đệm thường được sử dụng bởi hệ thống tập tin và hệ thống con thiết bị khối, có thể bao gồm những loại trong Bảng 8.1.

Bảng 8.1 Các loại bộ đệm ví dụ
| Bộ đệm | Ví dụ |
| --- | --- |
| Page cache | Operating system page cache |
| File system primary cache | ZFS ARC |
| File system secondary cache | ZFS L2ARC |
| Directory cache | dentry cache |
| inode cache | inode cache |
| Device cache | ZFS vdev |
| Block device cache | Buffer cache |

Các loại bộ đệm cụ thể được mô tả trong Mục 8.4, Kiến trúc, trong khi Chương 3, Hệ điều hành, có danh sách đầy đủ các bộ đệm (bao gồm mức ứng dụng và thiết bị).

### 8.3.3 I/O Ngẫu nhiên so với Tuần tự (Random vs. Sequential I/O)
Một chuỗi các I/O hệ thống tập tin logic có thể được mô tả là ngẫu nhiên hoặc tuần tự, dựa trên độ dời (offset) tập tin của mỗi I/O. Với I/O tuần tự, mỗi offset I/O bắt đầu tại điểm kết thúc của I/O trước đó. I/O ngẫu nhiên không có mối quan hệ rõ ràng giữa chúng, và offset thay đổi ngẫu nhiên. Một khối lượng công việc hệ thống tập tin ngẫu nhiên cũng có thể đề cập đến việc truy cập nhiều tập tin khác nhau một cách ngẫu nhiên.

(Hình 8.4 I/O tập tin tuần tự và ngẫu nhiên)

Hình 8.4 minh họa các mẫu truy cập này, trình bày một chuỗi I/O có thứ tự và các offset tập tin ví dụ.

Do các đặc tính hiệu năng của một số thiết bị lưu trữ nhất định (được mô tả trong Chương 9, Các đĩa), các hệ thống tập tin trong lịch sử đã cố gắng giảm thiểu I/O ngẫu nhiên bằng cách đặt dữ liệu tập tin trên đĩa một cách tuần tự và liên tục. Thuật ngữ phân mảnh (fragmentation) mô tả những gì xảy ra khi các hệ thống tập tin thực hiện việc này kém, khiến các tập tin bị rải rác trên một ổ đĩa, sao cho I/O logic tuần tự tạo ra I/O vật lý ngẫu nhiên.

Hệ thống tập tin có thể đo lường các mẫu truy cập I/O logic để chúng có thể xác định các khối lượng công việc tuần tự, và sau đó cải thiện hiệu năng của chúng bằng cách sử dụng prefetch hoặc read-ahead. Điều này hữu ích cho các đĩa quay (rotational disks); ít hữu ích hơn cho các ổ đĩa flash.

### 8.3.4 Prefetch (Tải trước)
Một khối lượng công việc hệ thống tập tin phổ biến liên quan đến việc đọc một lượng lớn dữ liệu tập tin một cách tuần tự, ví dụ, cho một bản sao lưu hệ thống tập tin. Dữ liệu này có thể quá lớn để khớp vào bộ đệm, hoặc nó có thể chỉ được đọc một lần và khó có khả năng được giữ lại trong bộ đệm (tùy thuộc vào chính sách loại bỏ của bộ đệm). Một khối lượng công việc như vậy sẽ thực hiện tương đối kém, vì nó sẽ có tỷ lệ trúng bộ đệm thấp.

Prefetch là một tính năng hệ thống tập tin phổ biến để giải quyết vấn đề này. Nó có thể phát hiện một khối lượng công việc đọc tuần tự dựa trên các offset I/O tập tin hiện tại và trước đó, sau đó dự đoán và phát ra các lệnh đọc đĩa trước khi ứng dụng yêu cầu chúng. Việc này làm đầy bộ đệm hệ thống tập tin, sao cho nếu ứng dụng thực hiện lệnh đọc như mong đợi, nó sẽ dẫn đến một cache hit (dữ liệu cần thiết đã có sẵn trong bộ đệm). Một kịch bản ví dụ như sau:
1. Một ứng dụng phát ra một lệnh read(2) tập tin, chuyển quyền thực thi cho kernel.
2. Dữ liệu không được đệm, vì vậy hệ thống tập tin phát lệnh đọc tới đĩa.
3. Con trỏ offset tập tin trước đó được so sánh với vị trí hiện tại, và nếu chúng là tuần tự, hệ thống tập tin phát thêm các lệnh đọc (prefetch).
4. Lệnh đọc đầu tiên hoàn thành, và kernel chuyển dữ liệu cùng quyền thực thi trở lại ứng dụng.
5. Bất kỳ lệnh đọc prefetch nào hoàn thành, làm đầy bộ đệm cho các lần đọc ứng dụng trong tương lai.
6. Các lần đọc ứng dụng tuần tự trong tương lai hoàn thành nhanh chóng thông qua bộ đệm trong RAM.

Kịch bản này cũng được minh họa trong Hình 8.5, nơi các lần đọc của ứng dụng tới các offset 1 và sau đó là 2 kích hoạt prefetch của ba offset tiếp theo.

(Hình 8.5 Prefetch hệ thống tập tin)

Khi việc phát hiện prefetch hoạt động tốt, các ứng dụng cho thấy hiệu năng đọc tuần tự được cải thiện đáng kể; các đĩa luôn đi trước các yêu cầu của ứng dụng (miễn là chúng có đủ băng thông để làm việc đó). Khi việc phát hiện prefetch hoạt động kém, các I/O không cần thiết được phát ra mà ứng dụng không cần đến, gây ô nhiễm bộ đệm và tiêu tốn tài nguyên đĩa và vận chuyển I/O. Các hệ thống tập tin thường cho phép tinh chỉnh prefetch khi cần thiết.

### 8.3.5 Read-Ahead (Đọc trước)
Trong lịch sử, prefetch cũng được biết đến như là read-ahead. Linux sử dụng thuật ngữ read-ahead cho một lệnh gọi hệ thống, readahead(2), cho phép các ứng dụng làm nóng bộ đệm hệ thống tập tin một cách rõ ràng.

### 8.3.6 Write-Back Caching
Write-back caching thường được sử dụng bởi các hệ thống tập tin để cải thiện hiệu năng ghi. Nó hoạt động bằng cách coi các lệnh ghi là đã hoàn thành sau khi chuyển tới bộ nhớ chính, và ghi chúng xuống đĩa vào lúc nào đó sau đó, một cách bất đồng bộ. Quá trình của hệ thống tập tin để ghi dữ liệu "bẩn" (dirty) này xuống đĩa được gọi là flushing (ghi xuất). Một chuỗi ví dụ như sau:
1. Một ứng dụng phát ra một lệnh write(2) tập tin, chuyển quyền thực thi cho kernel.
2. Dữ liệu từ không gian địa chỉ ứng dụng được sao chép vào kernel.
3. Kernel coi lệnh syscall write(2) là đã hoàn thành, chuyển quyền thực thi trở lại ứng dụng.
4. Một lúc nào đó sau đó, một tác vụ kernel bất đồng bộ tìm thấy dữ liệu đã ghi và phát các lệnh ghi đĩa.

Sự đánh đổi ở đây là độ tin cậy. Bộ nhớ chính dựa trên DRAM là loại bộ nhớ dễ bay hơi (volatile), và dữ liệu bẩn có thể bị mất trong trường hợp mất điện. Dữ liệu cũng có thể được ghi xuống đĩa một cách không hoàn chỉnh, để lại một trạng thái trên đĩa bị hỏng.

Nếu siêu dữ liệu (metadata) của hệ thống tập tin bị hỏng, hệ thống tập tin có thể không còn tải được nữa. Một trạng thái như vậy có thể chỉ có thể khôi phục được từ các bản sao lưu hệ thống, gây ra thời gian ngừng hoạt động kéo dài. Tệ hơn, nếu sự hư hỏng ảnh hưởng đến nội dung tập tin mà ứng dụng đọc và sử dụng, công việc kinh doanh có thể bị đe dọa.

Để cân bằng nhu cầu về cả tốc độ và độ tin cậy, các hệ thống tập tin có thể cung cấp write-back caching theo mặc định, và một tùy chọn ghi đồng bộ (synchronous write) để bỏ qua hành vi này và ghi trực tiếp vào các thiết bị lưu trữ bền vững.

### 8.3.7 Các lệnh ghi đồng bộ (Synchronous Writes)
Một lệnh ghi đồng bộ chỉ hoàn thành khi đã được ghi đầy đủ vào bộ lưu trữ bền vững (ví dụ: các thiết bị đĩa), bao gồm cả việc ghi bất kỳ thay đổi siêu dữ liệu hệ thống tập tin nào cần thiết. Những lệnh này chậm hơn nhiều so với các lệnh ghi bất đồng bộ (write-back caching), vì các lệnh ghi đồng bộ phải chịu độ trễ I/O của thiết bị đĩa (và có thể là nhiều I/O do metadata của hệ thống tập tin). Các lệnh ghi đồng bộ được sử dụng bởi một số ứng dụng như các trình ghi nhật ký cơ sở dữ liệu (database log writers), nơi rủi ro hư hỏng dữ liệu từ các lệnh ghi bất đồng bộ là không thể chấp nhận được.

Có hai dạng ghi đồng bộ: I/O riêng lẻ, được ghi đồng bộ, và các nhóm lệnh ghi trước đó, được cam kết (committed) một cách đồng bộ.

**Các lệnh ghi đồng bộ riêng lẻ (Individual Synchronous Writes)**
I/O ghi là đồng bộ khi một tập tin được mở bằng cách sử dụng cờ O_SYNC hoặc một trong các biến thể, O_DSYNC và O_RSYNC (mà kể từ Linux 2.6.31 được ánh xạ bởi glibc sang O_SYNC). Một số hệ thống tập tin có các tùy chọn mount để bắt buộc tất cả I/O ghi tới tất cả các tập tin phải là đồng bộ.

**Cam kết đồng bộ các lệnh ghi trước đó (Synchronously Committing Previous Writes)**
Thay vì ghi đồng bộ từng I/O riêng lẻ, một ứng dụng có thể cam kết một cách đồng bộ các lệnh ghi bất đồng bộ trước đó tại các điểm kiểm tra (checkpoints) trong mã của chúng, sử dụng lệnh gọi hệ thống fsync(2). Điều này có thể cải thiện hiệu năng bằng cách nhóm các lệnh ghi, và cũng có thể tránh việc cập nhật metadata nhiều lần bằng cách sử dụng write cancellation (hủy bỏ ghi).

Có những tình huống khác sẽ cam kết các lệnh ghi trước đó, chẳng hạn như đóng các handle tập tin, hoặc khi có quá nhiều bộ đệm chưa được cam kết trên một tập tin. Trường hợp đầu tiên thường có thể nhận thấy như những lần tạm dừng dài khi giải nén một kho lưu trữ gồm nhiều tập tin, đặc biệt là qua NFS.

### 8.3.8 Raw and Direct I/O
Đây là các loại I/O khác mà một ứng dụng có thể sử dụng, nếu được hỗ trợ bởi kernel hoặc hệ thống tập tin:

**Raw I/O** được phát trực tiếp tới các offset đĩa, bỏ qua hoàn toàn hệ thống tập tin. Nó đã được sử dụng bởi một số ứng dụng, đặc biệt là các cơ sở dữ liệu, thứ có thể quản lý và đệm dữ liệu của chính chúng tốt hơn bộ đệm của hệ thống tập tin. Một nhược điểm là sự phức tạp hơn trong phần mềm, và các khó khăn về quản trị: bộ công cụ hệ thống tập tin thông thường không thể được sử dụng cho việc sao lưu/khôi phục hoặc quan sát.

**Direct I/O** cho phép các ứng dụng sử dụng một hệ thống tập tin nhưng bỏ qua bộ đệm hệ thống tập tin, ví dụ, bằng cách sử dụng cờ open(2) O_DIRECT trên Linux. Điều này tương tự như các lệnh ghi đồng bộ (nhưng không có các đảm bảo mà O_SYNC cung cấp), và nó cũng hoạt động cho các lệnh đọc. Nó không trực tiếp như I/O thiết bị thô (raw device I/O), vì việc ánh xạ các offset tập tin sang các offset đĩa vẫn phải được thực hiện bởi mã hệ thống tập tin, và I/O cũng có thể bị thay đổi kích thước để khớp với kích thước được sử dụng bởi hệ thống tập tin cho bố cục trên đĩa (record size của nó) hoặc nó có thể báo lỗi (EINVAL). Tùy thuộc vào hệ thống tập tin, điều này có thể không chỉ vô hiệu hóa cache đọc và buffering ghi mà còn có thể vô hiệu hóa prefetch.

### 8.3.9 Non-Blocking I/O
Thông thường, I/O hệ thống tập tin sẽ hoàn thành ngay lập tức (ví dụ: từ bộ đệm) hoặc sau khi chờ đợi (ví dụ: cho I/O thiết bị đĩa). Nếu cần chờ đợi, luồng ứng dụng sẽ bị chặn (block) và rời khỏi CPU, cho phép các luồng khác thực thi trong khi nó chờ đợi. Mặc dù luồng bị chặn không thể thực hiện công việc khác, điều này thường không phải là vấn đề vì các ứng dụng đa luồng có thể tạo thêm các luồng để thực thi trong khi một số luồng khác bị chặn.

Trong một số trường hợp, non-blocking I/O là mong muốn, chẳng hạn như khi tránh chi phí hiệu năng hoặc tài nguyên của việc tạo luồng. Non-blocking I/O có thể được thực hiện bằng cách sử dụng các cờ O_NONBLOCK hoặc O_NDELAY cho syscall open(2), thứ khiến các lệnh đọc và ghi trả về một lỗi EAGAIN thay vì bị chặn, điều này báo cho ứng dụng thử lại sau. (Việc hỗ trợ cho điều này tùy thuộc vào hệ thống tập tin, thứ có thể chỉ tuân thủ non-blocking cho các khóa tập tin advisory hoặc mandatory.)

Hệ điều hành cũng có thể cung cấp một giao diện I/O bất đồng bộ riêng biệt, chẳng hạn như aio_read(3) và aio_write(3). Linux 5.1 đã thêm một giao diện I/O bất đồng bộ mới gọi là io_uring, với sự cải thiện về tính dễ sử dụng, hiệu quả và hiệu năng [Axboe 19].

Non-blocking I/O cũng đã được thảo luận trong Chương 5, Ứng dụng, Mục 5.2.6, Non-Blocking I/O.

### 8.3.10 Các tập tin được ánh xạ vào bộ nhớ (Memory-Mapped Files)
Đối với một số ứng dụng và khối lượng công việc, hiệu năng I/O hệ thống tập tin có thể được cải thiện bằng cách ánh xạ các tập tin vào không gian địa chỉ tiến trình và truy cập các offset bộ nhớ trực tiếp. Điều này tránh được việc thực thi syscall và chi phí chuyển đổi ngữ cảnh (context switch) phát sinh khi gọi các syscall read(2) và write(2) để truy cập dữ liệu tập tin. Nó cũng có thể tránh việc sao chép dữ liệu hai lần, nếu kernel hỗ trợ ánh xạ trực tiếp bộ đệm dữ liệu tập tin vào không gian địa chỉ tiến trình.

Các ánh xạ bộ nhớ được tạo bằng syscall mmap(2) và được loại bỏ bằng munmap(2). Các ánh xạ có thể được tinh chỉnh bằng madvise(2), như được tóm tắt trong Mục 8.8, Tinh chỉnh. Một số ứng dụng cung cấp một tùy chọn để sử dụng các syscall mmap (có thể được gọi là "mmap mode") trong cấu hình của chúng. Ví dụ, cơ sở dữ liệu Riak có thể sử dụng mmap cho kho lưu trữ dữ liệu trong bộ nhớ của nó.

Tôi đã nhận thấy một xu hướng cố gắng sử dụng mmap(2) để giải quyết các vấn đề hiệu năng hệ thống tập tin mà không phân tích chúng trước. Nếu vấn đề là độ trễ I/O cao từ các thiết bị đĩa, việc tránh các chi phí syscall nhỏ với mmap(2) có thể đạt được rất ít kết quả, khi mà độ trễ I/O đĩa cao vẫn hiện diện và chiếm ưu thế.

Một nhược điểm của việc sử dụng các ánh xạ trên các hệ thống đa bộ xử lý có thể là chi phí để giữ cho MMU của mỗi CPU được đồng bộ, cụ thể là các lệnh gọi chéo CPU (CPU cross calls) để loại bỏ các ánh xạ (TLB shootdowns). Tùy thuộc vào kernel và ánh xạ, những điều này có thể được giảm thiểu bằng cách trì hoãn các cập nhật TLB (lazy shootdowns) [Vahalia 96].

### 8.3.11 Siêu dữ liệu (Metadata)
Trong khi dữ liệu mô tả nội dung của các tập tin và thư mục, metadata mô tả thông tin về chúng. Metadata có thể đề cập đến thông tin có thể được đọc từ giao diện hệ thống tập tin (POSIX) hoặc thông tin cần thiết để triển khai bố cục trên đĩa của hệ thống tập tin. Chúng được gọi tương ứng là metadata logic và vật lý.

**Siêu dữ liệu Logic (Logical Metadata)**
Metadata logic là thông tin được đọc và ghi vào hệ thống tập tin bởi những bên tiêu thụ (các ứng dụng), hoặc là:
- **Một cách rõ ràng (Explicitly):** Đọc thống kê tập tin (stat(2)), tạo và xóa tập tin (creat(2), unlink(2)) và thư mục (mkdir(2), rmdir(2)), thiết lập các thuộc tính tập tin (chown(2), chmod(2)).
- **Một cách ngấm ngầm (Implicitly):** Các cập nhật dấu thời gian truy cập hệ thống tập tin, các cập nhật dấu thời gian sửa đổi thư mục, các cập nhật bitmap khối đã sử dụng, các thống kê không gian trống.

Một khối lượng công việc là "nặng về metadata" (metadata-heavy) thường đề cập đến metadata logic, ví dụ, các máy chủ web thực hiện stat(2) các tập tin để đảm bảo chúng không thay đổi kể từ khi đệm, với tốc độ lớn hơn nhiều so với việc đọc nội dung dữ liệu tập tin.

**Siêu dữ liệu Vật lý (Physical Metadata)**
Metadata vật lý đề cập đến các metadata bố cục trên đĩa cần thiết để ghi lại tất cả thông tin hệ thống tập tin. Các loại metadata đang được sử dụng tùy thuộc vào hệ thống tập tin và có thể bao gồm superblocks, inodes, các khối con trỏ dữ liệu (sơ cấp, thứ cấp...), và free lists.

Metadata logic và vật lý là một lý do cho sự khác biệt giữa I/O logic và vật lý.

### 8.3.12 I/O Logic so với Vật lý (Logical vs. Physical I/O)
Mặc dù nó có vẻ trái ngược với trực giác, I/O được yêu cầu bởi các ứng dụng tới hệ thống tập tin (I/O logic) có thể không khớp với I/O đĩa (I/O vật lý), vì một số lý do.

Các hệ thống tập tin làm nhiều việc hơn là chỉ trình diễn bộ lưu trữ bền vững (các đĩa) như một giao diện dựa trên tập tin. Chúng đệm các lệnh đọc, buffer các lệnh ghi, ánh xạ tập tin vào không gian địa chỉ, và tạo thêm I/O để duy trì metadata bố cục vật lý trên đĩa mà chúng cần để ghi lại mọi thứ đang ở đâu. Điều này có thể gây ra I/O đĩa không liên quan, gián tiếp, ngấm ngầm, bị thổi phồng (inflated), hoặc bị giảm bớt (deflated) so với I/O ứng dụng. Các ví dụ tiếp theo sau đây.

**Không liên quan (Unrelated)**
Đây là I/O đĩa không liên quan đến ứng dụng và có thể do:
- **Các ứng dụng khác.**
- **Các bên thuê khác (Other tenants):** I/O đĩa là từ một bên thuê đám mây khác (có thể thấy qua các công cụ hệ thống dưới một số công nghệ ảo hóa).
- **Các tác vụ kernel khác:** Ví dụ, khi kernel đang xây dựng lại một volume phần mềm RAID hoặc thực hiện xác minh checksum hệ thống tập tin bất đồng bộ (xem Mục 8.4, Kiến trúc).
- **Các tác vụ quản trị:** Chẳng hạn như sao lưu.

**Gián tiếp (Indirect)**
Đây là I/O đĩa gây ra bởi ứng dụng nhưng không có I/O ứng dụng tương ứng ngay lập tức. Điều này có thể do:
- **Prefetch hệ thống tập tin:** Thêm các I/O bổ sung mà có thể hoặc không thể được sử dụng bởi ứng dụng.
- **Buffering hệ thống tập tin:** Việc sử dụng write-back caching để trì hoãn và kết hợp các lệnh ghi để flush xuống đĩa sau đó. Một số hệ thống có thể buffer các lệnh ghi trong hàng chục giây trước khi ghi, thứ sau đó xuất hiện như các đợt bùng phát lớn, không thường xuyên.

**Ngấm ngầm (Implicit)**
Đây là I/O đĩa được kích hoạt trực tiếp bởi các sự kiện ứng dụng khác ngoài các lệnh đọc và ghi hệ thống tập tin rõ ràng, chẳng hạn như:
- **Các lệnh load/store được ánh xạ bộ nhớ:** Đối với các tập tin được ánh xạ bộ nhớ (mmap(2)), các lệnh load và store có thể kích hoạt I/O đĩa để đọc hoặc ghi dữ liệu. Các lệnh ghi có thể được buffer và ghi sau đó. Điều này có thể gây nhầm lẫn khi phân tích các thao tác hệ thống tập tin (read(2), write(2)) và không tìm thấy nguồn gốc của I/O (vì nó được kích hoạt bởi các chỉ lệnh chứ không phải các syscall).

**Bị giảm bớt (Deflated)**
I/O đĩa nhỏ hơn I/O ứng dụng, hoặc thậm chí không tồn tại. Điều này có thể do:
- **Caching hệ thống tập tin:** Đáp ứng các lệnh đọc từ bộ nhớ chính thay vì đĩa.
- **Hủy bỏ ghi hệ thống tập tin (File system write cancellation):** Các byte offset giống nhau được sửa đổi nhiều lần trước khi được flush một lần xuống đĩa.
- **Nén (Compression):** Giảm khối lượng dữ liệu từ I/O logic sang vật lý.
- **Coalescing (Kết hợp):** Hợp nhất các I/O tuần tự trước khi phát chúng tới đĩa (việc này làm giảm số lượng I/O, nhưng không phải tổng kích cỡ).
- **Hệ thống tập tin trong bộ nhớ (In-memory file system):** Nội dung có thể không bao giờ được ghi xuống đĩa (ví dụ: tmpfs).

**Bị thổi phồng (Inflated)**
I/O đĩa lớn hơn I/O ứng dụng. Đây là trường hợp điển hình do:
- **Siêu dữ liệu hệ thống tập tin:** Thêm các I/O bổ sung.
- **Kích thước bản ghi hệ thống tập tin (File system record size):** Làm tròn kích thước I/O (thổi phồng số byte), hoặc phân mảnh I/O (thổi phồng số lượng).
- **Journaling hệ thống tập tin:** Nếu được sử dụng, việc này có thể làm tăng gấp đôi số lệnh ghi đĩa, một lần cho journal và lần khác cho đích đến cuối cùng.
- **Parity của volume manager:** Các chu kỳ read-modify-write, thêm các I/O bổ sung.
- **Thổi phồng RAID:** Ghi thêm dữ liệu parity, hoặc dữ liệu tới các volume được nhân bản (mirrored).

**Ví dụ**
Để chỉ ra cách các yếu tố này có thể xảy ra đồng thời, ví dụ sau đây mô tả những gì có thể xảy ra với một lệnh ghi ứng dụng 1-byte:
1. Một ứng dụng thực hiện một lệnh ghi 1-byte vào một tập tin hiện có.
2. Hệ thống tập tin xác định vị trí đó là một phần của một bản ghi (record) hệ thống tập tin 128 Kbyte, thứ không được đệm (nhưng metadata để tham chiếu nó thì có).
3. Hệ thống tập tin yêu cầu bản ghi đó được nạp từ đĩa.
4. Tầng thiết bị đĩa chia lệnh đọc 128 Kbyte thành các lệnh đọc nhỏ hơn phù hợp cho thiết bị.
5. Các đĩa thực hiện nhiều lệnh đọc nhỏ, tổng cộng 128 Kbyte.
6. Hệ thống tập tin bây giờ thay thế 1 byte trong bản ghi bằng byte mới.
7. Một lúc nào đó sau đó, hệ thống tập tin hoặc kernel yêu cầu bản ghi bẩn 128 Kbyte được ghi ngược lại đĩa.
8. Các đĩa ghi bản ghi 128 Kbyte (được chia nhỏ nếu cần).
9. Hệ thống tập tin ghi metadata mới, ví dụ, để cập nhật các tham chiếu (cho copy-on-write) hoặc thời gian truy cập.
10. Các đĩa thực hiện thêm các lệnh ghi.

Vì vậy, trong khi ứng dụng chỉ thực hiện một lệnh ghi 1-byte duy nhất, các đĩa đã thực hiện nhiều lệnh đọc (tổng cộng 128 Kbyte) và nhiều lệnh ghi hơn nữa (trên 128 Kbyte).

### 8.3.13 Các thao tác là không bình đẳng (Operations Are Not Equal)
Như đã rõ ràng từ các phần trước, các thao tác hệ thống tập tin có thể thể hiện hiệu năng khác nhau dựa trên loại của chúng. Bạn không thể biết nhiều về một khối lượng công việc "500 thao tác/giây" chỉ từ tốc độ đơn thuần. Một số thao tác có thể trả về từ bộ đệm hệ thống tập tin ở tốc độ bộ nhớ chính; những thao tác khác có thể trả về từ đĩa và chậm hơn nhiều bậc độ lớn. Các yếu tố quyết định khác bao gồm liệu các thao tác là ngẫu nhiên hay tuần tự, đọc hay ghi, ghi đồng bộ hay ghi bất đồng bộ, kích thước I/O của chúng, liệu chúng có bao gồm các loại thao tác khác hay không, chi phí thực thi CPU của chúng (và hệ thống đang tải CPU như thế nào), và các đặc tính của thiết bị lưu trữ.

Thực hành phổ biến là micro-benchmark các thao tác hệ thống tập tin khác nhau để xác định các đặc tính hiệu năng này. Như một ví dụ, các kết quả trong Bảng 8.2 là từ một hệ thống tập tin ZFS, trên một bộ xử lý đa lõi Intel Xeon 2.4 GHz đang rảnh rỗi.

Bảng 8.2 Các độ trễ thao tác hệ thống tập tin ví dụ
| Thao tác | Trung bình (μs) |
| --- | --- |
| open(2) (đã đệm) | 2.2 |
| close(2) (sạch) | 0.7 |
| read(2) 4 Kbyte (đã đệm) | 3.3 |
| read(2) 128 Kbyte (đã đệm) | 13.9 |
| write(2) 4 Kbyte (bất đồng bộ) | 9.3 |
| write(2) 128 Kbyte (bất đồng bộ) | 55.2 |

Các thử nghiệm này không liên quan đến các thiết bị lưu trữ mà là một thử nghiệm về phần mềm hệ thống tập tin và tốc độ CPU. Một số hệ thống tập tin đặc biệt không bao giờ truy cập các thiết bị lưu trữ bền vững.

Các thử nghiệm này cũng là đơn luồng. Hiệu năng I/O song song có thể bị ảnh hưởng bởi loại và sự tổ chức của các khóa (locks) hệ thống tập tin đang được sử dụng.

### 8.3.14 Các hệ thống tập tin đặc biệt (Special File Systems)
Mục đích của một hệ thống tập tin thường là để lưu trữ dữ liệu bền vững, nhưng có các loại hệ thống tập tin đặc biệt được sử dụng trên Linux cho các mục đích khác, bao gồm các tập tin tạm thời (/tmp), các đường dẫn thiết bị kernel (/dev), các thống kê hệ thống (/proc), và cấu hình hệ thống (/sys).

### 8.3.15 Dấu thời gian truy cập (Access Timestamps)
Nhiều hệ thống tập tin hỗ trợ các dấu thời gian truy cập, thứ ghi lại thời gian mà mỗi tập tin và thư mục được truy cập (đọc). Điều này khiến metadata tập tin bị cập nhật bất cứ khi nào các tập tin được đọc, tạo ra một khối lượng công việc ghi tiêu tốn tài nguyên I/O đĩa. Mục 8.8, Tinh chỉnh, chỉ ra cách tắt các cập nhật này.

Một số hệ thống tập tin tối ưu hóa việc ghi dấu thời gian truy cập bằng cách trì hoãn và nhóm chúng lại để giảm sự can thiệp vào khối lượng công việc đang hoạt động.

### 8.3.16 Dung lượng (Capacity)
Khi các hệ thống tập tin đầy, hiệu năng có thể bị suy giảm vì một vài lý do. Đầu tiên, khi ghi dữ liệu mới, có thể mất nhiều thời gian CPU và I/O đĩa hơn để tìm các khối trống trên đĩa. Thứ hai, các vùng không gian trống trên đĩa có khả năng nhỏ hơn và nằm rải rác thưa thớt hơn, làm suy giảm hiệu năng do các I/O nhỏ hơn hoặc I/O ngẫu nhiên.

Vấn đề này nghiêm trọng đến mức nào tùy thuộc vào loại hệ thống tập tin, bố cục trên đĩa của nó, việc sử dụng copy-on-write của nó, và các thiết bị lưu trữ của nó. Các loại hệ thống tập tin khác nhau được mô tả trong phần tiếp theo.

---

## 8.4 Kiến trúc (Architecture)
Phần này giới thiệu kiến trúc hệ thống tập tin chung và cụ thể, bắt đầu với I/O stack, VFS, các bộ đệm và tính năng của hệ thống tập tin, các loại hệ thống tập tin phổ biến, các volume và pool. Nền tảng như vậy rất hữu ích khi xác định các thành phần hệ thống tập tin nào cần phân tích và tinh chỉnh. Để biết thêm về các chi tiết nội bộ sâu hơn và các chủ đề hệ thống tập tin khác, hãy tham khảo mã nguồn, nếu có sẵn, và các tài liệu bên ngoài. Một số trong số này được liệt kê ở cuối chương này.

### 8.4.1 File System I/O Stack
Hình 8.6 mô tả một mô hình chung của I/O stack hệ thống tập tin, tập trung vào giao diện hệ thống tập tin. Các thành phần, các tầng và các API cụ thể tùy thuộc vào loại hệ điều hành, phiên bản và các hệ thống tập tin được sử dụng. Một hình ảnh I/O stack cấp cao hơn được bao gồm trong Chương 3, Hệ điều hành, và một hình ảnh khác trình bày chi tiết hơn các thành phần đĩa có trong Chương 9, Các đĩa.

(Hình 8.6 I/O stack hệ thống tập tin chung)

Hình này trình bày đường dẫn của I/O từ các ứng dụng và thư viện hệ thống tới các syscall và qua kernel. Đường dẫn từ các system call trực tiếp tới hệ thống con thiết bị đĩa là raw I/O. Đường dẫn qua VFS và hệ thống tập tin là I/O hệ thống tập tin, bao gồm cả direct I/O, thứ bỏ qua bộ đệm hệ thống tập tin.

### 8.4.2 VFS
VFS (virtual file system interface) cung cấp một giao diện chung cho các loại hệ thống tập tin khác nhau. Vị trí của nó được trình bày trong Hình 8.7.

(Hình 8.7 Giao diện hệ thống tập tin ảo)

VFS có nguồn gốc từ SunOS và đã trở thành sự trừu tượng hóa tiêu chuẩn cho các hệ thống tập tin.

Thuật ngữ được sử dụng bởi giao diện VFS của Linux có thể hơi gây nhầm lẫn, vì nó tái sử dụng các thuật ngữ inodes và superblocks để đề cập đến các đối tượng VFS—các thuật ngữ có nguồn gốc từ cấu trúc dữ liệu trên đĩa của hệ thống tập tin Unix. Các thuật ngữ được sử dụng cho các cấu trúc dữ liệu trên đĩa của Linux thường được tiền tố bằng loại hệ thống tập tin của chúng, ví dụ, ext4_inode và ext4_super_block. Các VFS inodes và VFS superblocks chỉ tồn tại trong bộ nhớ.

Giao diện VFS cũng có thể phục vụ như một vị trí chung để đo lường hiệu năng của bất kỳ hệ thống tập tin nào. Việc này có thể khả thi bằng cách sử dụng các thống kê được cung cấp bởi hệ điều hành, hoặc instrumentation tĩnh hoặc động.

### 8.4.3 Các bộ đệm Hệ thống Tập tin (File System Caches)
Unix ban đầu chỉ có buffer cache để cải thiện hiệu năng truy cập thiết bị khối. Ngày nay, Linux có nhiều loại bộ đệm khác nhau. Hình 8.8 đưa ra một cái nhìn tổng quan về các bộ đệm hệ thống tập tin trên Linux, trình bày các bộ đệm chung có sẵn cho các loại hệ thống tập tin tiêu chuẩn.

(Hình 8.8 Các bộ đệm hệ thống tập tin Linux)

**Buffer Cache**
Unix đã sử dụng một buffer cache tại giao diện thiết bị khối để đệm các khối thiết bị đĩa. Đây là một bộ đệm riêng biệt, có kích thước cố định và, với sự bổ sung sau đó của page cache, đã nảy sinh các vấn đề tinh chỉnh khi cân bằng các khối lượng công việc khác nhau giữa chúng, cũng như các chi phí đệm gấp đôi (double caching) và đồng bộ hóa. Những vấn đề này phần lớn đã được giải quyết bằng cách sử dụng page cache để lưu trữ buffer cache, một phương pháp được giới thiệu bởi SunOS và được gọi là unified buffer cache (bộ đệm hợp nhất).

Linux ban đầu đã sử dụng một buffer cache như với Unix. Kể từ Linux 2.4, buffer cache cũng đã được lưu trữ trong page cache (do đó có đường viền nét đứt trong Hình 8.8) tránh việc đệm gấp đôi và chi phí đồng bộ hóa. Chức năng buffer cache vẫn tồn tại, cải thiện hiệu năng I/O thiết bị khối, và thuật ngữ này vẫn xuất hiện trong các công cụ quan sát của Linux (ví dụ: free(1)).

Kích thước của buffer cache là động và có thể quan sát được từ /proc.

**Page Cache**
Page cache lần đầu tiên được giới thiệu vào SunOS trong một đợt viết lại bộ nhớ ảo vào năm 1985 và được thêm vào SVR4 Unix [Vahalia 96]. Nó đệm các trang bộ nhớ ảo, bao gồm các trang hệ thống tập tin được ánh xạ, cải thiện hiệu năng I/O tập tin và thư mục. Nó hiệu quả hơn cho việc truy cập tập tin so với buffer cache, thứ yêu cầu dịch từ offset tập tin sang offset đĩa cho mỗi lần tra cứu. Nhiều loại hệ thống tập tin có thể sử dụng page cache, bao gồm những bên tiêu thụ ban đầu là UFS và NFS. Kích thước là động: page cache sẽ phát triển để sử dụng bộ nhớ khả dụng, giải phóng nó một lần nữa khi các ứng dụng cần.

Linux có một page cache với các thuộc tính tương tự. Kích thước của Linux page cache cũng là động, với một tunable để thiết lập sự cân bằng giữa việc loại bỏ khỏi page cache và việc swapping (swappiness; xem Chương 7, Bộ nhớ).

Các trang bộ nhớ bị bẩn (đã sửa đổi) và cần được sử dụng bởi một hệ thống tập tin sẽ được ghi xuất (flushed) xuống đĩa bởi các luồng kernel. Trước Linux 2.6.32, có một pool gồm các luồng page dirty flush (pdflush), từ hai đến tám luồng khi cần thiết. Những luồng này sau đó đã được thay thế bằng các flusher threads (tên là flush), thứ được tạo ra cho mỗi thiết bị để cân bằng tốt hơn khối lượng công việc cho mỗi thiết bị và cải thiện thông lượng. Các trang được flush xuống đĩa vì các lý do sau:
- Sau một khoảng thời gian (30 giây)
- Các lệnh gọi hệ thống sync(2), fsync(2), msync(2)
- Có quá nhiều trang bẩn (các tunables dirty_ratio và dirty_bytes)
- Không còn trang khả dụng trong page cache

Nếu có sự thâm hụt bộ nhớ hệ thống, một luồng kernel khác, page-out daemon (kswapd, còn được gọi là trình quét trang - page scanner), cũng có thể tìm và lập lịch các trang bẩn để được ghi xuống đĩa sao cho nó có thể giải phóng các trang bộ nhớ để tái sử dụng (xem Chương 7, Bộ nhớ). Để có khả năng quan sát, các luồng kswapd và flush có thể được nhìn thấy như các tác vụ kernel từ các công cụ hiệu năng hệ điều hành.

Xem Chương 7, Bộ nhớ, để biết thêm chi tiết về trình quét trang.

**Dentry Cache**
Dentry cache (Dcache) ghi nhớ các ánh xạ từ mục thư mục (struct dentry) sang VFS inode, tương tự như một cache tra cứu tên thư mục Unix (DNLC) trước đó. Dcache cải thiện hiệu năng của việc tra cứu tên đường dẫn (ví dụ: qua open(2)): khi một tên đường dẫn được duyệt qua, mỗi lần tra cứu tên có thể kiểm tra Dcache cho một ánh xạ inode trực tiếp, thay vì bước qua nội dung thư mục. Các mục Dcache được lưu trữ trong một bảng băm để tra cứu nhanh và có khả năng mở rộng (được băm bởi dentry cha và tên mục thư mục).

Hiệu năng đã được cải thiện hơn nữa qua nhiều năm, bao gồm cả thuật toán read-copy-update-walk (RCU-walk) [Corbet 10]. Điều này cố gắng duyệt qua tên đường dẫn mà không cập nhật số lượng tham chiếu dentry, thứ vốn gây ra các vấn đề về khả năng mở rộng do tính nhất quán của bộ đệm (cache coherency) với tốc độ tra cứu tên đường dẫn cao trên các hệ thống đa CPU. Nếu gặp một dentry không có trong bộ đệm, RCU-walk sẽ quay lại phương pháp duyệt theo số lượng tham chiếu (ref-walk) chậm hơn, vì số lượng tham chiếu sẽ là cần thiết trong quá trình tra cứu hệ thống tập tin và việc chặn (blocking). Đối với các khối lượng công việc bận rộn, hy vọng rằng dữ liệu dentry có khả năng sẽ được đệm, và cách tiếp cận RCU-walk sẽ thành công.

Dcache cũng thực hiện negative caching (đệm phủ định), thứ ghi nhớ các lần tra cứu cho các mục không tồn tại. Điều này cải thiện hiệu năng của các lần tra cứu thất bại, thứ thường xảy ra khi tìm kiếm các thư viện chia sẻ.

Dcache phát triển linh động, thu nhỏ lại thông qua LRU (least recently used) khi hệ thống cần thêm bộ nhớ. Kích thước của nó có thể được thấy qua /proc.

**Inode Cache**
Bộ đệm này chứa các VFS inodes (struct inodes), mỗi inode mô tả các thuộc tính của một đối tượng hệ thống tập tin, nhiều trong số đó được trả về qua syscall stat(2). Các thuộc tính này thường xuyên được truy cập cho các khối lượng công việc hệ thống tập tin, chẳng hạn như kiểm tra các quyền hạn khi mở tập tin, hoặc cập nhật các dấu thời gian trong quá trình sửa đổi. Các VFS inodes này được lưu trữ trong một bảng băm để tra cứu nhanh và có khả năng mở rộng (được băm bởi số inode và superblock hệ thống tập tin), mặc dù hầu hết các lần tra cứu sẽ được thực hiện thông qua Dentry cache.

Inode cache phát triển linh động, giữ ít nhất tất cả các inodes được ánh xạ bởi Dcache. Khi có áp lực bộ nhớ hệ thống, inode cache sẽ thu nhỏ lại, loại bỏ các inodes không có dentry liên kết. Kích thước của nó có thể được thấy qua các tập tin /proc/sys/fs/inode*.

### 8.4.4 Các tính năng Hệ thống Tập tin (File System Features)
Các tính năng hệ thống tập tin then chốt bổ sung ảnh hưởng đến hiệu năng được mô tả ở đây.

**Block so với Extent**
Các hệ thống tập tin dựa trên khối (block-based) lưu trữ dữ liệu trong các khối có kích thước cố định, được tham chiếu bởi các con trỏ được lưu trữ trong các khối metadata. Đối với các tập tin lớn, điều này có thể yêu cầu nhiều con trỏ khối và các khối metadata, và việc đặt các khối có thể trở nên rải rác, dẫn đến I/O ngẫu nhiên. Một số hệ thống tập tin dựa trên khối cố gắng đặt các khối một cách liên tục để tránh điều này. Một cách tiếp cận khác là sử dụng kích thước khối thay đổi, sao cho các kích thước lớn hơn có thể được sử dụng khi tập tin phát triển, điều này cũng làm giảm chi phí metadata.

Các hệ thống tập tin dựa trên Extent (extent-based) cấp phát trước không gian liên tục cho các tập tin (extents), phát triển chúng khi cần thiết. Các extents này có độ dài thay đổi, đại diện cho một hoặc nhiều khối liên tục.

Điều này cải thiện hiệu năng truyền phát (streaming) và có thể cải thiện hiệu năng I/O ngẫu nhiên do dữ liệu tập tin được tập trung tại một chỗ. Nó cũng cải thiện hiệu năng metadata vì có ít đối tượng hơn để theo dõi, mà không phải hy sinh không gian của các khối không sử dụng trong một extent.

**Journaling (Ghi nhật ký)**
Một journal (hoặc log) hệ thống tập tin ghi lại các thay đổi đối với hệ thống tập tin sao cho, trong trường hợp hệ thống bị sập hoặc mất điện, các thay đổi có thể được phát lại (replayed) một cách nguyên tử—hoặc thành công toàn bộ hoặc thất bại. Điều này cho phép các hệ thống tập tin nhanh chóng khôi phục về một trạng thái nhất quán. Các hệ thống tập tin không có journaling có thể bị hỏng trong quá trình hệ thống sập, nếu dữ liệu và siêu dữ liệu liên quan đến một thay đổi được ghi không hoàn chỉnh. Việc khôi phục từ một vụ sập như vậy đòi hỏi phải duyệt qua toàn bộ cấu trúc hệ thống tập tin, thứ có thể mất hàng giờ đối với các hệ thống tập tin lớn (hàng terabyte).

Journal được ghi xuống đĩa một cách đồng bộ, và đối với một số hệ thống tập tin, nó có thể được cấu hình để sử dụng một thiết bị riêng biệt. Một số journals ghi lại cả dữ liệu và siêu dữ liệu, thứ tiêu tốn nhiều tài nguyên I/O lưu trữ hơn vì tất cả I/O được ghi hai lần. Những cái khác chỉ ghi siêu dữ liệu và duy trì tính toàn vẹn dữ liệu bằng cách sử dụng copy-on-write.

Có một loại hệ thống tập tin chỉ bao gồm một journal: một log-structured file system, nơi tất cả các cập nhật dữ liệu và siêu dữ liệu được ghi vào một log liên tục và vòng tròn (circular log). Điều này tối ưu hóa hiệu năng ghi, vì các lệnh ghi luôn là tuần tự và có thể được hợp nhất để sử dụng kích thước I/O lớn hơn.

**Copy-on-Write**
Một hệ thống tập tin copy-on-write (COW) không ghi đè lên các khối hiện có mà thay vào đó thực hiện theo các bước sau:
1. Ghi các khối vào một vị trí mới (một bản sao mới).
2. Cập nhật các tham chiếu tới các khối mới.
3. Thêm các khối cũ vào free list.

Điều này giúp duy trì tính toàn vẹn của hệ thống tập tin trong trường hợp hệ thống gặp lỗi, và cũng cải thiện hiệu năng bằng cách chuyển các lệnh ghi ngẫu nhiên thành các lệnh tuần tự.

Khi một hệ thống tập tin gần đến mức dung lượng tối đa, COW có thể khiến bố cục dữ liệu trên đĩa của một tập tin bị phân mảnh, làm giảm hiệu năng (đặc biệt đối với các ổ HDD). Việc chống phân mảnh hệ thống tập tin, nếu có sẵn, có thể giúp khôi phục hiệu năng.

**Scrubbing (Lọc/Quét sạch)**
Đây là một tính năng hệ thống tập tin đọc bất đồng bộ tất cả các khối dữ liệu và xác minh checksums để phát hiện các ổ đĩa bị lỗi càng sớm càng tốt, lý tưởng nhất là khi lỗi vẫn còn có thể khôi phục được nhờ vào RAID. Tuy nhiên, I/O đọc của scrubbing có thể gây hại cho hiệu năng, vì vậy nó nên được phát ra ở mức ưu tiên thấp hoặc vào những thời điểm khối lượng công việc thấp.

**Các tính năng khác**
Các tính năng hệ thống tập tin khác có thể ảnh hưởng đến hiệu năng bao gồm snapshots, nén, tích hợp sẵn sự dư thừa (built-in redundancy), deduplication, hỗ trợ trim, và nhiều hơn nữa. Phần sau đây mô tả các tính năng như vậy cho các hệ thống tập tin cụ thể.

### 8.4.5 Các loại Hệ thống Tập tin (File System Types)
Phần lớn chương này mô tả các đặc điểm chung có thể được áp dụng cho tất cả các loại hệ thống tập tin. Các phần sau đây tóm tắt các tính năng hiệu năng cụ thể cho các hệ thống tập tin được sử dụng phổ biến. Việc phân tích và tinh chỉnh chúng được đề cập trong các phần sau.

**FFS**
Nhiều hệ thống tập tin cuối cùng đều dựa trên Berkeley fast file system (FFS), thứ được thiết kế để giải quyết các vấn đề với hệ thống tập tin Unix ban đầu. Một số nền tảng có thể giúp giải thích trạng thái của các hệ thống tập tin ngày nay.

Bố cục trên đĩa của hệ thống tập tin Unix ban đầu bao gồm một bảng các inodes, các khối lưu trữ 512-byte, và một superblock chứa thông tin được sử dụng khi cấp phát tài nguyên [Ritchie 74][Lions 77]. Bảng inode và các khối lưu trữ chia các phân vùng đĩa thành hai dải, thứ gây ra các vấn đề hiệu năng khi di chuyển đầu đọc (seeking) giữa chúng. Một vấn đề khác là việc sử dụng kích thước khối cố định nhỏ, 512 byte, thứ giới hạn thông lượng và tăng lượng metadata (con trỏ) cần thiết để lưu trữ các tập tin lớn. Một thực nghiệm để tăng gấp đôi con số này lên 1024 byte, và nút thắt cổ chai gặp phải sau đó đã được mô tả bởi [McKusick 84]:

> Mặc dù thông lượng đã tăng gấp đôi, hệ thống tập tin cũ vẫn chỉ sử dụng khoảng 4 phần trăm băng thông đĩa. Vấn đề chính là mặc dù free list ban đầu được sắp xếp để truy cập tối ưu, nó nhanh chóng trở nên xáo trộn khi các tập tin được tạo và xóa. Cuối cùng, free list trở nên hoàn toàn ngẫu nhiên, khiến các tập tin có các khối của chúng được cấp phát ngẫu nhiên trên khắp đĩa. Điều này buộc phải thực hiện một lần seek trước mỗi lần truy cập khối. Mặc dù các hệ thống tập tin cũ cung cấp tốc độ truyền tải lên đến 175 kilobyte mỗi giây khi chúng mới được tạo ra, tốc độ này đã giảm xuống còn 30 kilobyte mỗi giây sau một vài tuần sử dụng ở mức trung bình do sự ngẫu nhiên hóa việc đặt khối dữ liệu này.

Đoạn trích này mô tả sự phân mảnh free list, thứ làm giảm hiệu năng theo thời gian khi hệ thống tập tin được sử dụng.

(Hình 8.9 Các cylinder groups)

FFS đã cải thiện hiệu năng bằng cách chia phân vùng thành nhiều cylinder groups, được trình bày trong Hình 8.9, mỗi nhóm có mảng inode và các khối dữ liệu riêng của nó. Các file inodes và dữ liệu được giữ trong cùng một cylinder group nếu có thể, như hình ảnh trong Hình 8.9, giúp giảm việc seek đĩa. Các dữ liệu liên quan khác cũng được đặt gần nhau, bao gồm các inodes cho một thư mục và các mục của nó. Thiết kế của một inode là tương tự, với một hệ thống phân cấp các con trỏ và các khối dữ liệu, được hình ảnh hóa trong Hình 8.10 (các khối gián tiếp ba cấp, có ba cấp con trỏ, không được trình bày ở đây) [Bach 86].

(Hình 8.10 Cấu trúc dữ liệu Inode)

Kích thước khối đã được tăng lên tối thiểu là 4 Kbyte, cải thiện thông lượng. Điều này làm giảm số lượng khối dữ liệu cần thiết để lưu trữ một tập tin, và do đó làm giảm số lượng các khối gián tiếp cần thiết để tham chiếu đến các khối dữ liệu. Số lượng các khối con trỏ gián tiếp cần thiết còn được giảm bớt vì chính chúng cũng lớn hơn. Để tiết kiệm không gian với các tập tin nhỏ, mỗi khối có thể được chia thành các mảnh (fragments) 1 Kbyte.

Một tính năng hiệu năng khác của FFS là block interleaving: đặt các khối tập tin tuần tự trên đĩa với một khoảng cách giữa chúng là một hoặc nhiều khối [Doeppner 10]. Những khối bổ sung này cho phép kernel và bộ xử lý có thời gian để phát lệnh đọc tập tin tuần tự tiếp theo. Nếu không có interleaving, khối tiếp theo có thể đi qua đầu đọc đĩa (quay) trước khi nó sẵn sàng phát lệnh đọc, gây ra độ trễ khi nó phải chờ một vòng quay đầy đủ.

**ext3**
Linux extended file system (ext) được phát triển vào năm 1992 như là hệ thống tập tin đầu tiên cho Linux và VFS của nó, dựa trên hệ thống tập tin Unix ban đầu. Phiên bản thứ hai, ext2 (1993), bao gồm nhiều dấu thời gian và các cylinder groups từ FFS. Phiên bản thứ ba, ext3 (1999), bao gồm khả năng phát triển hệ thống tập tin và journaling.

Các tính năng hiệu năng then chốt, bao gồm cả những tính năng được thêm vào kể từ khi phát hành, là:
- **Journaling:** Chế độ ordered, chỉ dành cho siêu dữ liệu, hoặc chế độ journal, cho cả siêu dữ liệu và dữ liệu. Journaling cải thiện hiệu năng khởi động sau khi hệ thống bị sập, tránh việc phải chạy fsck. Nó cũng có thể cải thiện hiệu năng của một số khối lượng công việc ghi bằng cách kết hợp các lệnh ghi metadata.
- **Journal device:** Một thiết bị journal bên ngoài có thể được sử dụng, để khối lượng công việc của journal không tranh chấp với khối lượng công việc đọc.
- **Orlov block allocator:** Điều này rải các thư mục cấp cao nhất qua các cylinder groups, sao cho các thư mục con và nội dung có nhiều khả năng được đặt cùng nhau, làm giảm I/O ngẫu nhiên.
- **Directory indexes:** Những thứ này thêm các cây B-tree băm (hashed B-trees) vào hệ thống tập tin để tra cứu thư mục nhanh hơn.

Các tính năng có thể cấu hình được tài liệu hóa trong trang man mke2fs(8).

**ext4**
Hệ thống tập tin ext4 của Linux được phát hành vào năm 2008, mở rộng ext3 với các tính năng mới và các cải tiến hiệu năng: extents, dung lượng lớn, cấp phát trước với fallocate(2), trì hoãn cấp phát, journal checksumming, fsck nhanh hơn, bộ cấp phát đa khối (multiblock allocator), dấu thời gian nano giây, và snapshots.

Các tính năng hiệu năng then chốt, bao gồm cả những tính năng được thêm vào kể từ khi phát hành, là:
- **Extents:** Extents cải thiện việc đặt dữ liệu liên tục, làm giảm I/O ngẫu nhiên và tăng kích thước I/O cho I/O tuần tự. Chúng được giới thiệu trong Mục 8.4.4, Các tính năng hệ thống tập tin.
- **Cấp phát trước (Preallocation):** Thông qua syscall fallocate(2), điều này cho phép các ứng dụng cấp phát trước không gian mà có khả năng là liên tục, cải thiện hiệu năng ghi sau đó.
- **Trì hoãn cấp phát (Delayed allocation):** Việc cấp phát khối được trì hoãn cho đến khi nó được flush xuống đĩa, cho phép các lệnh ghi được nhóm lại (thông qua multiblock allocator), làm giảm sự phân mảnh.
- **fsck nhanh hơn:** Các khối chưa được cấp phát và các mục inode được đánh dấu, làm giảm thời gian chạy fsck.

Trạng thái của một số tính năng có thể được thấy qua hệ thống tập tin /sys. Ví dụ:
```bash
# cd /sys/fs/ext4/features
# grep . *
batched_discard:supported
casefold:supported
encryption:supported
lazy_itable_init:supported
meta_bg_resize:supported
metadata_csum_seed:supported
```
Các tính năng có thể cấu hình được tài liệu hóa trong trang man mke2fs(8). Một số tính năng, chẳng hạn như extents, cũng có thể được áp dụng cho các hệ thống tập tin ext3.

**XFS**
XFS được tạo ra bởi Silicon Graphics vào năm 1993 cho hệ điều hành IRIX của họ, để giải quyết các hạn chế về khả năng mở rộng trong hệ thống tập tin IRIX trước đó, EFS (dựa trên FFS) [Sweeney 96]. Các bản vá XFS đã được sáp nhập vào Linux kernel vào đầu những năm 2000. Ngày nay, XFS được hỗ trợ bởi hầu hết các bản phân phối Linux và có thể được sử dụng cho hệ thống tập tin gốc (root). Ví dụ, Netflix sử dụng XFS cho các thực thể cơ sở dữ liệu Cassandra của mình do hiệu năng cao của nó cho khối lượng công việc đó (và sử dụng ext4 cho hệ thống tập tin gốc).

Các tính năng hiệu năng then chốt, bao gồm cả những tính năng được thêm vào kể từ khi phát hành, là:
- **Allocation Groups (Các nhóm cấp phát):** Phân vùng được chia thành các allocation groups (AG) có kích thước bằng nhau có thể được truy cập song song. Để giới hạn sự tranh chấp, các metadata chẳng hạn như các inodes và danh sách khối trống của mỗi AG được quản lý độc lập, trong khi các tập tin và thư mục có thể trải dài qua các AG.
- **Extents:** (Xem mô tả trước đó trong ext4.)
- **Journalling:** Journaling cải thiện hiệu năng khởi động sau khi hệ thống bị sập, tránh việc phải chạy fsck(8). Nó cũng có thể cải thiện hiệu năng của một số khối lượng công việc ghi bằng cách kết hợp các lệnh ghi metadata.
- **Journal device:** Một thiết bị journal bên ngoài có thể được sử dụng, để khối lượng công việc của journal không tranh chấp với khối lượng công việc dữ liệu.
- **Striped allocation (Cấp phát dạng sọc):** Nếu hệ thống tập tin được tạo trên một thiết bị RAID sọc hoặc LVM, một đơn vị sọc (stripe unit) cho dữ liệu và journal có thể được cung cấp để đảm bảo các việc cấp phát dữ liệu được tối ưu hóa cho phần cứng cơ sở.
- **Trì hoãn cấp phát:** Việc cấp phát Extent được trì hoãn cho đến khi dữ liệu được flush xuống đĩa, cho phép các lệnh ghi được nhóm lại và giảm sự phân mảnh. Các khối được dành riêng cho các tập tin trong bộ nhớ sao cho có không gian sẵn sàng khi quá trình flush diễn ra.
- **Chống phân mảnh trực tuyến (Online defragmentation):** XFS cung cấp một công cụ defrag có thể vận hành trên một hệ thống tập tin trong khi đang được sử dụng tích cực. Trong khi XFS sử dụng extents và trì hoãn cấp phát để ngăn chặn sự phân mảnh, các khối lượng công việc và điều kiện nhất định vẫn có thể làm phân mảnh hệ thống tập tin.

Các tính năng có thể cấu hình được tài liệu hóa trong trang man mkfs.xfs(8). Dữ liệu hiệu năng nội bộ cho XFS có thể được thấy qua /prov/fs/xfs/stat. Dữ liệu này được thiết kế cho việc phân tích nâng cao: để biết thêm thông tin, hãy xem trang web XFS [XFS 06][XFS 10].

**ZFS**
ZFS được phát triển bởi Sun Microsystems và được phát hành vào năm 2005, kết hợp hệ thống tập tin với volume manager và bao gồm nhiều tính năng doanh nghiệp, khiến nó trở thành một lựa chọn hấp dẫn cho các máy chủ tập tin (filers). ZFS được phát hành dưới dạng mã nguồn mở và đang được sử dụng bởi một vài hệ điều hành, mặc dù thường là một phần bổ sung vì ZFS sử dụng giấy phép CDDL. Hầu hết quá trình phát triển đang diễn ra trong dự án OpenZFS, thứ mà vào năm 2019 đã công bố hỗ trợ cho Linux như là hệ điều hành chính [Ahrens 19]. Trong khi nó đang thấy được sự hỗ trợ và sử dụng ngày càng tăng trong Linux, vẫn có sự phản đối do giấy phép nguồn, bao gồm cả từ Linus Torvalds [Torvalds 20a].

Các tính năng hiệu năng ZFS then chốt, bao gồm cả những tính năng được thêm vào kể từ khi phát hành, là:
- **Pooled storage (Lưu trữ dạng pool):** Tất cả các thiết bị lưu trữ được gán đều được đặt trong một pool, từ đó các hệ thống tập tin được tạo ra. Điều này cho phép tất cả các thiết bị được sử dụng song song để đạt được thông lượng và IOPS tối đa. Các loại RAID khác nhau có thể được sử dụng: 0, 1, 10, Z (dựa trên RAID-5), Z2 (double-parity), và Z3 (triple-parity).
- **COW:** Sao chép các khối đã sửa đổi, sau đó nhóm và ghi chúng một cách tuần tự.
- **Logging:** ZFS flush các transaction groups (TXGs) của các thay đổi theo các lô (batches), thứ thành công hoặc thất bại như một khối nguyên vẹn sao cho định dạng trên đĩa luôn là nhất quán.
- **ARC:** Adaptive Replacement Cache đạt được tỷ lệ trúng bộ đệm cao bằng cách sử dụng nhiều thuật toán cache cùng lúc: most recently used (MRU) và most frequently used (MFU). Bộ nhớ chính được cân bằng giữa chúng dựa trên hiệu năng của chúng, thứ được biết đến bằng cách duy trì các siêu dữ liệu bổ sung (ghost lists) để xem mỗi thuật toán sẽ thực hiện như thế nào nếu nó chiếm giữ toàn bộ bộ nhớ chính.
- **Intelligent prefetch:** ZFS áp dụng các loại prefetch khác nhau khi thích hợp: cho siêu dữ liệu, cho znodes (nội dung tập tin), và cho vdevs (các thiết bị ảo).
- **Multiple prefetch streams:** Nhiều trình đọc truyền phát trên một tập tin có thể tạo ra một khối lượng công việc I/O ngẫu nhiên khi hệ thống tập tin seek giữa chúng. ZFS theo dõi các dòng prefetch riêng lẻ, cho phép các dòng mới tham gia cùng chúng.
- **Snapshots:** Do kiến trúc COW, các snapshots có thể được tạo ra gần như tức thời, trì hoãn việc sao chép các khối mới cho đến khi cần thiết.
- **ZIO pipeline:** I/O thiết bị được xử lý bởi một pipeline gồm các giai đoạn, mỗi giai đoạn được phục vụ bởi một pool gồm các luồng để cải thiện hiệu năng.
- **Nén:** Nhiều thuật toán được hỗ trợ, thứ thường làm giảm hiệu năng do chi phí CPU. Tùy chọn lzjb (Lempel-Ziv Jeff Bonwick) rất nhẹ và có thể cải thiện một phần hiệu năng lưu trữ bằng cách giảm tải I/O (vì nó được nén), với chi phí là một phần CPU.
- **SLOG:** ZFS separate intent log cho phép các lệnh ghi đồng bộ được ghi vào các thiết bị riêng biệt, tránh tranh chấp với khối lượng công việc của các đĩa trong pool. Các lệnh ghi vào SLOG chỉ được đọc trong trường hợp hệ thống gặp lỗi, để phát lại.
- **L2ARC:** Level 2 ARC là một tầng cache thứ hai sau bộ nhớ chính, để đệm các khối lượng công việc đọc ngẫu nhiên trên các ổ đĩa flash (SSDs). Nó không buffer các khối lượng công việc ghi, và chỉ chứa dữ liệu sạch đã tồn tại trên các đĩa lưu trữ của pool. Nó cũng có thể nhân bản dữ liệu trong ARC, sao cho hệ thống có thể khôi phục nhanh hơn trong trường hợp có sự nhiễu loạn flush bộ nhớ chính.
- **Khử trùng lặp dữ liệu (Data deduplication):** Một tính năng cấp hệ thống tập tin giúp tránh ghi lại nhiều bản sao của cùng một dữ liệu. Tính năng này có các tác động hiệu năng đáng kể, cả tốt (giảm I/O thiết bị) và xấu (khi bảng băm không còn khớp với bộ nhớ chính, I/O thiết bị trở nên bị thổi phồng, có lẽ là đáng kể). Phiên bản ban đầu chỉ dành cho các khối lượng công việc nơi bảng băm được kỳ vọng là sẽ luôn khớp trong bộ nhớ chính.

Có một hành vi của ZFS có thể làm giảm hiệu năng so với các hệ thống tập tin khác: theo mặc định, ZFS phát các lệnh flush cache tới các thiết bị lưu trữ, để đảm bảo rằng các lệnh ghi đã hoàn thành trong trường hợp mất điện. Đây là một trong các tính năng về tính toàn vẹn của ZFS; tuy nhiên, nó đi kèm với một chi phí: nó có thể gây ra độ trễ cho các thao tác ZFS phải chờ đợi đợt flush cache.

**btrfs**
B-tree file system (btrfs) dựa trên các cây B-tree copy-on-write. Đây là một kiến trúc kết hợp hệ thống tập tin và volume manager hiện đại, tương tự như ZFS, và được mong đợi cuối cùng sẽ cung cấp một bộ tính năng tương tự. Các tính năng hiện tại bao gồm lưu trữ dạng pool, dung lượng lớn, extents, COW, sự tăng trưởng và thu hẹp volume, các subvolumes, việc thêm và loại bỏ thiết bị khối, snapshots, clones, nén, và nhiều loại checksum khác nhau (bao gồm crc32c, xxhash64, sha256, và blake2b). Quá trình phát triển đã được bắt đầu bởi Oracle vào năm 2007.

Các tính năng hiệu năng then chốt bao gồm những điều sau:
- **Pooled storage:** Các thiết bị lưu trữ được đặt trong một volume kết hợp, từ đó các hệ thống tập tin được tạo ra. Điều này cho phép tất cả các thiết bị được sử dụng song song để đạt được thông lượng và IOPS tối đa. RAID 0, 1, và 10 có thể được sử dụng.
- **COW:** Nhóm và ghi dữ liệu một cách tuần tự.
- **Cân bằng trực tuyến (Online balancing):** Các đối tượng có thể được di chuyển giữa các thiết bị lưu trữ để cân bằng khối lượng công việc của chúng.
- **Extents:** Cải thiện bố cục tuần tự và hiệu năng.
- **Snapshots:** Do kiến trúc COW, các snapshots có thể được tạo ra gần như tức thời, trì hoãn việc sao chép các khối mới cho đến khi cần thiết.
- **Nén:** Hỗ trợ zlib và LZO.
- **Journaling:** Một cây nhật ký cho mỗi subvolume có thể được tạo ra để ghi nhật ký các khối lượng công việc COW đồng bộ.

Các tính năng liên quan đến hiệu năng được lên kế hoạch bao gồm RAID-5 và 6, RAID cấp đối tượng, các bản dump lũy tiến, và khử trùng lặp dữ liệu.

### 8.4.6 Các Volume và Pool
Trong lịch sử, các hệ thống tập tin được xây dựng trên một đĩa đơn hoặc một phân vùng đĩa. Các volume và pool cho phép các hệ thống tập tin được xây dựng trên nhiều đĩa và có thể được cấu hình bằng các chiến lược RAID khác nhau (xem Chương 9, Các đĩa).

(Hình 8.11 Các Volume và Pool)

Các Volume trình diễn nhiều đĩa như là một đĩa ảo duy nhất, trên đó hệ thống tập tin được xây dựng. Khi được xây dựng trên toàn bộ các đĩa (chứ không phải các lát hoặc phân vùng), các volume cô lập các khối lượng công việc, làm giảm các vấn đề hiệu năng do tranh chấp.

Phần mềm quản lý Volume bao gồm Logical Volume Manager (LVM) cho các hệ thống dựa trên Linux. Các Volume, hay các đĩa ảo, cũng có thể được cung cấp bởi các bộ điều khiển RAID phần cứng.

Pooled storage bao gồm nhiều đĩa trong một pool lưu trữ, từ đó nhiều hệ thống tập tin có thể được tạo ra. Điều này được trình bày trong Hình 8.11 với các volume để so sánh. Pooled storage linh hoạt hơn so với lưu trữ dạng volume, vì các hệ thống tập tin có thể lớn lên và thu nhỏ lại bất kể các thiết bị cơ sở. Cách tiếp cận này được sử dụng bởi các hệ thống tập tin hiện đại, bao gồm ZFS và btrfs, và cũng có thể thực hiện được bằng cách sử dụng LVM.

Pooled storage có thể sử dụng tất cả các thiết bị đĩa cho tất cả các hệ thống tập tin, cải thiện hiệu năng. Các khối lượng công việc không bị cô lập; trong một số trường hợp, nhiều pool có thể được sử dụng để phân tách các khối lượng công việc, với sự đánh đổi về tính linh hoạt, vì các thiết bị đĩa phải được đặt ban đầu trong pool này hoặc pool kia. Lưu ý rằng các đĩa trong pool có thể khác nhau về loại và kích thước, trong khi các volume có thể bị hạn chế trong các đĩa đồng nhất trong một volume.

Các cân nhắc hiệu năng bổ sung khi sử dụng cả phần mềm quản lý volume hoặc pooled storage bao gồm những điều sau:
- **Stripe width (Độ rộng sọc):** Khớp điều này với khối lượng công việc.
- **Khả năng quan sát (Observability):** Việc sử dụng thiết bị ảo có thể gây nhầm lẫn; hãy kiểm tra các thiết bị vật lý riêng biệt.
- **Chi phí CPU:** Đặc biệt là khi thực hiện tính toán RAID parity. Điều này đã trở nên ít vấn đề hơn với các CPU hiện đại, nhanh hơn. (Tính toán Parity cũng có thể được dời sang các bộ điều khiển RAID phần cứng.)
- **Rebuilding:** Còn được gọi là resilvering, đây là khi một đĩa trống được thêm vào một nhóm RAID (ví dụ: thay thế một đĩa bị hỏng) và nó được điền đầy bằng các dữ liệu cần thiết để gia nhập nhóm. Điều này có thể ảnh hưởng đáng kể đến hiệu năng vì nó tiêu tốn tài nguyên I/O và có thể kéo dài hàng giờ hoặc thậm chí hàng ngày.

Việc Rebuilding là một vấn đề ngày càng tồi tệ, vì dung lượng của các thiết bị lưu trữ tăng nhanh hơn thông lượng của chúng, làm tăng thời gian xây dựng lại, và khiến rủi ro của một lỗi hoặc các lỗi môi trường (medium errors) trong quá trình rebuild trở nên lớn hơn. Khi có thể, việc rebuild ngoại tuyến cho các ổ đĩa không được mount có thể cải thiện thời gian xây dựng lại.

---

## 8.5 Phương pháp luận (Methodology)
Phần này mô tả các phương pháp luận và các bài tập khác nhau cho việc phân tích và tinh chỉnh hệ thống tập tin. Các chủ đề được tóm tắt trong Bảng 8.3.

Bảng 8.3 Các phương pháp luận hiệu năng hệ thống tập tin
| Mục | Phương pháp luận | Các loại |
| --- | --- | --- |
| 8.5.1 | Phân tích đĩa | Phân tích quan sát |
| 8.5.2 | Phân tích độ trễ | Phân tích quan sát |
| 8.5.3 | Đặc tính hóa khối lượng công việc | Phân tích quan sát, quy hoạch dung lượng |
| 8.5.4 | Giám sát hiệu năng | Phân tích quan sát, quy hoạch dung lượng |
| 8.5.5 | Tinh chỉnh hiệu năng tĩnh | Phân tích quan sát, quy hoạch dung lượng |
| 8.5.6 | Tinh chỉnh bộ đệm | Phân tích quan sát, tinh chỉnh |
| 8.5.7 | Cô lập khối lượng công việc | Tinh chỉnh |
| 8.5.8 | Kiểm thử vi mô | Phân tích thực nghiệm |

Xem Chương 2, Các phương pháp luận, để biết thêm về các chiến lược và phần giới thiệu về nhiều nội dung trong số này.

Những điều này có thể được thực hiện riêng lẻ hoặc được sử dụng kết hợp. Gợi ý của tôi là sử dụng các chiến lược sau để bắt đầu, theo thứ tự này: phân tích độ trễ, giám sát hiệu năng, đặc tính hóa khối lượng công việc, kiểm thử vi mô, và tinh chỉnh hiệu năng tĩnh. Bạn có thể đưa ra một sự kết hợp và thứ tự khác hoạt động tốt nhất trong môi trường của mình.

Mục 8.6, Các Công cụ Quan trắc, chỉ ra các công cụ hệ điều hành để áp dụng các phương pháp này.

### 8.5.1 Phân tích Đĩa (Disk Analysis)
Một chiến lược khắc phục sự cố phổ biến là bỏ qua hệ thống tập tin và thay vào đó tập trung vào hiệu năng đĩa. Điều này giả định rằng I/O tệ nhất là I/O đĩa, vì vậy bằng cách chỉ phân tích các đĩa, bạn đã tập trung một cách thuận tiện vào nguồn gốc dự kiến của các vấn đề.

Với các hệ thống tập tin đơn giản hơn và các bộ đệm nhỏ hơn, điều này nói chung đã hoạt động tốt. Ngày nay, cách tiếp cận này trở nên gây nhầm lẫn và bỏ lỡ toàn bộ các lớp vấn đề (xem Mục 8.3.12, I/O Logic so với Vật lý).

### 8.5.2 Phân tích Độ trễ (Latency Analysis)
Để phân tích độ trễ, hãy bắt đầu bằng việc đo lường độ trễ của các thao tác hệ thống tập tin. Điều này nên bao gồm tất cả các thao tác đối tượng, không chỉ I/O (ví dụ: bao gồm cả sync(2)).

```
độ trễ thao tác = thời gian (hoàn thành thao tác) - thời gian (yêu cầu thao tác)
```

Các mốc thời gian này có thể được đo lường từ một trong bốn tầng, như được trình bày trong Bảng 8.4.

Bảng 8.4 Các mục tiêu (các tầng) để phân tích độ trễ hệ thống tập tin
| Tầng | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| Ứng dụng | Phép đo sát nhất về ảnh hưởng của độ trễ hệ thống tập tin lên ứng dụng; cũng có thể kiểm tra ngữ cảnh ứng dụng để xác định liệu độ trễ đang xảy ra trong chức năng chính của ứng dụng, hay nó là bất đồng bộ. | Kỹ thuật thay đổi giữa các ứng dụng và các phiên bản phần mềm ứng dụng. |
| Giao diện Syscall | Giao diện được tài liệu hóa tốt. Thường có thể quan sát được thông qua các công cụ hệ điều hành và truy vết tĩnh. | Syscalls ghi nhận tất cả các loại hệ thống tập tin, bao gồm cả các hệ thống tập tin không lưu trữ (thống kê, sockets), thứ có thể gây nhầm lẫn trừ khi được lọc. Thêm vào sự nhầm lẫn đó, cũng có thể có nhiều syscalls cho cùng một chức năng hệ thống tập tin. Ví dụ, cho read, có thể có read(2), pread64(2), preadv(2), preadv2(2), v.v., tất cả đều cần được đo lường. |
| VFS | Giao diện chuẩn cho tất cả các hệ thống tập tin; một lần gọi cho các thao tác hệ thống tập tin (ví dụ: vfs_write()) | VFS truy vết tất cả các loại hệ thống tập tin, bao gồm cả các hệ thống tập tin không lưu trữ, thứ có thể gây nhầm lẫn trừ khi được lọc. |
| Đỉnh của hệ thống tập tin | Chỉ truy vết loại hệ thống tập tin mục tiêu; một số ngữ cảnh nội bộ hệ thống tập tin cho các chi tiết mở rộng. | Đặc thù cho hệ thống tập tin; kỹ thuật truy vết có thể thay đổi giữa các phiên bản phần mềm hệ thống tập tin (mặc dù hệ thống tập tin có thể có một giao diện dạng VFS ánh xạ tới VFS, và vì vậy không thay đổi thường xuyên). |

Việc chọn tầng có thể phụ thuộc vào sự sẵn có của công cụ. Hãy kiểm tra các nguồn sau:
- **Tài liệu ứng dụng:** Một số ứng dụng đã cung cấp sẵn các chỉ số độ trễ hệ thống tập tin, hoặc khả năng cho phép thu thập chúng.
- **Các công cụ hệ điều hành:** Các hệ điều hành cũng có thể cung cấp các chỉ số, lý tưởng nhất là các thống kê riêng biệt cho mỗi hệ thống tập tin hoặc ứng dụng.
- **Instrumentation động:** Nếu hệ thống của bạn có instrumentation động (Linux kprobes và uprobes, được sử dụng bởi các trình truy vết khác nhau), tất cả các tầng có thể được kiểm tra thông qua các chương trình truy vết tùy chỉnh, mà không cần khởi động lại bất cứ thứ gì.

Độ trễ có thể được trình bày dưới dạng trung bình cho mỗi khoảng thời gian, các phân phối (ví dụ: các biểu đồ histogram hoặc các bản đồ nhiệt: xem Mục 8.6.18), hoặc dưới dạng một danh sách mọi thao tác và độ trễ của nó. Đối với các hệ thống tập tin có tỷ lệ trúng bộ đệm cao (trên 99%), các giá trị trung bình cho mỗi khoảng thời gian có thể bị chiếm ưu thế bởi độ trễ trúng bộ đệm. Điều này có thể không may mắn khi có các trường hợp độ trễ cao bị cô lập (ngoại lai) thứ quan trọng để xác định nhưng khó nhìn thấy từ một giá trị trung bình. Việc kiểm tra toàn bộ các phân phối hoặc độ trễ cho mỗi thao tác cho phép các giá trị ngoại lai như vậy được điều tra, cùng với ảnh hưởng của các bậc độ trễ khác nhau, bao gồm các lần trúng và trượt bộ đệm hệ thống tập tin.

Khi đã tìm thấy độ trễ cao, hãy tiếp tục với phân tích đào sâu (drill-down) vào hệ thống tập tin để xác định nguồn gốc.

**Chi phí Giao dịch (Transaction Cost)**
Một cách khác để trình bày độ trễ hệ thống tập tin là tổng thời gian dành cho việc chờ đợi trên hệ thống tập tin trong một giao dịch ứng dụng (ví dụ: một truy vấn cơ sở dữ liệu):

```
phần trăm thời gian trong hệ thống tập tin = 100 * tổng độ trễ hệ thống tập tin chặn / thời gian giao dịch ứng dụng
```

Điều này cho phép chi phí của các thao tác hệ thống tập tin được định lượng xét theo hiệu năng ứng dụng, và các cải tiến hiệu năng được dự đoán. Chỉ số này có thể được trình bày dưới dạng giá trị trung bình cho tất cả các giao dịch trong một khoảng thời gian, hoặc cho các giao dịch riêng lẻ.

Hình 8.12 trình bày thời gian dành cho một luồng ứng dụng đang phục vụ một giao dịch. Giao dịch này phát ra một lệnh đọc hệ thống tập tin duy nhất; ứng dụng bị chặn và chờ sự hoàn thành của nó, chuyển sang trạng thái off-CPU. Tổng thời gian bị chặn trong trường hợp này là thời gian cho lệnh đọc hệ thống tập tin duy nhất đó. Nếu nhiều I/O bị chặn được gọi trong một giao dịch, tổng thời gian là tổng của chúng.

(Hình 8.12 Độ trễ ứng dụng và hệ thống tập tin)

Như một ví dụ cụ thể, một giao dịch ứng dụng mất 200 ms, trong thời gian đó nó chờ đợi tổng cộng 180 ms cho nhiều I/O hệ thống tập tin. Thời gian mà ứng dụng bị chặn bởi hệ thống tập tin là 90% (100 * 180 ms / 200 ms). Việc loại bỏ độ trễ hệ thống tập tin có thể cải thiện hiệu năng lên đến 10 lần.

Như một ví dụ khác, nếu một giao dịch ứng dụng mất 200 ms, trong đó chỉ có 2 ms được dành cho hệ thống tập tin, thì hệ thống tập tin—và toàn bộ I/O stack đĩa—chỉ đóng góp 1% vào thời gian chạy giao dịch. Kết quả này vô cùng hữu ích, vì nó có thể hướng quá trình điều tra hiệu năng sang nguồn gốc thực sự của độ trễ.

Nếu ứng dụng phát I/O dưới dạng non-blocking, ứng dụng có thể tiếp tục thực thi on-CPU trong khi hệ thống tập tin phản hồi. Trong trường hợp này, độ trễ hệ thống tập tin chặn chỉ đo lường thời gian ứng dụng bị chặn off-CPU.

### 8.5.3 Đặc tính hóa Khối lượng công việc (Workload Characterization)
Đặc tính hóa tải được áp dụng là một bài tập quan trọng khi quy hoạch dung lượng, benchmarking, và mô phỏng khối lượng công việc. Nó cũng có thể dẫn đến một số cải thiện hiệu năng lớn nhất bằng cách xác định các công việc không cần thiết có thể được loại bỏ.

Dưới đây là các thuộc tính cơ bản đặc tính hóa khối lượng công việc hệ thống tập tin:
- Tốc độ thao tác và các loại thao tác.
- Thông lượng I/O tập tin.
- Kích thước I/O tập tin.
- Tỷ lệ đọc/ghi.
- Tỷ lệ ghi đồng bộ.
- Truy cập offset tập tin ngẫu nhiên so với tuần tự.

Tốc độ thao tác và thông lượng được định nghĩa trong Mục 8.1, Thuật ngữ. Ghi đồng bộ và ngẫu nhiên so với tuần tự đã được mô tả trong Mục 8.3, Các khái niệm.

Các đặc tính này có thể thay đổi theo từng giây, đặc biệt đối với các tác vụ ứng dụng được định thời thực thi theo các khoảng thời gian. Để đặc tính hóa khối lượng công việc tốt hơn, hãy thu thập các giá trị tối đa cũng như các giá trị trung bình. Tốt hơn nữa, hãy kiểm tra toàn bộ phân phối các giá trị theo thời gian.

Dưới đây là một mô tả khối lượng công việc ví dụ, để chỉ ra cách các thuộc tính này có thể được diễn đạt cùng nhau:

> Trên một cơ sở dữ liệu giao dịch tài chính, hệ thống tập tin có một khối lượng công việc đọc ngẫu nhiên, trung bình 18,000 lần đọc/giây với kích thước đọc trung bình là 4 Kbyte. Tổng tốc độ thao tác là 21,000 ops/giây, bao gồm các lệnh đọc, stats, opens, closes, và khoảng 200 lần ghi đồng bộ/giây. Tốc độ ghi ổn định trong khi tốc độ đọc thay đổi, lên đến đỉnh điểm là 39,000 lần đọc/giây.

Các đặc tính này có thể được mô tả xét theo một thực thể hệ thống tập tin duy nhất, hoặc tất cả các thực thể trên một hệ thống cùng loại.

**Đặc tính hóa Khối lượng công việc Nâng cao / Checklist**
Các chi tiết bổ sung có thể được bao gồm để đặc tính hóa khối lượng công việc. Những điều này đã được liệt kê ở đây như là các câu hỏi để cân nhắc, thứ cũng có thể phục vụ như một checklist khi nghiên cứu các vấn đề hệ thống tập tin một cách thấu đáo:
- Tỷ lệ trúng bộ đệm hệ thống tập tin là bao nhiêu? Tốc độ trượt (miss rate)?
- Dung lượng bộ đệm hệ thống tập tin và mức sử dụng hiện tại là bao nhiêu?
- Những bộ đệm nào khác hiện diện (thư mục, inode, buffer), và các thống kê của chúng là gì?
- Có bất kỳ nỗ lực nào đã được thực hiện để tinh chỉnh hệ thống tập tin trong quá khứ không? Có bất kỳ tham số hệ thống tập tin nào được thiết lập các giá trị khác với mặc định của chúng không?
- Những ứng dụng hoặc người dùng nào đang sử dụng hệ thống tập tin?
- Những tập tin và thư mục nào đang được truy cập? Được tạo và xóa?
- Có bất kỳ lỗi nào gặp phải không? Điều này là do các yêu cầu không hợp lệ, hay các vấn đề từ hệ thống tập tin?
- Tại sao I/O hệ thống tập tin được phát ra (đường dẫn lệnh gọi mức người dùng)?
- Ở mức độ nào các ứng dụng trực tiếp (đồng bộ) yêu cầu I/O hệ thống tập tin?
- Phân phối các thời điểm I/O đến là gì?

Nhiều câu hỏi trong số này có thể được đặt ra cho mỗi ứng dụng hoặc mỗi tập tin. Bất kỳ câu hỏi nào cũng có thể được kiểm tra theo thời gian, để tìm kiếm các giá trị tối đa, tối thiểu, và các biến đổi dựa trên thời gian. Đồng thời hãy xem Mục 2.5.10, Đặc tính hóa khối lượng công việc, trong Chương 2, Phương pháp luận, thứ cung cấp một bản tóm tắt cấp cao hơn về các đặc tính cần đo lường (ai, tại sao, cái gì, như thế nào).

**Đặc tính hóa Hiệu năng (Performance Characterization)**
Các danh sách đặc tính hóa khối lượng công việc trước đó kiểm tra khối lượng công việc được áp dụng. Phần sau đây kiểm tra hiệu năng kết quả:
- Độ trễ thao tác hệ thống tập tin trung bình là bao nhiêu?
- Có bất kỳ giá trị ngoại lai độ trễ cao nào không?
- Phân phối đầy đủ của độ trễ thao tác là gì?
- Các kiểm soát tài nguyên hệ thống cho hệ thống tập tin hoặc I/O đĩa có hiện diện và đang hoạt động không?

Ba câu hỏi đầu tiên có thể được đặt ra cho mỗi loại thao tác một cách riêng biệt.

**Truy vết Sự kiện (Event Tracing)**
Các công cụ truy vết có thể được sử dụng để ghi lại tất cả các thao tác hệ thống tập tin và các chi tiết vào một bản log để phân tích sau này. Điều này có thể bao gồm loại thao tác, các đối số thao tác, tên đường dẫn tập tin, các dấu thời gian bắt đầu và kết thúc, trạng thái hoàn thành, và ID cùng tên tiến trình, cho mọi I/O. Mặc dù đây có thể là công cụ tối thượng cho việc đặc tính hóa khối lượng công việc, nhưng trên thực tế nó có thể tiêu tốn chi phí đáng kể do tốc độ của các thao tác hệ thống tập tin, thường khiến nó trở nên không thực tế trừ khi được lọc mạnh mẽ (ví dụ: chỉ bao gồm các I/O chậm trong bản log: xem công cụ ext4slower(8) trong Mục 8.6.14).

### 8.5.4 Giám sát Hiệu năng (Performance Monitoring)
Giám sát hiệu năng có thể xác định các vấn đề đang hoạt động và các mô hình hành vi theo thời gian. Các chỉ số then chốt cho hiệu năng hệ thống tập tin là:
- Tốc độ thao tác (Operation rate)
- Độ trễ thao tác (Operation latency)

Tốc độ thao tác là đặc tính cơ bản nhất của khối lượng công việc được áp dụng, và độ trễ là hiệu năng kết quả. Giá trị cho độ trễ bình thường hoặc tệ phụ thuộc vào khối lượng công việc, môi trường và các yêu cầu về độ trễ của bạn. Nếu bạn không chắc chắn, có thể thực hiện các micro-benchmarks của khối lượng công việc đã biết là tốt so với khối lượng công việc tệ để điều tra độ trễ (ví dụ: các khối lượng công việc thường trúng bộ đệm hệ thống tập tin so với những khối lượng công việc thường trượt). Xem Mục 8.7, Thực nghiệm.

Chỉ số độ trễ thao tác có thể được giám sát dưới dạng trung bình cho mỗi giây, và có thể bao gồm các giá trị khác chẳng hạn như tối đa và độ lệch chuẩn. Lý tưởng nhất là có thể kiểm tra toàn bộ phân phối của độ trễ, ví dụ bằng cách sử dụng một biểu đồ histogram hoặc bản đồ nhiệt, để tìm kiếm các giá trị ngoại lai và các mô hình khác.

Cả tốc độ và độ trễ cũng có thể được ghi lại cho mỗi loại thao tác (đọc, ghi, stat, mở, đóng, v.v.). Việc thực hiện điều này sẽ giúp ích rất nhiều cho các cuộc điều tra về sự thay đổi khối lượng công việc và hiệu năng, bằng cách xác định các sự khác biệt trong các loại thao tác cụ thể.

Đối với các hệ thống áp đặt các kiểm soát tài nguyên dựa trên hệ thống tập tin, các thống kê có thể được bao gồm để chỉ ra liệu và khi nào việc điều tiết (throttling) được sử dụng.

Thật không may, trong Linux thường không có sẵn các thống kê cho các thao tác hệ thống tập tin (các ngoại lệ bao gồm, đối với NFS, thông qua nfsstat(8)).

### 8.5.5 Tinh chỉnh Hiệu năng Tĩnh (Static Performance Tuning)
Tinh chỉnh hiệu năng tĩnh tập trung vào các vấn đề của môi trường đã cấu hình. Đối với hiệu năng hệ thống tập tin, hãy kiểm tra các khía cạnh sau của cấu hình tĩnh:
- Có bao nhiêu hệ thống tập tin được mount và đang hoạt động tích cực?
- Kích thước bản ghi (record size) của hệ thống tập tin là bao nhiêu?
- Các dấu thời gian truy cập có được bật không?
- Những tùy chọn hệ thống tập tin nào khác được bật (nén, mã hóa...)?
- Bộ đệm hệ thống tập tin đã được cấu hình như thế nào? Kích thước tối đa?
- Các bộ đệm khác (thư mục, inode, buffer) đã được cấu hình như thế nào?
- Có bộ đệm tầng thứ hai hiện diện và đang được sử dụng không?
- Có bao nhiêu thiết bị lưu trữ hiện diện và đang được sử dụng?
- Cấu hình thiết bị lưu trữ là gì? RAID?
- Những loại hệ thống tập tin nào được sử dụng?
- Phiên bản của hệ thống tập tin (hoặc kernel) là gì?
- Có các lỗi/bản vá hệ thống tập tin nào cần được xem xét không?
- Có các kiểm soát tài nguyên nào đang được sử dụng cho I/O hệ thống tập tin không?

Việc trả lời các câu hỏi này có thể tiết lộ các lựa chọn cấu hình đã bị bỏ qua. Đôi khi một hệ thống đã được cấu hình cho một khối lượng công việc, và sau đó được chuyển mục đích sử dụng cho một khối lượng công việc khác. Phương pháp này sẽ nhắc nhở bạn xem xét lại những lựa chọn đó.

### 8.5.6 Tinh chỉnh Bộ đệm (Cache Tuning)
Kernel và hệ thống tập tin có thể sử dụng nhiều bộ đệm khác nhau, bao gồm buffer cache, directory cache, inode cache, và file system (page) cache. Các bộ đệm khác nhau đã được mô tả trong Mục 8.4, Kiến trúc. Những thứ này có thể được kiểm tra và thường xuyên được tinh chỉnh, tùy thuộc vào các tùy chọn tinh chỉnh có sẵn.

### 8.5.7 Cô lập Khối lượng công việc (Workload Separation)
Một số loại khối lượng công việc thực hiện tốt hơn khi được cấu hình để sử dụng các hệ thống tập tin và các thiết bị đĩa độc quyền của riêng chúng. Cách tiếp cận này được gọi là sử dụng "các trục quay riêng biệt" (separate spindles), vì việc tạo ra I/O ngẫu nhiên bằng cách di chuyển đầu đọc giữa hai vị trí khối lượng công việc khác nhau là đặc biệt tệ cho các đĩa quay (xem Chương 9, Các đĩa).

Ví dụ, một cơ sở dữ liệu có thể được hưởng lợi từ việc có các hệ thống tập tin và đĩa riêng biệt cho các tập tin nhật ký (log files) và các tập tin cơ sở dữ liệu của nó. Hướng dẫn cài đặt cho cơ sở dữ liệu thường chứa các lời khuyên về việc đặt các kho lưu trữ dữ liệu của nó.

### 8.5.8 Kiểm thử vi mô (Micro-Benchmarking)
Các công cụ benchmark cho việc benchmark hệ thống tập tin và đĩa (trong đó có rất nhiều công cụ) có thể được sử dụng để kiểm tra hiệu năng của các loại hệ thống tập tin khác nhau hoặc các thiết lập trong một hệ thống tập tin, cho các khối lượng công việc nhất định. Các yếu tố điển hình có thể được kiểm tra bao gồm:
- Các loại thao tác: Tốc độ các lệnh đọc, ghi, và các thao tác hệ thống tập tin khác.
- Kích thước I/O: 1 byte lên đến 1 Mbyte và lớn hơn.
- Mẫu offset tập tin: Ngẫu nhiên hoặc tuần tự.
- Mẫu truy cập ngẫu nhiên: Đồng nhất, ngẫu nhiên, hoặc phân phối Pareto.
- Loại ghi: Bất đồng bộ hoặc đồng bộ (O_SYNC).
- Kích thước tập làm việc (Working set size): Mức độ phù hợp với bộ đệm hệ thống tập tin.
- Tính song song (Concurrency): Số lượng I/O song song hoặc số lượng luồng thực hiện I/O.
- Ánh xạ bộ nhớ (Memory mapping): Truy cập tập tin qua mmap(2), thay vì read(2)/write(2).
- Trạng thái bộ đệm: Liệu bộ đệm hệ thống tập tin là "lạnh" (chưa được điền đầy) hay "ấm".
- Các tunables hệ thống tập tin: Có thể bao gồm nén, khử trùng lặp dữ liệu, và vân vân.

Các sự kết hợp phổ biến bao gồm đọc ngẫu nhiên, đọc tuần tự, ghi ngẫu nhiên, và ghi tuần tự. Tôi đã không bao gồm direct I/O trong danh sách này, vì mục đích của nó với micro-benchmarking là để bỏ qua hệ thống tập tin và kiểm tra hiệu năng thiết bị đĩa (xem Chương 9, Các đĩa).

Một yếu tố quan trọng khi micro-benchmarking các hệ thống tập tin là kích thước tập làm việc (WSS): khối lượng dữ liệu được truy cập. Tùy thuộc vào benchmark, đây có thể là tổng kích thước của các tập tin đang được sử dụng. Một kích thước tập làm việc nhỏ có thể trả về hoàn toàn từ bộ đệm hệ thống tập tin trong bộ nhớ chính (DRAM), trừ khi cờ direct I/O được sử dụng. Một kích thước tập làm việc lớn có thể trả về chủ yếu từ các thiết bị lưu trữ (đĩa). Sự khác biệt về hiệu năng có thể lên đến nhiều bậc độ lớn. Việc chạy một benchmark chống lại một hệ thống tập tin mới được mount và sau đó chạy lần thứ hai sau khi bộ đệm đã được điền đầy và so sánh kết quả của hai lần chạy thường là một minh họa tốt về WSS. (Đồng thời xem Mục 8.7.3, Xóa trống bộ đệm.)

Hãy xem xét các kỳ vọng chung cho các benchmark khác nhau, bao gồm tổng kích thước của các tập tin (WSS), trong Bảng 8.5.

Bảng 8.5 Các kỳ vọng benchmark hệ thống tập tin
| Bộ nhớ hệ thống | Tổng kích thước tập tin (WSS) | Benchmark | Kỳ vọng |
| --- | --- | --- | --- |
| 128 Gbyte | 10 Gbyte | Đọc ngẫu nhiên | 100% cache hits |
| 128 Gbyte | 10 Gbyte | Đọc ngẫu nhiên, direct I/O | 100% lệnh đọc đĩa (do direct I/O) |
| 128 Gbyte | 1,000 Gbyte | Đọc ngẫu nhiên | Chủ yếu là các lệnh đọc đĩa, với ~12% cache hits |
| 128 Gbyte | 10 Gbyte | Đọc tuần tự | 100% cache hits |
| 128 Gbyte | 1,000 Gbyte | Đọc tuần tự | Sự kết hợp của cache hits (hầu hết do prefetch) và các lệnh đọc đĩa |
| 128 Gbyte | 10 Gbyte | Các lệnh ghi được buffer | Chủ yếu là cache hits (buffering), với một số lần bị chặn khi ghi tùy thuộc vào hành vi hệ thống tập tin |
| 128 Gbyte | 10 Gbyte | Các lệnh ghi đồng bộ | 100% lệnh ghi đĩa |

Một số công cụ benchmark hệ thống tập tin không làm rõ những gì họ đang kiểm tra, và có thể hàm ý một benchmark đĩa nhưng lại sử dụng một tổng kích thước tập tin nhỏ, thứ trả về hoàn toàn từ bộ đệm và vì thế không kiểm tra các đĩa. Xem Mục 8.3.12, I/O Logic so với Vật lý, để hiểu sự khác biệt giữa việc kiểm tra hệ thống tập tin (I/O logic) và kiểm tra các đĩa (I/O vật lý).

Một số công cụ benchmark đĩa hoạt động thông qua hệ thống tập tin bằng cách sử dụng direct I/O để tránh caching và buffering. Hệ thống tập tin vẫn đóng một vai trò nhỏ, thêm các chi phí đường dẫn mã và các khác biệt ánh xạ giữa việc đặt tập tin và đặt trên đĩa.

Xem Chương 12, Benchmarking, để biết thêm về chủ đề chung này.

---

## 8.6 Các Công cụ Quan trắc (Observability Tools)
Phần này giới thiệu các công cụ quan sát hệ thống tập tin cho các hệ điều hành dựa trên Linux. Hãy xem phần trước để biết các chiến lược cần tuân theo khi sử dụng những công cụ này.

Các công cụ trong phần này được liệt kê trong Bảng 8.6.

Bảng 8.6 Các công cụ quan sát hệ thống tập tin
| Mục | Công cụ | Mô tả |
| --- | --- | --- |
| 8.6.1 | mount | Liệt kê các hệ thống tập tin và các cờ mount của chúng |
| 8.6.2 | free | Các thống kê dung lượng bộ đệm |
| 8.6.3 | top | Bao gồm tóm tắt sử dụng bộ nhớ |
| 8.6.4 | vmstat | Thống kê bộ nhớ ảo |
| 8.6.5 | sar | Các thống kê đa dạng, bao gồm cả lịch sử |
| 8.6.6 | slabtop | Thống kê bộ cấp phát slab của kernel |
| 8.6.7 | strace | Truy vết system call |
| 8.6.8 | fatrace | Truy vết các thao tác hệ thống tập tin sử dụng fanotify |
| 8.6.9 | latencytop | Hiển thị các nguồn gây độ trễ trên toàn hệ thống |
| 8.6.10 | opensnoop | Truy vết các tập tin đã được mở |
| 8.6.11 | filetop | Các tập tin hàng đầu đang được sử dụng theo IOPS và byte |
| 8.6.12 | cachestat | Thống kê bộ đệm trang (page cache) |
| 8.6.13 | ext4dist (xfs, zfs, btrfs, nfs) | Hiển thị phân phối độ trễ thao tác ext4 |
| 8.6.14 | ext4slower (xfs, zfs, btrfs, nfs) | Hiển thị các thao tác ext4 chậm |
| 8.6.15 | bpftrace | Truy vết hệ thống tập tin tùy chỉnh |

Đây là một sự lựa chọn các công cụ và khả năng để hỗ trợ Mục 8.5, Phương pháp luận. Nó bắt đầu với các công cụ truyền thống và sau đó bao gồm các công cụ dựa trên truy vết (tracing). Một số công cụ truyền thống có khả năng khả dụng trên các hệ điều hành dạng Unix khác nơi chúng bắt nguồn, bao gồm: mount(8), free(1), top(1), vmstat(8), và sar(1). Nhiều công cụ truy vết dựa trên BPF, và sử dụng các frontend BCC và bpftrace (Chương 15); chúng là: opensnoop(8), filetop(8), cachestat(8), ext4dist(8), và ext4slower(8).

Hãy xem tài liệu cho mỗi công cụ, bao gồm các trang man của nó, để biết đầy đủ các tham chiếu về các tính năng của nó.

### 8.6.1 mount
Lệnh mount(1) của Linux liệt kê các hệ thống tập tin đã được mount và các cờ mount của chúng:
```bash
$ mount
/dev/nvme0n1p1 on / type ext4 (rw,relatime,discard)
devtmpfs on /dev type devtmpfs (rw,relatime,size=986036k,nr_inodes=246509,mode=755)
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev)
[...]
```
Dòng đầu tiên chỉ ra rằng một hệ thống tập tin ext4 được lưu trữ trên /dev/nvme0n1p1 được mount trên /, với các cờ mount là rw, relatime, và discard. relatime là một tùy chọn cải thiện hiệu năng giúp giảm các cập nhật dấu thời gian truy cập inode, và chi phí I/O đĩa phát sinh, bằng cách chỉ cập nhật thời gian truy cập khi các thời gian sửa đổi (modify) hoặc thay đổi (change) cũng được cập nhật, hoặc nếu lần cập nhật cuối cùng đã cách đây hơn một ngày.

### 8.6.2 free
Lệnh free(1) của Linux hiển thị các thống kê bộ nhớ và swap. Hai lệnh sau đây hiển thị kết quả bình thường và kết quả rộng (-w), cả hai đều dưới dạng megabyte (-m):
```bash
$ free -m
              total        used        free      shared  buff/cache   available
Mem:           1950         568         163           0        1218        1187
Swap:             0           0           0
$ free -mw
              total        used        free      shared     buffers       cache   available
Mem:           1950         568         163           0          84        1133        1187
Swap:             0           0           0
```
Kết quả rộng hiển thị một cột buffers cho kích thước buffer cache, và một cột cache cho kích thước page cache. Kết quả mặc định kết hợp chúng thành buff/cache.

Một cột quan trọng là available (một sự bổ sung mới cho free(1)), thứ cho thấy lượng bộ nhớ thực sự khả dụng cho các ứng dụng mà không cần phải thực hiện swap. Nó tính đến cả bộ nhớ không thể được thu hồi ngay lập tức.

Các trường này cũng có thể được đọc từ /proc/meminfo, thứ cung cấp chúng dưới dạng kilobyte.

### 8.6.3 top
Một số phiên bản của lệnh top(1) bao gồm các chi tiết bộ đệm hệ thống tập tin. Những dòng này từ phiên bản Linux của top(1) bao gồm các thống kê buff/cache và available (avail Mem) được in bởi free(1):
```text
MiB Mem :   1950.0 total,    161.2 free,     570.3 used,    1218.6 buff/cache
MiB Swap:      0.0 total,      0.0 free,       0.0 used.    1185.9 avail Mem
```
Xem Chương 6, CPUs, để biết thêm về top(1).

### 8.6.4 vmstat
Lệnh vmstat(1), giống như top(1), cũng có thể bao gồm các chi tiết về bộ đệm hệ thống tập tin. Để biết thêm chi tiết về vmstat(1), hãy xem Chương 7, Bộ nhớ.

Phần sau đây chạy vmstat(1) với một khoảng thời gian là 1 để cung cấp các cập nhật mỗi giây:
```bash
$ vmstat 1
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0      0 167644  87032 1161112    0    0     7    14   14    1  4  2 90  0  5
 0  0      0 167636  87032 1161152    0    0     0     0  162  376  0  0 100 0  0
[...]
```
Cột buff hiển thị kích thước buffer cache, và cache hiển thị kích thước page cache, cả hai đều dưới dạng kilobyte.

### 8.6.5 sar
Trình báo cáo hoạt động hệ thống, sar(1), cung cấp các thống kê hệ thống tập tin đa dạng và có thể được cấu hình để ghi lại những thống kê này một cách định kỳ. sar(1) được đề cập trong các chương khác nhau trong cuốn sách này cho các thống kê khác nhau mà nó cung cấp, và được giới thiệu trong Mục 4.4, sar.

Thực thi sar(1) với khoảng thời gian một giây để báo cáo hoạt động hiện tại:
```bash
# sar -v 1
Linux 5.3.0-1009-aws (ip-10-1-239-218)    02/08/20    _x86_64_    (2 CPU)

21:20:24    dentunusd   file-nr  inode-nr    pty-nr
21:20:25        27027      1344     52945         2
21:20:26        27012      1312     52922         2
21:20:27        26997      1248     52899         2
[...]
```
Tùy chọn -v cung cấp các cột sau:
- **dentunusd:** Số lượng không sử dụng trong cache mục thư mục (các mục khả dụng).
- **file-nr:** Số lượng handle tập tin đang được sử dụng.
- **inode-nr:** Số lượng inode đang được sử dụng.
- **pty-nr:** Số lượng các terminal giả (pseudo-terminals) đang được sử dụng.

Cũng có một tùy chọn -r, thứ in các cột kbbuffers và kbcached cho các kích thước buffer cache và page cache, dưới dạng kilobyte.

### 8.6.6 slabtop
Lệnh slabtop(1) của Linux in thông tin về các slab caches của kernel, một số trong đó được sử dụng cho các bộ đệm hệ thống tập tin:
```bash
# slabtop -o
 Active / Total Objects (% used)            : 604675 / 684235 (88.4%)
 Active / Total Slabs (% used)              : 24040 / 24040 (100.0%)
 Active / Total Caches (% used)             : 99 / 159 (62.3%)
 Active / Total Size (% used)               : 140593.95K / 160692.10K (87.5%)
 Minimum / Average / Maximum Object         : 0.01K / 0.23K / 12.00K

  OBJS ACTIVE  USE OBJ SIZE  SLABS OBJ/SLAB CACHE SIZE NAME
165945 149714  90%    0.10K   4255       39     17020K buffer_head
107898  66011  61%    0.19K   5138       21     20552K dentry
 67350  67350 100%    0.13K   2245       30      8980K kernfs_node_cache
 41472  40551  97%    0.03K    324      128      1296K kmalloc-32
 35940  31460  87%    1.05K   2396       15     38336K ext4_inode_cache
 33514  33126  98%    0.58K   2578       13     20624K inode_cache
 24576  24576 100%    0.01K     48      512       192K kmalloc-8
[...]
```
Một số slab caches liên quan đến hệ thống tập tin có thể được thấy trong kết quả: dentry, ext4_inode_cache, và inode_cache. Không có chế độ kết quả -o (một lần), slabtop(1) sẽ làm mới và cập nhật màn hình.

Các Slab có thể bao gồm:
- **buffer_head:** Được sử dụng bởi buffer cache.
- **dentry:** dentry cache.
- **inode_cache:** inode cache.
- **ext3_inode_cache:** inode cache cho ext3.
- **ext4_inode_cache:** inode cache cho ext4.
- **xfs_inode:** inode cache cho XFS.
- **btrfs_inode:** inode cache cho btrfs.

slabtop(1) sử dụng /proc/slabinfo, thứ tồn tại nếu CONFIG_SLAB được bật.

### 8.6.7 strace
Độ trễ hệ thống tập tin có thể được đo lường tại giao diện syscall bằng cách sử dụng các công cụ truy vết bao gồm strace(1) cho Linux. Tuy nhiên, việc triển khai dựa trên ptrace(2) hiện tại của strace(1) có thể gây hại nghiêm trọng cho hiệu năng và có thể chỉ phù hợp để sử dụng khi chi phí hiệu năng là chấp nhận được và các phương pháp khác để phân tích độ trễ là không khả thi. Xem Chương 5, Mục 5.5.4, strace, để biết thêm về strace(1).

Ví dụ này cho thấy strace(1) định thời các lệnh đọc trên một hệ thống tập tin ext4:
```bash
$ strace -ttT -p 845
[...]
18:41:01.513110 read(9, "\334\260/\224\356k..."..., 65536) = 65536 <0.018225>
18:41:01.531646 read(9, "\371X\265|\244\317..."..., 65536) = 65536 <0.000056>
18:41:01.531984 read(9, "\357\311\347\1\241..."..., 65536) = 65536 <0.005760>
18:41:01.538151 read(9, "*\263\264\204|\370..."..., 65536) = 65536 <0.000033>
18:41:01.538549 read(9, "\205q\327\304f\370..."..., 65536) = 65536 <0.002033>
18:41:01.540923 read(9, "\6\2738>zw\321\353..."..., 65536) = 65536 <0.000032>
```
Tùy chọn -tt in các dấu thời gian tương đối ở bên trái, và -T in các thời gian syscall ở bên phải. Mỗi lệnh read(2) là cho 64 Kbyte, lệnh đầu tiên mất 18 ms, tiếp theo là 56 μs (có khả năng đã được đệm), sau đó là 5 ms. Các lệnh đọc được gửi tới file descriptor 9. Để kiểm tra xem đây là tới một hệ thống tập tin (và không phải là một socket), hoặc syscall open(2) sẽ hiển thị trong kết quả strace(1) sớm hơn, hoặc một công cụ khác như lsof(8) có thể được sử dụng. Bạn cũng có thể tìm thấy thông tin về FD 9 trong hệ thống tập tin /proc: /proc/845/fd{,info}/9.

Với các chi phí hiện tại của strace(1), độ trễ đo được có thể bị sai lệch bởi hiệu ứng người quan sát (observer effect). Xem các công cụ truy vết mới hơn, bao gồm ext4slower(8), thứ sử dụng per-CPU buffered tracing và BPF để giảm đáng kể chi phí, cung cấp các phép đo độ trễ chính xác hơn.

### 8.6.8 fatrace
fatrace(1) là một trình truy vết chuyên dụng sử dụng Linux fanotify API (thông báo truy cập tập tin). Kết quả ví dụ:
```bash
# fatrace
sar(25294): O /etc/ld.so.cache
sar(25294): RO /lib/x86_64-linux-gnu/libc-2.27.so
sar(25294): C /etc/ld.so.cache
sar(25294): O /usr/lib/locale/locale-archive
sar(25294): O /usr/share/zoneinfo/America/Los_Angeles
sar(25294): RC /usr/share/zoneinfo/America/Los_Angeles
sar(25294): RO /var/log/sysstat/sa09
sar(25294): R /var/log/sysstat/sa09
[...]
```
Mỗi dòng hiển thị tên tiến trình, PID, loại sự kiện, đường dẫn đầy đủ, và trạng thái tùy chọn. Loại sự kiện có thể là opens (O), reads (R), writes (W), và closes (C). fatrace(1) có thể được sử dụng cho việc đặc tính hóa khối lượng công việc: hiểu các tập tin được truy cập, và tìm kiếm các công việc không cần thiết có thể được loại bỏ.

Tuy nhiên, đối với một khối lượng công việc hệ thống tập tin bận rộn, fatrace(1) có thể tạo ra hàng chục nghìn dòng kết quả mỗi giây, và có thể tiêu tốn đáng kể tài nguyên CPU. Điều này có thể được giảm bớt phần nào bằng cách lọc theo một loại sự kiện. Các công cụ truy vết dựa trên BPF, bao gồm opensnoop(8) (Mục 8.6.10), cũng làm giảm đáng kể chi phí.

### 8.6.9 LatencyTOP
LatencyTOP là một công cụ để báo cáo các nguồn gốc của độ trễ, được tổng hợp trên toàn hệ thống và cho mỗi tiến trình. Độ trễ hệ thống tập tin được báo cáo bởi LatencyTOP. Ví dụ:
```text
Cause                               Maximum     Percentage
Reading from file                  209.6 msec      61.9 %
synchronous write                   82.6 msec      24.0 %
Marking inode dirty                  7.9 msec       2.2 %
Waiting for a process to die         4.6 msec       1.5 %
Waiting for event (select)           3.6 msec      10.1 %
Page fault                           0.2 msec       0.2 %

Process gzip (10969)               Total: 442.4 msec
Reading from file                  209.6 msec      70.2 %
synchronous write                   82.6 msec      27.2 %
Marking inode dirty                  7.9 msec       2.5 %
```
Phần trên là phần tóm tắt trên toàn hệ thống, và phần dưới là cho một tiến trình gzip(1) duy nhất, thứ đang nén một tập tin. Hầu hết độ trễ cho gzip(1) là do Reading from file ở mức 70.2%, với 27.2% trong synchronous write khi tập tin nén mới được ghi.

LatencyTOP được phát triển bởi Intel, nhưng nó đã không được cập nhật trong một thời gian dài, và trang web của nó không còn trực tuyến. Nó cũng yêu cầu các tùy chọn kernel thường không được bật. Bạn có thể thấy dễ dàng hơn khi đo lường độ trễ hệ thống tập tin bằng các công cụ truy vết BPF thay thế: xem các Mục từ 8.6.13 đến 8.6.15.

### 8.6.10 opensnoop
opensnoop(8) là một công cụ BCC và bpftrace thực hiện truy vết các lần mở tập tin. Nó hữu ích để khám phá vị trí của các tập tin dữ liệu, các tập tin nhật ký, và các tập tin cấu hình. Nó cũng có thể khám phá các vấn đề hiệu năng gây ra bởi việc mở tập tin thường xuyên, hoặc giúp khắc phục các sự cố gây ra bởi việc thiếu các tập tin. Dưới đây là một số kết quả ví dụ, với -T để bao gồm các dấu thời gian:
```bash
# opensnoop -T
TIME(s)       PID    COMM               FD ERR PATH
0.000000000   26447  sshd                5   0 /var/log/btmp
[...]
1.961686000   25983  mysqld              4   0 /etc/mysql/my.cnf
1.961715000   25983  mysqld              5   0 /etc/mysql/conf.d/
1.961770000   25983  mysqld              5   0 /etc/mysql/conf.d/mysql.cnf
1.961799000   25983  mysqld              5   0 /etc/mysql/conf.d/mysqldump.cnf
1.961818000   25983  mysqld              5   0 /etc/mysql/mysql.conf.d/
1.961843000   25983  mysqld              5   0 /etc/mysql/mysql.conf.d/mysql.cnf
1.961862000   25983  mysqld              5   0 /etc/mysql/mysql.conf.d/mysql.cnf
[...]
2.438417000   25983  mysqld              4   0 /var/log/mysql/error.log
[...]
2.816953000   25983  mysqld             30   0 ./binlog.000024
2.818827000   25983  mysqld             31   0 ./binlog.index_crash_safe
2.820621000   25983  mysqld              4   0 ./binlog.index
[...]
```
Kết quả này bao gồm việc khởi động của một cơ sở dữ liệu MySQL, và opensnoop(2) đã để lộ các tập tin cấu hình, tập tin nhật ký, các tập tin dữ liệu (các nhật ký nhị phân), và nhiều hơn nữa.

opensnoop(8) hoạt động bằng cách chỉ truy vết các syscall biến thể open(2): open(2) và openat(2). Chi phí được mong đợi là không đáng kể vì các lần mở thường không thường xuyên.

Các tùy chọn cho phiên bản BCC bao gồm:
- **-T:** Bao gồm một cột dấu thời gian
- **-x:** Chỉ hiển thị các lần mở thất bại
- **-p PID:** Chỉ truy vết tiến trình này
- **-n NAME:** Chỉ hiển thị các lần mở khi tên tiến trình chứa NAME

Tùy chọn -x có thể được sử dụng cho việc khắc phục sự cố: tập trung vào các trường hợp nơi các ứng dụng không thể mở các tập tin.

### 8.6.11 filetop
filetop(8) là một công cụ BCC giống như top(1) cho các tập tin, hiển thị các tên tập tin được đọc hoặc ghi thường xuyên nhất. Kết quả ví dụ:
```bash
# filetop
Tracing... Output every 1 secs. Hit Ctrl-C to end

19:16:22 loadavg: 0.11 0.04 0.01 3/189 23035

TID    COMM             READS  WRITES R_Kb    W_Kb   T FILE
23033  mysqld           481    0      7681    0      R sb1.ibd
23033  mysqld           3      0      48      0      R mysql.ibd
23032  oltp_read_only.  3      0      20      0      R oltp_common.lua
23031  oltp_read_only.  3      0      20      0      R oltp_common.lua
23032  oltp_read_only.  1      0      19      0      R Index.xml
23032  oltp_read_only.  4      0      16      0      R openssl.cnf
23035  systemd-udevd    4      0      16      0      R sys_vendor
[...]
```
Theo mặc định, hai mươi tập tin hàng đầu được hiển thị, được sắp xếp theo cột byte đọc. Dòng trên cùng cho thấy mysqld đã thực hiện 481 lần đọc từ một tập tin sb1.ibd, tổng cộng 7,681 Kbyte.

Công cụ này được sử dụng cho việc đặc tính hóa khối lượng công việc và khả năng quan sát hệ thống tập tin nói chung. Giống như việc bạn có thể khám phá một tiến trình tiêu tốn CPU không mong muốn bằng cách sử dụng top(1), điều này có thể giúp bạn khám phá một tập tin bận rộn I/O không mong muốn.

filetop theo mặc định cũng chỉ hiển thị các tập tin thông thường. Tùy chọn -a hiển thị tất cả các loại tập tin, bao gồm các TCP sockets và các nút thiết bị:
```bash
# filetop -a
[...]
TID    COMM    READS  WRITES R_Kb    W_Kb   T FILE
21701  sshd    1      0      16      0      O ptmx
23033  mysqld  1      0      16      0      R sbtest1.ibd
23335  sshd    1      0      8       0      S TCP
1      systemd 4      0      4       0      R comm
[...]
```
Kết quả bây giờ chứa loại tập tin khác (O) và socket (S). Trong trường hợp này, tập tin loại khác, ptmx, là một tập tin ký tự đặc biệt trong /dev.

Các tùy chọn bao gồm:
- **-C:** Không xóa màn hình: kết quả dạng cuốn (rolling output)
- **-a:** Hiển thị tất cả các loại tập tin
- **-r ROWS:** In số lượng hàng này (mặc định là 20)
- **-p PID:** Chỉ truy vết tiến trình này

Màn hình được làm mới mỗi giây (giống như top(1)) trừ khi -C được sử dụng. Tôi thích sử dụng -C sao cho kết quả nằm trong bộ đệm cuộn của terminal, trong trường hợp tôi cần tham khảo nó sau này.

### 8.6.12 cachestat
cachestat(8) là một công cụ BCC hiển thị các thống kê trúng và trượt (hit and miss) của bộ đệm trang (page cache). Điều này có thể được sử dụng để kiểm tra tỷ lệ trúng và hiệu quả của page cache, và chạy trong khi điều tra việc tinh chỉnh hệ thống và ứng dụng để lấy phản hồi về hiệu năng bộ đệm. Kết quả ví dụ:
```bash
$ cachestat -T 1
TIME      HITS  MISSES  DIRTIES HITRATIO  BUFFERS_MB  CACHED_MB
21:00:48   586       0     1870  100.00%         208        775
21:00:49   125       0     1775  100.00%         208        776
21:00:50   113       0     1644  100.00%         208        776
21:00:51    23       0     1389  100.00%         208        776
21:00:52   134       0     1906  100.00%         208        777
[...]
```
Kết quả này cho thấy một khối lượng công việc đọc hoàn toàn được đệm (HITS với 100.00% HITRATIO) và một khối lượng công việc ghi cao hơn (DIRTIES). Lý tưởng nhất, tỷ lệ trúng gần 100% sao cho các lệnh đọc của ứng dụng không bị chặn bởi I/O đĩa.

Nếu bạn gặp một tỷ lệ trúng thấp có thể gây hại cho hiệu năng, bạn có thể tinh chỉnh kích thước bộ nhớ của ứng dụng nhỏ hơn một chút, để lại thêm chỗ cho page cache. Nếu các thiết bị swap được cấu hình, cũng có tunable swappiness để ưu tiên việc loại bỏ khỏi page cache so với việc thực hiện swapping.

Các tùy chọn bao gồm -T để in một dấu thời gian.

Trong khi công cụ này cung cấp cái nhìn quan trọng cho tỷ lệ trúng page cache, nó cũng là một công cụ thực nghiệm sử dụng kprobes để truy vết các chức năng kernel nhất định, vì vậy nó sẽ cần bảo trì để hoạt động trên các phiên bản kernel khác nhau. Thậm chí tốt hơn, nếu các tracepoints hoặc các thống kê /proc được thêm vào, công cụ này có thể được viết lại để sử dụng chúng và trở nên ổn định. Việc sử dụng tốt nhất của nó ngày nay có thể chỉ đơn giản là để chỉ ra rằng một công cụ như vậy là khả thi.

### 8.6.13 ext4dist (xfs, zfs, btrfs, nfs)
ext4dist(8) là một công cụ BCC và bpftrace để instrument hệ thống tập tin ext4 và hiển thị phân phối của các độ trễ dưới dạng các biểu đồ histogram cho các thao tác phổ biến: reads, writes, opens, và fsync. Có các phiên bản cho các hệ thống tập tin khác: xfsdist(8), zfsdist(8), btrfsdist(8), và nfsdist(8). Kết quả ví dụ:
```bash
# ext4dist 10 1
Tracing ext4 operation latency... Hit Ctrl-C to end.

21:09:46:

operation = read
     usecs               : count    distribution
         0 -> 1          : 783     |***********************                 |
         2 -> 3          : 88      |**                                      |
         4 -> 7          : 449     |*************                           |
         8 -> 15         : 1306    |****************************************|
        16 -> 31         : 48      |*                                       |
        32 -> 63         : 12      |                                        |
        64 -> 127        : 39      |*                                       |
       128 -> 255        : 11      |                                        |
       256 -> 511        : 158     |****                                    |
       512 -> 1023       : 110     |***                                     |
      1024 -> 2047       : 33      |*                                       |

operation = write
     usecs               : count    distribution
         0 -> 1          : 1073    |****************************            |
         2 -> 3          : 324     |********                                |
         4 -> 7          : 1378    |************************************    |
         8 -> 15         : 1505    |****************************************|
        16 -> 31         : 183     |****                                    |
        32 -> 63         : 37      |                                        |
        64 -> 127        : 11      |                                        |
       128 -> 255        : 9       |                                        |

operation = open
     usecs               : count    distribution
         0 -> 1          : 672     |****************************************|
         2 -> 3          : 10      |                                        |

operation = fsync
     usecs               : count    distribution
       256 -> 511        : 485     |**********                              |
       512 -> 1023       : 308     |******                                  |
      1024 -> 2047       : 1779    |****************************************|
      2048 -> 4095       : 79      |*                                       |
      4096 -> 8191       : 26      |                                        |
      8192 -> 16383      : 4       |                                        |
```
Việc này đã sử dụng một khoảng thời gian 10 giây và một số lượng là 1 để hiển thị một lần truy vết 10 giây duy nhất. Nó cho thấy một sự phân phối độ trễ đọc bi-modal, với một mode giữa 0 và 15 micro giây, có khả năng là các lần trúng bộ đệm bộ nhớ, và một mode khác giữa 256 và 2048 micro giây, có khả năng là các lần đọc đĩa. Các phân phối của các thao tác khác cũng có thể được nghiên cứu. Các lệnh ghi thì nhanh, có khả năng là do buffering thứ sau đó được flush xuống đĩa bằng cách sử dụng thao tác fsync chậm hơn.

Công cụ này và công cụ đồng hành của nó ext4slower(8) (phần tiếp theo) cho thấy các độ trễ mà các ứng dụng có thể gặp phải. Việc đo lường độ trễ xuống tới mức đĩa là khả thi, và được trình bày trong Chương 9, nhưng các ứng dụng có thể không bị chặn trực tiếp bởi I/O đĩa, khiến các phép đo đó khó diễn giải hơn. Khi có thể, tôi sử dụng các công cụ ext4dist(8)/ext4slower(8) trước các công cụ độ trễ I/O đĩa. Xem Mục 8.3.12 cho các sự khác biệt giữa I/O logic tới hệ thống tập tin, được đo lường bởi công cụ này, và I/O vật lý tới các đĩa.

Các tùy chọn bao gồm:
- **-m:** In kết quả dưới dạng mili giây
- **-p PID:** Chỉ truy vết tiến trình này

Kết quả từ công cụ này có thể được hình ảnh hóa dưới dạng một bản đồ nhiệt độ trễ (latency heat map). Để biết thêm thông tin về I/O hệ thống tập tin chậm, hãy chạy ext4slower(8) và các biến thể của nó.

### 8.6.14 ext4slower (xfs, zfs, btrfs, nfs)
ext4slower(8) truy vết các thao tác ext4 phổ biến và in các chi tiết cho mỗi sự kiện cho những thao tác chậm hơn một ngưỡng (threshold) cho trước. Các thao tác được truy vết là reads, writes, opens, và fsync. Kết quả ví dụ:
```bash
# ext4slower
Tracing ext4 operations slower than 10 ms
TIME      COMM     PID    T BYTES OFF_KB LAT(ms) FILENAME
21:36:03  mysqld   22935  S 0     0      12.81   sbtest1.ibd
21:36:15  mysqld   22935  S 0     0      12.13   ib_logfile1
21:36:15  mysqld   22935  S 0     0      10.46   binlog.000026
21:36:15  mysqld   22935  S 0     0      13.66   ib_logfile1
21:36:15  mysqld   22935  S 0     0      11.79   ib_logfile1
[...]
```
Các cột hiển thị thời gian (TIME), tên tiến trình (COMM), và PID, loại thao tác (T: R cho reads, W cho writes, O cho opens, và S cho syncs), offset tính theo Kbyte (OFF_KB), độ trễ của thao tác tính theo mili giây (LAT(ms)), và tên tập tin (FILENAME).

Kết quả cho thấy một số thao tác sync (S) đã vượt quá 10 mili giây, ngưỡng mặc định cho ext4slower(8). Ngưỡng này có thể được cung cấp như một đối số; việc chọn 0 mili giây hiển thị tất cả các thao tác:
```bash
# ext4slower 0
Tracing ext4 operations
21:36:50  mysqld  22935  W 917504  2048   0.42  ibdata1
21:36:50  mysqld  22935  W 1024    14165  0.00  ib_logfile1
21:36:50  mysqld  22935  W 512     14166  0.00  ib_logfile1
21:36:50  mysqld  22935  S 0       0      3.21  ib_logfile1
21:36:50  mysqld  22935  W 1746    21714  0.02  binlog.000026
21:36:50  mysqld  22935  S 0       0      5.56  ibdata1
21:36:50  mysqld  22935  W 16384   4640   0.01  undo_001
[...]
```
Một mẫu hình có thể được thấy trong kết quả: mysqld thực hiện các lệnh ghi tới các tập tin theo sau bởi một thao tác sync muộn hơn.

Truy vết tất cả các thao tác có thể tạo ra một lượng lớn kết quả với các chi phí liên quan. Tôi chỉ thực hiện việc này trong các khoảng thời gian ngắn (ví dụ: mười giây) để hiểu các mẫu của các thao tác hệ thống tập tin thứ không hiển thị được trong các bản tóm tắt khác (ext4dist(8)).

Các tùy chọn bao gồm -p PID để chỉ truy vết một tiến trình duy nhất, và -j để tạo ra kết quả có thể phân tích được (CSV).

### 8.6.15 bpftrace
bpftrace là một trình truy vết dựa trên BPF cung cấp một ngôn ngữ lập trình cấp cao, cho phép tạo ra các lệnh một dòng (one-liners) mạnh mẽ và các script ngắn. Nó rất phù hợp cho việc phân tích hệ thống tập tin tùy chỉnh dựa trên các manh mối từ các công cụ khác.

bpftrace được giải thích trong Chương 15, BPF. Phần này trình bày một số ví dụ cho phân tích hệ thống tập tin: one-liners, truy vết syscall, truy vết VFS, và các thành phần nội bộ hệ thống tập tin.

**Các lệnh Một-Dòng (One-Liners)**
Các lệnh một dòng sau đây rất hữu ích và trình diễn các khả năng khác nhau của bpftrace.

Truy vết các tập tin được mở qua openat(2) kèm tên tiến trình:
```bash
bpftrace -e 't:syscalls:sys_enter_openat { printf("%s %s\n", comm, str(args->filename)); }'
```
Đếm các syscall read theo loại syscall:
```bash
bpftrace -e 'tracepoint:syscalls:sys_enter_*read* { @[probe] = count(); }'
```
Đếm các syscall write theo loại syscall:
```bash
bpftrace -e 'tracepoint:syscalls:sys_enter_*write* { @[probe] = count(); }'
```
Hiển thị phân phối kích thước yêu cầu syscall read():
```bash
bpftrace -e 'tracepoint:syscalls:sys_enter_read { @ = hist(args->count); }'
```
Hiển thị phân phối các byte đọc được (và lỗi) của syscall read():
```bash
bpftrace -e 'tracepoint:syscalls:sys_exit_read { @ = hist(args->ret); }'
```
Đếm các lỗi syscall read() theo mã lỗi:
```bash
bpftrace -e 't:syscalls:sys_exit_read /args->ret < 0/ { @[- args->ret] = count(); }'
```
Đếm các lệnh gọi VFS:
```bash
bpftrace -e 'kprobe:vfs_* { @[probe] = count(); }'
```
Đếm các lệnh gọi VFS cho PID 181:
```bash
bpftrace -e 'kprobe:vfs_* /pid == 181/ { @[probe] = count(); }'
```
Đếm các tracepoints ext4:
```bash
bpftrace -e 'tracepoint:ext4:* { @[probe] = count(); }'
```
Đếm các tracepoints xfs:
```bash
bpftrace -e 'tracepoint:xfs:* { @[probe] = count(); }'
```
Đếm các lệnh đọc tập tin ext4 theo tên tiến trình và user-level stack:
```bash
bpftrace -e 'kprobe:ext4_file_read_iter { @[ustack, comm] = count(); }'
```
Truy vết thời gian ZFS spa_sync():
```bash
bpftrace -e 'kprobe:spa_sync { time("%H:%M:%S ZFS spa_sync()\n"); }'
```
Đếm các tham chiếu dcache theo tên tiến trình và PID:
```bash
bpftrace -e 'kprobe:lookup_fast { @[comm, pid] = count(); }'
```

**Truy vết Syscall**
Syscalls là một mục tiêu tuyệt vời cho việc truy vết và là nguồn instrumentation cho nhiều công cụ truy vết. Tuy nhiên, một số syscall thiếu ngữ cảnh hệ thống tập tin, khiến chúng gây nhầm lẫn khi sử dụng. Tôi sẽ cung cấp một ví dụ về việc mọi thứ hoạt động (truy vết openat(2)) và không hoạt động (truy vết read(2)), cùng các biện pháp khắc phục được gợi ý.

**openat(2)**
Truy vết họ các syscall open(2) hiển thị các tập tin được mở. Ngày nay biến thể openat(2) thường được sử dụng phổ biến hơn. Truy vết nó:
```bash
# bpftrace -e 't:syscalls:sys_enter_openat { printf("%s %s\n", comm, str(args->filename)); }'
Attaching 1 probe...
sa1 /etc/sysstat/sysstat
sadc /etc/ld.so.cache
sadc /lib/x86_64-linux-gnu/libsensors.so.5
sadc /lib/x86_64-linux-gnu/libc.so.6
[...]
```
Kết quả này đã bắt được quá trình thực thi của sar(1) cho việc lưu trữ các thống kê, và các tập tin mà nó đang mở. bpftrace đã sử dụng đối số filename từ tracepoint; tất cả các đối số có thể được liệt kê bằng cách sử dụng -lv:
```bash
# bpftrace -lv t:syscalls:sys_enter_openat
tracepoint:syscalls:sys_enter_openat
    int __syscall_nr;
    int dfd;
    const char * filename;
    int flags;
    umode_t mode;
```
Các đối số là số syscall, file descriptor, filename, các cờ mở, và chế độ mở: đủ thông tin để sử dụng bởi các lệnh một dòng và các công cụ, chẳng hạn như opensnoop(8).

**read(2)**
read(2) nên là một mục tiêu truy vết hữu ích để hiểu độ trễ đọc của hệ thống tập tin. Tuy nhiên, hãy xem xét các đối số tracepoint (xem liệu bạn có thể nhận ra vấn đề không):
```bash
# bpftrace -lv t:syscalls:sys_enter_read
tracepoint:syscalls:sys_enter_read
    int __syscall_nr;
    unsigned int fd;
    char * buf;
    size_t count;
```
read(2) có thể được gọi cho các hệ thống tập tin, sockets, /proc, và các mục tiêu khác, và các đối số không phân biệt được giữa chúng. Để chỉ ra mức độ gây nhầm lẫn của điều này, lệnh sau đây đếm các syscall read(2) theo tên tiến trình:
```bash
# bpftrace -e 't:syscalls:sys_enter_read { @[comm] = count(); }'
Attaching 1 probe...
^C

@[systemd-journal]: 13
@[sshd]: 141
@[java]: 3472
```
Trong khi truy vết, Java đã thực hiện 3,472 syscall read(2), nhưng chúng là từ một hệ thống tập tin, một socket, hay thứ gì đó khác? (Các lần đọc sshd có lẽ là I/O socket.)

Những gì read(2) thực sự cung cấp là file descriptor (FD) dưới dạng một số nguyên, nhưng nó chỉ là một con số và không cho thấy loại FD (và bpftrace đang chạy trong một chế độ kernel bị hạn chế: nó không thể tra cứu thông tin FD trong /proc). Có ít nhất bốn giải pháp cho vấn đề này:
- In PID và FD từ bpftrace, và sau đó tra cứu các FD bằng cách sử dụng lsof(8) hoặc /proc để xem chúng là gì.
- Một trình hỗ trợ BPF sắp tới, get_fd_path(), có thể trả về tên đường dẫn cho một FD. Điều này sẽ giúp phân biệt các lần đọc hệ thống tập tin (thứ có một tên đường dẫn) với các loại khác.
- Truy vết từ VFS thay thế, nơi có nhiều cấu trúc dữ liệu hơn khả dụng.
- Truy vết trực tiếp các chức năng hệ thống tập tin, thứ loại trừ các loại I/O khác. Cách tiếp cận này được sử dụng bởi ext4dist(8) và ext4slower(8).

Phần tiếp theo về Truy vết Độ trễ VFS trình bày giải pháp dựa trên VFS.

**Truy vết VFS**
Vì hệ thống tập tin ảo (VFS) trừu tượng hóa tất cả các hệ thống tập tin (và các thiết bị khác), việc truy vết các lệnh gọi của nó cung cấp một điểm duy nhất để từ đó quan sát tất cả các hệ thống tập tin.

**Số lượng VFS**
Việc đếm các lệnh gọi VFS cung cấp một cái nhìn tổng quan cấp cao về các loại thao tác đang được sử dụng. Phần sau đây đếm các chức năng kernel bắt đầu bằng "vfs_" sử dụng kprobes:
```bash
# bpftrace -e 'kprobe:vfs_* { @[func] = count(); }'
Attaching 65 probes...
^C
[...]
@[vfs_statfs]: 36
@[vfs_readlink]: 164
@[vfs_write]: 364
@[vfs_lock_file]: 516
@[vfs_iter_read]: 2551
@[vfs_statx]: 3141
@[vfs_statx_fd]: 4214
@[vfs_open]: 5271
@[vfs_read]: 5602
@[vfs_getattr_nosec]: 7794
@[vfs_getattr]: 7795
```
Điều này cho thấy các loại thao tác khác nhau đang xảy ra trên toàn hệ thống. Trong khi truy vết, đã có 7,795 lệnh vfs_read().

**Độ trễ VFS**
Giống như với các syscall, các lệnh đọc VFS có thể dành cho các hệ thống tập tin, sockets, và các mục tiêu khác. Chương trình bpftrace sau đây lấy loại từ một cấu trúc kernel (tên superblock inode), cung cấp một sự phân tích độ trễ vfs_read() tính theo micro giây theo loại:
```bash
# vfsreadlat.bt
Tracing vfs_read() by type... Hit Ctrl-C to end.
^C
[...]
@us[sockfs]:
[0]                    141 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[1]                     91 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                         |
[2, 4)                  57 |@@@@@@@@@@@@@@@@@@@@@                                     |
[4, 8)                  53 |@@@@@@@@@@@@@@@@@@@                                       |
[8, 16)                 86 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                           |
[16, 32)                 2 |                                                          |
[...]

@us[proc]:
[0]                    242 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[1]                     41 |@@@@@@@@                                                  |
[2, 4)                  40 |@@@@@@@@                                                  |
[4, 8)                  61 |@@@@@@@@@@@@@                                             |
[8, 16)                 44 |@@@@@@@@@                                                 |
[16, 32)                40 |@@@@@@@@                                                  |
[32, 64)                 6 |@                                                         |
[64, 128)                3 |                                                          |

@us[ext4]:
[0]                    653 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  |
[1]                    447 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                               |
[2, 4)                   70 |@@@@                                                        |
[4, 8)                 774 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[8, 16)                417 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                 |
[16, 32)                 25 |@                                                           |
[32, 64)                  7 |                                                            |
[64, 128)              170 |@@@@@@@@@@@                                                  |
[128, 256)               55 |@@@                                                         |
[256, 512)               59 |@@@                                                         |
[512, 1K)              118 |@@@@@@@                                                      |
[1K, 2K)                  3 |@@                                                          |
```
Kết quả (đã bị lược bớt) cũng bao gồm các histogram độ trễ cho: sysfs, devpts, pipefs, devtmpfs, tmpfs, và anon_inodefs.

Mã nguồn là:
```c
#!/usr/local/bin/bpftrace
#include <linux/fs.h>

BEGIN
{
          printf("Tracing vfs_read() by type... Hit Ctrl-C to end.\n");
}

kprobe:vfs_read
{
          @file[tid] = ((struct file *)arg0)->f_inode->i_sb->s_type->name;
          @ts[tid] = nsecs;
}

kretprobe:vfs_read
/@ts[tid]/
{
          @us[str(@file[tid])] = hist((nsecs - @ts[tid]) / 1000);
          delete(@file[tid]); delete(@ts[tid]);
}

END
{
               clear(@file); clear(@ts);
}
```
Bạn có thể mở rộng công cụ này để bao gồm các thao tác khác, chẳng hạn như vfs_readv(), vfs_write(), vfs_writev(), vfs_v., v.v. Để hiểu mã này, hãy bắt đầu với Mục 15.2.4, Lập trình, thứ giải thích những điều cơ bản của việc định thời vfs_read().

Lưu ý rằng độ trễ này có thể hoặc không thể ảnh hưởng trực tiếp đến hiệu năng ứng dụng, như đã đề cập trong Mục 8.3.1, Độ trễ hệ thống tập tin. Nó phụ thuộc vào việc liệu độ trễ có gặp phải trong quá trình thực hiện một yêu cầu ứng dụng hay không, hay liệu nó xảy ra trong một tác vụ chạy nền bất đồng bộ. Để trả lời điều này, bạn có thể bao gồm stack trace người dùng (ustack) như một histogram key bổ sung, thứ có thể để lộ liệu lệnh gọi vfs_read() có diễn ra trong quá trình thực hiện yêu cầu ứng dụng hay không.

**Các thành phần nội bộ Hệ thống Tập tin (File System Internals)**
Nếu cần thiết, bạn có thể phát triển các công cụ tùy chỉnh chỉ ra hành vi của các thành phần nội bộ hệ thống tập tin. Hãy bắt đầu bằng cách thử các tracepoints, nếu có sẵn. Liệt kê chúng cho ext4:
```bash
# bpftrace -l 'tracepoint:ext4:*'
tracepoint:ext4:ext4_other_inode_update_time
tracepoint:ext4:ext4_free_inode
tracepoint:ext4:ext4_request_inode
tracepoint:ext4:ext4_allocate_inode
tracepoint:ext4:ext4_evict_inode
tracepoint:ext4:ext4_drop_inode
[...]
```
Mỗi tracepoint này có các đối số có thể được liệt kê bằng cách sử dụng -lv. Nếu các tracepoints không đủ (hoặc không khả dụng cho loại hệ thống tập tin của bạn), hãy xem xét việc sử dụng instrumentation động với kprobes. Liệt kê các mục tiêu kprobe cho ext4:
```bash
# bpftrace -lv 'kprobe:ext4_*'
kprobe:ext4_has_free_clusters
kprobe:ext4_validate_block_bitmap
kprobe:ext4_get_group_number
kprobe:ext4_get_group_no_and_offset
kprobe:ext4_get_group_desc
kprobe:ext4_wait_block_bitmap
[...]
```
Trong phiên bản kernel này (5.3) có 105 tracepoints ext4 và 538 kprobes ext4 khả thi.

### 8.6.17 Các Công cụ Khác (Other Tools)
Các công cụ quan sát hệ thống tập tin có trong các chương khác của cuốn sách này, và trong BPF Performance Tools [Gregg 19], được liệt kê trong Bảng 8.7.

Bảng 8.7 Các công cụ quan sát hệ thống tập tin khác
| Mục | Công cụ | Mô tả |
| --- | --- | --- |
| 5.5.6 | syscount | Đếm các syscall bao gồm các syscall liên quan đến hệ thống tập tin |
| [Gregg 19] | statsnoop | Truy vết các lệnh gọi tới các biến thể stat(2) |
| [Gregg 19] | syncsnoop | Truy vết sync(2) và các lệnh gọi biến thể với các dấu thời gian |
| [Gregg 19] | mmapfiles | Đếm các tập tin mmap(2) |
| [Gregg 19] | scread | Đếm các tập tin read(2) |
| [Gregg 19] | fmapfault | Đếm các lỗi ánh xạ tập tin (file map faults) |
| [Gregg 19] | filelife | Truy vết các tập tin tồn tại ngắn với tuổi thọ của chúng tính theo giây |
| [Gregg 19] | vfsstat | Các thống kê thao tác VFS phổ biến |
| [Gregg 19] | vfscount | Đếm tất cả các thao tác VFS |
| [Gregg 19] | vfssize | Hiển thị các kích thước đọc/ghi VFS |
| [Gregg 19] | fsrwstat | Hiển thị các lệnh đọc/ghi VFS theo loại hệ thống tập tin |
| [Gregg 19] | fileslower | Hiển thị các lệnh đọc/ghi tập tin chậm |
| [Gregg 19] | filetype | Hiển thị các lệnh đọc/ghi VFS theo loại tập tin và tiến trình |
| [Gregg 19] | ioprofile | Đếm các stacks trên I/O để chỉ ra các đường dẫn mã |
| [Gregg 19] | writesync | Hiển thị các lệnh ghi tập tin thông thường theo cờ sync |
| [Gregg 19] | writeback | Hiển thị các sự kiện write-back và các độ trễ |
| [Gregg 19] | dcstat | Thống kê trúng bộ đệm thư mục (directory cache hit stats) |
| [Gregg 19] | dcsnoop | Truy vết các lần tra cứu bộ đệm thư mục |
| [Gregg 19] | mountsnoop | Truy vết các lần mount và umount trên toàn hệ thống |
| [Gregg 19] | icstat | Thống kê trúng bộ đệm inode (inode cache hit stats) |
| [Gregg 19] | bufgrow | Sự phát triển của buffer cache theo tiến trình và số byte |
| [Gregg 19] | readahead | Hiển thị các lần trúng read ahead và hiệu quả của nó |

Các công cụ khác liên quan đến hệ thống tập tin Linux bao gồm:
- **df(1):** báo cáo việc sử dụng hệ thống tập tin và các thống kê dung lượng.
- **inotify:** một framework của Linux để giám sát các sự kiện hệ thống tập tin.

Một số loại hệ thống tập tin có các công cụ hiệu năng cụ thể của riêng chúng, bên cạnh những công cụ được cung cấp bởi hệ điều hành, ví dụ, ZFS.

**ZFS**
ZFS đi kèm với zpool(1M), thứ có một tùy chọn phụ iostat để quan sát các thống kê của ZFS pool. Nó báo cáo tốc độ thao tác của pool (đọc và ghi) và thông lượng.

Một phần bổ sung phổ biến là công cụ arcstat.pl, thứ báo cáo kích thước ARC và L2ARC cùng tỷ lệ trúng và trượt. Ví dụ:
```bash
$ arcstat 1
      time   read   miss   miss%   dmis    dm%    pmis   pm%     mmis   mm%   arcsz     c
04:45:47        0      0       0      0       0      0     0        0     0     14G   14G
04:45:49      15K     10       0     10       0      0     0        1     0     14G   14G
04:45:50      23K     81       0     81       0      0     0        1     0     14G   14G
04:45:51      65K     25       0     25       0      0     0        4     0     14G   14G
[...]
```
Các thống kê là cho mỗi khoảng thời gian và là:
- **read, miss:** Tổng số lần truy cập ARC, số lần trượt.
- **miss%, dm%, pm%, mm%:** Phần trăm trượt ARC tổng cộng, demand, prefetch, metadata.
- **dmis, pmis, mmis:** Các lần trượt cho demand, prefetch, metadata.
- **arcsz, c:** Kích thước ARC, kích thước mục tiêu ARC.

arcstat.pl là một chương trình Perl đọc các thống kê từ kstat.

### 8.6.18 Các hình ảnh hóa (Visualizations)
Tải được áp dụng cho các hệ thống tập tin có thể được vẽ biểu đồ theo thời gian dưới dạng một đồ thị đường, để giúp xác định các mẫu sử dụng dựa trên thời gian. Có thể hữu ích khi vẽ các đồ thị riêng biệt cho các lệnh đọc, ghi, và các thao tác hệ thống tập tin khác.

Phân phối độ trễ hệ thống tập tin được kỳ vọng là bi-modal: một mode tại độ trễ thấp cho các lần trúng bộ đệm hệ thống tập tin, và một mode khác tại độ trễ cao cho các lần trượt bộ đệm (I/O thiết bị lưu trữ). Vì lý do này, việc đại diện cho phân phối dưới dạng một giá trị duy nhất—chẳng hạn như trung bình, mode, hoặc trung vị—là gây nhầm lẫn.

Một cách để giải quyết vấn đề này là sử dụng một sự hình ảnh hóa cho thấy toàn bộ phân phối, chẳng hạn như một bản đồ nhiệt (heat map). Các bản đồ nhiệt đã được giới thiệu trong Chương 2, Các Phương pháp luận, Mục 2.10.3, Các Bản đồ nhiệt. Một bản đồ nhiệt độ trễ hệ thống tập tin ví dụ được trình bày trong Hình 8.13: nó cho thấy sự trôi qua của thời gian trên trục x và độ trễ I/O trên trục y [Gregg 09a].

Bản đồ nhiệt này cho thấy sự khác biệt mà việc bật một thiết bị L2ARC tạo ra đối với độ trễ NFSv3. Một thiết bị L2ARC là một bộ đệm ZFS thứ cấp, sau bộ nhớ chính, và thường sử dụng bộ nhớ flash (nó đã được đề cập trong Mục 8.3.2, Caching). Hệ thống trong Hình 8.13 có 128 Gbyte bộ nhớ chính (DRAM) và 600 Gbyte L2ARC (các ổ SSD tối ưu hóa việc đọc). Nửa bên trái của bản đồ nhiệt cho thấy không có thiết bị L2ARC (L2ARC đã bị tắt), và nửa bên phải cho thấy độ trễ với một thiết bị L2ARC.

(Hình 8.13 Bản đồ nhiệt độ trễ hệ thống tập tin)

Đối với nửa bên trái, độ trễ hệ thống tập tin hoặc là thấp hoặc là cao, được phân tách bởi một khoảng trống. Các độ trễ thấp là đường màu xanh lam ở phía dưới, khoảng 0 mili giây, thứ có khả năng là các lần trúng bộ đệm bộ nhớ chính. Các độ trễ cao bắt đầu từ khoảng 3 mili giây và mở rộng lên phía trên, xuất hiện như một "đám mây", thứ có khả năng là độ trễ đĩa quay. Sự phân phối độ trễ bi-modal này là điển hình cho độ trễ hệ thống tập tin khi được hỗ trợ bởi các đĩa quay.

Đối với nửa bên phải, L2ARC đã được bật và độ trễ bây giờ thường thấp hơn 3 mili giây, và có ít hơn các độ trễ đĩa cao. Bạn có thể thấy độ trễ của L2ARC đã lấp đầy phạm vi nơi đã có một khoảng trống ở phía bên trái của bản đồ nhiệt, làm giảm độ trễ hệ thống tập tin nói chung.

---

## 8.7 Thực nghiệm (Experimentation)
Phần này mô tả các công cụ để kiểm tra tích cực hiệu năng hệ thống tập tin. Xem Mục 8.5.8, Micro-Benchmarking, để biết một chiến lược được gợi ý để tuân theo.

Khi sử dụng các công cụ này, một ý tưởng tốt là để iostat(1) chạy liên tục để xác nhận rằng khối lượng công việc truyền tới các đĩa đúng như mong đợi, thứ có thể có nghĩa là không có gì cả. Ví dụ, khi kiểm tra một kích thước tập làm việc thứ nên dễ dàng khớp vào bộ đệm hệ thống tập tin, kỳ vọng với một khối lượng công việc đọc là 100% cache hits, vì vậy iostat(1) không nên cho thấy I/O đĩa đáng kể. iostat(1) được đề cập trong Chương 9, Các đĩa.

### 8.7.1 Tùy biến (Ad Hoc)
Lệnh dd(1) (sao chép thiết bị tới thiết bị) có thể được sử dụng để thực hiện các bài kiểm tra tùy biến về hiệu năng hệ thống tập tin tuần tự. Các lệnh sau đây thực hiện việc ghi, và sau đó đọc một tập tin 1 Gbyte có tên file1 với kích thước I/O là 1 Mbyte:
- **Ghi:** `dd if=/dev/zero of=file1 bs=1024k count=1k`
- **Đọc:** `dd if=file1 of=/dev/null bs=1024k`

Phiên bản Linux của dd(1) in các thống kê khi hoàn thành. Ví dụ:
```bash
$ dd if=/dev/zero of=file1 bs=1024k count=1k
1024+0 records in
1024+0 records out
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 0.76729 s, 1.4 GB/s
```
Kết quả này cho thấy một thông lượng ghi hệ thống tập tin là 1.4 Gbytes/s (write-back caching đang được sử dụng, vì vậy việc này chỉ làm bẩn bộ nhớ và sẽ được flush sau đó xuống đĩa, tùy thuộc vào các thiết lập tunable vm.dirty_*: xem Chương 7, Bộ nhớ, Mục 7.6.1, Các Tham số Tinh chỉnh).

### 8.7.2 Các công cụ Kiểm thử vi mô (Micro-Benchmark Tools)
Có nhiều công cụ benchmark hệ thống tập tin khả dụng, bao gồm Bonnie, Bonnie++, iozone, tiobench, SysBench, fio, và FileBench. Một vài công cụ được thảo luận ở đây, theo thứ tự độ phức tạp tăng dần. Đồng thời xem Chương 12, Benchmarking. Khuyến nghị cá nhân của tôi là sử dụng fio.

**Bonnie, Bonnie++**
Công cụ Bonnie là một chương trình C đơn giản để kiểm tra một vài khối lượng công việc trên một tập tin duy nhất, từ một luồng duy nhất. Nó ban đầu được viết bởi Tim Bray vào năm 1989 [Bray 90]. Cách sử dụng rất đơn giản, không yêu cầu các đối số (các giá trị mặc định sẽ được sử dụng):
```bash
$ ./Bonnie
File './Bonnie.9598', size: 104857600
[...]
                -------Sequential Output-------- ---Sequential Input-- --Random--
                -Per Char- --Block--- -Rewrite-- -Per Char- --Block--- --Seeks---
Machine      MB K/sec %CPU K/sec %CPU K/sec %CPU K/sec %CPU K/sec %CPU       /sec %CPU
          100 123396 100.0 1258402 100.0 996583 100.0 126781 100.0 2187052 100.0 164190.1 299.0
```
Kết quả bao gồm thời gian CPU trong mỗi bài kiểm tra, thứ mà ở mức 100% là một chỉ báo rằng Bonnie chưa bao giờ bị chặn bởi I/O đĩa, thay vào đó luôn trúng từ bộ đệm và duy trì on-CPU. Lý do là vì kích thước tập tin mục tiêu là 100 Mbyte, thứ hoàn toàn được đệm trên hệ thống này. Bạn có thể thay đổi kích thước tập tin bằng cách sử dụng `-s size`.

Có một phiên bản 64-bit gọi là Bonnie-64, cho phép kiểm tra các tập tin lớn hơn. Cũng có một bản viết lại bằng C++ gọi là Bonnie++ bởi Russell Coker [Coker 01].

Thật không may, các công cụ benchmark hệ thống tập tin như Bonnie có thể gây nhầm lẫn, trừ khi bạn hiểu rõ những gì đang được kiểm tra. Kết quả đầu tiên, một bài kiểm tra putc(3), có thể thay đổi dựa trên việc triển khai thư viện hệ thống, thứ sau đó trở thành mục tiêu của bài kiểm tra thay vì hệ thống tập tin. Xem ví dụ trong Chương 12, Benchmarking, Mục 12.3.2, Active Benchmarking.

**fio**
Flexible IO Tester (fio) bởi Jens Axboe là một công cụ benchmark hệ thống tập tin có thể tùy chỉnh với nhiều tính năng nâng cao [Axboe 20]. Hai tính năng đã dẫn dắt tôi sử dụng nó thay vì các công cụ benchmark khác là:
- Các phân phối ngẫu nhiên không đồng nhất (non-uniform random distributions), thứ có thể mô phỏng chính xác hơn một mẫu truy cập trong thế giới thực (ví dụ: `-random_distribution=pareto:0.9`).
- Báo cáo các bách phân vị độ trễ (latency percentiles), bao gồm 99.00, 99.50, 99.90, 99.95, 99.99.

Dưới đây là một kết quả ví dụ, cho thấy một khối lượng công việc đọc ngẫu nhiên với kích thước I/O 8 Kbyte, kích thước tập làm việc 5 Gbyte, và một mẫu truy cập không đồng nhất (pareto:0.9):
```bash
# fio --runtime=60 --time_based --clocksource=clock_gettime --name=randread --numjobs=1 --rw=randread --random_distribution=pareto:0.9 --bs=8k --size=5g --filename=fio.tmp
randread: (g=0): rw=randread, bs=8K-8K/8K-8K/8K-8K, ioengine=sync, iodepth=1
fio-2.0.13-97-gdd8d
Starting 1 process
Jobs: 1 (f=1): [r] [100.0% done] [3208K/0K/0K /s] [401 /0 /0 iops] [eta 00m:00s]
randread: (groupid=0, jobs=1): err= 0: pid=2864: Tue Feb 5 00:13:17 2013
  read : io=247408KB, bw=4122.2KB/s, iops=515 , runt= 60007msec
      clat (usec): min=3 , max=67928 , avg=1933.15, stdev=4383.30
          lat (usec): min=4 , max=67929 , avg=1934.40, stdev=4383.31
      clat percentiles (usec):
          |   1.00th=[    5],   5.00th=[     5], 10.00th=[      5], 20.00th=[        6],
          | 30.00th=[     6], 40.00th=[      6], 50.00th=[      7], 60.00th=[      620],
          | 70.00th=[    692], 80.00th=[ 1688], 90.00th=[ 7648], 95.00th=[10304],
          | 99.00th=[19584], 99.50th=[24960], 99.90th=[39680], 99.95th=[51456],
          | 99.99th=[63744]
      bw (KB/s)      : min= 1663, max=71232, per=99.87%, avg=4116.58, stdev=6504.45
[...]
```
Các bách phân vị độ trễ (clat) cho thấy các độ trễ rất thấp lên tới bách phân vị thứ 50, thứ mà tôi giả định, dựa trên độ trễ (5 đến 7 micro giây), là các lần trúng bộ đệm. Các bách phân vị còn lại cho thấy ảnh hưởng của việc trượt bộ đệm, bao gồm cả phần đuôi của hàng đợi; trong trường hợp này, bách phân vị thứ 99.99 đang hiển thị độ trễ 63 ms.

Mặc dù các bách phân vị này thiếu thông tin để thực sự hiểu những gì có lẽ là một sự phân phối đa chế độ (multimode distribution), chúng tập trung vào phần thú vị nhất: phần đuôi của chế độ chậm hơn (I/O đĩa).

Đối với một công cụ tương tự nhưng đơn giản hơn, bạn có thể thử SysBench (một ví dụ về việc sử dụng SysBench cho phân tích CPU trong Chương 6, Mục 6.8.2, SysBench). Mặt khác, nếu bạn muốn có nhiều quyền kiểm soát hơn nữa, hãy thử FileBench.

**FileBench**
FileBench là một công cụ benchmark hệ thống tập tin có thể lập trình được, nơi các khối lượng công việc ứng dụng có thể được mô phỏng bằng cách mô tả chúng trong Ngôn ngữ Mô hình Khối lượng Công việc (Workload Model Language) của nó. Điều này cho phép các luồng với các hành vi khác nhau được mô phỏng, và cho phép hành vi luồng đồng bộ được chỉ định. Nó đi kèm với một loạt các cấu hình này, được gọi là personalities, bao gồm một cấu hình để mô phỏng mô hình I/O của cơ sở dữ liệu Oracle. Thật không may, FileBench không phải là một công cụ dễ học và sử dụng, và có thể chỉ được quan tâm bởi những người làm việc toàn thời gian về các hệ thống tập tin.

### 8.7.3 Xóa trống Bộ đệm (Cache Flushing)
Linux cung cấp một cách để flush (loại bỏ các mục khỏi) bộ đệm hệ thống tập tin, thứ có thể hữu ích cho việc benchmark hiệu năng từ một trạng thái bộ đệm nhất quán và "lạnh", như bạn có sau khi khởi động hệ thống. Cơ chế này được mô tả rất đơn giản trong tài liệu mã nguồn kernel (Documentation/sysctl/vm.txt) dưới dạng:

Để giải phóng pagecache:
`echo 1 > /proc/sys/vm/drop_caches`
Để giải phóng các đối tượng slab có thể thu hồi (bao gồm dentries và inodes):
`echo 2 > /proc/sys/vm/drop_caches`
Để giải phóng các đối tượng slab và pagecache:
`echo 3 > /proc/sys/vm/drop_caches`

Nó có thể đặc biệt hữu ích để giải phóng mọi thứ (3) trước các lần chạy benchmark khác, sao cho hệ thống bắt đầu ở một trạng thái nhất quán (một bộ đệm lạnh), giúp cung cấp các kết quả benchmark nhất quán.

---

## 8.8 Tinh chỉnh (Tuning)
Nhiều cách tiếp cận tinh chỉnh đã được đề cập trong Mục 8.5, Phương pháp luận, bao gồm tinh chỉnh bộ đệm và đặc tính hóa khối lượng công việc. Điều thứ hai có thể dẫn đến những thắng lợi tinh chỉnh cao nhất bằng cách xác định và loại bỏ các công việc không cần thiết. Phần này bao gồm các tham số tinh chỉnh (tunables) cụ thể.

Các chi tiết cụ thể của việc tinh chỉnh—các tùy chọn có sẵn và những gì cần thiết lập—phụ thuộc vào phiên bản hệ điều hành, loại hệ thống tập tin, và khối lượng công việc dự kiến. Các phần sau đây cung cấp các ví dụ về những gì có thể khả dụng và tại sao chúng có thể cần được tinh chỉnh. Tôi đề cập đến các lệnh gọi ứng dụng và hai loại hệ thống tập tin ví dụ: ext4 và ZFS. Để tinh chỉnh page cache, hãy xem Chương 7, Bộ nhớ.

### 8.8.1 Các lệnh gọi ứng dụng
Mục 8.3.7, Các lệnh ghi đồng bộ, đã đề cập đến cách hiệu năng của các khối lượng công việc ghi đồng bộ có thể được cải thiện bằng cách sử dụng fsync(2) để flush một nhóm logic các lệnh ghi, thay vì thực hiện riêng lẻ khi sử dụng các cờ open(2) O_DSYNC/O_RSYNC.

Các lệnh gọi khác có thể cải thiện hiệu năng bao gồm posix_fadvise() và madvise(2), thứ cung cấp các gợi ý (hints) cho sự đủ điều kiện của bộ đệm.

**posix_fadvise()**
Lệnh gọi thư viện này (một wrapper cho syscall fadvise64(2)) vận hành trên một vùng của một tập tin và có nguyên mẫu hàm:
`int posix_fadvise(int fd, off_t offset, off_t len, int advice);`

Lời khuyên (advice) có thể như trình bày trong Bảng 8.8.

Bảng 8.8 Các cờ advice của posix_fadvise() trong Linux
| Advice | Mô tả |
| --- | --- |
| POSIX_FADV_SEQUENTIAL | Dải dữ liệu được chỉ định sẽ được truy cập một cách tuần tự. |
| POSIX_FADV_RANDOM | Dải dữ liệu được chỉ định sẽ được truy cập một cách ngẫu nhiên. |
| POSIX_FADV_NOREUSE | Dữ liệu sẽ không được sử dụng lại. |
| POSIX_FADV_WILLNEED | Dữ liệu sẽ được sử dụng lại trong tương lai gần. |
| POSIX_FADV_DONTNEED | Dữ liệu sẽ không được sử dụng lại trong tương lai gần. |

Kernel có thể sử dụng thông tin này để cải thiện hiệu năng, giúp nó quyết định thời điểm tốt nhất để prefetch dữ liệu, và thời điểm tốt nhất để đệm dữ liệu. Điều này có thể cải thiện tỷ lệ trúng bộ đệm cho các dữ liệu ưu tiên cao hơn, như được ứng dụng khuyên. Hãy xem trang man trên hệ thống của bạn cho danh sách đầy đủ các đối số advice.

**madvise()**
Lệnh gọi hệ thống này vận hành trên một ánh xạ bộ nhớ và có tóm tắt:
`int madvise(void *addr, size_t length, int advice);`

Lời khuyên có thể như trình bày trong Bảng 8.9.

Bảng 8.9 Các cờ advice của madvise(2) trong Linux
| Advice | Mô tả |
| --- | --- |
| MADV_RANDOM | Các offset sẽ được truy cập theo thứ tự ngẫu nhiên. |
| MADV_SEQUENTIAL | Các offset sẽ được truy cập theo thứ tự tuần tự. |
| MADV_WILLNEED | Dữ liệu sẽ cần thiết lần nữa (vui lòng đệm). |
| MADV_DONTNEED | Dữ liệu sẽ không cần thiết lần nữa (không cần phải đệm). |

Cũng như với posix_fadvise(), kernel có thể sử dụng thông tin này để cải thiện hiệu năng, bao gồm cả việc đưa ra các quyết định đệm tốt hơn.

### 8.8.2 ext4
Trên Linux, các hệ thống tập tin ext2, ext3, và ext4 có thể được tinh chỉnh theo một trong bốn cách:
- Các tùy chọn mount
- Lệnh tune2fs(8)
- Các tập tin thuộc tính /sys/fs/ext4
- Lệnh e2fsck(8)

**mount và tune2fs**
Các tùy chọn mount có thể được thiết lập tại thời điểm mount, hoặc thủ công với lệnh mount(8), hoặc tại thời điểm khởi động trong /boot/grub/menu.lst và /etc/fstab. Các tùy chọn có sẵn nằm trong các trang man cho mount(8). Một số tùy chọn ví dụ:
- **atime:** Không sử dụng tính năng noatime, vì vậy thời gian truy cập inode được kiểm soát bởi các mặc định của kernel. Xem thêm các mô tả về tùy chọn mount relatime và strictatime.
- **noatime:** Không cập nhật các dấu thời gian truy cập inode trên hệ thống tập tin này (ví dụ: để truy cập nhanh hơn trên news spool để tăng tốc các máy chủ tin tức).
- **relatime:** Cập nhật các dấu thời gian truy cập inode tương đối so với thời gian sửa đổi (modify) hoặc thay đổi (change). Thời gian truy cập chỉ được cập nhật nếu thời gian truy cập trước đó sớm hơn thời gian sửa đổi hoặc thay đổi hiện tại. (Tương tự như noatime, nhưng nó không làm hỏng mutt hoặc các ứng dụng khác cần biết liệu một tập tin đã được đọc kể từ lần cuối cùng nó được sửa đổi hay chưa.) Kể từ Linux 2.6.30, kernel mặc định theo hành vi được cung cấp bởi tùy chọn này (trừ khi noatime được chỉ định), và tùy chọn strictatime là bắt buộc để có được các ngữ nghĩa truyền thống. Ngoài ra, kể từ Linux 2.6.30, thời gian truy cập cuối cùng của tập tin luôn được cập nhật nếu nó đã cũ hơn 1 ngày.

Tùy chọn noatime trong lịch sử đã được sử dụng để cải thiện hiệu năng bằng cách tránh các cập nhật dấu thời gian truy cập và các I/O đĩa liên quan của chúng. Như được mô tả trong kết quả này, relatime hiện là mặc định, thứ cũng làm giảm các cập nhật này.

Trang man mount(8) bao gồm cả các tùy chọn mount chung và các tùy chọn mount cụ thể cho hệ thống tập tin; tuy nhiên, trong trường hợp của ext4, các tùy chọn mount cụ thể cho hệ thống tập tin có trang man riêng của chúng, ext4(5).

Các thiết lập mount hiện tại có thể được thấy bằng cách sử dụng `tune2fs -l device` và `mount` (không có tùy chọn). tune2fs(8) có thể thiết lập hoặc xóa các tùy chọn mount khác nhau, như được mô tả bởi trang man của chính nó.

Một tùy chọn mount được sử dụng phổ biến để cải thiện hiệu năng là noatime: nó tránh các cập nhật dấu thời gian truy cập tập tin, thứ—nếu không cần thiết cho người dùng hệ thống tập tin—sẽ làm giảm I/O phía sau (back-end).

**/sys/fs Property Files**
Một số tunables bổ sung có thể được thiết lập trực tiếp qua hệ thống tập tin /sys. Cho ext4:
```bash
# cd /sys/fs/ext4/nvme0n1p1
# ls
delayed_allocation_blocks      last_error_time            msg_ratelimit_burst
err_ratelimit_burst            lifetime_write_kbytes      msg_ratelimit_interval_ms
err_ratelimit_interval_ms      max_writeback_mb_bump      reserved_clusters
errors_count                   mb_group_prealloc          session_write_kbytes
extent_max_zeroout_kb          mb_max_to_scan             trigger_fs_error
first_error_time               mb_min_to_scan             warning_ratelimit_burst
inode_goal                     mb_order2_req              warning_ratelimit_interval_ms
inode_readahead_blks           mb_stats
journal_task                   mb_stream_req
# cat inode_readahead_blks
32
```
Kết quả này cho thấy ext4 sẽ đọc trước tối đa 32 khối bảng inode. Không phải tất cả các tập tin này đều là các tunables: một số chỉ dành cho thông tin. Chúng được tài liệu hóa trong mã nguồn Linux dưới Documentation/admin-guide/ext4.rst [Linux 20h], thứ cũng tài liệu hóa các tùy chọn mount.

**e2fsck**
Cuối cùng, lệnh e2fsck(8) có thể được sử dụng để đánh chỉ mục lại các thư mục trong một hệ thống tập tin ext4, thứ có thể giúp cải thiện hiệu năng. Ví dụ:
`e2fsck -D -f /dev/hdX`
Các tùy chọn khác cho e2fsck(8) liên quan đến việc kiểm tra và sửa chữa một hệ thống tập tin.

### 8.8.3 ZFS
ZFS hỗ trợ một số lượng lớn các tham số có thể tinh chỉnh (được gọi là các thuộc tính - properties) cho mỗi hệ thống tập tin, với một số lượng nhỏ hơn có thể được thiết lập trên toàn hệ thống. Những thứ này có thể được liệt kê bằng lệnh zfs(1). Ví dụ:
```bash
# zfs get all zones/var
NAME         PROPERTY                 VALUE                     SOURCE
[...]
zones/var    recordsize               128K                      default
zones/var    mountpoint               legacy                    local
zones/var    sharenfs                 off                       default
zones/var    checksum                 on                        default
zones/var    compression              off                       inherited from zones
zones/var    atime                    off                       inherited from zones
[...]
```
Kết quả (đã bị lược bớt) bao gồm các cột cho tên thuộc tính, giá trị hiện tại, và nguồn gốc (source). Nguồn cho thấy cách nó đã được thiết lập: liệu nó được kế thừa từ một dataset ZFS cấp cao hơn, là mặc định, hay được thiết lập cục bộ cho hệ thống tập tin đó.

Các tham số cũng có thể được thiết lập bằng cách sử dụng lệnh zfs(1M) và được mô tả trong trang man của nó. Các tham số then chốt liên quan đến hiệu năng được liệt kê trong Bảng 8.10.

Bảng 8.10 Các tham số tinh chỉnh then chốt của dataset ZFS
| Tham số | Các tùy chọn | Mô tả |
| --- | --- | --- |
| recordsize | 512 đến 128 K | Kích thước khối được gợi ý cho các tập tin |
| compression | on \| off \| lzjb \| gzip \| gzip-[1–9] \| zle \| lz4 | Các thuật toán nhẹ (ví dụ: lzjb) có thể cải thiện hiệu năng trong một số tình huống, bằng cách làm giảm tắc nghẽn I/O phía sau |
| atime | on \| off | Các cập nhật dấu thời gian truy cập (gây ra một số lệnh ghi sau các lệnh đọc) |
| primarycache | all \| none \| metadata | Chính sách ARC; sự ô nhiễm bộ đệm do các hệ thống tập tin ưu tiên thấp (ví dụ: các kho lưu trữ) có thể được giảm bớt bằng cách sử dụng "none" hoặc "metadata" (chỉ siêu dữ liệu) |
| secondarycache | all \| none \| metadata | Chính sách L2ARC |
| logbias | latency \| throughput | Lời khuyên cho các lệnh ghi đồng bộ: "latency" sử dụng các thiết bị nhật ký, trong khi "throughput" sử dụng các thiết bị pool |
| sync | standard \| always \| disabled | Hành vi ghi đồng bộ |

Tham số quan trọng nhất cần tinh chỉnh thường là record size, để khớp với I/O của ứng dụng. Nó thường mặc định là 128 Kbyte, thứ có thể không hiệu quả cho các I/O nhỏ, ngẫu nhiên. Lưu ý rằng điều này không áp dụng cho các tập tin nhỏ hơn kích thước bản ghi, thứ được lưu bằng cách sử dụng kích thước bản ghi động bằng với độ dài tập tin của chúng. Việc vô hiệu hóa atime cũng có thể cải thiện hiệu năng nếu các dấu thời gian đó là không cần thiết.

ZFS cũng cung cấp các tunables trên toàn hệ thống, bao gồm cho việc tinh chỉnh thời gian đồng bộ transaction group (TXG) (zfs_txg_synctime_ms, zfs_txg_timeout), và một ngưỡng cho các metaslabs để chuyển sang việc cấp phát tối ưu hóa không gian thay vì thời gian (metaslab_df_free_pct). Tinh chỉnh các TXG nhỏ hơn có thể cải thiện hiệu năng bằng cách giảm bớt sự tranh chấp và xếp hàng với các I/O khác.

Cũng như với các tunables kernel khác, hãy kiểm tra tài liệu của chúng cho danh sách đầy đủ, các mô tả, và các cảnh báo.

---

## 8.9 Các bài tập (Exercises)
1. Trả lời các câu hỏi sau về thuật ngữ hệ thống tập tin:
   - Sự khác biệt giữa I/O logic và I/O vật lý là gì?
   - Sự khác biệt giữa I/O ngẫu nhiên và tuần tự là gì?
   - Direct I/O là gì?
   - Non-blocking I/O là gì?
   - Kích thước tập làm việc (working set size) là gì?

2. Trả lời các câu hỏi khái niệm sau:
   - Vai trò của VFS là gì?
   - Mô tả độ trễ hệ thống tập tin, cụ thể là nơi nó có thể được đo lường từ đó.
   - Mục đích của prefetch (read-ahead) là gì?
   - Mục đích của direct I/O là gì?

3. Trả lời các câu hỏi sâu hơn sau:
   - Mô tả các lợi thế của việc sử dụng fsync(2) so với O_SYNC.
   - Mô tả các điểm mạnh và điểm yếu của mmap(2) so với read(2)/write(2).
   - Mô tả các lý do tại sao I/O logic trở nên bị thổi phồng (inflated) vào thời điểm nó trở thành I/O vật lý.
   - Mô tả các lý do tại sao I/O logic trở nên bị giảm bớt (deflated) vào thời điểm nó trở thành I/O vật lý.
   - Giải thích cách thức copy-on-write hệ thống tập tin có thể cải thiện hiệu năng.

4. Phát triển các quy trình sau cho hệ điều hành của bạn:
   - Một checklist tinh chỉnh bộ đệm hệ thống tập tin. Điều này nên liệt kê các bộ đệm hệ thống tập tin hiện có, cách kiểm tra kích thước và mức sử dụng hiện tại của chúng, và tỷ lệ trúng.
   - Một checklist đặc tính hóa khối lượng công việc cho các thao tác hệ thống tập tin. Bao gồm cách lấy mỗi chi tiết, và cố gắng sử dụng các công cụ quan sát hệ điều hành hiện có trước tiên.

5. Thực hiện các nhiệm vụ sau:
   - Chọn một ứng dụng, và đo lường các thao tác hệ thống tập tin và độ trễ. Bao gồm:
     - Phân phối đầy đủ của độ trễ thao tác hệ thống tập tin, không chỉ giá trị trung bình.
     - Phần của mỗi giây mà mỗi luồng ứng dụng dành cho các thao tác hệ thống tập tin.
   - Sử dụng một công cụ micro-benchmark, xác định kích thước của bộ đệm hệ thống tập tin bằng thực nghiệm. Giải thích các lựa chọn của bạn khi sử dụng công cụ. Đồng thời chỉ ra sự suy giảm hiệu năng (sử dụng bất kỳ chỉ số nào) khi tập làm việc không còn được đệm nữa.

6. (tùy chọn, nâng cao) Phát triển một công cụ quan sát cung cấp các chỉ số cho các lệnh ghi hệ thống tập tin đồng bộ so với bất đồng bộ. Điều này nên bao gồm tốc độ và độ trễ của chúng và có khả năng xác định PID tiến trình đã phát ra chúng, khiến nó phù hợp cho việc đặc tính hóa khối lượng công việc.

7. (tùy chọn, nâng cao) Phát triển một công cụ để cung cấp các thống kê cho I/O hệ thống tập tin gián tiếp và bị thổi phồng: các byte và I/O bổ sung không được phát trực tiếp bởi các ứng dụng. Công cụ nên phân tích I/O bổ sung này thành các loại khác nhau để giải thích lý do của chúng.

---

## 8.10 Các tài liệu tham khảo (References)
- [Ritchie 74] Ritchie, D. M., and Thompson, K., “The UNIX Time-Sharing System,” Communications of the ACM 17, no. 7, pp. 365–75, July 1974
- [Lions 77] Lions, J., A Commentary on the Sixth Edition UNIX Operating System, University of New South Wales, 1977.
- [McKusick 84] McKusick, M. K., Joy, W. N., Leffler, S. J., and Fabry, R. S., “A Fast File System for UNIX.” ACM Transactions on Computer Systems (TOCS) 2, no. 3, August 1984.
- [Bach 86] Bach, M. J., The Design of the UNIX Operating System, Prentice Hall, 1986.
- [Bray 90] Bray, T., “Bonnie,” http://www.textuality.com/bonnie, 1990.
- [Sweeney 96] Sweeney, A., “Scalability in the XFS File System,” USENIX Annual Technical Conference, 1996.
- [Vahalia 96] Vahalia, U., UNIX Internals: The New Frontiers, Prentice Hall, 1996.
- [Coker 01] Coker, R., “bonnie++,” https://www.coker.com.au/bonnie++, 2001.
- [XFS 06] “XFS User Guide,” 2006.
- [Gregg 09a] Gregg, B., “L2ARC Screenshots,” http://www.brendangregg.com/blog/2009-01-30/l2arc-screenshots.html, 2009.
- [Corbet 10] Corbet, J., “Dcache scalability and RCU-walk,” LWN.net, http://lwn.net/Articles/419811, 2010.
- [Doeppner 10] Doeppner, T., Operating Systems in Depth: Design and Programming, Wiley, 2010.
- [XFS 10] “Runtime Stats,” https://xfs.org/index.php/Runtime_Stats, 2010.
- [Oracle 12] “ZFS Storage Pool Maintenance and Monitoring Practices,” Oracle Solaris Administration: ZFS File Systems, 2012.
- [Ahrens 19] Ahrens, M., “State of OpenZFS,” OpenZFS Developer Summit 2019, 2019.
- [Axboe 19] Axboe, J., “Efficient IO with io_uring,” https://kernel.dk/io_uring.pdf, 2019.
- [Gregg 19] Gregg, B., BPF Performance Tools: Linux System and Application Observability, Addison-Wesley, 2019.
- [Axboe 20] Axboe, J., “Flexible I/O Tester,” https://github.com/axboe/fio, last updated 2020.
- [Linux 20h] “ext4 General Information,” Linux documentation, 2020.
- [Torvalds 20a] Torvalds, L., “Re: Do not blame anyone. Please give polite, constructive criticism,” 2020.
