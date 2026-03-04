# Chương 11: Điện toán đám mây (Cloud Computing)

Sự trỗi dậy của điện toán đám mây giải quyết một số vấn đề cũ trong lĩnh vực hiệu năng trong khi tạo ra những vấn đề mới. Một môi trường đám mây có thể được tạo ra ngay lập tức và mở rộng theo nhu cầu, mà không có các chi phí thông thường của việc xây dựng và quản lý một trung tâm dữ liệu tại chỗ. Đám mây cũng cho phép độ chi tiết tốt hơn cho các lần triển khai—các phần của một máy chủ có thể được sử dụng bởi các khách hàng khác nhau khi cần thiết. Tuy nhiên, điều này mang lại những thách thức riêng của nó: chi phí hiệu năng của các công nghệ ảo hóa, và tranh chấp tài nguyên với các bên thuê lân cận.

Các mục tiêu học tập của chương này là:
- Hiểu kiến trúc điện toán đám mây và các ý nghĩa hiệu năng của nó.
- Hiểu các loại ảo hóa: phần cứng, OS, và phần cứng trọng lượng nhẹ.
- Trở nên quen thuộc với các thành phần nội bộ ảo hóa, bao gồm việc sử dụng các I/O proxies, và các kỹ thuật tinh chỉnh.
- Có kiến thức làm việc về các chi phí dự kiến cho các khối lượng công việc khác nhau dưới mỗi loại ảo hóa.
- Chẩn đoán các vấn đề hiệu năng từ máy chủ và khách, hiểu cách thức sử dụng công cụ có thể thay đổi tùy thuộc vào loại ảo hóa nào đang được sử dụng.

Trong khi toàn bộ cuốn sách này có thể áp dụng cho phân tích hiệu năng đám mây, chương này tập trung vào các chủ đề hiệu năng duy nhất của đám mây: cách các hypervisors và ảo hóa hoạt động, cách các kiểm soát tài nguyên có thể được áp dụng cho các khách, và cách khả năng quan sát hoạt động từ máy chủ và khách. Các nhà cung cấp đám mây thường cung cấp các dịch vụ và các APIs tùy chỉnh của riêng họ, thứ không được bao quát ở đây: hãy xem tài liệu mà mỗi nhà cung cấp đám mây cung cấp cho bộ dịch vụ riêng của họ.

Chương này bao gồm bốn phần chính:
- **Nền tảng (Background)** trình bày kiến trúc điện toán đám mây chung và các ý nghĩa hiệu năng của chúng.
- **Ảo hóa phần cứng (Hardware virtualization)** nơi một hypervisor quản lý nhiều thực thể hệ điều hành khách, mỗi cái chạy kernel riêng của nó với các thiết bị ảo hóa. Phần này sử dụng các hypervisors Xen, KVM, và Amazon Nitro làm ví dụ.
- **Ảo hóa OS (OS virtualization)** nơi một kernel duy nhất quản lý hệ thống, tạo ra các thực thể OS ảo được cô lập với nhau. Phần này sử dụng Linux containers làm ví dụ.
- **Ảo hóa phần cứng trọng lượng nhẹ (Lightweight hardware virtualization)** cung cấp một giải pháp tốt-nhất-của-cả-hai-thế giới, nơi các thực thể ảo hóa phần cứng trọng lượng nhẹ chạy với các kernels chuyên dụng, với thời gian boot và lợi ích mật độ tương tự như các containers. Phần này sử dụng AWS Firecracker làm hypervisor ví dụ.

Các công nghệ ảo hóa được sắp xếp theo thời điểm chúng được đưa vào sử dụng rộng rãi trong đám mây. Ví dụ, Amazon Elastic Compute Cloud (EC2) đã cung cấp các thực thể ảo hóa phần cứng vào năm 2006, các OS virtualized containers vào năm 2017 (Amazon Fargate), và các máy ảo hóa trọng lượng nhẹ vào năm 2019 (Amazon Firecracker).

## 11.1 Nền tảng (Background)
Điện toán đám mây cho phép các tài nguyên tính toán được phân phối như một dịch vụ, mở rộng từ các phần nhỏ của một máy chủ tới các hệ thống đa máy chủ. Các khối xây dựng của đám mây của bạn tùy thuộc vào mức độ của stack phần mềm được cài đặt và cấu hình. Chương này tập trung vào các dịch vụ đám mây sau đây, cả hai đều cung cấp *server instances* có thể là:
- **Các thực thể phần cứng (Hardware instances):** Còn được gọi là *infrastructure as a service* (IaaS), được cung cấp bằng cách sử dụng ảo hóa phần cứng. Mỗi thực thể máy chủ là một máy ảo.
- **Các thực thể OS (OS instances):** Cho việc cung cấp các thực thể trọng lượng nhẹ, thông thường qua ảo hóa OS.

Cùng với nhau, những thứ này có thể được đề cập đến như *server instances*, *cloud instances*, hoặc chỉ là *instances*. Các ví dụ về các nhà cung cấp đám mây hỗ trợ những thứ này là Amazon Web Services (AWS), Microsoft Azure, và Google Cloud Platform (GCP). Cũng có các loại đám mây sơ khai khác bao gồm các chức năng như một dịch vụ (FaaS) (xem Mục 11.5, Các loại khác).

Để tóm tắt thuật ngữ đám mây then chốt: *cloud computing* mô tả một framework cung cấp động cho các thực thể. Một hoặc nhiều thực thể chạy dưới dạng *guests* (khách) của một *host* (máy chủ) hệ thống vật lý. Các khách cũng được gọi là *tenants* (bên thuê), và thuật ngữ *multitenancy* được sử dụng để mô tả việc chúng chạy trên cùng một máy chủ. Máy chủ có thể được quản lý bởi các nhà cung cấp đám mây vận hành một *public cloud*, hoặc có thể được quản lý bởi công ty của bạn cho việc sử dụng nội bộ như một phần của một *private cloud*. Một số công ty xây dựng một *hybrid cloud* trải dài cả các đám mây công cộng và riêng tư. Các khách đám mây (bên thuê) được quản lý bởi những người dùng cuối của họ.

Đối với ảo hóa phần cứng, một công nghệ được gọi là *hypervisor* (hoặc *virtual machine monitor*, VMM) tạo ra và quản lý các thực thể *virtual machine*, thứ xuất hiện như các máy tính chuyên dụng và cho phép toàn bộ các hệ điều hành và các kernels được cài đặt.

Các thực thể thông thường có thể được tạo ra (và bị hủy bỏ) trong vài phút hoặc vài giây và ngay lập tức được đưa vào sử dụng sản xuất. Một *cloud API* thường được cung cấp sao cho việc cung cấp này có thể được tự động hóa bởi một chương trình khác.

Điện toán đám mây có thể được hiểu sâu hơn bằng cách thảo luận về các chủ đề liên quan đến hiệu năng khác nhau: các loại thực thể, tinh chỉnh, quy hoạch dung lượng, lưu trữ, và đa thuê. Những nội dung này được tóm tắt trong các phần sau đây.

### 11.1.1 Các loại thực thể (Instance Types)
Các nhà cung cấp đám mây thường cung cấp các loại thực thể và kích thước khác nhau.

Một số loại thực thể là chung và được cân bằng trên các tài nguyên. Những cái khác có thể được tối ưu hóa cho một tài nguyên nhất định: bộ nhớ, CPUs, đĩa, v.v. Như một ví dụ, AWS nhóm các loại thực thể thành các "families" (được viết tắt bằng một ký tự) và các thế hệ (một con số), hiện tại đang cung cấp:
- **m5:** Mục đích chung (cân bằng)
- **c5:** Tối ưu hóa tính toán
- **i3, d2:** Tối ưu hóa lưu trữ
- **r4, x1:** Tối ưu hóa bộ nhớ
- **p1, g3, f1:** Tính toán tăng tốc (GPUs, FPGAs, v.v.)

Bên trong mỗi họ thực thể có một sự đa dạng về kích thước. Họ AWS m5, ví dụ, trải dài từ m5.large (2 vCPUs và 8 Gbytes bộ nhớ chính) tới m5.24xlarge (hai mươi tư lần cực lớn: 96 vCPUs và 384 Gbytes bộ nhớ chính).

Thường có một tỷ lệ giá cả/hiệu năng khá nhất quán trên các kích thước, cho phép khách hàng chọn kích thước phù hợp nhất với khối lượng công việc của họ.

Một số nhà cung cấp, chẳng hạn như Google Cloud Platform, cũng cung cấp các loại máy tùy chỉnh nơi lượng tài nguyên có thể được lựa chọn.

Với rất nhiều tùy chọn và sự dễ dàng của việc tái triển khai các thực thể, loại thực thể đã trở thành giống như một tham số tinh chỉnh có thể được sửa đổi khi cần thiết. Đây là một cải tiến lớn so với mô hình doanh nghiệp truyền thống của việc lựa chọn và đặt hàng phần cứng vật lý mà công ty có lẽ sẽ không thể thay đổi trong nhiều năm.

### 11.1.2 Kiến trúc có khả năng mở rộng (Scalable Architecture)
Các môi trường doanh nghiệp trong lịch sử đã sử dụng một cách tiếp cận *vertical scalability* (mở rộng theo chiều dọc) để xử lý tải: xây dựng các hệ thống đơn lẻ lớn hơn (mainframes). Cách tiếp cận này có các hạn chế của nó. Có một giới hạn thực tế về kích thước vật lý mà một máy tính có thể được xây dựng (thứ có thể bị giới hạn bởi kích thước của cửa thang máy hoặc các thùng vận chuyển), và có các khó khăn ngày càng tăng với tính nhất quán của bộ đệm ẩn CPU khi số lượng CPU tăng lên, cũng như điện năng và làm mát. Giải pháp cho những hạn chế này là mở rộng tải qua nhiều hệ thống (có lẽ nhỏ); điều này được gọi là *horizontal scalability* (mở rộng theo chiều ngang). Trong doanh nghiệp, nó đã được sử dụng cho các cụm máy tính (computer farms), đặc biệt với tính toán hiệu năng cao (HPC), nơi việc sử dụng nó có trước đám mây.

Điện toán đám mây cũng dựa trên khả năng mở rộng theo chiều ngang. Một môi trường ví dụ được trình bày trong Hình 11.1, bao gồm các trình cân bằng tải, các máy chủ web, các máy chủ ứng dụng, và các cơ sở dữ liệu.

(Hình 11.1 Kiến trúc đám mây: mở rộng theo chiều ngang)

Mỗi tầng môi trường bao gồm một hoặc nhiều máy chủ chạy song song, với nhiều cái hơn được thêm vào để xử lý tải. Các thực thể có thể được thêm vào riêng lẻ, hoặc kiến trúc có thể được chia thành các phân vùng dọc (vertical partitions), nơi một nhóm bao gồm các máy chủ cơ sở dữ liệu, các máy chủ ứng dụng, và các máy chủ web được coi như một đơn vị duy nhất.

Một thách thức của mô hình này là việc triển khai các cơ sở dữ liệu truyền thống, nơi một cơ sở dữ liệu thực thể phải là sơ cấp. Dữ liệu cho những cơ sở dữ liệu này, chẳng hạn như MySQL, có thể được chia tách logic thành các nhóm được gọi là *shards*, mỗi cái trong số đó được quản lý bởi cơ sở dữ liệu của riêng nó (hoặc cặp sơ cấp/thứ cấp). Các kiến trúc cơ sở dữ liệu phân tán, chẳng hạn như Riak, xử lý việc thực thi song song một cách linh động, trải rộng tải qua các thực thể khả dụng. Hiện nay có các cơ sở dữ liệu *cloud-native*, được thiết kế để sử dụng trên đám mây, bao gồm Cassandra, CockroachDB, Amazon Aurora, và Amazon DynamoDB.

Với kích thước thực thể trên-mỗi-máy chủ thông thường là nhỏ, ví dụ, 8 Gbytes (trên các host vật lý với 512 Gbytes hoặc nhiều hơn của DRAM), khả năng mở rộng chi tiết có thể được sử dụng để đạt được giá cả/hiệu năng tối ưu, thay vì đầu tư trả trước vào các hệ thống khổng lồ thứ có thể chủ yếu ở trạng thái rảnh rỗi.

### 11.1.3 Quy hoạch Dung lượng (Capacity Planning)
Các máy chủ tại chỗ có thể là một chi phí hạ tầng đáng kể, cho cả phần cứng và phí dịch vụ có thể kéo dài trong nhiều năm. Nó cũng có thể mất nhiều tháng cho các máy chủ mới để được đưa vào sản xuất: thời gian dành cho các đợt phê duyệt, chờ đợi cho việc có hàng bộ phận, vận chuyển, lắp đặt, cài đặt, và kiểm tra. Quy hoạch dung lượng là cực kỳ quan trọng, sao cho các hệ thống có kích thước phù hợp được mua: quá nhỏ có nghĩa là thất bại, quá lớn là tốn kém (và, với các phí dịch vụ, có thể tốn kém cho nhiều năm sau đó). Quy hoạch dung lượng cũng là cần thiết để dự đoán các sự gia tăng trong nhu cầu từ trước, sao cho các thủ tục mua sắm dài hơi có thể được hoàn thành kịp thời.

Mức chi phí cho các thực thể máy chủ đám mây là khác nhau. Các thực thể máy chủ không tốn kém, và có thể được tạo ra và bị hủy bỏ gần như ngay lập tức. Thay vì dành thời gian quy hoạch những gì có thể là cần thiết, các công ty có thể tăng số lượng thực thể họ sử dụng *khi cần thiết*, phản ứng lại tải thực tế. Việc này có thể được thực hiện tự động qua cloud API, dựa trên các chỉ số từ phần mềm giám sát hiệu năng. Một doanh nghiệp nhỏ hoặc startup có thể phát triển từ một thực thể duy nhất tới hàng nghìn thực thể, mà không cần một nghiên cứu quy hoạch dung lượng chi tiết như sẽ được kỳ vọng trong các môi trường doanh nghiệp.

Đối với các startups đang phát triển, một yếu tố khác cần cân nhắc là tốc độ thay đổi mã. Các trang web thường cập nhật mã sản xuất của họ hàng tuần, hàng ngày, hoặc thậm chí nhiều lần một ngày. Một quy hoạch dung lượng có thể mất nhiều tuần và, bởi vì nó dựa trên một ảnh chụp nhanh của các chỉ số hiệu năng, có thể bị lỗi thời vào lúc nó được hoàn thành. Điều này khác biệt so với các môi trường doanh nghiệp chạy các phần mềm thương mại, thứ có thể không thay đổi quá một vài lần mỗi năm.

Các hoạt động được thực hiện trong đám mây cho quy hoạch dung lượng bao gồm:
- **Dynamic sizing:** Tự động thêm và loại bỏ các thực thể máy chủ
- **Scalability testing:** Mua một môi trường đám mây lớn trong một thời lượng ngắn, nhằm kiểm tra khả năng mở rộng chống lại tải tổng hợp (đây là một hoạt động benchmarking)

Ghi nhớ các giới hạn thời gian, cũng có tiềm năng cho việc mô phỏng khả năng mở rộng (tương tự như các nghiên cứu doanh nghiệp) để ước tính khả năng mở rộng thực sự rơi xuống mức nào so với nơi nó đáng lẽ phải ở theo lý thuyết.

**Dynamic Sizing (Auto Scaling)**
Các nhà cung cấp đám mây thường hỗ trợ triển khai các nhóm các thực thể máy chủ có thể tự động chia tỉ lệ khi tải tăng lên (ví dụ: một AWS auto scaling group (ASG)). Điều này cũng hỗ trợ một kiến trúc microservice, nơi ứng dụng được chia thành các phần mạng nhỏ hơn có thể được chia tỉ lệ riêng lẻ khi cần thiết.

Auto scaling có thể giải quyết nhu cầu phản hồi nhanh chóng với các thay đổi trong tải, nhưng nó cũng mang lại rủi ro cung cấp quá mức (*over-provisioning*), như được mô tả trong Hình 11.2. Ví dụ, một cuộc tấn công DoS có thể xuất hiện như một sự gia tăng trong tải, kích hoạt một sự gia tăng tốn kém trong các thực thể máy chủ. Có một rủi ro tương tự với các thay đổi ứng dụng làm giảm hiệu năng, yêu cầu thêm nhiều thực thể để xử lý cùng một lượng tải. Giám sát là quan trọng để xác minh rằng những sự gia tăng này mang lại ý nghĩa.

(Hình 11.2 Chia tỉ lệ linh động)

Các nhà cung cấp đám mây tính phí theo giờ, phút, hoặc thậm chí từng giây, cho phép người dùng mở rộng lên *và xuống* nhanh chóng. Các chi phí tiết kiệm được có thể được nhận diện ngay lập tức khi họ thu nhỏ quy mô. Điều này có thể được tự động hóa sao cho số lượng thực thể khớp với một mẫu hàng ngày, chỉ cung cấp đủ dung lượng cho mỗi phút trong ngày khi cần thiết. Netflix thực hiện điều này cho đám mây của họ, thêm và loại bỏ hàng chục nghìn thực thể hàng ngày để khớp với mẫu truyền phát hàng ngày của họ, một ví dụ về điều này được trình bày trong Hình 11.3 [Gregg 14b].

(Hình 11.3 Các dòng truyền phát Netflix mỗi giây)

Như các ví dụ khác, vào tháng 12 năm 2012, Pinterest đã báo cáo việc cắt giảm chi phí từ $54/giờ xuống $20/giờ bằng cách tự động tắt hệ thống đám mây của họ sau giờ cao điểm để phản hồi tải lưu lượng [Hoff 12], và vào năm 2018 Shopify đã chuyển sang đám mây và thấy sự tiết kiệm hạ tầng lớn: các máy chủ di chuyển với mức trung bình thời gian rảnh rỗi 61% tới các thực thể đám mây với mức trung bình thời gian rảnh rỗi 19% [Kwiatkowski 19]. Tiết kiệm ngay lập tức cũng có thể là kết quả của việc tinh chỉnh hiệu năng, nơi số lượng thực thể cần thiết để xử lý tải bị giảm bớt.

Một số kiến trúc đám mây (xem Mục 11.3, Ảo hóa OS) có thể phân bổ linh động thêm nhiều tài nguyên CPU hơn, nếu có sẵn, bằng cách sử dụng một chiến lược được gọi là *bursting*. Điều này có thể được cung cấp mà không tốn thêm chi phí và nhằm mục đích giúp ngăn chặn việc cung cấp quá mức bằng cách cung cấp một bộ đệm trong quá trình tải tăng lên, thứ có thể được kiểm tra để xác định liệu nó có thực sự và có khả năng tiếp tục hay không. Nếu có, thêm nhiều thực thể hơn có thể được cung cấp sao cho các tài nguyên được đảm bảo tiếp tục duy trì.

Bất kỳ kỹ thuật nào trong số này đều nên hiệu quả hơn đáng kể so với các môi trường doanh nghiệp—đặc biệt là những nơi có kích thước cố định được chọn để xử lý tải cao điểm dự kiến cho tuổi thọ của máy chủ: những máy chủ như vậy chạy chủ yếu rảnh rỗi.

### 11.1.4 Lưu trữ (Storage)
Một thực thể đám mây yêu cầu lưu trữ cho OS, phần mềm ứng dụng, và các tập tin tạm thời. Trên các hệ thống Linux, đây là gốc (root) và các phân vùng khác. Những thứ này có thể được phục vụ bởi lưu trữ vật lý cục bộ hoặc bằng lưu trữ mạng. Lưu trữ này là tạm thời và bị phá hủy khi thực thể bị hủy bỏ (và được gọi là *ephemeral drives*). Đối với lưu trữ bền vững, một dịch vụ độc lập thường được sử dụng, thứ cung cấp lưu trữ tới các thực thể dưới dạng hoặc:
- **Kho lưu trữ tập tin (File store):** Ví dụ, các tập tin qua NFS
- **Kho lưu trữ khối (Block store):** Chẳng hạn như các khối qua iSCSI
- **Kho lưu trữ đối tượng (Object store):** Qua một API, thường dựa trên HTTP

Những thứ này vận hành qua một mạng, và cả hạ tầng mạng và các thiết bị lưu trữ đều được chia sẻ với các bên thuê khác. Vì những lý do này, hiệu năng có thể kém dự đoán hơn nhiều so với các đĩa cục bộ, mặc dù tính nhất quán hiệu năng có thể được cải thiện bằng việc sử dụng các kiểm soát tài nguyên bởi nhà cung cấp đám mây.

Các nhà cung cấp đám mây thường cung cấp các dịch vụ riêng của họ cho những thứ này. Ví dụ, Amazon cung cấp Amazon Elastic File System (EFS) như một kho lưu trữ tập tin, Amazon Elastic Block Store (EBS) như một kho lưu trữ khối, và Amazon Simple Storage Service (S3) như một kho lưu trữ đối tượng.

Cả lưu trữ cục bộ và mạng đều được hình ảnh hóa trong Hình 11.4.

(Hình 11.4 Lưu trữ đám mây)

Độ trễ gia tăng cho việc truy cập lưu trữ mạng thường được giảm thiểu bằng cách sử dụng các bộ đệm ẩn trong bộ nhớ cho dữ liệu được truy cập thường xuyên.

Một số dịch vụ lưu trữ cho phép một tốc độ IOPS được mua khi hiệu năng đáng tin cậy là mong muốn (ví dụ: Amazon EBS Provisioned IOPS volume).

### 11.1.5 Đa thuê (Multitenancy)
Unix là một hệ điều hành đa nhiệm, được thiết kế để đối phó với nhiều người dùng và các tiến trình truy cập cùng các tài nguyên. Các sự bổ sung sau này của Linux đã cung cấp các giới hạn và kiểm soát tài nguyên để chia sẻ các tài nguyên này một cách công bằng hơn, và khả năng quan sát để xác định và định lượng khi nào có các vấn đề hiệu năng liên quan đến tranh chấp tài nguyên.

Điện toán đám mây khác biệt ở chỗ toàn bộ các thực thể hệ điều hành có thể cùng tồn tại trên cùng một hệ thống vật lý. Mỗi khách là hệ thống điều hành được cô lập của chính nó: các khách (thông thường) không thể quan sát người dùng và các tiến trình từ những khách khác trên cùng một host—thứ sẽ được coi là một rò rỉ thông tin—mặc dù họ chia sẻ cùng các tài nguyên vật lý.

Vì các tài nguyên được chia sẻ giữa các bên thuê, các vấn đề hiệu năng có thể được gây ra bởi *noisy neighbors* (hàng xóm ồn ào). Ví dụ, một khách khác trên cùng một host có thể thực hiện một bản dump cơ sở dữ liệu đầy đủ trong thời gian tải cao điểm của họ, gây nhiễu cho lưu lượng đĩa và mạng của bạn. Tệ hơn, một người hàng xóm có thể đang đánh giá nhà cung cấp đám mây bằng cách thực hiện các micro-benchmarks nhằm làm bão hòa các tài nguyên một cách có chủ ý để tìm ra giới hạn của chúng.

Có một số giải pháp cho vấn đề này. Các hiệu ứng đa thuê có thể được kiểm soát bởi *resource management*: thiết lập các *resource controls* hệ điều hành cung cấp cách ly hiệu năng (performance isolation) (cũng được gọi là *resource isolation*). Điều này là nơi các giới hạn hoặc các mức ưu tiên cho mỗi bên thuê được áp đặt cho việc sử dụng các tài nguyên hệ thống: CPU, bộ nhớ, đĩa hoặc I/O hệ thống tập tin, và thông lượng mạng.

Bên cạnh việc giới hạn việc sử dụng tài nguyên, việc có khả năng quan sát tranh chấp đa thuê có thể giúp các nhà vận hành đám mây điều chỉnh các giới hạn và cân bằng tải tốt hơn cho các khách trên các máy chủ có sẵn. Mức độ quan sát tùy thuộc vào loại ảo hóa.

### 11.1.6 Điều phối (Kubernetes)
Nhiều công ty chạy các đám mây riêng của họ bằng cách sử dụng *orchestration software* chạy trên chính các phần cứng của riêng họ hoặc các hệ thống đám mây khác. Cái phổ biến nhất hiện nay là Kubernetes (được viết tắt là k8s), ban đầu được tạo ra bởi Google. Kubernetes, tiếng Hy Lạp của "Helmsman," là một hệ thống mã nguồn mở quản lý việc triển khai ứng dụng bằng cách sử dụng các containers (thông thường là các containers Docker, mặc dù bất kỳ runtime nào triển khai Open Container Interface cũng sẽ hoạt động, chẳng hạn như containerd) [Kubernetes 20b]. Các nhà cung cấp đám mây công cộng cũng đã tạo ra các dịch vụ Kubernetes để đơn giản hóa việc triển khai đối với các kiến trúc đó, bao gồm Google Kubernetes Engine (GKE), Amazon Elastic Kubernetes Service (Amazon EKS), và Microsoft Azure Kubernetes Service (AKS).

Kubernetes triển khai các containers dưới dạng các nhóm được đặt cùng nhau gọi là *Pods*, nơi các containers có thể chia sẻ tài nguyên và liên lạc với nhau cục bộ (localhost). Mỗi Pod có địa chỉ IP riêng của nó như một sự trừu tượng hóa cho các endpoints được cung cấp bởi một nhóm các Pods với siêu dữ liệu bao gồm một địa chỉ IP, và một sự tồn tại và giao diện ổn định cho các endpoints này, trong khi bản thân các Pods có thể bị thêm vào và loại bỏ, cho phép chúng được coi là dùng một lần (disposable). Các dịch vụ Kubernetes hỗ trợ kiến trúc microservices. Kubernetes bao gồm các chiến lược auto-scaling, chẳng hạn như "Horizontal Pod Autoscaler" thứ có thể mở rộng các bản sao (replicas) của một Pod dựa trên mức sử dụng tài nguyên mục tiêu hoặc chỉ số khác. Trong Kubernetes, các máy vật lý được gọi là *Nodes*, và một nhóm các Nodes thuộc về một Kubernetes *cluster* nếu chúng kết nối tới cùng một máy chủ Kubernetes API.

Các thách thức về hiệu năng trong Kubernetes bao gồm lập lịch (nơi chạy các containers trên một cluster để tối đa hóa hiệu năng), và hiệu năng mạng, khi các thành phần bổ sung được sử dụng để triển khai mạng container và cân bằng tải.

Đối với việc lập lịch, Kubernetes tính đến tài khoản CPU và các yêu cầu bộ nhớ cùng các giới hạn, và metadata chẳng hạn như *node taints* (nơi các Nodes được đánh dấu để loại trừ khỏi việc lập lịch) và *label selectors* (metadata tùy chỉnh). Kubernetes hiện không giới hạn I/O khối (hỗ trợ cho điều này, sử dụng blkio cgroup, có thể được thêm vào trong tương lai [Xu 20]) khiến cho việc tranh chấp đĩa trở thành một nguồn gây ra các vấn đề hiệu năng tiềm tàng.

Đối với mạng, Kubernetes cho phép các thành phần mạng khác nhau được sử dụng, và xác định thành phần nào để sử dụng là một hoạt động quan trọng để đảm bảo hiệu năng tối đa. Mạng container có thể được triển khai bằng phần mềm plugin container network interface (CNI); ví dụ phần mềm CNI bao gồm Calico, dựa trên netfilter hoặc iptables, và Cilium, dựa trên BPF. Cả hai đều là mã nguồn mở [Calico 20][Cilium 20b]. Cho cân bằng tải, Cilium cũng cung cấp một giải pháp thay thế BPF cho kube-proxy [Borkmann 19].

## 11.2 Ảo hóa phần cứng
Ảo hóa phần cứng tạo ra một máy ảo (VM) có thể chạy một toàn bộ hệ điều hành, bao gồm kernel của chính nó. Các VMs được tạo ra bởi các hypervisors, cũng được gọi là các trình quản lý máy ảo (VMMs). Một sự phân loại phổ biến của các hypervisors nhận diện chúng dưới dạng Type 1 hoặc 2 [Goldberg 73], đó là:
- **Type 1** thực thi trực tiếp trên các bộ xử lý. Quản trị Hypervisor có thể được thực hiện bởi một khách có đặc quyền thứ có thể tạo và khởi chạy các khách mới. Type 1 cũng được gọi là hypervisor *native* hoặc *bare-metal*. Điều này bao gồm trình lập lịch CPU riêng của nó cho các VMs khách. Một ví dụ là hypervisor Xen.
- **Type 2** được thực thi bên trong một OS host, thứ có các đặc quyền để quản trị hypervisor và khởi chạy các khách mới. Đối với loại này, hệ thống chạy một OS truyền thống thứ chạy phần mềm hypervisor. Việc lập lịch các khách được thực hiện bởi trình lập lịch CPU của host, và các khách xuất hiện như các tiến trình trên host.

Mặc dù bạn có thể vẫn gặp các thuật ngữ Type 1 và Type 2, với những tiến bộ trong các công nghệ hypervisor sự phân loại này không còn được áp dụng một cách nghiêm ngặt nữa [Liguori, 07]—Type 2 đã được làm giống như Type 1 bằng cách sử dụng các mô-đun kernel sao cho các phần của hypervisor có quyền truy cập trực tiếp vào phần cứng. Một sự phân loại thực tế hơn được trình bày trong Hình 11.5, minh họa hai cấu hình chung mà tôi đặt tên là Config A và B [Gregg 19].

(Hình 11.5 Các cấu hình hypervisor phổ biến)

Các cấu hình này là:
- **Config A:** Cũng được gọi là một hypervisor native hoặc bare-metal. Phần mềm hypervisor chạy trực tiếp trên các bộ xử lý, tạo ra các miền để chạy các máy ảo khách, và lập lịch các vCPUs khách ảo lên các CPUs thực. Một miền có đặc quyền (số 0 trong Hình 11.5) có thể quản trị những cái khác. Một ví dụ phổ biến là hypervisor Xen.
- **Config B:** Phần mềm hypervisor được thực thi bởi một OS host, và có thể được cấu tạo từ các mô-đun cấp kernel và các tiến trình cấp người dùng. Host OS có các đặc quyền để quản trị hypervisor, và các kernels khách của nó. VM vCPUs của nó cùng với các tiến trình khác trên host. Bằng cách sử dụng các mô-đun kernel, cấu hình này cũng cung cấp quyền truy cập trực tiếp vào phần cứng. Một ví dụ phổ biến là KVM hypervisor.

Cả hai cấu hình có thể liên quan đến một I/O proxy (ví dụ: sử dụng phần mềm QEMU) trong domain 0 (Xen) hoặc host OS (KVM), để phục vụ khách I/O. Điều này thêm các chi phí vào I/O, và qua nhiều năm đã được tối ưu hóa bằng cách thêm các truyền tải bộ nhớ chung và các kỹ thuật khác.

Trình hypervisor phần cứng gốc, tiên phong bởi VMware vào năm 1998, đã sử dụng *binary translations* để thực hiện ảo hóa phần cứng [VMware 07]. Điều này liên quan đến việc viết lại các chỉ lệnh có đặc quyền chẳng hạn như các syscalls và các thao tác bảng trang trước khi thực thi. Các chỉ lệnh không có đặc quyền có thể chạy trực tiếp trên bộ xử lý. Điều này cung cấp một hệ thống ảo hoàn chỉnh bao gồm các thành phần phần cứng không sửa đổi vào đó một hệ điều hành không sửa đổi có thể được cài đặt. Chi phí hiệu năng cao cho việc này thường có thể chấp nhận được cho sự tiết kiệm được cung cấp bởi việc hợp nhất máy chủ.

Điều này kể từ đó đã được cải thiện bởi:
- **Hỗ trợ ảo hóa bộ xử lý (Processor virtualization support):** Các phần mở rộng AMD-V và Intel VT-x đã được giới thiệu vào năm 2005–2006 để cung cấp hỗ trợ phần cứng nhanh hơn cho các thao tác VM bởi bộ xử lý. Những phần mở rộng này đã cải thiện tốc độ của các chỉ lệnh ảo hóa có đặc quyền và MMU.
- **Ảo hóa một phần (Paravirtualization - paravirt hoặc PV):** Cung cấp một hệ thống ảo bao gồm một giao diện cho hệ điều hành khách để sử dụng các tài nguyên host (qua *hypercalls*), mà không cần ảo hóa hoàn toàn tất cả các thành phần. Ví dụ, việc kích hoạt một bộ định thời thường liên quan đến nhiều chỉ lệnh có đặc quyền thứ phải được mô phỏng bởi hypervisor. Điều này có thể được đơn giản hóa thành một hypercall duy nhất để sử dụng bởi hệ thống paravirtualized, mang lại hiệu quả cao hơn cho hypervisor. Để hiệu quả hơn nữa, hypervisor Xen nhóm các hypercalls này thành một *multicall*. Paravirtualization có thể bao gồm việc sử dụng một trình điều khiển thiết bị paravirtualized bởi khách để truyền tải các gói tin mạng hiệu quả hơn tới mạng vật lý paravirtualization (thứ mà Windows trong lịch sử đã không cung cấp).
- **Hỗ trợ thiết bị phần cứng (Device hardware support):** Để tối ưu hóa hơn nữa hiệu năng VM, các bộ xử lý khác ngoài các bộ xử lý đã được thêm hỗ trợ máy ảo. Điều này bao gồm single root I/O virtualization (SR-IOV) cho các thiết bị mạng và lưu trữ, thứ cho phép các VMs khách truy cập trực tiếp phần cứng. Điều này yêu cầu sự hỗ trợ của trình điều khiển (các ví dụ về trình điều khiển là ixgbe, ena, hv_netvsc, và nvme).

Qua nhiều năm, Xen đã phát triển và cải thiện hiệu năng của nó. Các Xen VMs hiện đại thường boot trong chế độ ảo hóa phần cứng (HVM) và sau đó sử dụng các trình điều khiển PV với hỗ trợ HVM cho hiệu năng được cải thiện: một cấu hình được gọi là PVHVM. Điều này có thể được cải thiện hơn nữa bằng cách dựa hoàn toàn trên ảo hóa phần cứng cho một số trình điều khiển, chẳng hạn như SR-IOV cho mạng và các thiết bị lưu trữ.

### 11.2.1 Triển khai (Implementation)
Có nhiều triển khai khác nhau của ảo hóa phần cứng, và một số đã được đề cập (Xen và KVM). Các ví dụ là:
- **VMware ESX:** Lần đầu tiên phát hành vào năm 2001, VMware ESX là một sản phẩm dành cho doanh nghiệp cho việc hợp nhất máy chủ và là một thành phần then chốt của sản phẩm điện toán đám mây VMware vSphere. Hypervisor của nó là một microkernel chạy trực tiếp trên phần cứng (bare metal), và máy ảo đầu tiên được tạo ra được gọi là *service console*, thứ có thể quản trị hypervisor và các máy ảo mới.
- **Xen:** Lần đầu tiên phát hành vào năm 2003, Xen bắt đầu như một dự án nghiên cứu tại Đại học Cambridge và sau đó được mua lại bởi Citrix. Xen là một Type 1 hypervisor chạy các khách paravirtualized cho hiệu năng cao; hỗ trợ sau này đã được thêm vào cho các khách ảo hóa phần cứng cho sự hỗ trợ hệ điều hành không sửa đổi (Windows). Các miền ảo hóa được gọi là *domains*, với domain có đặc quyền nhất được gọi là *dom0*, từ đó hypervisor được quản trị và các miền mới được khởi chạy. Xen là mã nguồn mở và có thể được chạy từ Linux. Amazon Elastic Compute Cloud (EC2) trước đây dựa trên Xen.
- **Hyper-V:** Phát hành cùng với Windows Server 2008, Hyper-V là một Type 1 hypervisor tạo ra các *partitions* cho việc thực thi các hệ điều hành khách. Microsoft Azure public cloud có thể được coi như đang chạy một phiên bản Hyper-V tùy chỉnh (các chi tiết chính xác không được công bố công khai).
- **KVM:** Được phát triển bởi Qumranet, một startup đã được Red Hat mua lại vào năm 2008. KVM là một Type 2 hypervisor, thực thi như một mô-đun kernel. Nó hỗ trợ các phần mở rộng ảo hóa phần cứng và, cho hiệu năng cao, sử dụng paravirtualization cho một số thiết bị nhất định nơi được hỗ trợ bởi hệ điều hành khách. Để tạo ra một thực thể máy ảo ảo hóa phần cứng hoàn chỉnh, nó được ghép nối với một tiến trình người dùng mang tên QEMU (Quick Emulator), một VMM (VMM hypervisor) có thể tạo và quản lý các máy ảo. QEMU ban đầu là một hypervisor mã nguồn mở Type 2 chất lượng cao sử dụng binary translation, được viết bởi Fabrice Bellard. KVM là mã nguồn mở, và được sử dụng bởi Google cho Google Compute Engine [Google 20c].
- **Nitro:** Được ra mắt bởi AWS vào năm 2017, hypervisor này sử dụng các thành phần dựa trên KVM với hỗ trợ phần cứng cho tất cả các tài nguyên chính: các bộ xử lý, mạng, lưu trữ, các ngắt, và các bộ định thời [Gregg 17e]. Không có QEMU proxy nào được sử dụng. Nitro cung cấp hiệu năng gần bare-metal cho các khách VMs.

Các phần sau đây mô tả các chủ đề hiệu năng liên quan đến ảo hóa phần cứng: overhead (chi phí), các kiểm soát tài nguyên, và khả năng quan sát. Những thứ này khác biệt dựa trên việc triển khai và cấu hình của nó.

### 11.2.2 Chi phí (Overhead)
Hiểu khi nào và khi nào không kỳ vọng chi phí hiệu năng từ ảo hóa là quan trọng trong việc điều tra các vấn đề hiệu năng đám mây.

Ảo hóa phần cứng được thực hiện theo nhiều cách khác nhau. Việc truy cập tài nguyên có thể yêu cầu proxying và biên dịch bởi hypervisor, thêm chi phí, hoặc nó có thể sử dụng các công nghệ dựa trên phần cứng để tránh những chi phí này. Các phần sau đây tóm tắt các chi phí hiệu năng cho CPU, thực thi, ánh xạ bộ nhớ, kích thước bộ nhớ, thực hiện I/O, và tranh chấp từ các bên thuê khác.

**CPU**
Nhìn chung, các ứng dụng khách thực thi trực tiếp trên các bộ xử lý, và các ứng dụng bị giới hạn bởi CPU có thể trải nghiệm hiệu năng thực tế tương tự như một hệ thống bare-metal. Các chi phí CPU có thể gặp phải khi thực hiện các lệnh gọi xử lý có đặc quyền, truy cập phần cứng, và ánh xạ bộ nhớ chính, tùy thuộc vào cách chúng được xử lý bởi hypervisor. Phần sau đây mô tả cách các chỉ lệnh CPU được xử lý bởi các loại ảo hóa phần cứng khác nhau:
- **Binary translation:** Các chỉ lệnh kernel khách hoạt động trên tài nguyên vật lý được xác định và biên dịch. Binary translation được sử dụng trước khi ảo hóa được hỗ trợ bởi phần cứng có sẵn. Không có sự hỗ trợ phần cứng cho ảo hóa, sơ đồ được VMware sử dụng liên quan đến việc chạy một trình giám sát máy ảo (VMM) trong ring 0 của bộ xử lý và di chuyển kernel khách sang chạy trong ring 1, thứ trước đó đã không được sử dụng (các ứng dụng chạy trong ring 3, và hầu hết các bộ xử lý cung cấp bốn rings; các rings bảo vệ đã được giới thiệu trong Chương 3, Hệ điều hành, Mục 3.2.2, Các chế độ Kernel và User). Bởi vì một số chỉ lệnh kernel khách giả định chúng đang chạy trong ring 0, để thực thi từ ring 1 chúng cần được biên dịch, gọi vào VMM sao cho ảo hóa có thể được áp dụng. Việc biên dịch này được thực hiện trong quá trình chạy (runtime), tiêu tốn chi phí CPU đáng kể.
- **Paravirtualization:** Các chỉ lệnh trong hệ điều hành khách phải được ảo hóa được thay thế bằng các hypercalls tới hypervisor. Hiệu năng có thể được cải thiện nếu hệ điều hành khách được sửa đổi để tối ưu hóa các hypercalls, làm cho nó nhận thức được rằng nó đang chạy trên phần cứng ảo hóa.
- **Hardware-assisted:** Các chỉ lệnh kernel khách không sửa đổi hoạt động trên phần cứng được xử lý bởi hypervisor, thứ chạy một VMM tại một cấp độ ring bên dưới 0. Thay vì biên dịch các chỉ lệnh nhị phân, các chỉ lệnh có đặc quyền của kernel khách bị ép buộc phải trap tới VMM có đặc quyền cao hơn, thứ sau đó có thể mô phỏng đặc quyền để hỗ trợ ảo hóa [Adams 06].

Ảo hóa được hỗ trợ bởi phần cứng thường được ưa chuộng hơn, tùy thuộc vào việc triển khai và tải khối lượng công việc, trong khi paravirtualization được sử dụng để cải thiện hiệu năng của một số khối lượng công việc (đặc biệt là I/O) nếu hệ điều hành khách hỗ trợ nó.

Như một ví dụ về các khác biệt triển khai, mô hình binary translation của VMware đã được tối ưu hóa mạnh mẽ qua nhiều năm, và như họ đã viết vào năm 2007 [VMware 07]:

> Do chi phí chuyển đổi khách sang hypervisor cao và mô hình lập trình cứng nhắc, cách tiếp cận binary translation của VMware hiện nay vượt qua các triển khai ảo hóa được hỗ trợ bởi phần cứng thế hệ đầu tiên trong hầu hết các tình huống. Mô hình lập trình cứng nhắc trong thế hệ đầu tiên triển khai để lại ít không gian cho sự linh hoạt của phần mềm trong việc quản lý hoặc là tần suất hoặc là chi phí của các đợt chuyển đổi khách tới hypervisor.

Tốc độ của các đợt chuyển đổi giữa khách và hypervisor, cũng như thời gian dành cho hypervisor, có thể được nghiên cứu như một thước đo của chi phí CPU. Những sự kiện này thường được đề cập đến như *guest exits*, khi CPU ảo ngừng thực thi bên trong khách khi điều này xảy ra. Hình 11.6 cho thấy chi phí CPU liên quan đến các guest exits bên trong KVM.

Hình vẽ trình bày luồng các guest exits giữa tiến trình người dùng, kernel host, và khách. Thời gian dành cho bên ngoài các exit xử lý khách là chi phí CPU của ảo hóa phần cứng; thời gian dành cho việc xử lý guest exits càng nhiều, chi phí càng lớn. Khi các guest exits, một tập con của các sự kiện có thể được xử lý trực tiếp trong kernel. Những cái không thể phải rời khỏi kernel và quay trở lại tiến trình người dùng; điều này tạo ra các chi phí thậm chí lớn hơn so với các exits có thể được xử lý bởi kernel.

(Hình 11.6 Chi phí CPU ảo hóa phần cứng)

Ví dụ, với triển khai Linux KVM, các chi phí này có thể được nghiên cứu thông qua các chức năng guest exit của chúng, thứ được ánh xạ trong mã nguồn như sau (từ arch/x86/kvm/vmx/vmx.c trong Linux 5.2, đã bị lược bớt):
```c
/*
 * The exit handlers return 1 if the exit was handled fully and guest execution
 * may resume. Otherwise they set the kvm_run parameter to indicate what needs
 * to be done to userspace and return 0.
 */
static int (*kvm_vmx_exit_handlers[])(struct kvm_vcpu *vcpu) = {
    [EXIT_REASON_EXCEPTION_NMI]           = handle_exception,
    [EXIT_REASON_EXTERNAL_INTERRUPT]      = handle_external_interrupt,
    [EXIT_REASON_TRIPLE_FAULT]            = handle_triple_fault,
    [EXIT_REASON_NMI_WINDOW]              = handle_nmi_window,
    [EXIT_REASON_IO_INSTRUCTION]          = handle_io,
    [EXIT_REASON_CR_ACCESS]               = handle_cr,
    [EXIT_REASON_DR_ACCESS]               = handle_dr,
    [EXIT_REASON_CPUID]                   = handle_cpuid,
    [EXIT_REASON_MSR_READ]                = handle_rdmsr,
    [EXIT_REASON_MSR_WRITE]               = handle_wrmsr,
    [EXIT_REASON_PENDING_INTERRUPT]       = handle_interrupt_window,
    [EXIT_REASON_HLT]                     = handle_halt,
    [EXIT_REASON_INVD]                    = handle_invd,
    [EXIT_REASON_INVLPG]                  = handle_invlpg,
    [EXIT_REASON_RDPMC]                   = handle_rdpmc,
    [EXIT_REASON_VMCALL]                  = handle_vmcall,
    [...]
    [EXIT_REASON_XSAVES]                  = handle_xsaves,
    [EXIT_REASON_XRSTORS]                 = handle_xrstors,
    [EXIT_REASON_PML_FULL]                = handle_pml_full,
    [EXIT_REASON_INVPID]                  = handle_invpcid,
    [EXIT_REASON_VMFUNC]                  = handle_vmx_instruction,
    [EXIT_REASON_PREEMPTION_TIMER]        = handle_preemption_timer,
    [EXIT_REASON_ENCLS]                   = handle_encls,
};
```
Trong khi các tên gọi là ngắn gọn, chúng có thể cung cấp một ý tưởng về các lý do một khách có thể gọi tới một hypervisor, gây ra chi phí CPU.

Một guest exit phổ biến là chỉ lệnh halt, thường được gọi bởi luồng rảnh rỗi khi kernel không thể tìm thấy thêm công việc để thực hiện (điều này cho phép bộ xử lý hoạt động trong các chế độ năng lượng thấp cho đến khi bị ngắt quãng). Nó được xử lý bởi hàm handle_halt() (đã thấy trong danh sách trước đó cho EXIT_REASON_HLT), thứ cuối cùng gọi kvm_vcpu_halt() (arch/x86/kvm/x86.c):
```c
int kvm_vcpu_halt(struct kvm_vcpu *vcpu)
{
          ++vcpu->stat.halt_exits;
          if (lapic_in_kernel(vcpu)) {
              vcpu->arch.mp_state = KVM_MP_STATE_HALTED;
              return 1;
          } else {
              vcpu->run->exit_reason = KVM_EXIT_HLT;
              return 0;
          }
}
```
Với nhiều loại guest exit, mã nguồn được giữ nhỏ để giảm thiểu chi phí CPU. Ví dụ này bắt đầu với một sự gia tăng thống kê vcpu, thứ theo dõi có bao nhiêu lần halts đã xảy ra. Các chức năng còn lại thực hiện sự mô phỏng phần cứng cần thiết cho chỉ lệnh có đặc quyền này. Các chức năng này có thể được instrument trên Linux sử dụng kprobes trên host hypervisor, để theo dõi loại của chúng và thời lượng của các đợt exits của chúng. Exits cũng có thể được theo dõi toàn cầu sử dụng tracepoint kvm:kvm_exit, thứ được sử dụng trong Mục 11.2.4, Khả năng quan sát.

Ảo hóa các thiết bị phần cứng chẳng hạn như bộ điều khiển ngắt và các bộ định thời độ phân giải cao cũng phát sinh một số chi phí CPU (và một lượng nhỏ bộ nhớ).

**Ánh xạ Bộ nhớ (Memory Mapping)**
Như đã mô tả trong Chương 7, Bộ nhớ, hệ điều hành làm việc với MMU để tạo ra các ánh xạ bảng trang từ ảo sang bộ nhớ vật lý, đệm chúng trong TLB để cải thiện hiệu năng. Đối với ảo hóa, việc ánh xạ một trang bộ nhớ mới (page fault) từ khách tới phần cứng liên quan đến hai bước:
1. Dịch từ ảo-sang-vật lý khách, được thực hiện bởi kernel khách.
2. Dịch từ vật lý khách-sang-host (thực sự), được thực hiện bởi VMM của hypervisor.

Ánh xạ từ ảo-sang-vật lý-host sau đó có thể được đệm ẩn trong TLB, sao cho các lần truy cập tiếp theo có thể vận hành ở tốc độ bình thường—không yêu cầu dịch thêm. Các bộ xử lý hiện đại hỗ trợ ảo hóa MMU, sao cho các ánh xạ đã rời khỏi TLB có thể được nạp lại nhanh hơn trong phần cứng một mình (duyệt bảng trang). Tính năng hỗ trợ việc này được gọi là *extended page tables* (EPT) trên Intel và *nested page tables* (NPT) trên AMD [Milewski 11].

Không có EPT/NPT, một cách tiếp cận khác để cải thiện hiệu năng là duy trì *shadow page tables* của các ánh xạ ảo-sang-vật lý-host, thứ được quản lý bởi hypervisor và sau đó được truy cập trong quá trình thực thi của khách bằng cách ghi đè lên thanh ghi CR3 của khách. Với chiến lược này, kernel khách duy trì các bảng trang riêng của mình, thứ mà hypervisor ánh xạ vào một tập hợp các bảng trang thực (shadow page tables). Hypervisor ngắt quãng các thay đổi đối với các bảng trang này và tạo ra các ánh xạ tương ứng tới các trang vật lý thực trong các shadow pages. Sau đó, trong quá trình thực thi của khách, hypervisor ghi đè lên thanh ghi CR3 để trỏ tới các shadow pages.

**Memory Size (Kích thước Bộ nhớ)**
Không giống như ảo hóa OS, có một số bên tiêu thụ bộ nhớ bổ sung khi sử dụng ảo hóa phần cứng. Mỗi khách chạy kernel riêng của nó, thứ tiêu tốn một lượng nhỏ bộ nhớ. Kiến trúc lưu trữ cũng có thể dẫn đến việc đệm ẩn gấp đôi (double caching), nơi cả khách và host đệm cùng một dữ liệu. Các hypervisors kiểu KVM cũng chạy một tiến trình VMM cho mỗi VM, chẳng hạn như QEMU, thứ tự thân nó tiêu tốn một phần bộ nhớ.

**I/O**
Trong lịch sử, I/O là nguồn gốc lớn nhất của chi phí cho ảo hóa phần cứng. Điều này là vì mọi thiết bị I/O đều phải được dịch bởi hypervisor. Đối với mạng tần suất cao, chẳng hạn như mạng 10 Gbit/s, một mức độ chi phí I/O (gói tin) thấp có thể gây ra một sự sụt giảm đáng kể trong hiệu năng. Các công nghệ đã được tạo ra để giảm bớt các chi phí I/O này, đỉnh điểm là sự hỗ trợ phần cứng cho việc loại bỏ hoàn toàn các chi phí này. Sự hỗ trợ phần cứng như vậy bao gồm ảo hóa I/O MMU (AMD-Vi và Intel VT-d).

Một phương pháp để cải thiện hiệu năng I/O là sử dụng các trình điều khiển paravirtualized, thứ có thể kết hợp I/O và thực hiện các ngắt thiết bị ít hơn để giảm bớt các chi phí hypervisor.

Một kỹ thuật khác là *PCI pass-through*, thứ gán một thiết bị PCI trực tiếp cho khách, sao cho nó có thể được sử dụng như trên một hệ thống bare-metal. PCI pass-through có thể cung cấp hiệu năng tốt nhất trong số các tùy chọn có sẵn, nhưng nó làm giảm tính linh hoạt khi cấu hình hệ thống với nhiều bên thuê, vì một số thiết bị hiện nay được sở hữu bởi các khách và không thể được chia sẻ. Điều này cũng có thể làm phức tạp hóa việc di chuyển trực tiếp (live migration) [Xen 19].

Có một số công nghệ để cải thiện tính linh hoạt của việc sử dụng các thiết bị PCI với ảo hóa, bao gồm single root I/O virtualization (SR-IOV, đã đề cập trước đó) và multiroot I/O virtualization (MR-IOV). Những thuật ngữ này đề cập đến số lượng các cấu trúc liên kết PCI root complex được để lộ, cung cấp phần cứng ảo hóa theo các cách khác nhau. Đám mây Amazon EC2 sử dụng những công nghệ này để tăng tốc mạng đầu tiên và sau đó là I/O lưu trữ, thứ được kích hoạt theo mặc định với hypervisor Nitro [Gregg 17e].

Các cấu hình phổ biến của đường dẫn I/O Xen, KVM, và Nitro được mô tả trong Hình 11.7.

(Hình 11.7 Đường dẫn I/O Xen, KVM, và Nitro)

GK là "guest kernel," và BE là "back end." Các mũi tên đứt đoạn chỉ ra *control path*, nơi các thành phần thông báo cho nhau, hoặc đồng bộ hoặc bất đồng bộ, rằng có thêm dữ liệu sẵn sàng để truyền tải. *Data path* (các mũi tên liền nét) có thể được triển khai trong một số trường hợp bởi bộ nhớ chia sẻ và các ring buffers. Một control path không được hiển thị cho Nitro, vì nó sử dụng cùng một đường dẫn dữ liệu cho việc truy cập trực tiếp vào phần cứng.

Có các cách khác nhau để cấu hình Xen và KVM, không được hình ảnh hóa ở đây. Hình này cho thấy chúng sử dụng các tiến trình I/O proxy (thông thường là phần mềm QEMU), thứ được tạo ra cho mỗi VM khách. Nhưng chúng cũng có thể được cấu hình để sử dụng SR-IOV, cho phép các VMs khách truy cập trực tiếp phần cứng (không được hình ảnh hóa cho Xen hoặc KVM trong Hình 11.7). Nitro yêu cầu sự hỗ trợ phần cứng, loại bỏ nhu cầu cho các I/O proxies.

Xen cải thiện hiệu năng I/O của nó bằng cách sử dụng một *device channel*—một vận chuyển bộ nhớ chia sẻ bất đồng bộ giữa dom0 và các miền khách (domU). Điều này tránh được chi phí CPU và bus của việc tạo ra một bản sao dữ liệu I/O bổ sung khi nó được truyền giữa các miền. Nó cũng có thể sử dụng các miền riêng biệt cho việc thực hiện I/O, như được mô tả trong Mục 11.2.3, Kiểm soát tài nguyên.

Số lượng các bước trong đường dẫn I/O, cả control và data, là cực kỳ quan trọng cho hiệu năng: càng ít, càng tốt. Vào năm 2006, các nhà phát triển KVM đã so sánh một hệ thống có đặc quyền như Xen với KVM và thấy rằng KVM có thể thực hiện I/O bằng cách sử dụng một nửa số bước (năm so với mười, mặc dù bài kiểm tra được thực hiện mà không có paravirtualization vì vậy không phản ánh hầu hết các cấu hình hiện đại) [Qumranet 06].

Vì hypervisor Nitro loại bỏ các bước I/O bổ sung, tôi kỳ vọng tất cả các nhà cung cấp đám mây lớn sẽ làm theo, sử dụng hỗ trợ phần cứng để loại bỏ các I/O proxies.

**Multi-Tenant Contention (Tranh chấp Đa thuê)**
Tùy thuộc vào cấu hình hypervisor và bao nhiêu CPUs và CPU caches được chia sẻ giữa các bên thuê, có thể có thời gian CPU bị lấy mất và ô nhiễm bộ đệm ẩn CPU gây ra bởi các bên thuê khác, làm giảm hiệu năng. Đây là vấn đề điển hình với các containers hơn là các VMs, vì các containers thúc đẩy việc chia sẻ để hỗ trợ sự bùng phát CPU.

Các bên thuê thực hiện I/O có thể gây ra các ngắt làm gián đoạn việc thực thi ứng dụng, tùy thuộc vào cấu hình hypervisor.

Tranh chấp tài nguyên có thể được quản lý bởi các kiểm soát tài nguyên.

### 11.2.3 Kiểm soát tài nguyên (Resource Controls)
Là một phần của cấu hình khách, các giới hạn CPU và bộ nhớ chính thường được cấu hình. Phần mềm hypervisor cũng có thể cung cấp các kiểm soát tài nguyên cho mạng và I/O đĩa.

Đối với các hypervisors kiểu KVM, host OS cuối cùng kiểm soát các tài nguyên vật lý, và các kiểm soát tài nguyên khả dụng từ host OS cũng khả dụng cho các khách, bên cạnh bất kỳ thứ gì hypervisor cung cấp. Cho Linux, điều này có nghĩa là cgroups, tasksets, và các kiểm soát tài nguyên khác. Xem Mục 11.3, Ảo hóa OS, để biết thêm về các kiểm soát tài nguyên mà host OS có thể cung cấp. Các phần sau đây mô tả các kiểm soát tài nguyên từ các hypervisors Xen và KVM, như các ví dụ.

**CPUs**
Các tài nguyên CPU thường được phân bổ cho các khách dưới dạng các CPU ảo (vCPUs). Những thứ này sau đó được lập lịch bởi hypervisor. Số lượng vCPUs được gán giới hạn một cách thô sơ việc sử dụng CPU của khách.

Đối với Xen, hạn ngạch (quota) CPU chi tiết có thể được áp dụng bởi trình lập lịch CPU của hypervisor. Các trình lập lịch bao gồm [Cherkasova 07][Matthews 08]:
- **Borrowed virtual time (BVT):** Một trình lập lịch dựa trên sự công bằng (fair-share) dựa trên việc phân bổ thời gian ảo, thứ có thể được vay mượn trước để cung cấp thực thi độ trễ thấp cho các ứng dụng thực tế và tương tác.
- **Simple earliest deadline first (SEDF):** Một trình lập lịch thời gian thực cho phép các đảm bảo thời gian chạy được cấu hình, với trình lập lịch trao mức ưu tiên cho thời hạn cuối sớm nhất.
- **Credit-based:** Hỗ trợ các độ ưu tiên (*weights*) và các caps cho việc sử dụng CPU, và cân bằng tải qua nhiều CPUs.

Đối với KVM, hạn ngạch CPU chi tiết có thể được áp dụng bởi host OS, ví dụ bằng cách sử dụng trình lập lịch kernel host *fair-share* đã được mô tả trước đó. Trên Linux, điều này có thể được áp dụng bằng cách sử dụng các kiểm soát băng thông CPU cgroup.

Có các giới hạn về cách cả hai công nghệ có thể tôn trọng các *mức ưu tiên* của khách. Việc sử dụng CPU của một khách thường là không rõ ràng đối với hypervisor, và các mức ưu tiên luồng kernel của khách thường không thể được nhìn thấy hoặc được tôn trọng. Ví dụ, một daemon xoay vòng nhật ký ưu tiên thấp trong một khách có thể có mức ưu tiên hypervisor tương tự như một máy chủ ứng dụng quan trọng trong một khách khác.

Đối với Xen, việc sử dụng CPU bởi IDDs có thể được giám sát, và các khách có thể bị tính phí cho việc sử dụng này. Từ [Gupta 06]:

> Trình lập lịch đã sửa đổi của chúng tôi, SEDF-DC cho SEDF-Debt Collector, định kỳ nhận phản hồi từ XenMon về lượng CPU tiêu tốn bởi IDDs cho việc xử lý I/O thay mặt cho mỗi khách. Sử dụng thông tin này, SEDF-DC hạn chế việc phân bổ CPU cho các miền khách để đáp ứng một giới hạn CPU kết hợp được chỉ định.

Một kỹ thuật mới hơn được sử dụng trong Xen là *stub domains*, thứ chạy một mini-OS.

**CPU Caches**
Ngoài việc phân bổ vCPUs, mức sử dụng bộ đệm ẩn CPU có thể được kiểm soát bằng công nghệ Intel cache allocation technology (CAT). Nó cho phép LLC được phân chia giữa các khách, và các phân vùng được chia sẻ. Điều này có thể ngăn cản một khách làm ô nhiễm bộ đệm ẩn của khách khác, nó cũng có thể gây hại cho hiệu năng bằng cách giới hạn việc sử dụng bộ đệm ẩn.

**Memory Capacity (Dung lượng Bộ nhớ)**
Các giới hạn bộ nhớ được áp đặt như một phần của cấu hình khách, với việc khách chỉ thấy lượng bộ nhớ đã thiết lập. Kernel khách sau đó thực hiện các thao tác riêng của nó (paging, swapping) để duy trì bên trong giới hạn của nó.

Trong nỗ lực tăng tính linh hoạt so với cấu hình tĩnh, VMware đã phát triển một *balloon driver* [Waldspurger 02], thứ có thể giảm lượng bộ nhớ được sử dụng bởi một khách đang chạy bằng cách "làm phồng" một mô-đun balloon bên trong nó, thứ tiêu tốn bộ nhớ khách. Bộ nhớ này sau đó được kernel host thu hồi để sử dụng cho các khách khác. Balloon cũng có thể bị xì hơi (deflated), trả lại bộ nhớ cho kernel khách để sử dụng. Trong quá trình này, kernel khách thực thi các thói quen quản lý bộ nhớ bình thường của chính nó (ví dụ: paging). VMware, Xen, và KVM đều hỗ trợ cho balloon drivers.

Khi các balloon drivers đang được sử dụng (để kiểm tra từ khách, tìm kiếm "balloon" trong kết quả của dmesg(1)), tôi sẽ tìm kiếm các vấn đề hiệu năng mà chúng có thể gây ra.

**File System Capacity (Dung lượng Hệ thống tập tin)**
Các khách được cung cấp các virtual disk volumes từ host. Đối với các hypervisors kiểu KVM, đây có thể là các tệp phần mềm volume được tạo ra bởi OS và có kích thước tương ứng. Ví dụ, hệ thống tập tin ZFS có thể tạo ra các virtual volumes với một kích thước mong muốn.

**Device I/O**
Các kiểm soát tài nguyên bằng phần mềm ảo hóa phần cứng trong lịch sử đã tập trung vào việc kiểm soát mức sử dụng CPU, thứ có thể gián tiếp kiểm soát mức sử dụng I/O.

Thông lượng mạng có thể được điều tiết bởi các thiết bị chuyên dụng bên ngoài hoặc, trong trường hợp của các hypervisors kiểu KVM, bởi các tính năng kernel của host. Ví dụ, Linux có các kiểm soát băng thông mạng từ cgroups cũng như các qdiscs khác nhau, thứ có thể được cấu hình để phục vụ các giao diện mạng khách.

Cách ly hiệu năng mạng cho Xen đã được nghiên cứu, với kết luận sau [Adamczyk 12]:

> ...khi ảo hóa mạng được cân nhắc, điểm yếu của Xen là thiếu sự cách ly hiệu năng phù hợp.

Các tác giả của [Adamczyk 12] cũng đề xuất một giải pháp cho việc lập lịch I/O mạng Xen, thứ thêm các tham số có thể tinh chỉnh cho mức ưu tiên và tốc độ I/O mạng. Nếu bạn đang sử dụng Xen, hãy kiểm tra xem liệu tính năng này hoặc một tính năng tương tự đã được cung cấp chưa.

Đối với các hypervisors với sự hỗ trợ phần cứng đầy đủ (ví dụ: Nitro), các giới hạn I/O có thể được hỗ trợ bởi phần cứng, hoặc bởi các thiết bị bên ngoài. Trong đám mây Amazon EC2, các giới hạn mạng I/O và đĩa I/O cho các thiết bị gắn mạng được điều tiết theo hạn ngạch sử dụng các hệ thống bên ngoài.

### 11.2.4 Khả năng quan sát (Observability)
Những gì có thể quan sát được trên các hệ thống ảo hóa tùy thuộc vào hypervisor và vị trí từ đó các công cụ quan sát được khởi chạy. Nhìn chung:
- **Từ khách có đặc quyền (Xen) hoặc host (KVM):** Tất cả các tài nguyên vật lý nên quan sát được bằng cách sử dụng các công cụ OS tiêu chuẩn đã bao quát trong các chương trước. I/O khách có thể quan sát được bằng cách phân tích các I/O proxies, nếu được sử dụng. Các thống kê sử dụng tài nguyên cho mỗi khách nên khả dụng từ hypervisor. Các thành phần nội bộ khách, bao gồm các tiến trình của họ, không thể quan sát được trực tiếp. Một số I/O có thể không quan sát được nếu thiết bị sử dụng pass-through hoặc SR-IOV.
- **Từ host có hỗ trợ phần cứng (Nitro):** Việc sử dụng SR-IOV làm cho I/O thiết bị khó quan sát hơn từ host vì khách đang truy cập trực tiếp phần cứng, và không qua một proxy hoặc kernel host. (Amazon thực sự có khả năng quan sát hypervisor trên Nitro nhưng không được công khai.)
- **Từ các khách:** Các tài nguyên ảo hóa và việc sử dụng chúng bởi khách có thể được thấy, và các vấn đề vật lý được suy luận. Các công cụ truy vết kernel, bao gồm các công cụ dựa trên BPF, đều hoạt động vì VM có kernel chuyên dụng của riêng nó.

Từ khách có đặc quyền hoặc host (các hypervisors Xen hoặc KVM), mức sử dụng tài nguyên vật lý thường có thể được quan sát ở mức cao: mức sử dụng, độ bão hòa, các lỗi, IOPS, thông lượng, loại I/O. Những chi tiết này thường có thể được diễn đạt cho mỗi khách, sao cho những người dùng bận rộn có thể nhanh chóng được nhận diện. Các chi tiết về những tiến trình khách nào đang thực hiện I/O và các stack gọi ứng dụng của họ không thể quan sát được trực tiếp. Chúng có thể được quan sát bằng cách đăng nhập vào khách (với điều kiện việc thực hiện điều đó là được ủy quyền và cấu hình, ví dụ: SSH) và sử dụng các công cụ quan sát mà hệ điều hành khách cung cấp.

Khi pass-through hoặc SR-IOV được sử dụng, khách có thể thực hiện các lệnh gọi I/O trực tiếp tới phần cứng. Điều này có thể bỏ qua các đường dẫn I/O trong hypervisor, và các thống kê mà chúng thường thu thập. Kết quả là I/O đó có thể trở nên không nhìn thấy được đối với hypervisor, và không xuất hiện trong iostat(1) hoặc các công cụ khác. Một cách giải quyết khả thi là sử dụng PMCs để kiểm tra các sự kiện liên quan đến I/O, và suy luận I/O theo cách đó.

Để nhận diện nguồn gốc thực sự của một vấn đề hiệu năng khách, nhà vận hành đám mây có thể cần đăng nhập vào cả hypervisor và các công cụ quan sát từ cả hai. Truy vết đường dẫn I/O trở nên phức tạp do các bước liên quan và cũng có thể bao gồm phân tích các thành phần nội bộ I/O proxy và một I/O proxy, nếu được sử dụng.

Từ khách, mức sử dụng tài nguyên vật lý có thể không quan sát được hoàn toàn. Điều này có thể cám dỗ các khách hàng đổ lỗi cho các vấn đề hiệu năng bí ẩn cho sự tranh chấp tài nguyên gây ra bởi các người hàng xóm ồn ào. Để mang lại sự yên tâm cho các khách hàng đám mây (và giảm bớt các yêu cầu hỗ trợ), thông tin về mức sử dụng tài nguyên vật lý (đã được lọc bỏ các thông tin nhạy cảm) có thể được cung cấp qua các phương tiện khác, bao gồm SNMP hoặc một cloud API.

Để làm cho hiệu năng container dễ dàng quan sát và hiểu hơn, có nhiều giải pháp giám sát khác nhau trình bày các biểu đồ, dashboard, và các biểu đồ định hướng để hiển thị môi trường container của bạn. Các phần mềm bao gồm Google cAdvisor [Google 20d] và Cilium Hubble [Cilium 19] (cả hai đều là mã nguồn mở).

Các phần sau đây trình bày các ví dụ về các công cụ quan sát thô có thể được sử dụng từ các vị trí khác nhau, và mô tả một chiến lược để phân tích hiệu năng. Xen và KVM được sử dụng để trình diễn loại thông tin mà phần mềm ảo hóa có thể cung cấp (Nitro không được bao gồm vì nó là sở hữu độc quyền của Amazon).

#### 11.2.4.1 Privileged Guest/Host
Tất cả các tài nguyên hệ thống (CPUs, bộ nhớ, hệ thống tập tin, đĩa, mạng) nên quan sát được bằng cách sử dụng các công cụ đã bao quát trong các chương trước (với ngoại lệ của I/O qua pass-through/SR-IOV).

**Xen**
Đối với các hypervisors kiểu Xen, các vCPUs khách tồn tại trong hypervisor và không nhìn thấy được từ khách có đặc quyền (dom0) bằng cách sử dụng các công cụ OS tiêu chuẩn. Cho Xen, công cụ xentop(1) có thể được sử dụng thay thế:
```bash
# xentop
xentop - 02:01:05  Xen 3.3.2-rc1-xvm
2 domains: 1 running, 1 blocked, 0 paused, 0 crashed, 0 dying, 0 shutdown
Mem: 50321636k total, 12498976k used, 37822660k free    CPUs: 16 @ 2394MHz
      NAME  STATE   CPU(sec) CPU(%)     MEM(k) MEM(%)  MAXMEM(k) MAXMEM(%) VCPUS NETS
NETTX(k) NETRX(k) VBDS   VBD_OO   VBD_RD   VBD_WR  SSID
    Domain-0 -----r    6087972    2.6    9692160   19.3   no limit       n/a    16    0
0        0      0        0        0        0     0
  Doogle_Win --b---     172137    2.0    2105212    4.2    2105344       4.2     1    2
0        0      2        0        0        0     0
[...]
```
Các trường bao gồm:
- **CPU(%):** Phần trăm sử dụng CPU (tổng cho nhiều CPUs)
- **MEM(k):** Sử dụng bộ nhớ chính (Kbytes)
- **MEM(%):** Phần trăm sử dụng bộ nhớ chính của bộ nhớ hệ thống
- **MAXMEM(k):** Giới hạn kích thước bộ nhớ chính tối đa (Kbytes)
- **MAXMEM(%):** Giới hạn bộ nhớ chính tối đa dưới dạng phần trăm của bộ nhớ hệ thống
- **VCPUS:** Số lượng vCPUs được gán
- **NETS:** Số lượng giao diện mạng ảo hóa
- **NETTX(k):** Truyền tải mạng (Kbytes)
- **NETRX(k):** Nhận mạng (Kbytes)
- **VBDS:** Số lượng thiết bị khối ảo
- **VBD_OO:** Các yêu cầu thiết bị khối ảo bị chặn và xếp hàng (bão hòa)
- **VBD_RD:** Các yêu cầu đọc thiết bị khối ảo
- **VBD_WR:** Các yêu cầu ghi thiết bị khối ảo

Kết quả xentop(1) được cập nhật mỗi 3 giây theo mặc định và có thể lựa chọn bằng cách sử dụng `-d delay_secs`.

Cho phân tích Xen nâng cao còn có công cụ xentrace(8), thứ có thể truy xuất một nhật ký các loại sự kiện cố định từ hypervisor. Sau đó chúng có thể được xem bằng cách sử dụng xenanalyze để điều tra các vấn đề lập lịch với hypervisor và trình lập lịch CPU được sử dụng. Cũng có xenoprof, trình profile trên toàn hệ thống cho Xen (MMU và các khách) trong Xen source.

**KVM**
Đối với các hypervisors kiểu KVM, các thực thể khách là nhìn thấy được bên trong host OS. Ví dụ:
```bash
host$ top
top - 15:27:55 up 26 days, 22:04,  1 user,  load average: 0.26, 0.24, 0.28
Tasks: 499 total,   1 running, 408 sleeping,   2 stopped,   0 zombie
%Cpu(s): 19.9 us,  4.8 sy,  0.0 ni, 74.2 id,  1.1 wa,  0.0 hi,  0.1 si,  0.0 st
KiB Mem : 24422712 total,  6018936 free, 12767036 used,  5636740 buff/cache
KiB Swap: 32460792 total,  31868716 free,   592076 used.  8715220 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
24881 libvirt+  20   0 6161864 1.051g  19448 S 171.9  4.5   0:25.88 qemu-system-x86

21897 root       0 -20       0      0      0 I   2.3  0.0   0:00.47 kworker/u17:8
23445 root       0 -20       0      0      0 I   2.3  0.0   0:00.24 kworker/u17:7
15476 root       0 -20       0      0      0 I   2.0  0.0   0:01.23 kworker/u17:2
23038 root       0 -20       0      0      0 I   2.0  0.0   0:00.28 kworker/u17:0

22784 root       0 -20       0      0      0 I   1.7  0.0   0:00.36 kworker/u17:1
[...]
```
Tiến trình qemu-system-x86 là một khách KVM, thứ bao gồm các luồng cho mỗi vCPU và các luồng cho I/O proxies. Tổng mức sử dụng CPU cho khách có thể được thấy trong kết quả top(1) trước đó, và mức sử dụng cho mỗi vCPU có thể được kiểm tra bằng cách sử dụng các công cụ khác. Ví dụ, sử dụng pidstat(1):
```bash
host$ pidstat -tp 24881 1
03:40:44 PM   UID      TGID       TID    %usr %system  %guest %wait    %CPU CPU Command
03:40:45 PM 64055 24881         -   17.00   17.00 147.00  0.00 181.00    0 qemu-system-x86
03:40:45 PM 64055     -     24881    9.00    5.00    0.00  0.00   14.00    0 |_qemu-system-x86
03:40:45 PM 64055     -     24889    0.00    0.00    0.00  0.00    0.00    6 |_qemu-system-x86
03:40:45 PM 64055     -     24897    1.00    3.00   69.00  1.00   73.00    4 |_CPU 0/KVM
03:40:45 PM 64055     -     24899    1.00    4.00   79.00  0.00   84.00    5 |_CPU 1/KVM
03:40:45 PM 64055     -     24901    0.00    0.00    0.00  0.00    0.00    2 |_vnc_worker
03:40:45 PM 64055     -     25811    0.00    0.00    0.00    0.00    0.00    7 |_worker
03:40:45 PM 64055     -     25812    0.00    0.00    0.00    0.00    0.00    6 |_worker
[...]
```
Kết quả này hiển thị các luồng CPU, mang tên CPU 0/KVM và CPU 1/KVM đang tiêu tốn lần lượt 73% và 84% CPU.

Ánh xạ các tiến trình QEMU tới các tên thực thể khách của chúng thường là một vấn đề của việc kiểm tra các đối số tiến trình của chúng (ps -wwfp PID) để đọc tùy chọn -name.

Một lĩnh vực quan trọng khác cho phân tích là các exits của CPU ảo khách. Các loại exits có thể xảy ra có thể cho thấy những gì một khách đang làm: liệu một vCPU là rảnh rỗi, đang thực hiện I/O, hay đang thực hiện tính toán. Trên Linux, lệnh perf(1) kvm subcommand cung cấp các thống kê cấp cao cho các KVM exits. Ví dụ:
```bash
host# perf kvm stat live
11:12:07.687968

Analyze events for all VMs, all VCPUs:

             VM-EXIT Samples Samples%    Time%   Min Time    Max Time         Avg time

           MSR_WRITE    1668   68.90%    0.28%      0.67us     31.74us   3.25us ( +-  2.20% )
                 HLT     466   19.25%   99.63%      2.61us 100512.98us 4160.68us ( +- 14.77% )
    PREEMPTION_TIMER     112    4.63%    0.03%      2.53us     10.42us   4.71us ( +-  2.68% )
    PENDING_INTERRUPT      82    3.39%    0.01%      0.92us     18.95us   3.44us ( +-  6.23% )
  EXTERNAL_INTERRUPT      53    2.19%    0.01%      0.82us      7.46us   3.22us ( +-  6.57% )
      IO_INSTRUCTION      37    1.53%    0.04%      5.36us     84.88us  19.97us ( +- 11.87% )
            MSR_READ       2    0.08%    0.00%      3.33us      4.80us   4.07us ( +- 18.05% )
       EPT_MISCONFIG       1    0.04%    0.00%     19.94us     19.94us  19.94us ( +-  0.00% )

Total Samples:2421, Total events handled time:1946040.48us.
[...]
```
Điều này hiển thị các lý do cho việc thoát máy ảo, và các thống kê cho từng lý do. Các exits có thời lượng dài nhất trong ví dụ này là cho HLT (halt), khi các vCPUs ảo đi vào trạng thái rảnh rỗi. Các cột là:
- **VM-EXIT:** Loại exit
- **Samples:** Số lượng exits trong khi truy vết
- **Samples%:** Số lượng exits dưới dạng phần trăm tổng thể
- **Time%:** Thời gian dành cho các exits dưới dạng phần trăm tổng thể
- **Min Time:** Thời gian exit tối thiểu
- **Max Time:** Thời gian exit tối đa
- **Avg time:** Thời gian exit trung bình

Mặc dù nó có thể không dễ dàng cho một nhà vận hành để thấy trực tiếp bên trong một máy ảo khách, việc kiểm tra các exits cho phép bạn đặc tính hóa mức độ chi phí ảo hóa phần cứng có thể hoặc không thể đang ảnh hưởng đến một bên thuê. Nếu bạn thấy một số lượng exits thấp và một phần trăm cao trong số đó là HLT, bạn biết rằng CPU khách là khá rảnh rỗi. Mặt khác, nếu bạn thấy một số lượng cao các I/O operations, với các ngắt được cả tạo ra và được đưa vào khách, thì rất có khả năng khách đang thực hiện I/O qua các NICs và các đĩa ảo của nó.

Để phân tích KVM nâng cao, có nhiều tracepoints:
```bash
host# perf list | grep kvm
  kvm:kvm_ack_irq                                    [Tracepoint event]
  kvm:kvm_age_page                                   [Tracepoint event]
  kvm:kvm_apic                                       [Tracepoint event]
  kvm:kvm_apic_accept_irq                            [Tracepoint event]
  kvm:kvm_apic_ipi                                   [Tracepoint event]
  kvm:kvm_async_pf_completed                         [Tracepoint event]
  kvm:kvm_async_pf_doublefault                       [Tracepoint event]
  kvm:kvm_async_pf_not_present                       [Tracepoint event]
  kvm:kvm_async_pf_ready                             [Tracepoint event]
  kvm:kvm_avic_incomplete_ipi                        [Tracepoint event]
  kvm:kvm_avic_unaccelerated_access                  [Tracepoint event]
  kvm:kvm_cpuid                                      [Tracepoint event]
  kvm:kvm_cr                                         [Tracepoint event]
  kvm:kvm_emulate_insn                               [Tracepoint event]
  kvm:kvm_enter_smm                                  [Tracepoint event]
  kvm:kvm_entry                                      [Tracepoint event]
  kvm:kvm_eoi                                        [Tracepoint event]
  kvm:kvm_exit                                       [Tracepoint event]
[...]
```
Đặc biệt quan tâm là kvm:kvm_exit (đã được đề cập trước đó) và kvm:kvm_entry. Liệt kê các đối số kvm:kvm_exit sử dụng bpftrace:
```bash
host# bpftrace -lv t:kvm:kvm_exit
tracepoint:kvm:kvm_exit
    unsigned int exit_reason;
    unsigned long guest_rip;
    u32 isa;
    u64 info1;
    u64 info2;
```
Điều này cung cấp lý do exit (exit_reason), con trỏ chỉ lệnh trả về của khách (guest_rip), và các chi tiết khác. Cùng với kvm:kvm_entry, thứ hiển thị khi khách KVM được vào (hoặc nói cách khác, khi exit hoàn thành), thời lượng của exit có thể được đo lường cùng với lý do của nó. Trong *BPF Performance Tools* [Gregg 19] tôi đã phát hành kvmexits.bt, một công cụ bpftrace để hiển thị các lý do exit dưới dạng một biểu đồ histogram (nó cũng là mã nguồn mở và trực tuyến [Gregg 19e]). Kết quả ví dụ:
```bash
host# kvmexits.bt
Attaching 4 probes...
Tracing KVM exits. Ctrl-C to end
^C
[...]

@exit_ns[30, IO_INSTRUCTION]:
[1K, 2K)                 1 |                                                    |
[2K, 4K)                12 |@@@                                                 |
[4K, 8K)                71 |@@@@@@@@@@@@@@@@@@@@@@@@                            |
[8K, 16K)              198 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[16K, 32K)             129 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  |
[32K, 64K)              94 |@@@@@@@@@@@@@@@@@@@@@@@@                            |
[64K, 128K)             37 |@@@@@@@@@                                           |
[128K, 256K)            12 |@@@                                                 |
[256K, 512K)            23 |@@@@@@                                              |
[512K, 1M)               2 |                                                    |
[1M, 2M)                 0 |                                                    |
[2M, 4M)                 1 |                                                    |
[4M, 8M)                 2 |                                                    |

@exit_ns[48, EPT_VIOLATION]:
[512, 1K)             6160 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        |
[1K, 2K)              6885 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   |
[2K, 4K)              7686 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[4K, 8K)              2220 |@@@@@@@@@@@@@@@                                     |
[8K, 16K)              582 |@@@@                                                |
[16K, 32K)             244 |@                                                   |
[32K, 64K)              47 |                                                    |
[64K, 128K)              3 |                                                    |
```
Kết quả bao gồm các biểu đồ histograms cho mỗi exit: chỉ có hai cái được bao gồm ở đây. Điều này cho thấy IO_INSTRUCTION exits thường mất ít hơn 512 micro giây, với một vài giá trị ngoại lai đạt tới dải 2 tới 8 mili giây.

Một ví dụ khác của phân tích nâng cao là tạo hồ sơ (profiling) nội dung của thanh ghi CR3. Mọi tiến trình trong khách đều có không gian địa chỉ riêng của nó và tập hợp các bảng trang mô tả các bản dịch bộ nhớ ảo-sang-vật lý. Gốc của bảng trang này được lưu trữ trong thanh ghi CR3. Bằng cách lấy mẫu thanh ghi CR3 từ host (ví dụ: sử dụng bpftrace), bạn có thể xác định liệu một domain khách duy nhất là đang hoạt động trong khách (cùng giá trị CR3) hay liệu nó đang chuyển đổi giữa các tiến trình (các giá trị CR3 khác nhau).

Để biết thêm thông tin, bạn phải đăng nhập vào khách.

#### 11.2.4.2 Guest
Từ một khách ảo hóa phần cứng, chỉ các thiết bị ảo mới có thể được nhìn thấy (trừ khi pass-through/SR-IOV được sử dụng). Điều này bao gồm các CPUs, thứ cho biết các vCPUs được phân bổ cho khách. Ví dụ, kiểm tra các CPUs từ một khách KVM sử dụng mpstat(1):
```bash
kvm-guest$ mpstat -P ALL 1
Linux 4.15.0-91-generic (ubuntu0)    03/22/2020    _x86_64_    (2 CPU)

10:51:34 PM CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
10:51:35 PM all   14.95    0.00   35.57    0.00    0.00    0.00    0.00    0.00    0.00   49.48
10:51:35 PM   0   11.34    0.00   28.87    0.00    0.00    0.00    0.00    0.00    0.00   59.79
10:51:35 PM   1   17.71    0.00   42.71    0.00    0.00    0.00    0.00    0.00    0.00   39.58
10:51:35 PM CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
10:51:36 PM all   11.56    0.00   37.19    0.00    0.00    0.00    0.50    0.00    0.00   50.75
10:51:36 PM   0    8.05    0.00   22.99    0.00    0.00    0.00    0.00    0.00    0.00   68.97
10:51:36 PM   1   15.04    0.00   48.67    0.00    0.00    0.00    0.00    0.00    0.00   36.28
[...]
```
Kết quả cho thấy các trạng thái của hai vCPUs khách duy nhất.

Lệnh vmstat(8) của Linux bao gồm một cột cho phần trăm CPU bị đánh cắp (st), thứ là một ví dụ hiếm hoi của một thống kê nhận thức ảo hóa. Stolen cho thấy thời gian CPU không khả dụng cho khách: nó đã bị tiêu tốn bởi các bên thuê khác hoặc các chức năng hypervisor khác (chẳng hạn như xử lý I/O của chính bạn, hoặc điều tiết do loại thực thể).
```bash
xen-guest$ vmstat 1
procs -----------memory---------- ---swap-- -----io---- --system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 107500 141348 301680    0    0     0     0 1006    9 99  0  0  0  1
 1  0      0 107500 141348 301680    0    0     0     0 1006   11 97  0  0  0  3
 1  0      0 107500 141348 301680    0    0     0     0  978    9 95  0  0  0  5
 3  0      0 107500 141348 301680    0    0     0     4  912   15 99  0  0  0  1
 2  0      0 107500 141348 301680    0    0     0     0   33    7  3  0  0  0 97
 3  0      0 107500 141348 301680    0    0     0     0   34    6 100  0  0  0  0
 5  0      0 107500 141348 301680    0    0     0     0   35    7  1  0  0  0 99
 2  0      0 107500 141348 301680    0    0     0    48   38   16  2  0  0  0 98
[...]
```
Trong ví dụ này, một khách Xen với một chính sách giới hạn CPU tích cực đã được kiểm tra. Trong 4 giây đầu tiên, hơn 90% thời gian CPU là trong chế độ user mode của khách, với một vài phần trăm bị đánh cắp. Hành vi này sau đó thay đổi một cách mạnh mẽ, với hầu hết thời gian CPU bị đánh cắp.

Việc hiểu mức sử dụng CPU ở cấp độ chu kỳ thường yêu cầu sử dụng các bộ đếm phần cứng (xem Chương 4, Các Công cụ Quan trắc, Mục 4.3.9, Bộ đếm phần cứng (PMCs)). Những thứ này có thể hoặc không thể khả dụng cho khách, tùy thuộc vào cấu hình hypervisor. Ví dụ, Xen hỗ trợ sử dụng PMC bởi các khách, và tinh chỉnh để chỉ định PMCs nào được cho phép [Gregg 17f].

Vì các thiết bị đĩa và mạng được ảo hóa, một chỉ số quan trọng để phân tích là *latency* (độ trễ), chỉ ra thiết bị phản hồi như thế nào với ảo hóa, các giới hạn, và các bên thuê khác. Các chỉ số như phần trăm bận rộn là khó để diễn giải mà không biết các tài nguyên cơ sở và giới hạn.

Độ trễ thiết bị một cách chi tiết có thể được nghiên cứu bằng cách sử dụng các công cụ truy vết kernel, bao gồm perf(1), Ftrace, và BPF (Chương 13, 14, và 15). May mắn thay, tất cả những thứ này đều hoạt động trong các khách vì họ có các kernels chuyên dụng riêng, và người dùng root có toàn quyền truy cập kernel. Ví dụ, chạy biosnoop(8) dựa trên BPF trong một khách KVM:
```bash
kvm-guest# biosnoop
TIME(s)        COMM           PID    DISK   T SECTOR    BYTES   LAT(ms)
0.000000000    systemd-journa 389    vda    W 13103112  4096       3.41
0.001647000    jbd2/vda2-8    319    vda    W 8700872   360448     0.77
0.011814000    jbd2/vda2-8    319    vda    W 8701576   4096       0.20
1.711989000    jbd2/vda2-8    319    vda    W 8701584   20480      0.72
1.718005000    jbd2/vda2-8    319    vda    W 8701624   4096       0.67
[...]
```
Kết quả hiển thị độ trễ thiết bị đĩa ảo. Lưu ý rằng với containers (Mục 11.3, Ảo hóa OS) những công cụ truy vết kernel này có thể không hoạt động, sao cho người dùng cuối có thể không có khả năng kiểm tra I/O thiết bị và các mục tiêu khác một cách chi tiết.

#### 11.2.4.3 Chiến lược (Strategy)
Các chương trước đã bao quát các kỹ thuật phân tích cho các tài nguyên hệ thống vật lý và bao gồm các phương pháp luận khác nhau. Những điều này có thể được tuân theo bởi các nhà vận hành host, và ở một mức độ nào đó bởi các khách, ghi nhớ những hạn chế đã được đề cập trước đó. Đối với các khách, mức độ sử dụng tài nguyên cấp cao thường quan sát được, nhưng việc đào sâu vào kernel thông thường là không khả thi.

Ngoài các tài nguyên vật lý, các giới hạn đám mây được áp đặt bởi các kiểm soát tài nguyên cũng nên được kiểm tra, cho cả máy chủ host và các bên thuê khách. Vì những giới hạn này, khi hiện diện, được gặp phải muộn hơn so với các giới hạn vật lý, chúng có nhiều khả năng đang có hiệu lực và nên được kiểm tra trước tiên.

Vì nhiều công cụ quan sát truyền thống được tạo ra trước khi các containers và các kiểm soát tài nguyên tồn tại (ví dụ: top(1), iostat(1)), chúng không bao gồm thông tin kiểm soát tài nguyên theo mặc định, và người dùng có thể quên kiểm tra chúng.

Dưới đây là một số bình luận và chiến lược cho việc kiểm tra mỗi kiểm soát tài nguyên:
- **CPU:** Xem lưu đồ Hình 11.13. Việc sử dụng cpusets, băng thông, và shares tất cả đều cần được kiểm tra.
- **Bộ nhớ:** Cho bộ nhớ chính, kiểm tra mức sử dụng hiện tại so với bất kỳ giới hạn bộ nhớ cgroup nào.
- **Dung lượng hệ thống tập tin:** Điều này nên quan sát được cho bất kỳ hệ thống tập tin nào (bao gồm cả sử dụng df(1)).
- **I/O Đĩa:** Kiểm tra cấu hình của các đợt điều tiết blkio cgroup (/sys/fs/cgroup/blkio) và các thống kê từ các tập tin blkio.throttle.io_serviced và blkio.throttle.io_service_bytes: nếu chúng đang tăng với tốc độ tương tự như các đợt điều tiết, thì đó là bằng chứng cho thấy đĩa I/O bị giới hạn thông lượng. Nếu có sẵn truy vết BPF, công cụ blkthrot(8) cũng có thể được sử dụng để xác nhận việc điều tiết blkio [Gregg 19].
- **I/O Mạng:** Kiểm tra thông lượng mạng hiện tại so với bất kỳ giới hạn băng thông đã biết nào, thứ có thể chỉ quan sát được từ host. Việc gặp phải giới hạn khiến độ trễ mạng I/O tăng lên, khi các bên thuê bị điều tiết.

Một bình luận cuối cùng: phần này mô tả cgroup v1 và trạng thái hiện tại của các containers Linux. Các khả năng kernel đang thay đổi nhanh chóng, để lại các khu vực khác chẳng hạn như tài liệu của nhà cung cấp và nhận thức của container trong công cụ đang đuổi theo. Để cập nhật với Linux containers bạn sẽ cần kiểm tra các sự bổ sung trong các bản phát hành kernel mới, và đọc qua thư mục Tài liệu (Documentation) trong mã nguồn Linux. Tôi cũng khuyên bạn nên đọc bất kỳ tài liệu nào được viết bởi Tejun Heo, nhà phát triển dẫn đầu của cgroups v2, bao gồm Documentation/admin-guide/cgroup-v2.rst trong Linux source [Heo 15].

## 11.3 Ảo hóa OS (OS Virtualization)
Ảo hóa OS phân vùng hệ thống vận hành thành các thực thể mà Linux gọi là *containers*, thứ hoạt động giống như các máy chủ khách riêng biệt và có thể được quản trị và khởi động lại độc lập với host. Những thứ này cung cấp các thực thể boot nhanh, hiệu quả cho các khách hàng đám mây, và các máy chủ mật độ cao cho các nhà vận hành đám mây. Các khách ảo hóa OS được mô tả trong Hình 11.9.

(Hình 11.9 Ảo hóa hệ điều hành)

Cách tiếp cận này có nguồn gốc từ lệnh chroot(8) của Unix, thứ cô lập một tiến trình vào một cây thư mục con của hệ thống tập tin (nó thay đổi thư mục cấp cao nhất, "/", như được thấy bởi tiến trình, tới một nơi nào đó khác). Vào năm 1998, FreeBSD đã phát triển điều này xa hơn dưới dạng *FreeBSD jails*, cung cấp các ngăn (compartments) cô lập hoạt động giống như các máy chủ riêng của họ. Vào năm 2005, Solaris 10 đã bao gồm một phiên bản mang tên *Solaris Zones*, với các kiểm soát tài nguyên khác nhau. Trong khi đó Linux đã thêm các khả năng cô lập tiến trình theo từng phần, với *namespaces* lần đầu tiên được thêm vào vào năm 2002 cho Linux 2.4.19, và *control groups* (cgroups) lần đầu tiên được thêm vào vào năm 2008 cho Linux 2.6.24 [Corbet 07a][Corbet 07b][Linux 20m]. Namespaces và cgroups được kết hợp để tạo ra các containers, thứ thông thường cũng sử dụng seccomp-bpf cho việc kiểm soát truy cập syscall.

Một sự khác biệt then chốt so với các công nghệ ảo hóa phần cứng là chỉ có một kernel duy nhất đang chạy. Sau đây là các ưu điểm hiệu năng của các containers so với các VMs phần cứng (Mục 11.2, Ảo hóa phần cứng):
- **Thời gian khởi tạo nhanh:** thông thường được đo bằng mili giây.
- **Các khách có thể sử dụng bộ nhớ hoàn toàn cho các ứng dụng** (không có thêm kernel).
- **Có một unified file system cache**—điều này có thể tránh các kịch bản đệm ẩn gấp đôi giữa host và khách.
- **Kiểm soát chi tiết hơn đối với việc chia sẻ tài nguyên** (cgroups).
- **Cho các nhà vận hành host: cải thiện khả năng quan sát hiệu năng**, vì các tiến trình khách là trực tiếp nhìn thấy được cùng với các tương tác của chúng.
- **Các containers có thể có khả năng chia sẻ các trang bộ nhớ cho các tập tin chung**, giải phóng không gian trong page cache và cải thiện tỷ lệ trúng bộ đệm ẩn CPU.
- **CPUs là các CPUs thực;** các giả định bởi các khóa mutex thích ứng (adaptive mutex locks) vẫn còn giá trị.

Và có những nhược điểm:
- **Tăng cường tranh chấp cho các tài nguyên kernel** (các khóa, bộ đệm ẩn, hàng đợi).
- **Cho các khách: giảm khả năng quan sát hiệu năng**, vì kernel thông thường không thể được phân tích.
- **Bất kỳ đợt kernel panic nào cũng ảnh hưởng đến tất cả các khách.**
- **Các khách không thể chạy các mô-đun kernel tùy chỉnh.**
- **Các khách không thể chạy các kernels PGO dài hạn hơn** (xem Mục 3.5.1, PGO Kernels).
- **Các khách không thể chạy các phiên bản kernel hoặc các kernels khác nhau.**

Cân nhắc hai nhược điểm đầu tiên cùng nhau: một khách di chuyển từ một VM sang một container sẽ gặp phải các vấn đề tranh chấp kernel nhiều khả năng hơn trong khi cũng mất đi khả năng phân tích chúng. Họ sẽ trở nên phụ thuộc nhiều hơn vào nhà vận hành host cho loại phân tích này.

Một nhược điểm phi hiệu năng cho các containers là chúng được coi là kém bảo mật hơn vì các tầng cô lập là mỏng hơn. Tất cả những điều này được giải quyết bởi ảo hóa trọng lượng nhẹ, được bao quát trong Mục 11.4.

Các phần sau đây mô tả các chi tiết ảo hóa Linux OS: triển khai, chi phí (overhead), kiểm soát tài nguyên, và khả năng quan sát.

### 11.3.1 Triển khai (Implementation)
Trong Linux kernel không có khái niệm về một container. Có, tuy nhiên, các namespaces và cgroups, thứ mà phần mềm không gian người dùng (ví dụ, Docker) sử dụng để tạo ra cái mà nó gọi là *containers*. Một cấu hình container điển hình được mô tả trong Hình 11.10.

(Hình 11.10 Linux containers)

Bất chấp mỗi container có một tiến trình với ID 1 bên trong container, đây là các tiến trình khác nhau như khi chúng thuộc về các namespaces khác nhau.

Bởi vì nhiều lần triển khai container sử dụng Kubernetes, kiến trúc của nó được mô tả trong Hình 11.11. Kubernetes đã được giới thiệu trong Mục 11.1.6, Điều phối (Kubernetes).

(Hình 11.11 Kubernetes node)

Hình 11.11 cũng cho thấy đường dẫn mạng giữa các Pods qua Kube Proxy, và mạng container được cấu hình bởi một CNI.

Một ưu điểm của Kubernetes là nhiều containers có thể dễ dàng được tạo ra để chia sẻ các namespaces giống nhau, như một phần của một Pod. Điều này cho phép các phương thức liên lạc nhanh hơn giữa các containers.

**Namespaces (Không gian tên)**
Một namespace lọc chế độ xem của hệ thống sao cho các containers chỉ có thể thấy và quản trị các tiến trình, các điểm mount, và các tài nguyên khác của riêng họ. Đây là cơ chế chính cung cấp sự cô lập của một container khỏi các containers khác trên hệ thống. Các namespaces được lựa chọn được liệt kê trong Bảng 11.1.

Bảng 11.1 Các không gian tên Linux được lựa chọn
| Namespace | Mô tả |
| --- | --- |
| cgroup | Cho khả năng hiển thị cgroup |
| ipc | Cho khả năng hiển thị giao tiếp liên tiến trình |
| mnt | Cho các điểm mount hệ thống tập tin |
| net | Cho cách ly network stack; lọc các giao diện, sockets, định tuyến, v.v., thứ đang được thấy |
| pid | Cho khả năng hiển thị tiến trình; lọc /proc |
| time | Cho các đồng hồ hệ thống riêng biệt cho mỗi container |
| user | Cho các User IDs |
| uts | Cho thông tin máy chủ; syscall uname(2) |

Các namespaces hiện tại trên một hệ thống có thể được liệt kê với lsns(8):
```bash
# lsns
        NS TYPE      NPROCS   PID USER             COMMAND
4026531835 cgroup       105     1 root             /sbin/init
4026531836 pid          105     1 root             /sbin/init
4026531837 user         105     1 root             /sbin/init
4026531838 uts          102     1 root             /sbin/init
4026531839 ipc          105     1 root             /sbin/init
4026531840 mnt           98     1 root             /sbin/init
4026531860 mnt            1    19 root             kdevtmpfs
4026531992 net          105     1 root             /sbin/init
4026532166 mnt            1   241 root             /lib/systemd/systemd-udevd
4026532167 uts            1   241 root             /lib/systemd/systemd-udevd
[...]
```
Kết quả lsns(8) này cho thấy tiến trình init có sáu namespaces khác nhau, đang được sử dụng bởi hơn 100 tiến trình.

Có một số tài liệu cho các namespaces trong mã nguồn Linux, cũng như trong các trang man, bắt đầu với namespaces(7).

**Control Groups (Cgroups)**
Các nhóm kiểm soát (cgroups) giới hạn việc sử dụng các tài nguyên. Có hai phiên bản của cgroups trong Linux kernel, v1 và v2; nhiều dự án chẳng hạn như Kubernetes vẫn đang sử dụng v1 (v2 đang được tiến hành). Các v1 cgroups bao gồm những cái được liệt kê trong Bảng 11.2.

Bảng 11.2 Các cgroups Linux được lựa chọn
| cgroup | Mô tả |
| --- | --- |
| blkio | Giới hạn I/O khối (I/O đĩa): byte và IOPS |
| cpu | Giới hạn mức sử dụng CPU dựa trên các phần chia sẻ (shares) |
| cpuacct | Kế toán cho mức sử dụng CPU cho các nhóm tiến trình |
| cpuset | Gán bộ nhớ và các nút bộ nhớ CPU tới các containers |
| devices | Kiểm soát việc quản trị thiết bị |
| hugetlb | Giới hạn việc sử dụng các trang khổng lồ (huge pages) |
| memory | Giới hạn bộ nhớ tiến trình, bộ nhớ kernel, và việc sử dụng swap |
| net_cls | Thiết lập các classids trên các gói tin cho việc sử dụng bởi qdiscs và tường lửa |
| net_pri | Thiết lập các mức ưu tiên mạng |
| perf_event | Cho phép perf giám sát các tiến trình trong một cgroup |
| pids | Giới hạn số lượng tiến trình có thể được tạo ra |
| rdma | Giới hạn mức sử dụng tài nguyên RDMA và InfiniBand |

Những cgroups này có thể được cấu hình để giới hạn tranh chấp tài nguyên giữa các containers, ví dụ bằng cách đặt một giới hạn cứng cho CPU và sử dụng bộ nhớ, hoặc các giới hạn mềm (share-based) cho CPU và bộ nhớ đĩa. Chúng cũng có thể được sử dụng để lọc các gói tin mạng từ các containers khác nhau, như được hình ảnh hóa trong Hình 11.10.

cgroups v2 là theo thứ bậc (hierarchy-based) và giải quyết các thiếu sót khác nhau của v1. Kỳ vọng rằng các công nghệ container sẽ di chuyển sang v2 trong những năm tới, với v1 cuối cùng bị khai tử. Bản phân phối Fedora 31 OS, phát hành năm 2019, đã chuyển sang cgroups v2.

Có một số tài liệu cho các namespaces trong mã nguồn Linux dưới Documentation/cgroup-v1 và Documentation/admin-guide/cgroup-v2.rst, cũng như trong các trang man cgroups(7).

Phần sau đây mô tả các chủ đề ảo hóa container: chi phí (overhead), kiểm soát tài nguyên, và khả năng quan sát. Những thứ này khác biệt dựa trên việc triển khai container cụ thể và cấu hình của nó.

### 11.3.2 Chi phí (Overhead)
Chi phí thực thi container nên là trọng lượng nhẹ: mức sử dụng CPU và bộ nhớ của ứng dụng nên trải nghiệm hiệu năng bare-metal, mặc dù có thể có một số lệnh gọi bổ sung bên trong kernel cho I/O do các tầng trong hệ thống tập tin và đường dẫn mạng. Các vấn đề hiệu năng lớn nhất được gây ra bởi tranh chấp đa thuê, khi các containers thúc đẩy việc chia sẻ kernel và các tài nguyên vật lý nặng nề hơn. Các phần sau đây tóm tắt các chi phí hiệu năng cho việc thực thi CPU, sử dụng bộ nhớ, thực hiện I/O, và tranh chấp từ các bên thuê khác.

**CPU**
Khi một luồng container đang chạy trong chế độ user mode, không có các chi phí CPU trực tiếp: các luồng chạy trực tiếp trên CPU cho đến khi chúng hoặc nhường quyền hoặc bị chiếm quyền ưu tiên (preempted). Trên Linux, cũng không có thêm chi phí CPU cho việc chạy các tiến trình trong các namespaces và cgroups: tất cả các tiến trình đã nằm trong namespaces mặc định và các cấu hình cgroup, cho dù các containers có đang được sử dụng hay không.

Hiệu năng CPU rất có khả năng bị suy giảm do tranh chấp với các bên thuê khác (xem phần Multi-Tenant Contention sau đây).

Với các điều phối viên chẳng hạn như Kubernetes, các thành phần mạng bổ sung có thể thêm một số chi phí CPU cho việc xử lý các gói tin mạng (ví dụ, với nhiều dịch vụ (hàng nghìn); các chi phí cho mỗi gói tin đầu tiên của kube-proxy khi phải xử lý các bộ quy tắc iptables lớn được thiết lập do một số lượng lớn các dịch vụ Kubernetes được sử dụng. Chi phí này có thể được khắc phục bằng cách thay thế kube-proxy bằng BPF thay thế [Borkmann 20]).

**Ánh xạ Bộ nhớ (Memory Mapping)**
Ánh xạ bộ nhớ, các lệnh loads, và stores nên thực thi mà không có chi phí.

**Memory Size (Kích thước Bộ nhớ)**
Các ứng dụng có thể sử dụng toàn bộ lượng bộ nhớ được phân bổ cho container. So sánh điều này với các VMs phần cứng, thứ chạy một kernel cho mỗi bên thuê, mỗi kernel tiêu tốn một lượng nhỏ bộ nhớ chính.

Một cấu hình container chung (việc sử dụng OverlayFS) cho phép chia sẻ page cache giữa các containers đang truy cập cùng một tập tin. Điều này có thể giải phóng một phần bộ nhớ so với các VMs, thứ nhân bản các tập tin chung (ví dụ: các thư viện hệ thống) trong bộ nhớ.

**I/O**
Chi phí I/O tùy thuộc vào cấu hình container, vì nó có thể bao gồm các tầng bổ sung cho việc cách ly cho:
- **Hệ thống tập tin I/O:** Ví dụ, overlayfs
- **Mạng I/O:** Ví dụ, mạng bridge

Phần sau đây là một kernel stack trace cho thấy một lệnh ghi hệ thống tập tin container được xử lý bởi overlayfs (và được hỗ trợ bởi hệ thống tập tin XFS):
```text
blk_mq_make_request+1
generic_make_request+420
submit_bio+108
_xfs_buf_ioapply+798
__xfs_buf_submit+226
xlog_bdstrat+48
xlog_sync+703
__xfs_log_force_lsn+469
xfs_log_force_lsn+143
xfs_file_fsync+244
xfs_file_buffered_aio_write+629
do_iter_readv_writev+316
do_iter_write+128
ovl_write_iter+376
__vfs_write+274
vfs_write+173
ksys_write+90
do_syscall_64+85
entry_SYSCALL_64_after_hwframe+68
```
Overlayfs có thể được thấy trong stack dưới dạng hàm ovl_write_iter().

Vấn đề này quan trọng như thế nào tùy thuộc vào khối lượng công việc và tốc độ IOPS của nó. Đối với các máy chủ IOPS thấp (ví dụ: <1000 IOPS), nó sẽ tiêu tốn chi phí không đáng kể.

**Multi-Tenant Contention (Tranh chấp Đa thuê)**
Sự hiện diện của các bên thuê đang chạy khác có khả năng gây ra tranh chấp tài nguyên và các ngắt làm gián đoạn hiệu năng, bao gồm:
- Các bộ đệm ẩn CPU có thể có tỷ lệ trúng thấp hơn, vì các bên thuê khác đang tiêu thụ và loại bỏ các mục. Đối với một số bộ xử lý và kernels, việc chuyển đổi ngữ cảnh tới một container khác thậm chí có thể flush bộ đệm ẩn L1.
- Các bộ đệm ẩn TLB cũng có thể có tỷ lệ trúng thấp hơn do sử dụng từ bên thuê khác, và cũng flush trên các chuyển đổi ngữ cảnh (thứ có thể được tránh nếu PCID đang được sử dụng).
- Việc thực thi CPU có thể bị gián đoạn trong các khoảng thời gian ngắn cho các thiết bị của bên thuê khác (ví dụ: các thói quen dịch vụ ngắt I/O mạng).
- Việc thực thi kernel có thể gặp phải sự tranh chấp bổ sung cho các bộ đệm, hàng đợi, và các khóa, vì một hệ thống container đa thuê có thể tăng tải của họ theo một bậc độ lớn hoặc hơn. Sự tranh chấp như vậy có thể làm suy giảm hiệu năng ứng dụng một cách nhẹ nhàng, tùy thuộc vào tài nguyên kernel và các đặc tính khả năng mở rộng của nó.
- Network I/O có thể gặp phải các chi phí CPU do việc sử dụng iptables để triển khai mạng container.
- Có thể có sự tranh chấp cho các tài nguyên hệ thống (CPUs, đĩa, các giao diện mạng) từ các bên thuê khác đang sử dụng chúng.

Một bài đăng bởi Gianluca Borello mô tả cách hiệu năng của một container được tìm thấy là chậm dần và đều đặn do dcache. Ông đã theo dõi nó xuống tới mức stat(2) độ trễ cao hơn, gây ra bởi các containers của bên thuê khác [Borello 17]. Ông đã lần ra nó nhờ dcache.

Một vấn đề khác, được báo cáo bởi Maxim Leonovich, đã chỉ ra cách việc di chuyển từ các VMs đơn thuê tới đa thuê đã làm tăng tốc độ các lệnh gọi posix_fadvise() cho kernel, tạo ra một nút thắt cổ chai [Leonovich 18].

Mục cuối cùng trong danh sách được quản lý bởi các kiểm soát tài nguyên. Trong khi một số yếu tố này tồn tại trong một môi trường đa người dùng truyền thống, chúng phổ biến hơn nhiều trong một hệ thống container đa thuê.

### 11.3.3 Kiểm soát tài nguyên
Các kiểm soát tài nguyên điều tiết quyền truy cập vào tài nguyên sao cho chúng có thể được chia sẻ một cách công bằng. Trên Linux, những điều này được cung cấp chủ yếu qua cgroups.

Các kiểm soát tài nguyên riêng lẻ có thể được phân loại là *mức ưu tiên* (priorities) hoặc *giới hạn* (limits). Các mức ưu tiên điều tiết mức tiêu thụ tài nguyên để cân bằng mức sử dụng giữa các hàng xóm dựa trên một giá trị quan trọng. Các giới hạn là một giá trị trần của mức tiêu thụ tài nguyên. Mỗi loại được sử dụng khi phù hợp—cho một số tài nguyên, điều đó có nghĩa là cả hai. Các ví dụ được liệt kê trong Bảng 11.3.

Bảng 11.3 Các kiểm soát tài nguyên container Linux
| Tài nguyên | Mức ưu tiên | Giới hạn |
| --- | --- | --- |
| CPU | CFS shares | cpusets (toàn bộ CPUs), CFS bandwidth (phân số CPUs) |
| Dung lượng bộ nhớ | Memory soft limits | Memory limits |
| Dung lượng Swap | - | Swap limits |
| Dung lượng hệ thống tập tin | - | File system quotas/limits |
| Bộ đệm ẩn tập tin | - | Kernel memory limits |
| Disk I/O | blkio weights | blkio IOPS limits, blkio throughput limits |
| Network I/O | net_prio priorities, qdiscs (fq, v.v.), Custom BPF | qdiscs (fq, v.v.), Custom BPF |

Những thứ này được mô tả trong các phần sau đây theo các thuật ngữ chung, dựa trên cgroup v1. Các bước để cấu hình những thứ này tùy thuộc vào nền tảng container bạn đang sử dụng (Docker, Kubernetes, v.v.); hãy xem tài liệu liên quan của họ.

**CPUs**
Các CPU có thể được phân bổ giữa các containers sử dụng cgroup cpusets, và các phần chia sẻ (shares) và băng thông (bandwidth) từ CFS scheduler.

**cpusets**
Cgroup cpusets cho phép toàn bộ các CPU được phân bổ cho các containers cụ thể. Lợi ích là các containers đó có thể chạy trên CPU mà không bị gián đoạn bởi những cái khác, và dung lượng CPU khả dụng cho chúng là nhất quán. Nhược điểm là dung lượng CPU rảnh rỗi là không khả dụng cho các containers khác sử dụng.

**Shares và Bandwidth**
CPU *shares*, được cung cấp bởi trình lập lịch CFS, là một cách tiếp cận khác cho việc phân bổ CPU cho phép các containers chia sẻ công suất CPU rảnh rỗi của họ. Shares hỗ trợ khái niệm *bursting*, nơi một container có thể thực thi nhanh hơn một cách hiệu quả bằng cách sử dụng công suất CPU rảnh rỗi từ các containers khác. Khi không có công suất rảnh rỗi, bao gồm cả khi host bị cung cấp quá mức, shares cung cấp một phân chia nỗ lực tốt nhất (best-effort division) của tài nguyên CPU giữa các containers cần chúng.

CFS làm việc bằng cách gán các đơn vị phân bổ được gọi là shares tới các containers, thứ được sử dụng để tính toán lượng CPU mà một container bận rộn sẽ nhận được tại một thời điểm nhất định. Tính toán này sử dụng công thức:

```
container CPU = (tổng CPUs × container shares) / tổng shares của các containers bận rộn trên hệ thống
```

Cân nhắc một hệ thống đã phân bổ 100 shares giữa nhiều máy chủ. Tại một thời điểm, chỉ các containers A và B muốn tài nguyên CPU. Container A có 10 shares, và container B có 30 shares. Do đó, container A có thể sử dụng 25% tổng tài nguyên CPU trên hệ thống: tất cả CPUs × 10/(10 + 30).

Bây giờ hãy cân nhắc một hệ thống nơi tất cả các containers đều bận rộn tại cùng một thời điểm. Một container CPU được gán sẽ là:

```
container CPU = tất cả CPUs × container shares / tổng shares trên hệ thống
```

Đối với kịch bản được mô tả, container A sẽ nhận được 10% công suất CPU (tất cả CPUs × 10/100). Việc phân bổ shares cung cấp một đảm bảo tối thiểu về việc sử dụng CPU. Bursting cho phép container sử dụng nhiều hơn. Container A có thể sử dụng bất cứ thứ gì từ 10% tới 100% công suất CPU, tùy thuộc vào số lượng các containers khác bận rộn.

Một vấn đề với shares là việc bursting có thể gây nhầm lẫn cho quy hoạch dung lượng, đặc biệt là khi nhiều hệ thống giám sát không hiển thị các thống kê bursting (họ nên làm vậy). Một thử nghiệm người dùng cuối trên một container có thể phản ánh hiệu năng tối đa bởi mức sử dụng CPU. Bursting có thể cho phép hiệu năng này chỉ khả thi nhờ vào bursting. Sau đó, khi các bên thuê khác chuyển đến, container của họ không còn có thể burst và sẽ gặp phải hiệu năng thấp hơn. Hãy tưởng tượng container A ban đầu đang trên một hệ thống rảnh rỗi và nhận được 100% CPU, nhưng sau đó chỉ nhận được 10% khi các containers khác đã được thêm vào. Tôi đã thấy kịch bản này xảy ra trong đời thực trong vô số trường hợp, nơi người dùng cuối nghĩ rằng phải có một vấn đề hiệu năng hệ thống và yêu cầu tôi giúp gỡ lỗi nó. Sau đó họ thất vọng khi biết rằng hệ thống đang hoạt động như ý định, và tốc độ chậm hơn mười lần là chuẩn mực mới vì các containers khác đã chuyển đến. Đối với khách hàng, điều này có thể cảm thấy giống như mồi nhử và lừa dối (bait and switch).

Có thể giảm bớt vấn đề bursting quá mức bằng cách giới hạn nó sao cho hiệu năng sụt giảm không quá nghiêm trọng (ngay cả khi điều này có nghĩa là công suất CPU nhàn rỗi bị lãng phí). Trên Linux, điều này được thực hiện bằng cách sử dụng các kiểm soát *bandwidth* CFS, thứ có thể thiết lập một giới hạn trên cho việc sử dụng CPU. Ví dụ, container A có thể có băng thông của nó được thiết lập ở mức 20% của toàn hệ thống, sao cho việc chuyển đổi với shares nằm trong phạm vi từ 10 tới 20%, tùy thuộc vào sự sẵn có CPU nhàn rỗi. Phạm vi này từ một mức tối thiểu CPU dựa trên share tới mức tối đa băng thông được hình ảnh hóa trong Hình 11.12. Nó giả định rằng có đủ các luồng bận rộn trong mỗi container để sử dụng các CPUs khả dụng (nếu không thì các containers trở nên bị giới hạn-CPU do chính khối lượng công việc của họ, trước khi chạm tới các giới hạn do hệ thống áp đặt).

(Hình 11.12 CPU shares và bandwidth)

Các kiểm soát băng thông thường được để lộ dưới dạng phần trăm của toàn bộ CPUs: 2.5 sẽ có nghĩa là hai rưỡi CPUs. Điều này ánh xạ tới các thiết lập kernel, thứ thực sự là *periods* và *quotas* tính theo micro giây: một container nhận được một quota gồm số micro giây CPU trong mỗi khoảng thời gian (period).

Một cách khác để quản lý bursting là cho các nhà vận hành container thông báo cho người dùng cuối của họ khi họ đang bursting trong một khoảng thời gian (ví dụ: nhiều ngày) sao cho họ không nảy sinh các kỳ vọng sai lầm về hiệu năng. Sau đó, người dùng cuối có thể được khuyến khích nâng cấp kích thước container của họ sao cho họ nhận được các phần chia sẻ (shares) cao hơn, và một sự đảm bảo tối thiểu cao hơn về việc phân bổ CPU.

**CPU Caches**
Mức sử dụng bộ đệm ẩn CPU có thể được kiểm soát sử dụng Intel cache allocation technology (CAT) để tránh việc một container làm ô nhiễm bộ đệm ẩn CPU. Điều này đã được mô tả trong Mục 11.2.3, Kiểm soát tài nguyên, và có cùng một cảnh báo: việc giới hạn truy cập bộ đệm ẩn cũng gây hại cho hiệu năng.

**Dung lượng Bộ nhớ**
Memory cgroup cung cấp bốn cơ chế để quản lý mức sử dụng bộ nhớ. Bảng 11.4 mô tả chúng qua tên thiết lập cgroup của họ.

Bảng 11.4 Các thiết lập cgroup bộ nhớ Linux
| Tên | Mô tả |
| --- | --- |
| memory.limit_in_bytes | Một giới hạn kích thước, tính bằng byte. Nếu một container cố gắng sử dụng nhiều hơn kích thước được phân bổ, nó sẽ gặp phải swapping (nếu được cấu hình) hoặc OOM killer. |
| memory.soft_limit_in_bytes | Một giới hạn kích thước, tính bằng byte. Một cách tiếp cận nỗ lực tốt nhất (best-effort) liên quan đến việc thu hồi bộ nhớ để điều hướng các containers tới giới hạn mềm của họ. |
| memory.kmem.limit_in_bytes | Một giới hạn kích thước cho bộ nhớ kernel, tính bằng byte. |
| memory.kmem.tcp.limit_in_bytes | Một giới hạn kích thước cho bộ nhớ đệm TCP, tính bằng byte. |
| memory.pressure_level | Một thông báo áp lực thấp có thể được sử dụng qua lệnh gọi hệ thống eventfd(2). Điều này đòi hỏi các ứng dụng phải hỗ trợ cấu hình mức áp lực và sử dụng system call. |

Cũng có các thông báo hành động thông qua cgroups để các ứng dụng có thể thực hiện hành động khi bộ nhớ sắp cạn: memory.pressure_level và memory.oom_control. Những thứ này yêu cầu cấu hình các thông báo qua syscall eventfd(2).

Lưu ý rằng bộ nhớ không sử dụng của một container có thể được sử dụng bởi các containers khác trong kernel page cache, cải thiện hiệu năng (một hình thức của bursting bộ nhớ).

**Dung lượng Swap**
Memory cgroup cũng cho phép một giới hạn swap được cấu hình. Thiết lập thực sự là bộ nhớ + swap: memsw.limit_in_bytes, thứ là bộ nhớ cộng với swap.

**Dung lượng Hệ thống Tập tin**
Dung lượng hệ thống tập tin thường có thể bị giới hạn bởi hệ thống hạn ngạch tập tin (file system quota). Ví dụ, hệ thống tập tin XFS hỗ trợ cả hạn ngạch cho người dùng, nhóm, và các dự án (projects), nơi các giới hạn mềm có thể cho phép một số vượt quá tạm thời dưới một giới hạn cứng. ZFS và btrfs cũng có hạn ngạch.

**Bộ đệm ẩn Hệ thống Tập tin**
Trong Linux, bộ nhớ được sử dụng bởi file system page cache cho một container được tính cho container đó trong memory cgroup: không yêu cầu thiết lập bổ sung. Nếu container cấu hình swap, mức độ ưu tiên giữa việc favoring swapping so với việc loại bỏ page cache có thể được kiểm soát bởi thiết lập memory.swappiness, tương tự như vm.swappiness trên toàn hệ thống (Chương 7, Bộ nhớ, Mục 7.6.1, Các tham số tinh chỉnh).

**I/O Đĩa**
Blkio cgroup cung cấp các cơ chế để quản lý I/O đĩa. Bảng 11.5 mô tả chúng qua tên thiết lập cgroup của họ.

Bảng 11.5 Các thiết lập blkio cgroup Linux
| Tên | Mô tả |
| --- | --- |
| blkio.weight | Một trọng số cgroup kiểm soát các tài nguyên đĩa trong quá trình tải, tương tự như CPU shares. Nó được sử dụng với trình lập lịch I/O BFQ. |
| blkio.weight_device | Một thiết lập trọng số cho một thiết bị cụ thể. |
| blkio.throttle.read_bps_device | Một giới hạn cho tốc độ đọc byte/s. |
| blkio.throttle.write_bps_device | Một giới hạn cho tốc độ ghi byte/s. |
| blkio.throttle.read_iops_device | Một giới hạn cho IOPS đọc. |
| blkio.throttle.write_iops_device | Một giới hạn cho IOPS ghi. |

Cũng giống như với CPU shares và băng thông, các thiết lập blkio weights và throttle cho phép các tài nguyên I/O đĩa được chia sẻ dựa trên một chính sách về mức ưu tiên và các giới hạn.

**I/O Mạng**
Net_prio cgroup cho phép các mức ưu tiên được thiết lập cho lưu lượng mạng outbound. Những thứ này giống như tùy chọn socket SO_PRIORITY (xem socket(7)), và kiểm soát mức ưu tiên của việc xử lý gói tin trong network stack. Net_cls cgroup có thể gắn thẻ các gói tin với một class ID để quản lý sau này bởi qdiscs. (Điều này cũng hoạt động cho Kubernetes Pods, thứ có thể sử dụng một net_cls cho mỗi Pod.)

Kỷ luật xếp hàng (qdiscs, xem Chương 10, Mạng, Mục 10.4.3, Phần mềm) có thể vận hành trên các class IDs hoặc được gán cho các giao diện mạng ảo container để ưu tiên và điều tiết lưu lượng mạng. Có hơn 50 loại qdiscs khác nhau, mỗi cái có các chính sách, tính năng, và các tunables riêng của chúng. Ví dụ, các cài đặt Kubernetes kubernetes.io/ingress-bandwidth và kubernetes.io/egress-bandwidth được triển khai bằng cách tạo ra một token bucket filter (tbf) qdisc [CNI 18]. Mục 10.7.6, tc, cung cấp một ví dụ về việc thêm và loại bỏ một qdisc tới một giao diện mạng.

Các chương trình BPF có thể được gắn vào cgroups cho các kiểm soát tài nguyên lập trình tùy chỉnh và tường lửa. Một ví dụ là phần mềm Cilium, thứ sử dụng một sự kết hợp của các chương trình BPF tại các tầng khác nhau chẳng hạn như XDP, cgroup, và tc (qdiscs), để hỗ trợ an ninh mạng, cân bằng tải, và các khả năng tường lửa giữa các containers [Cilium 20a].

### 11.3.4 Khả năng Quan sát (Observability)
Những gì có thể quan sát được tùy thuộc vào vị trí từ đó các công cụ quan sát được khởi chạy và các thiết lập bảo mật của host. Bởi vì các containers có thể được cấu hình theo nhiều cách khác nhau, tôi sẽ mô tả trường hợp điển hình. Nhìn chung:
- **Từ host** (không gian tên có đặc quyền nhất): Mọi thứ đều có thể được quan sát, bao gồm các tài nguyên phần cứng, các hệ thống tập tin, các tiến trình khách, các phiên TCP khách, v.v. Các tiến trình khách có thể được thấy và phân tích mà không cần đăng nhập vào các khách. Các hệ thống tập tin khách cũng có thể được duyệt dễ dàng từ host (nhà vận hành đám mây).
- **Từ các khách:** Container thông thường chỉ có thể thấy các tiến trình, hệ thống tập tin, giao diện mạng, và các phiên TCP của chính nó. Một mối quan tâm lớn là các thống kê trên toàn hệ thống chẳng hạn như đối với CPUs và các đĩa: những thứ này thường hiển thị host hơn là chỉ container. Trạng thái của những thống kê này thường không được tài liệu hóa (tôi đã phải viết tài liệu của riêng mình trong Mục 11.3.4.1, Các Công cụ Truyền thống). Các thành phần nội bộ kernel thông thường không thể được kiểm tra, vì các công cụ hiệu năng sử dụng các kernel tracing frameworks (Chương 13 tới 15) thường không hoạt động.

Điểm cuối cùng đã được mô tả trước đó: các containers có nhiều khả năng gặp phải các vấn đề tranh chấp kernel, đồng thời họ cũng bị mất khả năng chẩn đoán những vấn đề đó của người dùng cuối.

Một mối quan tâm phổ biến cho phân tích hiệu năng container là sự hiện diện khả thi của "noisy neighbors" (các bên thuê container khác tiêu thụ tài nguyên một cách tích cực và gây tranh chấp cho những người khác). Vì các tiến trình container đều nằm dưới một kernel duy nhất và có thể được phân tích đồng thời từ host, điều này không khác gì phân tích hiệu năng truyền thống của nhiều tiến trình chạy trên một hệ thống time-sharing. Sự khác biệt chính là cgroups có thể áp đặt các giới hạn phần mềm bổ sung (các kiểm soát tài nguyên) thứ gặp phải trước các giới hạn phần cứng.

Nhiều công cụ giám sát được viết cho các hệ thống độc lập chưa phát triển hỗ trợ cho ảo hóa OS (containers), và mù quáng đối với cgroup và các giới hạn phần mềm khác. Các khách hàng cố gắng sử dụng những thứ này trong các containers có thể thấy rằng chúng dường như hoạt động, nhưng trên thực tế chỉ hiển thị các tài nguyên hệ thống vật lý. Không có sự hỗ trợ cho việc quan sát các kiểm soát tài nguyên đám mây, các công cụ này có thể báo cáo sai rằng các hệ thống có khoảng trống (headroom) khi thực tế chúng đã chạm tới các giới hạn phần mềm. Họ cũng có thể hiển thị mức sử dụng tài nguyên cao thực sự là do các bên thuê khác.

Trên Linux, khả năng quan sát container từ cả host và khách được làm cho phức tạp và tiêu tốn nhiều thời gian hơn do thực tế là hiện tại không có container ID trong kernel, cũng như không có nhiều hỗ trợ container từ các công cụ hiệu năng truyền thống.

Những thách thức này được mô tả trong các phần sau đây tóm tắt trạng thái của các công cụ hiệu năng truyền thống, khám phá khả năng quan sát từ host và các containers, và mô tả một chiến lược để phân tích hiệu năng.

#### 11.3.4.1 Các Công cụ Truyền thống (Traditional Tools)
Dưới dạng tóm tắt về các công cụ hiệu năng truyền thống, Bảng 11.6 mô tả những gì các công cụ khác nhau hiển thị khi chạy từ host và từ một container điển hình (một container sử dụng các namespaces process và mount). Các tình huống mà kết quả có thể không mong đợi, chẳng hạn như khi container có thể quan sát các thống kê của host, được tô đậm.

Bảng 11.6 Các công cụ truyền thống của Linux
| Công cụ | Từ Host | Từ Container |
| --- | --- | --- |
| top | Tiêu đề tóm tắt hiển thị host; bảng tiến trình hiển thị tất cả các tiến trình host và container | **Tiêu đề tóm tắt hiển thị các thống kê hỗn hợp; một số là từ host và một số là từ container.** Bảng tiến trình hiển thị các tiến trình container |
| ps | Hiển thị tất cả các tiến trình | Hiển thị các tiến trình container |
| uptime | Hiển thị mức trung bình tải trên toàn hệ thống | **Hiển thị mức trung bình tải của host** |
| mpstat | Hiển thị mức sử dụng CPU và host | **Hiển thị mức sử dụng vCPUs và host CPU** |
| vmstat | Hiển thị CPUs, bộ nhớ, và các thống kê host khác | **Hiển thị vCPUs, bộ nhớ, và các thống kê host khác** |
| pidstat | Hiển thị tất cả các tiến trình | Hiển thị các tiến trình container |
| free | Hiển thị bộ nhớ host | **Hiển thị bộ nhớ host** |
| iostat | Hiển thị các đĩa host | **Hiển thị các đĩa host** |
| pidstat -d | Hiển thị I/O đĩa của tất cả các tiến trình | Hiển thị I/O đĩa của các tiến trình container |
| sar -n DEV, TCP 1 | Hiển thị các giao diện mạng và các thống kê TCP của host | Hiển thị các giao diện mạng và các thống kê TCP của container |
| perf | Có thể tạo hồ sơ (profile) mọi thứ | **Hoặc không chạy được, hoặc có thể được bật và sau đó có thể tạo hồ sơ các bên thuê khác** |
| tcpdump | Có thể ngửi (sniff) tất cả các giao diện | Chỉ ngửi các giao diện container |
| dmesg | Hiển thị kernel log | **Không chạy được** |

Theo thời gian, hỗ trợ container cho các công cụ có thể cải thiện sao cho chúng chỉ hiển thị các thống kê cụ thể cho container hoặc, thậm chí tốt hơn, hiển thị một sự phân chia giữa container so với host. Những chủ đề này được giải thích thêm trong các phần tiếp theo về khả năng quan sát của host và khách.

#### 11.3.4.2 Host
Khi đăng nhập vào host, tất cả các tài nguyên hệ thống (CPUs, bộ nhớ, hệ thống tập tin, đĩa, mạng) có thể được kiểm tra bằng các công cụ đã bao quát trong các chương trước. Có hai yếu tố bổ sung cần kiểm tra khi sử dụng các containers:
- Các thống kê cho mỗi container
- Ảnh hưởng của các kiểm soát tài nguyên

Như đã mô tả trong Mục 11.3.1, Triển khai, không có khái niệm về một container trong kernel: một container chỉ là một tập hợp các namespaces và cgroups. Container ID mà bạn thấy được tạo ra và quản lý bởi phần mềm không gian người dùng. Dưới đây là các container IDs ví dụ từ Kubernetes (trong trường hợp này, một Pod với một container duy nhất) và Docker:
```bash
# kubectl get pod
NAME                          READY   STATUS              RESTARTS   AGE
kubernetes-b94cb9bff-kqvm1    0/1     ContainerCreating   0          3m
[...]
# docker ps
CONTAINER ID   IMAGE    COMMAND   CREATED        STATUS          PORTS   NAMES
6280172ea7b9   ubuntu   "bash"    4 weeks ago    Up 4 weeks              eager_bhaskara
[...]
```
Điều này trình bày một vấn đề cho các công cụ hiệu năng truyền thống chẳng hạn như ps(1), top(1), và vân vân. Để hiển thị một container ID, họ sẽ cần hỗ trợ cho Kubernetes, Docker, và mọi nền tảng container khác. Thay vào đó, nếu có hỗ trợ kernel cho một container ID, nó sẽ trở thành tiêu chuẩn để được hỗ trợ bởi tất cả các công cụ hiệu năng. Đây là trường hợp với Solaris kernel, nơi các containers được gọi là *zones* và có một zone ID dựa trên kernel có thể được quan sát sử dụng ps(1) và những cái khác. (Tiêu đề Truy vết BPF sau đây hiển thị một giải pháp Linux sử dụng nodename từ không gian tên UTS cho ID container.)

Trong thực tế, các thống kê hiệu năng theo container ID trên Linux có thể được kiểm tra bằng cách sử dụng:
- **Các công cụ container** được cung cấp bởi nền tảng container; ví dụ: Docker có một công cụ để hiển thị mức sử dụng tài nguyên theo container.
- **Phần mềm giám sát hiệu năng**, thứ điển hình là có các plugins cho các nền tảng container khác nhau.
- **Các thống kê Cgroup** và các công cụ sử dụng chúng. Điều này yêu cầu một bước bổ sung để tìm ra cgroups nào ánh xạ tới container nào.
- **Namespace mapping** từ host, chẳng hạn như bằng cách sử dụng nsenter(1), để cho phép các công cụ hiệu năng host được chạy bên trong container. Một tiến trình khách có thể được nhận diện từ host, và nsenter(1) được sử dụng với tùy chọn -p (không gian tên PID). Mặc dù các thống kê hiệu năng có thể không phải cho một mình container: xem Bảng 11.6. Tùy chọn -n (không gian tên mạng) cũng hữu ích cho việc chạy các công cụ mạng bên trong cùng không gian tên mạng (ping(8), tcpdump(8)).
- **Truy vết BPF**, thứ có thể đọc thông tin cgroup và không gian tên từ kernel.

Các phần sau đây cung cấp các ví dụ cho các công cụ container, thống kê cgroup, việc nhập không gian tên (namespace entering), và truy vết BPF, cũng như khả năng quan sát kiểm soát tài nguyên.

**Các công cụ Container**
Trình điều phối container Kubernetes cung cấp một cách để kiểm tra việc sử dụng tài nguyên cơ bản bằng cách sử dụng kubectl top.

Kiểm tra các hosts ("nodes"):
```bash
# kubectl top nodes
NAME                          CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
bgregg-i-03cb3a7e46298b38e    1781m        10%    2880Mi          9%
```
Thời gian CPU(cores) hiển thị số mili giây tích lũy của thời gian CPU, và CPU% hiển thị mức sử dụng hiện tại của node.

Kiểm tra các containers ("Pods"):
```bash
# kubectl top pods
NAME                          CPU(cores)   MEMORY(bytes)
kubernetes-b94cb9bff-p7jsp    73m          9Mi
```
Điều này hiển thị thời gian CPU tích lũy và kích thước bộ nhớ hiện tại.

Những lệnh này yêu cầu một metrics server đang chạy, thứ có thể được thêm vào theo mặc định tùy thuộc vào cách bạn khởi tạo Kubernetes. Các công cụ giám sát khác cũng có thể hiển thị những chỉ số này trong một GUI, bao gồm cAdvisor, Sysdig, và Google Cloud Monitoring [Kubernetes 20c].

Công nghệ Docker container cung cấp một số lệnh phụ phân tích docker(1), bao gồm stats. Ví dụ, từ một host sản xuất:
```bash
# docker stats
CONTAINER     CPU %   MEM USAGE / LIMIT     MEM %   NET I/O     BLOCK I/O     PIDS
353426a09db1  526.81% 4.061 GiB / 8.5 GiB   47.78%  0 B / 0 B   2.818 MB / 0 B 247
6bf166a66e08  303.82% 3.448 GiB / 8.5 GiB   40.57%  0 B / 0 B   2.032 MB / 0 B 267
58dcf8aed0a7  41.01%  1.322 GiB / 2.5 GiB   52.89%  0 B / 0 B   0 B / 0 B      229
61061566ffe5  85.92%  220.9 MiB / 3.023 GiB 7.14%   0 B / 0 B   43.4 MB / 0 B  61
bdc721460293  2.69%   1.204 GiB / 3.906 GiB 30.82%  0 B / 0 B   4.35 MB / 0 B  66
[...]
```
Điều này cho thấy một container với UUID 353426a09db1 đang tiêu tốn tổng cộng 527% CPU cho khoảng thời gian cập nhật này và đang sử dụng 4 Gbytes bộ nhớ chính so với giới hạn 8.5 Gbyte. Cho khoảng thời gian đó không có mạng I/O, và chỉ một lượng nhỏ (Mbytes) I/O đĩa.

**Các Thống kê Cgroup**
Các thống kê cgroup khác nhau khả dụng từ /sys/fs/cgroup. Những thứ này được đọc và vẽ đồ thị bởi các công cụ và trình giám sát container khác nhau, và có thể được kiểm tra trực tiếp tại dòng lệnh:
```bash
# cd /sys/fs/cgroup/cpu,cpuacct/docker/02a7cf65f82e3f3e75283944caa4462e82f...
# cat cpuacct.usage
1615816262506
# cat cpu.stat
nr_periods 507
nr_throttled 74
throttled_time 3816445175
```
Tập tin cpuacct.usage hiển thị mức sử dụng CPU của cgroup này tính bằng nano giây. Tập tin cpu.stat hiển thị số lượng các khoảng thời gian mà cgroup này bị điều tiết (nr_throttled), cũng như tổng thời gian bị điều tiết tính theo nano giây. Ví dụ này cho thấy cgroup này đã bị điều tiết 74 lần trong tổng cộng 507 khoảng thời gian, cho tổng cộng 3.8 giây thời gian bị điều tiết.

Cũng có một cpuacct.usage_percpu, lần này là một cgroup Kubernetes:
```bash
# cd /sys/fs/cgroup/cpu,cpuacct/kubepods/burstable/pod82e745...
# cat cpuacct.usage_percpu
37944772821 35729154566 35996200949 36443793055 36517861942 36156377488 36176348313
35874604278 37378190414 35464528409 35291309575 35829280628 36105557113 36538524246
36077297144 35976388595
```
Kết quả bao gồm 16 trường cho hệ thống 16-CPU này, với tổng thời gian CPU tính theo nano giây. Các chỉ số cgroupv1 được tài liệu hóa trong mã nguồn kernel dưới Documentation/cgroup-v1/cpuacct.txt.

Các công cụ dòng lệnh sử dụng những thống kê này bao gồm htop(1) và systemd-cgtop(1). Chẳng hạn, chạy systemd-cgtop(1) trên một host container sản xuất:
```bash
# systemd-cgtop
Control Group                               Tasks   %CPU   Memory  Input/s Output/s
/                                               -  798.2    45.9G        -        -
/docker                                      1082  790.1    42.1G        -        -
/docker/dcf3a...9d28fc4a1c72bbaff4a24834      200  610.5    24.0G        -        -
/docker/370a3...e64ca01198f1e843ade7ce21      170  174.0     3.0G        -        -
/system.slice                                 748    5.3     4.1G        -        -
/system.slice/daemontools.service             422    4.0     2.8G        -        -
/docker/dc277...42ab0603bbda2ac8af67996b      160    2.5     2.3G        -        -
/user.slice                                     5    2.0    15.7M        -        -
/user.slice/user-0.slice                        5    2.0    15.7M        -        -
/user.slice/u....slice/session-c26.scope        3    2.0    13.3M        -        -
/docker/ab452...c946f8447f2a4184f3fccff2a     174    1.0     6.3G        -        -
/docker/e18bd...26ffdd7368b870aa3d1deb7a      156    0.8     2.9G        -        -
[...]
```
Kết quả này cho thấy một cgroup mang tên /docker/dcf3a... đang tiêu tốn 610.5% tổng CPU cho khoảng thời gian cập nhật này (trải dài qua nhiều CPUs) và 24 Gbytes của bộ nhớ chính, với 200 tác vụ đang chạy. Kết quả cũng hiển thị một số cgroups được tạo ra bởi systemd cho các dịch vụ hệ thống (/system.slice) và người dùng (/user.slice).

**Namespace Mapping**
Các containers thông thường sử dụng các namespaces khác nhau cho các ID tiến trình và các lần mount. Đối với các không gian tên tiến trình, điều đó có nghĩa là PID trong khách không có khả năng khớp với PID trong host.

Khi chẩn đoán các vấn đề hiệu năng, trước tiên hãy đăng nhập vào container sao cho tôi có thể thấy vấn đề từ quan điểm của người dùng cuối. Sau đó, tôi có thể đăng nhập vào host để tiếp tục điều tra bằng các công cụ trên toàn hệ thống, nhưng PID có thể không giống nhau. Việc ánh xạ được trình bày trong tập tin /proc/PID/status. Ví dụ, từ host:
```bash
host# grep NSpid /proc/4915/status
NSpid:    4915    753
```
Điều này cho thấy PID 4915 trên host là PID 753 trong khách. Thật không may, tôi thường cần làm điều ngược lại: cho PID 753 của container, tôi cần tìm PID của host. Một cách (hơi kém hiệu quả) để làm điều này là quét tất cả các status files:
```bash
host# awk '$1 == "NSpid:" && $3 == 753 { print $2 }' /proc/*/status
4915
```
Trong trường hợp này nó chỉ ra rằng PID khách 753 là PID host 4915. Lưu ý rằng kết quả có thể hiển thị nhiều hơn một PID host, vì "753" có thể xuất hiện trong nhiều không gian tên tiến trình. Trong trường hợp đó, bạn sẽ cần tìm ra 753 nào là từ không gian tên khớp. Tệp /proc/PID/ns chứa các liên kết tượng trưng (symlinks) chứa các ID không gian tên, và có thể được sử dụng cho mục đích này. Kiểm tra chúng từ khách và sau đó là host:
```bash
guest# ls -lh /proc/753/ns/pid
lrwxrwxrwx 1 root root 0 Mar 15 20:47 /proc/753/ns/pid -> 'pid:[4026532216]'

host# ls -lh /proc/4915/ns/pid
lrwxrwxrwx 1 root root 0 Mar 15 20:46 /proc/4915/ns/pid -> 'pid:[4026532216]'
```
Lưu ý các ID không gian tên khớp nhau (4026532216): điều này xác nhận rằng PID host 4915 là giống như PID khách 753.

Các không gian tên mount trình diện các thách thức tương tự. Chạy lệnh perf(1) từ host, chẳng hạn, các tìm kiếm trong /tmp/perf-PID.map cho các tệp ký hiệu (symbol files) bổ sung, nhưng các ứng dụng container gửi chúng tới /tmp trong container, thứ không giống như /tmp trong host. Ngoài ra, PID có thể khác biệt do các không gian tên tiến trình. Alice Goldfuss lần đầu tiên đăng tải một cách giải quyết cho vấn đề này liên quan đến việc di chuyển và đổi tên các tệp ký hiệu đó sao cho chúng có sẵn trong host [Goldfuss 17]. perf(1) kể từ đó đã đạt được sự hỗ trợ không gian tên để tránh vấn đề này, và kernel cung cấp một ánh xạ không gian tên /proc/PID/root để truy cập trực tiếp vào gốc của container ("/"). Ví dụ:
```bash
host# ls -lh /proc/4915/root/tmp
total 0
-rw-r--r-- 1 root root 0 Mar 15 20:54 I_am_in_the_container.txt
```
Đây là danh sách một tệp trong /tmp của container.

Ngoài các tệp /proc, lệnh nsenter(1) có thể thực hiện các lệnh khác trong các không gian tên đã chọn. Các lần nhập không gian tên mount (-m) và process (-p) sau đây từ PID 4915 (-t 4915):
```bash
# nsenter -t 4915 -m -p top
top - 21:14:24 up 32 days, 23:23,  0 users,  load average: 0.32, 0.09, 0.02
Tasks: 3 total,   2 running, 1 sleeping,   0 stopped,   0 zombie
%Cpu(s): 0.2 us,  0.1 sy,  0.0 ni, 99.4 id,  0.0 wa,  0.0 hi,  0.0 si,  0.2 st
KiB Mem : 1996844 total,    98400 free,   858060 used,  1040384 buff/cache
KiB Swap:        0 total,        0 free,        0 used.   961564 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
  753 root      20   0  818504  93428  11996 R 100.0  4.7   0:27.88 java
    1 root      20   0   18504   3212   2796 S    0.0  0.2   0:17.57 bash
  766 root      20   0   38364   3420   2968 R    0.0  0.2   0:00.00 top
```
Điều này cho thấy tiến trình hàng đầu là java với PID 753.

**Truy vết BPF**
Một số công cụ truy vết BPF đã có hỗ trợ container, nhưng nhiều cái thì không. May mắn thay, việc thêm hỗ trợ cho các công cụ bpftrace khi cần thiết thường không khó; ví dụ sau đây là một mẫu. Chương 15 có lời giải thích về lập trình bpftrace.

Công cụ forks.bt đếm số lượng các tiến trình mới được tạo ra trong khi truy vết bằng cách instrument các syscalls clone(2), fork(2), và vfork(2). Nguồn là:
```c
#!/usr/local/bin/bpftrace

tracepoint:syscalls:sys_enter_clone,
tracepoint:syscalls:sys_enter_fork,
tracepoint:syscalls:sys_enter_vfork
{
          @new_processes = count();
}
```
Kết quả ví dụ:
```bash
# ./forks.bt
Attaching 3 probes...
^C

@new_processes: 590
```
Điều này cho thấy 590 tiến trình mới được tạo ra trên toàn hệ thống trong khi truy vết.

Để chia nhỏ điều này theo container, một cách tiếp cận là in ra nodename (hostname) từ UTS namespace. Điều này dựa trên việc phần mềm container cấu hình namespace này, thứ là điển hình cho trường hợp này. Mã nguồn trở thành, với các bổ sung được tô đậm:
```c
#!/usr/local/bin/bpftrace

#include <linux/sched.h>
#include <linux/nsproxy.h>
#include <linux/utsname.h>

tracepoint:syscalls:sys_enter_clone,
tracepoint:syscalls:sys_enter_fork,
tracepoint:syscalls:sys_enter_vfork
{
          $task = (struct task_struct *)curtask;
          $nodename = $task->nsproxy->uts_ns->name.nodename;
          @new_processes[$nodename] = count();
}
```
Mã bổ sung này duyệt qua từ task_struct kernel hiện tại tới uts namespace nodename, và bao gồm nó trong bản đồ kết quả @new_processes như một khóa.

Kết quả ví dụ:
```bash
# ./forks.bt
Attaching 3 probes...
^C

@new_processes[ip-10-1-239-218]: 171
@new_processes[efe9f9be6185]: 743
```
Kết quả hiện được chia nhỏ theo container, cho thấy nodename 6280172ea7b9 (một container) đã tạo ra 743 tiến trình trong khi truy vết. Nodename còn lại, ip-10-1-239-218, là hệ thống host.

Việc này chỉ hoạt động vì các lệnh gọi syscall vận hành trong ngữ cảnh tác vụ (tiến trình), vì vậy curtask trả về task_struct chịu trách nhiệm từ đó chúng ta lấy uts nodename. Nếu các sự kiện bất đồng bộ của tiến trình được truy vết, ví dụ, hoàn thành ngắt từ I/O đĩa, thì tiến trình đang on-CPU có thể không phải là bên chịu trách nhiệm và curtask sẽ không nhận diện nodename chính xác.

Vì việc lấy uts nodename có thể trở nên được sử dụng phổ biến trong bpftrace, tôi tưởng tượng chúng ta sẽ thêm một biến tích hợp sẵn, nodename, sao cho sự bổ sung duy nhất là:
```c
@new_processes[nodename] = count();
```
Kiểm tra các bản cập nhật bpftrace để xem liệu tính năng này đã được thêm vào chưa.

**Resource Controls (Kiểm soát Tài nguyên)**
Các kiểm soát tài nguyên được liệt kê trong Mục 11.3.3, Kiểm soát Tài nguyên, phải được quan sát để nhận diện khi nào một container bị giới hạn bởi chúng. Các công cụ hiệu năng và tài liệu truyền thống tập trung vào các tài nguyên vật lý, và mù quáng trước những giới hạn do phần mềm áp đặt này.

Kiểm tra các kiểm soát tài nguyên đã được mô tả trong phương pháp USE (Chương 2, Các phương pháp luận, Mục 2.5.9, Phương pháp USE), thứ lặp qua các tài nguyên và kiểm tra các giới hạn, sự bão hòa, và các lỗi. Với các kiểm soát tài nguyên hiện diện, chúng cũng phải được kiểm tra cho từng tài nguyên.

Phần trước mang tên Cgroup Statistics đã trình bày tập tin /sys/fs/cgroup/.../cpu.stat, thứ cung cấp các thống kê về sự bão hòa CPU: số lượng các khoảng thời gian bị điều tiết (nr_throttled), và tổng thời gian tính theo nano giây. Ví dụ này cho thấy cgroup này đã bị điều tiết 74 lần trong số 507 khoảng thời gian, cho tổng cộng 3.8 giây thời gian bị điều tiết.

Các CPU cũng có thể được quản lý bởi shares, như đã được mô tả trong phần CPU Shares and Bandwidth sớm hơn. Một container bị giới hạn bởi shares khó nhận diện hơn, vì không có thống kê nào. Tôi đã phát triển lưu đồ trong Hình 11.13 cho quá trình xác định liệu và cách các CPU container bị điều tiết [Gregg 17g]:

(Hình 11.13 Phân tích điều tiết CPU Container)

Quá trình trong Hình 11.13 xác định liệu và cách thức một container CPUs được điều tiết bằng cách sử dụng năm thống kê:
- **Throttled time:** cpu cgroup throttled_time
- **Non-voluntary context switches:** Có thể được đọc từ /proc/PID/status dưới dạng nonvoluntary_ctxt_switches
- **Host has idle CPU:** Có thể được đọc từ mpstat(1) %idle, /proc/stat, và các công cụ khác
- **cpuset CPUs 100% busy:** Nếu cpusets đang được sử dụng, mức sử dụng của chúng có thể được đọc từ mpstat(1), /proc/stat, v.v.
- **All other tenants idle:** Có thể được xác định từ một công cụ đặc thù cho container (docker stat), hoặc các công cụ hệ thống cho thấy sự thiếu hụt tranh chấp cho các tài nguyên CPU (ví dụ: top(1) chỉ hiển thị một container tiêu tốn %CPU)

Một quá trình tương tự có thể được phát triển cho các tài nguyên khác, và hỗ trợ các thống kê bao gồm mức sử dụng cgroup nên được làm sẵn có trong các công cụ và trình giám sát. Một công cụ hoặc trình giám sát lý tưởng thực hiện việc xác định cho bạn, và báo cáo nếu và khi các khách bị điều tiết.

#### 11.3.4.3 Guest (Container)
Bạn có thể kỳ vọng rằng các công cụ hiệu năng chạy từ một container sẽ chỉ hiển thị các thống kê của container, nhưng điều đó thường không phải là trường hợp. Ví dụ, chạy iostat(1) trên một container rảnh rỗi:
```bash
container# iostat -sxz 1
[...]
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          57.29    0.00    8.54   33.17    0.00    1.01

Device             tps      kB/s    rqm/s   await aqu-sz  areq-sz  %util
nvme0n1        2578.00  12436.00   331.00    0.33   0.00     4.82 100.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          51.78    0.00    7.61   40.61    0.00    0.00

Device             tps      kB/s    rqm/s   await aqu-sz  areq-sz  %util
nvme0n1        2664.00  11020.00    88.00    0.32   0.00     4.14  98.80
[...]
```
Kết quả này hiển thị cả khối lượng công việc CPU và đĩa, thế nhưng container này hoàn toàn rảnh rỗi. Điều này có thể gây nhầm lẫn cho những người mới làm quen với ảo hóa OS—tại sao container của tôi lại bận rộn? Đó là vì các công cụ đang hiển thị các thống kê của host bao gồm cả hoạt động từ các bên thuê khác.

Trạng thái của các công cụ hiệu năng này đã được tóm tắt trong Mục 11.3.4, Khả năng Quan sát, tiểu mục Traditional Tools. Những công cụ này đang trở nên "nhận thức container" (container aware) hơn theo thời gian, hỗ trợ các thống kê cgroup và cung cấp các thống kê chỉ dành cho container trong một container.

Có các thống kê cgroup cho I/O khối. Từ cùng một container:
```bash
container# cat /sys/fs/cgroup/blkio/blkio.throttle.io_serviced
259:0 Read 452
259:0 Write 352
259:0 Sync 692
259:0 Async 112
259:0 Discard 0
259:0 Total 804
Total 804
container# sleep 10
container# cat /sys/fs/cgroup/blkio/blkio.throttle.io_serviced
259:0 Read 452
259:0 Write 352
259:0 Sync 692
259:0 Async 112
259:0 Discard 0
259:0 Total 804
Total 804
```
Các loại thao tác được đếm. Tôi đã in chúng hai lần với một lệnh ngủ 10 để thiết lập một khoảng thời gian: bạn có thể thấy rằng các số lượng không tăng lên trong khoảng thời gian đó; do đó, container không phát hành I/O đĩa. Có một tập tin khác cho số byte: blkio.throttle.io_service_bytes.

Thật không may, những bộ đếm này không cung cấp tất cả các thống kê mà iostat(1) cần. Nhiều bộ đếm hơn cần được để lộ qua cgroup sao cho iostat(1) có thể trở nên nhận thức container.

**Container Awareness (Nhận thức Container)**
Việc làm cho một công cụ nhận thức container không nhất thiết có nghĩa là hạn chế chế độ xem của nó chỉ vào container riêng của nó: Có những lợi ích đối với một container khi thấy trạng thái của các tài nguyên vật lý. Nó tùy thuộc vào mục tiêu cho việc sử dụng các containers, thứ có thể là:
A) **Container là một máy chủ cô lập:** Nếu đây là mục tiêu, như thường lệ là trường hợp của các nhà cung cấp đám mây, thì việc làm cho các công cụ nhận thức container có nghĩa là chúng chỉ nên hiển thị hoạt động của container hiện tại. iostat(1), ví dụ, chỉ nên hiển thị hoạt động I/O đĩa của container hiện tại và không phải của những cái khác. Điều này có thể được triển khai bằng cách cô lập tất cả các nguồn thống kê để chỉ hiển thị container hiện tại (/proc, /sys, netlink, v.v.). Một sự cô lập như vậy sẽ vừa giúp ích vừa cản trở việc phân tích của khách: việc chẩn đoán tranh chấp tài nguyên từ các bên thuê khác sẽ khó khăn hơn cho khách và sẽ phụ thuộc vào sự suy luận từ các đợt gia tăng không giải thích được trong độ trễ thiết bị.
B) **Container là một giải pháp đóng gói (packaging solution):** Đối với các công ty vận hành các đám mây container riêng của họ, việc cô lập một container khỏi các thống kê của host có thể không nhất thiết là bắt buộc. Cho phép người dùng thấy các thống kê host (như hiện nay đang được thực hiện một cách tình cờ), như đã thấy trước đó với iostat(1)) có nghĩa là người dùng cuối có thể hiểu được trạng thái của các thiết bị phần cứng và các vấn đề gây ra bởi những người hàng xóm ồn ào. Để làm cho iostat(1) nhận thức container hơn trong kịch bản này có nghĩa là cung cấp một bản phân tích cho thấy việc sử dụng container hiện tại so với host hoặc việc sử dụng của các container khác, thay vì che giấu những thống kê đó.

Đối với cả hai kịch bản, các công cụ cũng nên hỗ trợ việc hiển thị các kiểm soát tài nguyên khi phù hợp như một phần của khả năng quan sát container. Để tiếp tục với ví dụ iostat(1), nó cũng có thể cung cấp một giới hạn %cap dựa trên các giới hạn blkio throughput và IOPS, sao cho một container biết liệu I/O đĩa có bị giới hạn bởi các kiểm soát tài nguyên hay không.

Nếu khả năng quan sát tài nguyên vật lý được cho phép, các khách sẽ có khả năng loại trừ một số loại vấn đề, bao gồm cả những người hàng xóm ồn ào. Điều này có thể giảm nhẹ gánh nặng hỗ trợ cho các nhà vận hành container: mọi người có xu hướng đổ lỗi cho những gì họ không thể quan sát. Đây cũng là một sự khác biệt quan trọng so với ảo hóa phần cứng, thứ che giấu các tài nguyên vật lý khỏi các khách và không có cách nào để chia sẻ những thống kê đó (trừ khi các phương tiện bên ngoài được sử dụng). Lý tưởng nhất, sẽ có một thiết lập trong tương lai trong Linux để kiểm soát việc chia sẻ các thống kê host, sao cho mỗi môi trường container có thể lựa chọn giữa A hoặc B như mong muốn.

**Tracing Tools**
Các công cụ truy vết dựa trên kernel tiên tiến, chẳng hạn như perf(1), Ftrace, và BPF, có các vấn đề tương tự phía trước để làm cho chúng nhận thức container. Chúng hiện không hoạt động từ bên trong một container do các quyền hạn cần thiết cho các lệnh gọi hệ thống khác nhau (perf_event_open(2), bpf(2), v.v.) và quyền truy cập vào các tập tin /proc và /sys khác nhau. Mô tả tương lai của họ cho các kịch bản A và B sớm hơn:
A) **Yêu cầu cô lập:** Cho phép các containers sử dụng các công cụ truy vết có thể thực hiện được thông qua:
   - **Lọc kernel:** Các sự kiện và các đối số của chúng có thể được lọc bởi kernel, sao cho, ví dụ, truy vết tracepoint block:block_rq_issue chỉ hiển thị I/O đĩa của container hiện tại.
   - **Host API:** Host để lộ việc truy cập vào các công cụ truy vết nhất định qua một API bảo mật hoặc GUI. Một container có thể, ví dụ, yêu cầu các công cụ BCC phổ biến chẳng hạn như execsnoop(8) và biolatency(8) để thực thi, và host sẽ xác thực yêu cầu, thực thi một phiên bản được lọc của công cụ, và trả về với kết quả.
B) **Không yêu cầu cô lập:** Các tài nguyên (syscalls, /proc, và /sys) được cung cấp sẵn trong container sao cho các công cụ truy vết hoạt động. Trình truy vết có thể trở nên nhận thức container để tạo điều kiện thuận lợi cho việc lọc các sự kiện chỉ cho container hiện tại.

Việc làm cho các công cụ và các thống kê nhận thức container đã là một quá trình chậm chạp trong Linux và các kernels khác, và có khả năng sẽ mất nhiều năm trước khi chúng hoàn thành. Điều này khiến nhiều người dùng nâng cao là những người đang ghi nhật ký vào các hệ thống để sử dụng các công cụ hiệu năng tại dòng lệnh; nhiều người dùng thay vào đó sử dụng các sản phẩm giám sát với các agents đã nhận thức container (ở một mức độ nào đó).

#### 11.3.4.4 Chiến lược
Các chương trước đã bao quát các kỹ thuật phân tích cho các tài nguyên hệ thống vật lý và bao gồm các phương pháp luận khác nhau. Những điều này có thể được tuân theo cho các nhà vận hành host, và ở một mức độ nào đó bởi các khách, ghi nhớ những hạn chế đã đề cập trước đó. Đối với khách, mức sử dụng tài nguyên cấp cao thông thường quan sát được, nhưng việc đào sâu vào kernel thông thường là không khả thi.

Bên cạnh các tài nguyên vật lý, các giới hạn đám mây được áp đặt bởi các kiểm soát tài nguyên cũng nên được kiểm tra, bởi cả các nhà vận hành host và các bên thuê khách. Khi hiện diện, chúng có nhiều khả năng đang có hiệu lực và nên được kiểm tra trước tiên.

Bởi vì nhiều công cụ quan sát truyền thống đã được tạo ra trước khi các containers và các kiểm soát tài nguyên tồn tại (ví dụ: top(1), iostat(1)), chúng không bao gồm thông tin kiểm soát tài nguyên theo mặc định, và người dùng có thể quên kiểm tra chúng.

Dưới đây là một số bình luận và chiến lược cho việc kiểm tra từng kiểm soát tài nguyên:
- **CPU:** Xem lưu đồ Hình 11.13. Việc sử dụng cpusets, băng thông, và shares tất cả đều cần được kiểm tra.
- **Bộ nhớ:** Cho bộ nhớ chính, kiểm tra mức sử dụng hiện tại so với bất kỳ giới hạn bộ nhớ cgroup nào.
- **Dung lượng hệ thống tập tin:** Điều này nên quan sát được cho bất kỳ hệ thống tập tin nào (bao gồm cả sử dụng df(1)).
- **I/O Đĩa:** Kiểm tra cấu hình của các đợt điều tiết blkio cgroup (/sys/fs/cgroup/blkio) và các thống kê từ các tập tin blkio.throttle.io_serviced và blkio.throttle.io_service_bytes: nếu chúng đang tăng với cùng một tốc độ như các đợt điều tiết, thì đó là bằng chứng cho thấy đĩa I/O bị giới hạn thông lượng. Nếu có sẵn truy vết BPF, công cụ blkthrot(8) cũng có thể được sử dụng để xác nhận việc điều tiết blkio [Gregg 19].
- **I/O Mạng:** Kiểm tra thông lượng mạng hiện tại so với bất kỳ giới hạn băng thông đã biết nào, thứ có thể chỉ quan sát được từ host. Việc gặp phải giới hạn khiến độ trễ mạng I/O tăng lên, khi các bên thuê bị điều tiết.

Một bình luận cuối cùng: phần này mô tả cgroup v1 và trạng thái hiện tại của các containers Linux. Các khả năng kernel đang thay đổi nhanh chóng, để lại các khu vực khác chẳng hạn như tài liệu của nhà cung cấp và nhận thức container trong công cụ đang đuổi theo. Để cập nhật với Linux containers bạn sẽ cần kiểm tra các sự bổ sung trong các bản phát hành kernel mới, và đọc qua thư mục Tài liệu (Documentation) trong mã nguồn Linux. Tôi cũng khuyên bạn nên đọc bất kỳ tài liệu nào được viết bởi Tejun Heo, nhà phát triển dẫn đầu của cgroups v2, bao gồm Documentation/admin-guide/cgroup-v2.rst trong Linux source [Heo 15].

## 11.4 Ảo hóa trọng lượng nhẹ (Lightweight Virtualization)
Ảo hóa phần cứng trọng lượng nhẹ đã được thiết kế để trở thành cái tốt nhất của cả hai thế giới: sự bảo mật của ảo hóa phần cứng với hiệu quả và thời gian boot nhanh của các containers. Chúng được mô tả trong Hình 11.14 dựa trên Firecracker, bên cạnh các containers để so sánh.

Ảo hóa phần cứng trọng lượng nhẹ sử dụng một hypervisor trọng lượng nhẹ dựa trên ảo hóa phần cứng, và một số lượng tối thiểu các thiết bị được mô phỏng. Điều này khác biệt so với các máy ảo hóa phần cứng đầy đủ (Mục 11.2, Ảo hóa phần cứng), thứ bắt nguồn từ các máy tính để bàn ảo và bao gồm hỗ trợ cho video, âm thanh, BIOS, bus PCI, và các thiết bị khác, cũng như các mức độ khác nhau của hỗ trợ bộ xử lý. Một hypervisor chỉ dành cho điện toán máy chủ không cần hỗ trợ những thiết bị này, và một cái được viết ngày nay có thể giả định rằng các tính năng ảo hóa phần cứng hiện đại đã có sẵn.

(Hình 11.14 Ảo hóa trọng lượng nhẹ)

Để mô tả sự khác biệt mà điều này tạo ra: bộ giả lập nhanh (QEMU) là một phần mềm hypervisor ảo hóa phần cứng hoàn chỉnh được sử dụng cho KVM, và có hơn 1.4 triệu dòng mã (phiên bản QEMU 4.2). Amazon Firecracker là một hypervisor trọng lượng nhẹ và chỉ có 50 nghìn dòng mã [Agache 20].

Các máy ảo trọng lượng nhẹ (Lightweight VMs) hoạt động tương tự như cấu hình Config B của các VMs ảo hóa phần cứng được mô tả trong Mục 11.2. So với các VMs ảo hóa phần cứng, Lightweight VMs có thời gian boot nhanh hơn nhiều, chi phí bộ nhớ thấp hơn, và bảo mật được cải thiện. Các hypervisors trọng lượng nhẹ có thể cải thiện bảo mật hơn nữa bằng cách cấu hình các namespaces như một tầng bảo mật khác, như được hình ảnh hóa trong Hình 11.14.

Một số triển khai mô tả các máy ảo trọng lượng nhẹ là các containers, và những cái khác sử dụng thuật ngữ *MicroVM*. Tôi thích thuật ngữ MicroVM hơn, vì thuật ngữ containers thường được liên kết với ảo hóa OS.

### 11.4.1 Triển khai
Có một vài dự án ảo hóa phần cứng trọng lượng nhẹ, bao gồm:
- **Intel Clear Containers:** Ra mắt vào năm 2015, dự án này đã sử dụng các tính năng Intel VT để cung cấp các máy ảo trọng lượng nhẹ. Dự án này đã chứng minh tiềm năng của các containers ảo hóa phần cứng, đạt được thời gian boot dưới 45 ms [Kadera 16]. Vào năm 2017, Intel Clear Containers đã tham gia dự án Kata Containers, nơi quá trình phát triển được tiếp tục.
- **Kata Containers:** Ra mắt vào năm 2017, dự án này dựa trên Intel Clear Containers và Hyper.sh RunV, và nằm dưới sự quản trị của OpenStack foundation. Khẩu hiệu trang web của nó là: "Tốc độ của các containers, sự bảo mật của các VMs" [Kata Containers 20].
- **Google gVisor:** Ra mắt vào năm 2018 dưới dạng mã nguồn mở, gVisor sử dụng một kernel không gian người dùng chuyên dụng cho các khách, được viết bằng Go, thứ cải thiện bảo mật container.
- **Amazon Firecracker:** Ra mắt vào năm 2019 dưới dạng mã nguồn mở [Firecracker 20], dự án này sử dụng KVM với một VMM trọng lượng nhẹ thay vì QEMU, và đạt được thời gian boot khoảng 100 ms (boot hệ thống) [Agache 20].

Các phần sau đây mô tả việc triển khai chung thường được sử dụng: một hypervisor ảo hóa phần cứng trọng lượng nhẹ (Intel Clear Containers, Kata Containers, Firecracker). gVisor là một cách tiếp cận khác triển khai kernel trọng lượng nhẹ riêng của nó, và có các đặc tính giống với các containers ảo hóa OS hơn (Mục 11.3, Ảo hóa OS).

### 11.4.2 Chi phí (Overhead)
Chi phí là tương tự như của ảo hóa phần cứng KVM đã được mô tả trong Mục 11.2.2, Chi phí, với một dấu ấn bộ nhớ (memory footprint) thấp hơn đáng kể vì VMM là nhỏ hơn nhiều. Intel Clear Containers 2.0 đã báo cáo chi phí bộ nhớ 48–50 Mbytes cho mỗi container [Kadera 16]; Amazon Firecracker đã báo cáo chi phí thấp hơn là 5 Mbytes [Agache 20].

### 11.4.3 Kiểm soát tài nguyên
Vì VMM chạy như một tiến trình trên host, chúng có thể được quản lý bởi các kiểm soát tài nguyên cấp OS: cgroups, qdiscs, v.v., tương tự như việc ảo hóa KVM được mô tả trong Mục 11.2.3, Kiểm soát tài nguyên. Những kiểm soát tài nguyên cấp OS này cũng đã được thảo luận chi tiết hơn cho các containers trong Mục 11.3.3, Kiểm soát tài nguyên.

### 11.4.4 Khả năng quan sát
Khả năng quan sát là tương tự như của ảo hóa phần cứng KVM đã được mô tả trong Mục 11.2.4, Khả năng quan sát. Tóm lại:
- **Từ host:** Tất cả các tài nguyên vật lý có thể được quan sát bằng cách sử dụng các công cụ OS tiêu chuẩn, như đã bao quát trong các chương trước. Các VMs khách là nhìn thấy được dưới dạng các tiến trình. Các thành phần nội bộ khách, bao gồm các tiến trình bên trong VM và hệ thống tập tin của chúng, không thể quan sát được trực tiếp. Để một nhà vận hành hypervisor phân tích các thành phần nội bộ khách, họ phải được cấp quyền truy cập (ví dụ: SSH).
- **Từ các khách:** Các tài nguyên ảo hóa và việc sử dụng chúng bởi khách có thể được thấy, và các vấn đề vật lý được suy luận. Các công cụ truy vết kernel, bao gồm các công cụ dựa trên BPF, đều hoạt động vì VM có kernel chuyên dụng của riêng nó.

Như một ví dụ về khả năng quan sát, phần sau đây hiển thị một Firecracker VM như được quan sát sử dụng top(1) từ host:
```bash
host# top
top - 15:26:22 up 25 days, 22:03,  2 users,  load average: 4.48, 2.10, 1.18
Tasks: 495 total,   1 running, 398 sleeping,   2 stopped,   0 zombie
%Cpu(s): 25.4 us,  0.1 sy,  0.0 ni, 74.4 id,  0.0 wa,  0.0 hi,  0.1 si,  0.0 st
KiB Mem : 24422712 total,  8268972 free, 10321548 used,  5832192 buff/cache
KiB Swap: 32460792 total, 31906152 free,   554640 used. 11185060 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND
30785 root      20   0 1057360 297292 296772 S 200.0  1.2   0:22.03 firecracker
31568 bgregg    20   0  110076   3336   2316 R  45.7  0.0   0:01.93 sshd
31437 bgregg    20   0   57028   8052   5436 R  22.8  0.0   0:01.09 ssh
30719 root      20   0  120320  16348  10756 S   0.3  0.1   0:00.83 ignite-spawn
    1 root      20   0  227044   7140   3540 S   0.0  0.0  15:32.13 systemd
[...]
```
Toàn bộ VM xuất hiện như một tiến trình duy nhất mang tên firecracker. Kết quả này cho thấy nó đang tiêu thụ 200% CPU (2 CPUs). Từ host, bạn không thể biết những yêu cầu khách nào đang tiêu thụ CPU này.

Phần sau đây hiển thị top(1) chạy *từ khách*:
```bash
guest# top
top - 22:26:30 up 16 min,  1 user,  load average: 1.89, 0.89, 0.38
Tasks: 67 total,   3 running, 35 sleeping,   0 stopped,   0 zombie
%Cpu(s): 81.0 us, 19.0 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  1014468 total,   793660 free,    51424 used,   169384 buff/cache
KiB Swap:        0 total,        0 free,        0 used.   831400 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND
 1104 root      20   0   18592   1232    700 R 100.0  0.1   0:05.77 bash
 1105 root      20   0   18592   1232    700 R 100.0  0.1   0:05.59 bash
 1106 root      20   0   38916   3468   2944 R   4.8  0.3   0:00.01 top
    1 root      20   0   77224   8352   6648 S   0.0  0.8   0:00.38 systemd
    3 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 rcu_gp
[...]
```
Kết quả bây giờ chỉ ra rằng CPU đã bị tiêu tốn bởi hai chương trình bash. Đồng thời so sánh sự khác biệt giữa các bản tóm tắt tiêu đề: host có mức trung bình tải một phút là 4.48, trong khi khách có 1.89. Các chi tiết khác cũng khác biệt, vì kernel khách đang duy trì các thống kê chỉ dành cho khách. Như đã mô tả trong Mục 11.3.4, đây là điều khác biệt đối với các containers, nơi các thống kê nhìn thấy được từ khách có thể hiển thị một cách không mong đợi các thống kê trên toàn hệ thống từ host.

Như một ví dụ khác, phần sau đây hiển thị mpstat(1) được thực thi từ khách:
```bash
guest# mpstat -P ALL 1
Linux 4.19.47 (cd41e0d846509816)    03/21/20    _x86_64_    (2 CPU)

22:11:07  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
22:11:08  all   81.50    0.00   18.50    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:11:08    0   82.83    0.00   17.17    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:11:08    1   80.20    0.00   19.80    0.00    0.00    0.00    0.00    0.00    0.00    0.00
[...]
```
Kết quả này chỉ hiển thị hai CPUs, vì khách đã được gán hai vCPUs.

## 11.5 Các loại khác (Other Types)
Các sơ đồ và công nghệ điện toán đám mây khác bao gồm:
- **Functions as a service (FaaS):** Nhà phát triển gửi một chức năng ứng dụng lên đám mây, thứ được chạy theo nhu cầu. Điều này đơn giản hóa quá trình phát triển phần mềm cho đám mây, vì không có máy chủ để quản lý ("serverless"), nhưng cũng có các hệ quả hiệu năng. Thời gian khởi động cho chức năng có thể là đáng kể, và nếu không có một máy chủ, việc phân tích hiệu năng vượt ra ngoài các công cụ quan sát dòng lệnh truyền thống. Phân tích hiệu năng thường bị giới hạn ở các dấu thời gian do ứng dụng cung cấp.
- **Software as a service (SaaS):** Cung cấp phần mềm cấp cao mà không cần người dùng cuối phải tự cấu hình các máy chủ hoặc chính ứng dụng đó. Phân tích hiệu năng là giới hạn đối với các nhà vận hành: không có sự truy cập tới các máy chủ, người dùng cuối có thể thực hiện rất ít ngoài việc định thời phía máy khách (client-bound timing).
- **Unikernels:** Công nghệ này biên dịch một ứng dụng cùng với các phần kernel tối thiểu thành một file nhị phân phần mềm duy nhất có thể được thực thi bởi các hypervisors phần cứng trực tiếp, không yêu cầu hệ điều hành. Trong khi có thể có các lợi ích hiệu năng, chẳng hạn như giảm thiểu việc di chuyển chỉ lệnh và do đó ô nhiễm cache CPU, cũng như các lợi ích bảo mật do tước bỏ các mã kernel không sử dụng, Unikernels cũng tạo ra các thách thức về khả năng quan sát vì không có OS từ đó chạy các công cụ quan sát. Các thống kê kernel, chẳng hạn như những cái tìm thấy trong /proc, cũng có thể không tồn tại. May mắn thay, các triển khai thông thường cho phép Unikernel được chạy như một tiến trình bình thường, cung cấp một đường dẫn cho phân tích (mặc dù trong một môi trường khác so với hypervisor). Các hypervisors cũng có thể phát triển các cách thức để tạo hồ sơ chúng, chẳng hạn như qua tạo hồ sơ stack: Tôi đã phát triển một bản thử nghiệm tạo ra các bản đồ nhiệt (flame graphs) cho một MirageOS Unikernel đang chạy [Gregg 16a].

Đối với tất cả những loại này, không có hệ điều hành cho người dùng cuối để đăng nhập vào (hoặc container để vào) và thực hiện phân tích hiệu năng truyền thống. FaaS và SaaS phải được phân tích bởi các nhà vận hành. Unikernels yêu cầu các công cụ và thống kê tùy chỉnh, và lý tưởng nhất là hỗ trợ tạo hồ sơ từ hypervisor.

## 11.6 So sánh (Comparisons)
Việc so sánh các công nghệ có thể giúp bạn hiểu chúng tốt hơn, ngay cả khi bạn không ở trong vị trí để thay đổi công nghệ đang được sử dụng bởi công ty của bạn. Các thuộc tính hiệu năng của ba công nghệ được thảo luận trong chương này được so sánh trong Bảng 11.7.

Bảng 11.7 So sánh các thuộc tính hiệu năng công nghệ ảo hóa
| Thuộc tính | Ảo hóa Phần cứng | Ảo hóa OS (Containers) | Ảo hóa Trọng lượng nhẹ |
| --- | --- | --- | --- |
| Ví dụ | KVM | Containers | FireCracker |
| Hiệu năng CPU | Cao (Hỗ trợ CPU) | Cao | Cao (Hỗ trợ CPU) |
| Phân bổ CPU | Cố định vào vCPUs | Linh hoạt (shares + bandwidth) | Cố định vào vCPUs |
| Thông lượng I/O | Cao (với SR-IOV) | Cao (không có chi phí nội tại) | Cao (với SR-IOV) |
| Độ trễ I/O | Thấp (với SR-IOV và không QEMU) | Thấp (không có chi phí nội tại) | Thấp (với SR-IOV) |
| Chi phí truy cập bộ nhớ | Một số (EPT/NPT hoặc shadow page tables) | Không | Một số (EPT/NPT hoặc shadow page tables) |
| Mất mát bộ nhớ | Một số (các kernels bổ sung, các bảng trang) | Không | Một số (các kernels bổ sung, các bảng trang) |
| Phân bổ bộ nhớ | Cố định (và có khả năng đệm ẩn gấp đôi) | Linh hoạt (bộ nhớ khách không sử dụng được dùng cho file system cache của host) | Cố định (và có khả năng đệm ẩn gấp đôi) |
| Các kiểm soát tài nguyên | Nhiều nhất (kernel cộng với các kiểm soát hypervisor) | Nhiều (tùy thuộc vào kernel) | Nhiều nhất (kernel cộng với các kiểm soát hypervisor) |
| Khả năng quan sát: từ host | Trung bình (thống kê sử dụng tài nguyên, các thống kê hypervisor, OS cho KVM-like hypervisors, nhưng không thể thấy các thành phần nội bộ của khách) | Cao (thấy mọi thứ) | Trung bình (thống kê sử dụng tài nguyên, các thống kê hypervisor, OS cho KVM-like hypervisors, nhưng không thể thấy các thành phần nội bộ của khách) |
| Khả năng quan sát: từ khách | Cao (toàn bộ kernel và việc kiểm tra thiết bị ảo) | Trung bình (chỉ user mode, các bộ đếm kernel, khả năng hiển thị kernel đầy đủ bị hạn chế) với các chỉ số bổ sung trên toàn host (ví dụ: iostat(1)) | Cao (toàn bộ kernel và việc kiểm tra thiết bị ảo) |
| Khả năng quan sát nghiêng về | Người dùng cuối | Các nhà vận hành host | Người dùng cuối |
| Độ phức tạp của Hypervisor | Cao nhất (bổ sung một hypervisor phức tạp) | Trung bình (OS) | Cao (bổ sung một hypervisor trọng lượng nhẹ) |
| Các khách OS khác nhau | Có | Thường không (đôi khi có thể với dịch syscall, thứ có thể thêm các chi phí) | Có |

Lưu ý rằng bảng này tập trung vào chỉ riêng hiệu năng. Có những sự khác biệt khác, ví dụ, các containers đã được mô tả là có độ bảo mật yếu hơn [Agache 20].

Trong khi bảng này sẽ trở nên lỗi thời khi có thêm nhiều tính năng được phát triển cho những công nghệ ảo hóa này, nó vẫn phục vụ để chỉ ra các loại nội dung cần tìm kiếm, ngay cả khi các công nghệ ảo hóa hoàn toàn mới được phát triển mà không khớp với bất kỳ loại nào trong số này.

Các công nghệ ảo hóa thường được so sánh bằng cách sử dụng micro-benchmarking để xem cái nào thực hiện tốt nhất. Thật không may, điều này bỏ qua tầm quan trọng của việc có khả năng quan sát hệ thống, thứ có thể dẫn đến các thắng lợi hiệu năng lớn nhất. Khả năng quan sát thường giúp việc nhận diện và loại bỏ các công việc không cần thiết dễ dàng hơn, mang lại hiệu năng tối đa cao hơn nhiều so với các khác biệt ảo hóa nhỏ.

Đối với các nhà vận hành đám mây, tùy chọn ảo hóa cao nhất là các containers, vì từ host họ có thể thấy tất cả các tiến trình và các tương tác của chúng. Đối với người dùng cuối, đó là các máy ảo, vì những máy đó cung cấp cho họ quyền truy cập kernel đầy đủ, cho phép họ sử dụng các công cụ hiệu năng dựa trên kernel, bao gồm những thứ trong các Chương 13, 14, và 15. Một tùy chọn khác là các containers có quyền truy cập kernel đầy đủ, trao cho người dùng khả năng hiển thị mọi thứ; tuy nhiên, tùy chọn này chỉ khả thi khi người dùng cũng là nhà vận hành vì nó thiếu sự cô lập an toàn giữa các containers.

Ảo hóa vẫn là một lĩnh vực đang phát triển, với các hypervisors phần cứng trọng lượng nhẹ chỉ xuất hiện trong những năm gần đây. Với các lợi ích của chúng, đặc biệt cho khả năng quan sát của người dùng cuối, tôi kỳ vọng việc sử dụng chúng sẽ tăng lên.

## 11.7 Các bài tập (Exercises)
1. Trả lời các câu hỏi sau về thuật ngữ ảo hóa:
   - Sự khác biệt giữa host và guest là gì?
   - Một tenant là gì?
   - Một hypervisor là gì?
   - Ảo hóa phần cứng là gì?
   - Ảo hóa OS là gì?

2. Trả lời các câu hỏi khái niệm sau:
   - Mô tả vai trò của cách ly hiệu năng (performance isolation).
   - Mô tả các chi tiết hiệu năng với ảo hóa phần cứng hiện đại (ví dụ: Nitro).
   - Mô tả các chi phí hiệu năng với ảo hóa OS (ví dụ: Linux containers).
   - Mô tả khả năng quan sát hệ thống vật lý từ một khách ảo hóa phần cứng (hoặc Xen hoặc KVM).
   - Mô tả khả năng quan sát hệ thống vật lý từ một khách ảo hóa OS.
   - Giải thích sự khác biệt giữa ảo hóa phần cứng (ví dụ: Xen hoặc KVM) và ảo hóa phần cứng trọng lượng nhẹ (ví dụ: Firecracker).

3. Chọn một công nghệ ảo hóa và trả lời những điều sau đây cho các khách:
   - Mô tả cách một giới hạn bộ nhớ được áp dụng, và nó được nhìn thấy từ khách như thế nào. (Quản trị viên hệ thống nên làm gì khi bộ nhớ khách bị cạn kiệt?)
   - Nếu có một giới hạn CPU được áp đặt, hãy mô tả cách nó được áp dụng và nó được nhìn thấy từ khách như thế nào.
   - Nếu có một giới hạn I/O đĩa được áp đặt, hãy mô tả cách nó được áp dụng và nó được nhìn thấy từ khách như thế nào.
   - Nếu có một giới hạn I/O mạng được áp đặt, hãy mô tả cách nó được áp dụng và nó được nhìn thấy từ khách như thế nào.

4. Phát triển một checklist phương pháp USE cho các kiểm soát tài nguyên. Bao gồm cách lấy từng chỉ số (ví dụ: lệnh nào để thực thi) và cách diễn giải kết quả. Thử sử dụng các công cụ quan sát OS hiện có trước khi cài đặt các sản phẩm phần mềm bổ sung.

## 11.8 Các tài liệu tham khảo (References)
- [Goldberg 73] Goldberg, R. P., *Architectural Principles for Virtual Computer Systems*, Harvard University (Thesis), 1972.
- [Waldspurger 02] Waldspurger, C., “Memory Resource Management in VMware ESX Server,” *Proceedings of the 5th Symposium on Operating Systems Design and Implementation*, 2002.
- [Cherkasova 05] Cherkasova, L., and Gardner, R., “Measuring CPU Overhead for I/O Processing in the Xen Virtual Machine Monitor,” *USENIX ATEC*, 2005.
- [Adams 06] Adams, K., and Agesen, O., “A Comparison of Software and Hardware Techniques for x86 Virtualization,” *ASPLOS*, 2006.
- [Gupta 06] Gupta, D., Cherkasova, L., Gardner, R., and Vahdat, A., “Enforcing Performance Isolation across Virtual Machines in Xen,” *ACM/IFIP/USENIX Middleware*, 2006.
- [Qumranet 06] “KVM: Kernel-based Virtualization Driver,” Qumranet Whitepaper, 2006.
- [Cherkasova 07] Cherkasova, L., Gupta, D., and Vahdat, A., “Comparison of the Three CPU Schedulers in Xen,” *ACM SIGMETRICS*, 2007.
- [Corbet 07a] Corbet, J., “Process containers,” *LWN.net*, https://lwn.net/Articles/236038, 2007.
- [Corbet 07b] Corbet, J., “Notes from a container,” *LWN.net*, https://lwn.net/Articles/256389, 2007.
- [Liguori, 07] Liguori, A., “The Myth of Type I and Type II Hypervisors,” http://blog.codemonkey.ws/2007/10/myth-of-type-i-and-type-ii-hypervisors.html, 2007.
- [VMware 07] “Understanding Full Virtualization, Paravirtualization, and Hardware Assist,” https://www.vmware.com/techpapers/2007/understanding-full-virtualization-paravirtualizat-1008.html, 2007.
- [Matthews 08] Matthews, J., et al. *Running Xen: A Hands-On Guide to the Art of Virtualization*, Prentice Hall, 2008.
- [Milewski 11] Milewski, B., “Virtual Machines: Virtualizing Virtual Memory,” http://corensic.wordpress.com/2011/12/05/virtual-machines-virtualizing-virtual-memory, 2011.
- [Adamczyk 12] Adamczyk, B., and Chydzinski, A., “Performance Isolation Issues in Network Virtualization in Xen,” *International Journal on Advances in Networks and Services*, 2012.
- [Hoff 12] Hoff, T., “Pinterest Cut Costs from $54 to $20 Per Hour by Automatically Shutting Down Systems,” http://highscalability.com/blog/2012/12/12/pinterest-cut-costs-from-54-to-20-per-hour-by-automatically.html, 2012.
- [Gregg 14b] Gregg, B., “From Clouds to Roots: Performance Analysis at Netflix,” http://www.brendangregg.com/blog/2014-09-27/from-clouds-to-roots.html, 2014.
- [Heo 15] Heo, T., “Control Group v2,” *Linux documentation*, https://www.kernel.org/doc/Documentation/cgroup-v2.txt, 2015.
- [Gregg 16a] Gregg, B., “Unikernel Profiling: Flame Graphs from dom0,” http://www.brendangregg.com/blog/2016-01-27/unikernel-profiling-from-dom0.html, 2016.
- [Kadera 16] Kadera, M., “Accelerating the Next 10,000 Clouds,” https://www.slideshare.net/Docker/accelerating-the-next-10000-clouds-by-michael-kadera-intel, 2016.
- [Borello 17] Borello, G., “Container Isolation Gone Wrong,” *Sysdig blog*, https://sysdig.com/blog/container-isolation-gone-wrong, 2017.
- [Goldfuss 17] Goldfuss, A., “Making FlameGraphs with Containerized Java,” https://blog.alicegoldfuss.com/making-flamegraphs-with-containerized-java, 2017.
- [Gregg 17e] Gregg, B., “AWS EC2 Virtualization 2017: Introducing Nitro,” http://www.brendangregg.com/blog/2017-11-29/aws-ec2-virtualization-2017.html, 2017.
- [Gregg 17f] Gregg, B., “The PMCs of EC2: Measuring IPC,” http://www.brendangregg.com/blog/2017-05-04/the-pmcs-of-ec2.html, 2017.
- [Gregg 17g] Gregg, B., “Container Performance Analysis at DockerCon 2017,” http://www.brendangregg.com/blog/2017-05-15/container-performance-analysis-dockercon-2017.html, 2017.
- [CNI 18] “bandwidth plugin,” https://github.com/containernetworking/plugins/blob/master/plugins/meta/bandwidth/README.md, 2018.
- [Denis 18] Denis, X., “A Pods Architecture to Allow Shopify to Scale,” https://engineering.shopify.com/blogs/engineering/a-pods-architecture-to-allow-shopify-to-scale, 2018.
- [Leonovich 18] Leonovich, M., “Another reason why your Docker containers may be slow,” https://hackernoon.com/another-reason-why-your-docker-containers-may-be-slow-d37207dec27f, 2018.
- [Borkmann 19] Borkmann, D., and Pumputis, M., “Kube-proxy Removal,” https://cilium.io/blog/2019/08/20/cilium-16/#kubeproxy-removal, 2019.
- [Cilium 19] “Announcing Hubble - Network, Service & Security Observability for Kubernetes,” https://cilium.io/blog/2019/11/19/announcing-hubble/, 2019.
- [Gregg 19] Gregg, B., *BPF Performance Tools: Linux System and Application Observability*, Addison-Wesley, 2019.
- [Gregg 19e] Gregg, B., “kvmexits.bt,” https://github.com/brendangregg/bpf-perf-tools-book/blob/master/originals/Ch16_Hypervisors/kvmexits.bt, 2019.
- [Kwiatkowski 19] Kwiatkowski, A., “Autoscaling in Reality: Lessons Learned from Adaptively Scaling Kubernetes,” https://conferences.oreilly.com/velocity/vl-eu/public/schedule/detail/78924, 2019.
- [Xen 19] “Xen PCI Passthrough,” http://wiki.xen.org/wiki/Xen_PCI_Passthrough, 2019.
- [Agache 20] Agache, A., et al., “Firecracker: Lightweight Virtualization for Serverless Applications,” https://www.usenix.org/publications/proceedings/firecracker-lightweight-virtualization-for-serverless-applications, 2020.
- [Calico 20] “Cloud Native Networking and Network Security,” https://github.com/projectcalico/calico, last updated 2020.
- [Cilium 20a] “API-aware Networking and Security,” https://cilium.io, accessed 2020.
- [Cilium 20b] “eBPF-based Networking, Security, and Observability,” https://github.com/cilium/cilium, last updated 2020.
- [Firecracker 20] “Secure and Fast microVMs for Serverless Computing,” https://github.com/firecracker-microvm/firecracker, last updated 2020.
- [Google 20c] “Google Compute Engine FAQ,” https://developers.google.com/compute/docs/faq#whatis, accessed 2020.
- [Google 20d] “Analyzes Resource Usage and Performance Characteristics of Running containers,” https://github.com/google/cadvisor, last updated 2020.
- [Kata Containers 20] “Kata Containers,” https://katacontainers.io, accessed 2020.
- [Linux 20m] “mount_namespaces(7),” http://man7.org/linux/man-pages/man7/mount_namespaces.7.html, accessed 2020.
- [Weaveworks 20] “Ignite a Firecracker microVM,” https://github.com/weaveworks/ignite, last updated 2020.
- [Kubernetes 20b] “Production-Grade Container Orchestration,” https://kubernetes.io, accessed 2020.
- [Kubernetes 20c] “Tools for Monitoring Resources,” https://kubernetes.io/docs/tasks/debug-application-cluster/resource-usage-monitoring, last updated 2020.
- [Torvalds 20b] Torvalds, L., “Re: [GIT PULL] x86/mm changes for v5.8,” https://lkml.org/lkml/2020/6/1/1567, 2020.
- [Xu 20] Xu, P., “iops limit for pod/pvc/pv #92287,” https://github.com/kubernetes/kubernetes/issues/92287, 2020.
