# 🚀 Lộ Trình 12 Tuần System Design Toàn Diện (System Design Mastery)

> *"Học System Design không nên chỉ dừng ở việc ghi nhớ sơ đồ để đi phỏng vấn. Người học cần hiểu vì sao hệ thống được thiết kế như vậy và mỗi quyết định phải đánh đổi điều gì."*

Bộ tài liệu này được tải về, tổng hợp và biên soạn chuyên sâu dựa trên chuỗi bài giảng kiến trúc phân tán kinh điển của tác giả **Franco Fernando** (*The Polymathic Engineer*), kết hợp các mô hình kiến trúc thực chiến tại các tập đoàn công nghệ hàng đầu thế giới (Google, Amazon, Netflix, Meta).

> 📖 **Đặc biệt:** Bạn có thể xem ngay [Tổng Hợp Toàn Bộ Nguồn Học System Design Đỉnh Cao](file:///Users/kaka/learning/software_development/system_design/tai_lieu_va_nguon_hoc_system_design.md) (sách kinh điển, GitHub repos, Engineering blogs Big Tech, video channels và research papers).

---

## 🗺️ Bản Đồ Lộ Trình 12 Tuần Theo Thứ Tự Chuẩn

Dưới đây là 12 chủ đề được sắp xếp theo đúng trình tự tư duy kiến trúc, từ thu thập yêu cầu, tính toán quy mô, phân tầng mạng, cho đến lưu trữ và điều phối phân tán:

| Tuần | Chủ đề | Mục tiêu cốt lõi | Sự đánh đổi (Trade-off) chính | Tài liệu chi tiết |
| :---: | :--- | :--- | :--- | :---: |
| **1** | **Xác Định Yêu Cầu** *(Requirements Gathering)* | Bóc tách Functional (FR) & Non-Functional (NFR); định hình API | Breadth vs Depth; Rõ ràng vs Phức tạp sớm | [Xem bài học](file:///Users/kaka/learning/software_development/system_design/01_xac_dinh_yeu_cau.md) |
| **2** | **Ước Tính Nhanh Quy Mô** *(Back of the Envelope)* | Tính toán QPS, Storage, RAM Cache, Băng thông mạng | Ước tính nhanh bậc quy mô vs Độ chính xác tuyệt đối | [Xem bài học](file:///Users/kaka/learning/software_development/system_design/02_uoc_tinh_quy_mo.md) |
| **3** | **Latency Và Throughput** | Phân biệt thời gian vs tốc độ dòng chảy; Định luật Little; P99 | Tối ưu độ trễ vs Tối ưu thông lượng (Batching) | [Xem bài học](file:///Users/kaka/learning/software_development/system_design/03_latency_va_throughput.md) |
| **4** | **High Availability (HA)** | Đo lường các số 9 SLA, loại bỏ SPOF, Active-Active, Failover | Chi phí hạ tầng & độ phức tạp vs Số lượng số 9 | [Xem bài học](file:///Users/kaka/learning/software_development/system_design/04_high_availability.md) |
| **5** | **Các Phương Pháp Mở Rộng** *(Scale Cube)* | Trục X (Cloning), Trục Y (Microservices), Trục Z (Data Sharding) | Stateless Web Tier; Độc lập dịch vụ vs Độ phức tạp mạng | [Xem bài học](file:///Users/kaka/learning/software_development/system_design/05_cac_phuong_phap_mo_rong.md) |
| **6** | **Load Balancer** | Phân tầng Layer 4 (TCP) vs Layer 7 (HTTP); Các thuật toán định tuyến | Tốc độ L4 vs Khả năng định tuyến thông minh L7 | [Xem bài học](file:///Users/kaka/learning/software_development/system_design/06_load_balancer.md) |
| **7** | **Caching** | Cache-Aside, Write-Through/Back, xử lý 4 thảm họa Cache | Tốc độ siêu nhanh từ RAM vs Tính nhất quán dữ liệu | [Xem bài học](file:///Users/kaka/learning/software_development/system_design/07_caching.md) |
| **8** | **Database Replication** | Single-Leader, Multi-Leader, Leaderless; Định lý Quorum ($W+R>N$) | Đồng bộ (Chậm, an toàn) vs Bất đồng bộ (Nhanh, lag) | [Xem bài học](file:///Users/kaka/learning/software_development/system_design/08_replication.md) |
| **9** | **Database Sharding** | Phân mảnh ngang; Range vs Hash; Distributed Transactions | Scale ghi không giới hạn vs Mất khả năng JOIN dễ dàng | [Xem bài học](file:///Users/kaka/learning/software_development/system_design/09_database_sharding.md) |
| **10** | **Message Queues & Event-Driven** | Cắt đỉnh tải Flash Sale, RabbitMQ vs Kafka, Idempotency | Giao tiếp bất đồng bộ vs Khó gỡ lỗi (Debugging) | [Xem bài học](file:///Users/kaka/learning/software_development/system_design/10_message_queue_va_event_driven.md) |
| **11** | **Consistent Hashing** | Vòng tròn băm (Hash Ring), Virtual Nodes (Vnodes), Gossip/Raft | Giảm thiểu 90% dịch chuyển dữ liệu khi scale cụm | [Xem bài học](file:///Users/kaka/learning/software_development/system_design/11_consistent_hashing.md) |
| **12** | **CAP, PACELC & Case Study** | Bản chất sự cố mạng; Khung 4 bước phỏng vấn; Case Study Twitter | Consistency vs Availability; Fan-out Write vs Read | [Xem bài học](file:///Users/kaka/learning/software_development/system_design/12_cap_theorem_va_case_study.md) |

---

## 📁 Cấu Trúc Kho Tài Nguyên Tải Về

Hệ thống đã lưu trữ toàn bộ dữ liệu gốc để bạn có thể học tập và tra cứu offline mọi lúc:

```text
/Users/kaka/learning/software_development/system_design/
├── 01_xac_dinh_yeu_cau.md               # Tài liệu chuyên sâu Tuần 1
├── 02_uoc_tinh_quy_mo.md                # Tài liệu chuyên sâu Tuần 2
├── 03_latency_va_throughput.md          # Tài liệu chuyên sâu Tuần 3
├── 04_high_availability.md              # Tài liệu chuyên sâu Tuần 4
├── 05_cac_phuong_phap_mo_rong.md        # Tài liệu chuyên sâu Tuần 5
├── 06_load_balancer.md                  # Tài liệu chuyên sâu Tuần 6
├── 07_caching.md                        # Tài liệu chuyên sâu Tuần 7
├── 08_replication.md                    # Tài liệu chuyên sâu Tuần 8
├── 09_database_sharding.md              # Tài liệu chuyên sâu Tuần 9
├── 10_message_queue_va_event_driven.md  # Tài liệu mở rộng Tuần 10
├── 11_consistent_hashing.md             # Tài liệu mở rộng Tuần 11
├── 12_cap_theorem_va_case_study.md      # Tài liệu tổng kết Tuần 12
├── README.md                            # Trang mục lục và hướng dẫn này
│
├── html/                                # 9 tệp trang web HTML gốc từ Substack
│   ├── 01_xac_dinh_yeu_cau.html
│   ├── 02_uoc_tinh_quy_mo.html
│   └── ...
├── original_markdown/                   # 9 tệp Markdown gốc trích xuất trực tiếp
│   ├── 01_xac_dinh_yeu_cau.md
│   ├── 02_uoc_tinh_quy_mo.md
│   └── ...
├── raw_json/                            # 9 tệp JSON API metadata (tác giả, ngày đăng)
│   ├── 01_xac_dinh_yeu_cau.json
│   └── ...
└── images/                              # 25 hình ảnh, infographic & sơ đồ gốc
    ├── 01_xac_dinh_yeu_cau_img_1.png
    ├── 02_uoc_tinh_quy_mo_img_1.png
    ├── 05_cac_phuong_phap_mo_rong_img_1.png
    └── ...
```

---

## 💡 Phương Pháp Học Tập Đạt Hiệu Quả Tối Đa

1. **Tuân thủ đúng thứ tự 12 tuần:** Các chủ đề được thiết kế tuần tự theo dạng bậc thang (ví dụ: cần hiểu *Scale Cube* ở tuần 5 trước khi hiểu *Load Balancer* ở tuần 6 và *Sharding* ở tuần 9).
2. **Luôn tự hỏi về "Đánh đổi" (Trade-off):** Khi đọc bất kỳ giải pháp nào, hãy tự trả lời 3 câu hỏi:
   - *Tại sao không dùng giải pháp đơn giản hơn?*
   - *Khi áp dụng giải pháp này, hệ thống sẽ phải trả giá bằng điều gì (Chi phí, độ trễ, hay độ phức tạp)?*
   - *Khi nào thì KHÔNG NÊN dùng giải pháp này?*
3. **Thực hành vẽ lại sơ đồ:** Hãy tự tay phác thảo lại các sơ đồ Mermaid trong tài liệu trên giấy nháp hoặc Excalidraw để biến kiến thức thành phản xạ tự nhiên.
