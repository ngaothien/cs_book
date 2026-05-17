# 16 Kiểm tra tốc độ (Testing speed)

Kiểm tra tốc độ của một chương trình là một phần quan trọng trong công việc tối ưu hóa. Bạn phải kiểm tra xem các sửa đổi của bạn có thực sự làm tăng tốc độ hay không.

Có nhiều trình biên dịch cấu hình (profilers) khác nhau có sẵn, hữu ích cho việc tìm kiếm các "điểm nóng" (hot spots) và đo lường hiệu suất tổng thể của một chương trình. Tuy nhiên, các profiler không phải lúc nào cũng chính xác, và có thể khó để đo lường chính xác những gì bạn muốn khi chương trình dành phần lớn thời gian chờ dữ liệu nhập từ người dùng hoặc đọc các tệp đĩa. Xem trang 16 để thảo luận về việc cấu hình (profiling).

Khi một điểm nóng đã được xác định, có thể sẽ hữu ích nếu bạn cô lập điểm nóng đó và chỉ thực hiện các phép đo trên phần mã này. Điều này có thể được thực hiện với độ phân giải của xung nhịp CPU bằng cách sử dụng bộ đếm tem thời gian (time stamp counter). Đây là một bộ đếm đếm số xung nhịp kể từ khi CPU được khởi động. Độ dài của một chu kỳ xung nhịp là nghịch đảo của tần số xung nhịp, như được giải thích trên trang 16. Nếu bạn đọc giá trị của bộ đếm tem thời gian trước và sau khi thực thi một đoạn mã quan trọng thì bạn có thể có được lượng thời gian tiêu thụ chính xác dưới dạng độ chênh lệch giữa hai lần đếm xung nhịp.

Giá trị của bộ đếm tem thời gian có thể thu được bằng hàm `ReadTSC` được liệt kê trong ví dụ 16.1 dưới đây. Mã này chỉ hoạt động đối với các trình biên dịch hỗ trợ các hàm nội tại (intrinsic functions). Ngoài ra, bạn có thể sử dụng tệp tiêu đề `timingtest.h` từ www.agner.org/optimize/testp.zip hoặc lấy hàm `ReadTSC` dưới dạng một hàm thư viện từ www.agner.org/optimize/asmlib.zip.

```cpp
// Ví dụ 16.1
#include <intrin.h>        // Hoặc #include <ia32intrin.h> v.v.

long long ReadTSC() {      // Trả về bộ đếm tem thời gian
   int dummy[4];           // Dùng cho kết quả trả về không sử dụng
   volatile int DontSkip;  // volatile để ngăn việc bị tối ưu hóa
   long long clock;        // Thời gian
   __cpuid(dummy, 0);      // Tuần tự hóa (Serialize)
   DontSkip = dummy[0];    // Ngăn việc hàm cpuid bị tối ưu hóa bỏ đi
   clock = __rdtsc();      // Đọc thời gian
   return clock;
}
```

Bạn có thể sử dụng hàm này để đo số đếm xung nhịp trước và sau khi thực thi đoạn mã quan trọng. Một kịch bản thiết lập kiểm tra (test setup) có thể trông như thế này:

```cpp
// Ví dụ 16.2

#include <stdio.h>
#include <asmlib.h>        // Sử dụng ReadTSC() từ thư viện asmlib..
                           // hoặc từ ví dụ 16.1
void CriticalFunction();   // Đây là hàm chúng ta muốn đo

...

const int NumberOfTests = 10;         // Số lần kiểm tra
int i; long long time1;
long long timediff[NumberOfTests];    // Độ chênh lệch thời gian cho mỗi bài kiểm tra
for (i = 0; i < NumberOfTests; i++) { // Lặp lại NumberOfTests lần

   time1 = ReadTSC();                 // Thời gian trước bài kiểm tra

   CriticalFunction();                // Hàm quan trọng để kiểm tra

   timediff[i] = ReadTSC() - time1;   // (thời gian sau) - (thời gian trước)
}
printf("\nResults:");                 // In tiêu đề
for (i = 0; i < NumberOfTests; i++) { // Vòng lặp để in ra kết quả
   printf("\n%2i  %10I64i", i, timediff[i]);
}
```

Đoạn mã trong ví dụ 16.2 gọi hàm quan trọng 10 lần và lưu trữ thời gian tiêu thụ của mỗi lần chạy trong một mảng. Sau đó các giá trị này được xuất ra sau vòng lặp kiểm tra. Thời gian được đo bằng cách này bao gồm cả thời gian để gọi hàm `ReadTSC`. Bạn có thể trừ giá trị này ra khỏi các số đếm (counts). Điều này được đo đạc đơn giản bằng cách loại bỏ lệnh gọi đến `CriticalFunction` trong ví dụ 16.2.

Thời gian đo được diễn giải theo cách sau. Số đếm đầu tiên thường cao hơn các số đếm tiếp theo. Đây là thời gian cần thiết để thực thi `CriticalFunction` khi mã và dữ liệu không được lưu trong bộ đệm (uncached). Các số đếm tiếp theo đưa ra thời gian thực thi khi mã và dữ liệu được lưu trong bộ đệm (cached) tốt nhất có thể. Số đếm đầu tiên và các số đếm tiếp theo đại diện cho các giá trị "trường hợp xấu nhất" (worst case) và "trường hợp tốt nhất" (best case). Việc giá trị nào trong hai giá trị này gần với sự thật hơn phụ thuộc vào việc `CriticalFunction` được gọi một lần hay nhiều lần trong chương trình hoàn chỉnh và liệu có mã nào khác sử dụng bộ đệm xen giữa các lần gọi `CriticalFunction` hay không. Nếu nỗ lực tối ưu hóa của bạn tập trung vào hiệu suất của CPU thì bạn nên xem xét các số đếm ở "trường hợp tốt nhất" để thấy xem một sửa đổi nào đó có mang lại lợi ích không. Mặt khác, nếu nỗ lực tối ưu hóa của bạn tập trung vào việc sắp xếp dữ liệu nhằm cải thiện hiệu suất bộ đệm, thì bạn cũng có thể xem xét các số đếm "trường hợp xấu nhất". Trong mọi trường hợp, các số đếm xung nhịp (clock counts) nên được nhân với chu kỳ xung nhịp (clock period) và với số lần `CriticalFunction` được gọi trong một ứng dụng điển hình để tính ra độ trễ thời gian mà người dùng cuối (end user) có khả năng sẽ gặp phải.

Đôi khi, số lượng đếm xung nhịp mà bạn đo được cao hơn nhiều so với bình thường. Điều này xảy ra khi một chuyển đổi tác vụ (task switch) xảy ra trong quá trình thực thi `CriticalFunction`. Bạn không thể tránh khỏi điều này trong một hệ điều hành được bảo vệ (protected operating system), nhưng bạn có thể giảm thiểu vấn đề bằng cách tăng mức độ ưu tiên của luồng (thread priority) lên trước khi kiểm tra và đặt mức độ ưu tiên trở lại bình thường sau đó.

Các số lượng đếm xung nhịp thường bị dao động và có thể khó để thu được những kết quả có thể tái lập (reproducible results). Điều này là do các CPU hiện đại có thể thay đổi tần số xung nhịp của chúng một cách tự động tùy thuộc vào khối lượng công việc (work load). Tần số xung nhịp được tăng lên khi khối lượng công việc cao và giảm xuống khi khối lượng công việc thấp nhằm mục đích tiết kiệm điện. Có nhiều cách khác nhau để có được các phép đo thời gian có thể tái lập nhiều hơn:

*   Làm nóng (warm up) CPU bằng cách cung cấp cho nó một số công việc nặng (heavy work) để làm ngay trước đoạn mã cần kiểm tra.
*   Vô hiệu hóa các tùy chọn tiết kiệm điện trong thiết lập BIOS.
*   Trên các CPU Intel: sử dụng bộ đếm chu kỳ xung nhịp lõi (core clock cycle counter) (xem bên dưới)

## 16.1 Sử dụng các bộ đếm giám sát hiệu suất (Using performance monitor counters)

Nhiều CPU có một tính năng kiểm tra được tích hợp sẵn được gọi là bộ đếm giám sát hiệu suất (performance monitor counters). Bộ đếm giám sát hiệu suất là một bộ đếm bên trong CPU có thể được thiết lập để đếm các sự kiện nhất định, chẳng hạn như số lượng lệnh máy (machine instructions) đã được thực thi, lỗi bộ đệm (cache misses), lỗi dự đoán rẽ nhánh (branch mispredictions), v.v. Các bộ đếm này có thể rất hữu ích cho việc điều tra các sự cố hiệu suất (performance problems). Các bộ đếm giám sát hiệu suất là dành riêng cho từng CPU (CPU-specific) và mỗi mô hình CPU có bộ các tùy chọn theo dõi hiệu suất riêng.

Các nhà cung cấp CPU đang cung cấp các công cụ cấu hình (profiling tools) phù hợp với các CPU của họ. Profiler của Intel được gọi là VTune; Profiler của AMD được gọi là CodeAnalyst. Những profiler này rất hữu ích cho việc xác định các điểm nóng (hot spots) trong mã.

Dành cho nghiên cứu của riêng tôi, tôi đã phát triển một công cụ kiểm tra (test tool) để sử dụng các bộ đếm giám sát hiệu suất. Công cụ kiểm tra của tôi hỗ trợ cả các bộ xử lý Intel, AMD và VIA, và nó có sẵn từ www.agner.org/optimize/testp.zip. Công cụ này không phải là một profiler. Nó không nhằm mục đích tìm kiếm các điểm nóng, mà là để nghiên cứu một đoạn mã sau khi các điểm nóng đã được xác định.

Công cụ kiểm tra của tôi có thể được sử dụng theo hai cách. Cách đầu tiên là chèn đoạn mã cần kiểm tra vào trong chính chương trình kiểm tra (test program) đó và biên dịch lại. Tôi đang sử dụng cách này để kiểm tra từng lệnh hợp ngữ riêng lẻ (single assembly instructions) hoặc một chuỗi mã nhỏ. Cách thứ hai là thiết lập các bộ đếm giám sát hiệu suất trước khi chạy một chương trình bạn muốn tối ưu hóa, và đọc các bộ đếm hiệu suất ở bên trong chương trình của bạn trước và sau đoạn mã bạn muốn kiểm tra. Bạn có thể sử dụng nguyên tắc giống như trong ví dụ 16.2 ở trên, nhưng đọc một hoặc nhiều bộ đếm giám sát hiệu suất thay vì (hoặc bổ sung thêm vào) bộ đếm tem thời gian (time stamp counter). Công cụ kiểm tra có thể thiết lập và bật một hoặc nhiều bộ đếm giám sát hiệu suất trong tất cả các lõi CPU và để chúng ở trạng thái bật (có một bộ đếm trong mỗi lõi CPU). Các bộ đếm sẽ vẫn bật cho đến khi bạn tắt chúng hoặc cho đến khi máy tính được khởi động lại hoặc đi vào chế độ ngủ (sleep mode). Xem sổ tay hướng dẫn của công cụ kiểm tra của tôi để biết thêm chi tiết (www.agner.org/optimize/testp.zip).

Một bộ đếm giám sát hiệu suất đặc biệt hữu ích trong các bộ xử lý Intel được gọi là chu kỳ xung nhịp lõi (core clock cycles). Bộ đếm core clock cycles đang đếm các chu kỳ xung nhịp theo tần số xung nhịp thực tế (actual clock frequency) mà lõi CPU đang chạy, thay vì tần số xung nhịp bên ngoài (external clock). Điều này đưa ra một phép đo gần như không phụ thuộc vào sự thay đổi của tần số xung nhịp. Bộ đếm chu kỳ xung nhịp lõi rất hữu ích khi kiểm tra xem phiên bản mã nào nhanh nhất vì bạn có thể tránh được vấn đề tần số xung nhịp tăng giảm.

Hãy nhớ chèn một công tắc (switch) vào chương trình của bạn để tắt việc đọc các bộ đếm khi bạn không kiểm tra. Cố gắng đọc các bộ đếm giám sát hiệu suất khi chúng bị tắt (disabled) sẽ làm hỏng (crash) chương trình.

## 16.2 Những cạm bẫy của kiểm tra đơn vị (The pitfalls of unit-testing)

Đó là thông lệ chung khi kiểm tra từng chức năng (function) hoặc class một cách riêng biệt trong quy trình phát triển phần mềm. Hoạt động kiểm tra đơn vị (unit-testing) này là cần thiết để xác minh tính đúng đắn về mặt chức năng (functionality) của một hàm đã được tối ưu hóa, nhưng không may là unit-test không cung cấp thông tin đầy đủ về hiệu suất của hàm đó xét về khía cạnh tốc độ.

Giả sử rằng bạn có hai phiên bản khác nhau của một hàm quan trọng và bạn muốn tìm ra xem cái nào nhanh nhất. Cách điển hình để kiểm tra điều này là tạo ra một chương trình kiểm tra nhỏ gọi hàm quan trọng đó nhiều lần với một bộ dữ liệu kiểm tra (test data) phù hợp và đo lường xem nó cần mất bao nhiêu thời gian. Phiên bản hoạt động tốt nhất dưới thử nghiệm unit-test này có thể có một footprint bộ nhớ (kích thước tiêu thụ bộ nhớ) lớn hơn phiên bản thay thế kia. Mức phạt (penalty) về tốc độ từ việc xảy ra các lỗi không tìm thấy trong bộ đệm (cache misses) sẽ không được nhìn thấy trong unit-test bởi vì tổng số lượng mã và bộ nhớ dữ liệu được chương trình kiểm tra đó sử dụng thường ít hơn kích thước bộ đệm (cache size).

Khi hàm quan trọng được đưa vào chương trình cuối cùng (final program), rất có thể bộ đệm mã (code cache) và bộ đệm dữ liệu (data cache) là các tài nguyên bị giới hạn khắt khe (critical resources). Các CPU hiện đại nhanh đến mức các chu kỳ xung nhịp tiêu tốn cho việc thực thi lệnh ít có khả năng trở thành điểm nghẽn (bottleneck) hơn so với kích thước truy cập bộ nhớ và bộ đệm (memory access and cache size). Nếu đúng như vậy thì phiên bản tối ưu của hàm quan trọng có thể là phiên bản chiếm nhiều thời gian hơn trong thử nghiệm unit-test nhưng có footprint bộ nhớ nhỏ hơn.

Nếu, ví dụ, bạn muốn tìm hiểu xem liệu trải (roll out) một vòng lặp lớn có đem lại lợi ích gì không thì bạn không thể dựa vào unit-test mà không tính đến các hiệu ứng của bộ đệm (cache effects).

Bạn có thể tính toán hàm sử dụng bao nhiêu bộ nhớ bằng cách xem link map hoặc assembly listing. Sử dụng tùy chọn "generate map file" (tạo tệp bản đồ) cho linker (trình liên kết). Việc sử dụng cả bộ đệm mã và bộ đệm dữ liệu đều có thể đóng vai trò then chốt (critical). Vùng đệm chứa đích đến cho các lệnh rẽ nhánh (branch target buffer) cũng là một bộ đệm có thể đóng vai trò quan trọng. Do đó, số lượng lệnh nhảy (jumps), gọi hàm (calls) và rẽ nhánh (branches) trong một hàm cũng nên được xem xét.

Một thử nghiệm hiệu suất thực tế nên bao gồm không chỉ một hàm duy nhất hoặc điểm nóng mà còn cả vòng lặp trong cùng (innermost loop) có chứa các hàm quan trọng và các điểm nóng. Thử nghiệm phải được thực hiện với một bộ dữ liệu thực tế nhằm thu được kết quả đáng tin cậy cho các sai sót về dự đoán rẽ nhánh (branch mispredictions). Việc đo lường hiệu suất không nên bao gồm bất kỳ phần nào của chương trình mà chờ đợi người dùng nhập liệu (user input). Khoảng thời gian tiêu tốn cho hoạt động vào/ra trên tập tin (file input and output) cần được đo riêng biệt.

Sai lầm trong việc đo lường hiệu suất bằng unit-testing (kiểm tra đơn vị) thật không may là rất phổ biến. Ngay cả một số thư viện hàm được tối ưu hóa tốt nhất hiện có cũng sử dụng quá nhiều kỹ thuật trải vòng lặp (loop unrolling) dẫn đến footprint bộ nhớ trở nên lớn một cách vô lý.

## 16.3 Kiểm tra tình huống xấu nhất (Worst-case testing)

Hầu hết các bài kiểm tra hiệu suất đều được thực hiện dưới các điều kiện tốt nhất (best-case conditions). Mọi ảnh hưởng nhiễu (disturbing influences) đều bị loại bỏ, tất cả các tài nguyên đều đủ dùng, và các điều kiện lưu vào bộ đệm (caching) đều ở mức tối ưu. Bài kiểm tra điều kiện tốt nhất (best-case testing) hữu ích vì nó mang lại kết quả đáng tin cậy và có thể tái lập cao hơn. Nếu bạn muốn so sánh hiệu suất của hai cách triển khai khác nhau cho cùng một thuật toán, thì bạn cần loại bỏ tất cả các ảnh hưởng gây nhiễu để các phép đo chính xác và có thể tái lập một cách rõ ràng nhất.

Tuy nhiên, có những trường hợp cần thiết và có tính thực tiễn hơn khi kiểm tra hiệu suất dưới các điều kiện xấu nhất (worst-case). Ví dụ, nếu bạn muốn đảm bảo rằng thời gian phản hồi (response time) khi người dùng thao tác không bao giờ vượt quá giới hạn cho phép, thì bạn nên kiểm tra thời gian phản hồi ở các điều kiện tồi tệ nhất.

Các phần mềm sinh ra luồng âm thanh hoặc video (streaming audio or video) cũng nên được thử nghiệm dưới các tình huống xấu nhất để luôn đảm bảo rằng chúng có thể đáp ứng kịp thời tốc độ thời gian thực (real-time speed). Việc chậm trễ (delays) hoặc trục trặc (glitches) trong sản phẩm đầu ra (output) là không thể chấp nhận được.

Mỗi phương pháp sau đây có khả năng phù hợp khi thực hiện một bài kiểm tra hiệu suất tình huống xấu nhất:

*   Lần đầu tiên bạn kích hoạt một phần nhất định của chương trình, nó có thể sẽ chậm hơn những lần tiếp theo do quá trình tải muộn (lazy loading) của mã, lỗi không tìm thấy trong bộ đệm (cache misses) và sai sót dự đoán rẽ nhánh (branch mispredictions).
*   Kiểm tra toàn bộ gói phần mềm (software package), bao gồm tất cả các thư viện runtime (runtime libraries) và các framework, chứ không cách ly (isolating) một hàm duy nhất. Việc chuyển đổi giữa các phần khác nhau của gói phần mềm sẽ làm tăng khả năng xảy ra trường hợp một vài phần của mã không có trong bộ nhớ (uncached) hoặc thậm chí là bị hoán đổi xuống ổ đĩa (swapped to disk).
*   Phần mềm dựa vào các máy chủ hoặc tài nguyên mạng cần được chạy thử nghiệm trên mạng có lưu lượng truy cập lớn (heavy traffic) và một máy chủ hoạt động hết công suất chứ không phải là trên một máy chủ thử nghiệm dành riêng (dedicated test server).
*   Dùng các tệp dữ liệu kích cỡ lớn và những cơ sở dữ liệu có chứa thật nhiều dữ liệu.
*   Sử dụng một chiếc máy tính cũ kĩ, với CPU hoạt động chậm, lượng RAM thì thiếu hụt, nhiều phần mềm không hề liên quan bị cài đặt thêm vào, hàng loạt quy trình chạy ẩn (background processes) cũng đang hoạt động, và dùng một ổ đĩa cứng bị chậm cũng như bị phân mảnh (fragmented).
*   Hãy thử kiểm tra với nhiều thương hiệu (brands) của các CPU khác nhau, với các mẫu (types) thẻ đồ họa (graphics cards) khác nhau,...
*   Hãy sử dụng thử cùng một chương trình chống vi rút (antivirus) với chức năng tự động quét hết toàn bộ tệp vào thời điểm truy cập.
*   Chạy thử hàng loạt tiến trình (processes) hay nhiều luồng (threads) thực thi hoàn toàn song song nhau (simultaneously). Nếu là bộ vi xử lý hỗ trợ công nghệ siêu luồng (hyperthreading), thì hãy thử chạy thử đồng thời luôn hai luồng (threads) bên trong cùng chung bộ vi xử lý lõi (processor core).
*   Hãy cố gắng phân bổ một lượng bộ nhớ RAM nhiều hơn so với mức thực tế hiện tại, để qua đó thúc đẩy hệ thống phải dùng kỹ năng trao đổi bộ nhớ bằng ổ đĩa (swapping of memory to disk).
*   Khơi mào để tạo ra nhiều lỗi sai sót không tìm thấy bộ nhớ cache (cache misses) với cách làm thay đổi kích thước bộ nhớ hoặc dùng cách tạo dữ liệu bên trong của một vòng lặp ngoài cùng với dung lượng cao và phình to hơn so với cỡ tối đa mà bộ đệm cache cho phép (cache size). Một phương án nữa thay cho chuyện này là việc bạn có thể chủ động cố tình loại bỏ hiệu lực (invalidate) của bộ nhớ cache. Một hệ điều hành (operating system) thường sẽ có một hàm phụ trách giải quyết vấn đề riêng này, không thì bạn có thể sử dụng hàm cơ bản vốn có của cấu trúc mã (intrinsic function) có sẵn chức năng này `_mm_clflush`.
*   Tạo kích động các sai lệch đối với dự báo cho việc rẽ nhánh (branch mispredictions) bằng phương án tạo tập hợp tài nguyên ngẫu nhiên nhiều hơn một cách bình thường.
