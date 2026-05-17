# 12 Sử dụng các toán tử vectơ (Using vector operations)

Những chuỗi phụ thuộc kéo dài quá mức thường gây căng thẳng cho nguồn tài nguyên thực thi không tuần tự (out-of-order resources) của CPU, dẫu cho chúng không được đem nối sang phiên chạy của vòng lặp tiếp theo. Một mẫu CPU hiện đại thông thường có khả năng giải quyết hơn cả trăm phép tính bị tắc nghẽn (pending operations) (hãy xem cẩm nang 3: "Vi kiến trúc của các CPU Intel, AMD và VIA"). Có thể sẽ rất hữu ích khi bạn phân tách một vòng lặp rồi giữ các phần kết quả trung gian lại để qua đó bẻ gãy một chuỗi phụ thuộc dài lê thê.

Các bộ vi xử lý ngày nay đều mang trong mình các chỉ lệnh vectơ ngõ hầu cho phép thực hiện nhiều lệnh thao tác tính toán trên tất cả các phần tử thuộc một tập hợp vectơ cùng một lúc. Cơ chế này còn được gọi là các toán tử Đơn-lệnh-Đa-Dữ-liệu (Single-Instruction-Multiple-Data hay SIMD). Tổng kích thước của mỗi một cấu trúc vectơ có thể ở dạng 64 bit (MMX), 128 bit (XMM), 256 bit (YMM) và 512 bit (ZMM).

Các toán tử vectơ tỏ ra khá hữu ích khi chúng ta thao tác tính toán trên một tập dữ liệu cỡ lớn nơi cùng một kiểu phép tính được áp dụng đồng thời trên nhiều phần tử dữ liệu và cấu trúc lập trình cũng cho phép thực hiện việc tính toán song song. Ví dụ như khi xử lý hình ảnh, xử lý âm thanh, hay các phép tính toán học trên nhóm vectơ và ma trận. Những thuật toán vốn mang tính dây chuyền theo bản chất tự nhiên, điển hình như hầu hết các thuật toán sắp xếp (sorting algorithms), sẽ không phù hợp cho việc ứng dụng các toán tử vectơ. Các thuật toán phụ thuộc nặng nề vào việc tra cứu bảng dữ liệu (table lookup) hay cần thao tác tráo đổi dữ liệu (data shuffling) nhiều, ví dụ như một vài thuật toán mã hóa, có lẽ cũng không mấy thích hợp cho thao tác dựa trên hệ vectơ.

Các toán tử vectơ sử dụng một nhóm các thanh ghi vectơ (vector registers) mang tính đặc chủng. Kích thước tối đa của mỗi bộ thanh ghi vectơ là 128 bit (XMM) nếu có sẵn nhóm tập lệnh SSE2, 256 bit (YMM) nếu tập lệnh AVX được bộ vi xử lý và hệ điều hành hỗ trợ, và 512 bit hễ nhóm chỉ lệnh AVX512 khả dụng. Số lượng các phần tử trong mỗi vectơ phụ thuộc vào kích thước và kiểu của các thành phần dữ liệu, như sau:

| Kiểu phần tử (Type of elements) | Kích thước của mỗi phần tử, bits | Số lượng phần tử | Tổng kích thước vectơ, bits | Tập lệnh (Instruction set) |
| --- | --- | --- | --- | --- |
| char | 8 | 8 | 64 | MMX |
| short int | 16 | 4 | 64 | MMX |
| int | 32 | 2 | 64 | MMX |
| int64_t | 64 | 1 | 64 | MMX |
| char | 8 | 16 | 128 | SSE2 |
| short int | 16 | 8 | 128 | SSE2 |
| int | 32 | 4 | 128 | SSE2 |
| int64_t | 64 | 2 | 128 | SSE2 |
| float | 32 | 4 | 128 | SSE |
| double | 64 | 2 | 128 | SSE2 |
| char | 8 | 32 | 256 | AVX2 |
| short int | 16 | 16 | 256 | AVX2 |
| int | 32 | 8 | 256 | AVX2 |
| int64_t | 64 | 4 | 256 | AVX2 |
| float | 32 | 8 | 256 | AVX |
| double | 64 | 4 | 256 | AVX |
| char | 8 | 64 | 512 | AVX512BW |
| short int | 16 | 32 | 512 | AVX512BW |
| int | 32 | 16 | 512 | AVX512 |
| int64_t | 64 | 8 | 512 | AVX512 |
| float | 32 | 16 | 512 | AVX512 |
| double | 64 | 8 | 512 | AVX512 |
*Bảng 12.1. Các lớp vectơ được định nghĩa bên trong các tệp tiêu đề (header files) của Intel*

Ví dụ, một bộ thanh ghi XMM 128-bit có thể được biên chế thành một loại vectơ chứa 8 khối số nguyên 16-bit hoặc 4 số dạng `float` mỗi khi nhóm tập lệnh SSE2 được xài tới. Các loại thanh ghi MMX đời cũ, mang mốc kích thước nằm ở khoảng không 64-bit, tốt nhất nên được né tránh vì chúng không thể bị hòa lẫn chung với các luồng mã dấu phẩy động mang hệ kiểu x87.

Các vectơ dạng XMM 128-bit bắt buộc phải được căn lề 16 (aligned by 16), cụ thể là được lưu vào trong một địa chỉ bộ nhớ có khả năng chia hết cho 16 (xem chi tiết phía dưới). Các loại vectơ 256-bit YMM nên được căn lề theo dạng 32 và các thanh ghi 512-bit ZMM theo khoảng 64, nhưng những ràng buộc để căn lề ít mang vẻ ngặt nghèo hơn trong quá trình biên dịch cho hệ AVX và các nhóm tập lệnh xuất hiện ở đời sau đó.

Toán tử vectơ luôn đạt tốc độ đặc biệt kinh khủng khi hoạt động trên các bộ xử lý đời mới. Rất nhiều hệ xử lý có khả năng tính toán cả một hệ vectơ lẹ hệt như việc tính toán vô hướng (scalar - ám chỉ những hệ thông tin không ở dạng vectơ). Các thế hệ bộ vi xử lý đời đầu vốn hỗ trợ mức kích thước vectơ kiểu mới thông thường chỉ sở hữu những đơn vị thực thi (execution units), cổng truy cập bộ nhớ (memory ports), v.v. bằng có một nửa kích cỡ so với chủng loại vectơ to lớn nhất. Thế nên các đơn vị kể trên đành phải được thao tác sử dụng liên tiếp hai lần ngõ hầu vận chuyển đầy đủ cho một nhóm vectơ kích thước toàn phần.

Việc sử dụng các phép tính vectơ càng đem lại vô vàn ưu thế hễ các phần tử mang kích thước càng nhỏ. Ví như, bạn đổi lại được những 4 phép toán cộng số `float` bằng đúng với lượng thời gian mà bạn cần để hoàn thành vỏn vẹn 2 phép toán cộng dành cho số kiểu `double`. Thường sẽ luôn luôn đem lại ưu điểm mỗi khi xài đến các phép tính vectơ bên trên những bộ CPU đương đại nếu lượng dữ liệu có mốc kích thước nằm lọt vừa vặn vào trong một thanh ghi vectơ. Đôi lúc nó lại không mang lại chút mặt lợi nào nếu đòi hỏi quá nhiều khâu thao túng dữ liệu lằng nhằng (data manipulation) chỉ để ném lượng thông tin phù hợp nằm gọn gàng cho vừa khít với kích cỡ của các thành phần trong vectơ.

## 12.1 Tập lệnh AVX và các thanh ghi YMM
Các thanh ghi mang kiểu XMM 128-bit sẽ được nới rộng trở thành các thanh ghi 256-bit có tên gọi là YMM khi nằm ở trong lòng tập lệnh AVX. Ưu điểm chủ lực của hệ thống AVX này đó là nó cung cấp một nhóm các vectơ chứa điểm dấu phẩy động ở mức rộng lớn hơn. Đồng thời cũng tồn tại một số những lợi điểm khác có khả năng kích phát hiệu năng xử lý lên mức nào đó. Ngoài ra, bộ tập lệnh AVX2 cũng cho phép sử dụng những nhóm vectơ số nguyên đạt mốc 256-bit.

Đoạn mã được biên dịch nhắm vào tập lệnh AVX chỉ có cửa khởi chạy nếu cơ cấu AVX này được chống lưng hỗ trợ bởi cả CPU lẫn hệ điều hành. Dạng lệnh AVX được hỗ trợ rộng rãi trong Windows 7 và Windows Server 2008 R2 cũng như được tiếp nhận ở mức nhân kernel của hệ Linux từ đời 2.6.30 và những phiên bản sau đó. Tập lệnh AVX được hậu thuẫn bởi những trình biên dịch thế hệ mới nhất tới từ Microsoft, Intel, Gnu và Clang.

Có xuất hiện một khúc mắc khi mà bạn tiến hành pha tạp các dòng mã nguồn được biên dịch cùng với sự hỗ trợ từ phía AVX xen kẽ với nhóm không được hỗ trợ khi làm việc ở một vài bộ xử lý thuộc hãng Intel. Ở đó có nảy sinh một mốc án phạt hiệu năng (performance penalty) trong khoảnh khắc hoán chuyển chéo qua lại từ mã xài AVX về lại thể thức phi AVX bắt nguồn từ một biến chuyển ở phía trạng thái của khối thanh ghi YMM. Ngõ hầu thoát khỏi cái án phạt ngớ ngẩn trên thì bạn phải né nó bằng hành vi đánh tiếng gọi thẳng tên hàm bản thể (intrinsic function) `_mm256_zeroupper()` đi trước khi làm bất kỳ đường hoán chuyển qua lại nào từ phía AVX cho đổ bộ về dải mã không dùng AVX. Mánh khóe này vô cùng có tính ứng dụng ở trong một loạt các trường hợp dưới đây:

* Giả như chỉ có duy nhất một vùng thân xác chương trình có biên dịch đi kèm sự hỗ trợ đắc lực từ phía AVX và mảng râu ria còn lại trong chương trình đó không hề dính dáng tới AVX thì nhớ gọi thẳng `_mm256_zeroupper()` lúc chuẩn bị cất bước thoát khỏi nhóm xài AVX.
* Nếu như một biến hàm được tiến hành biên dịch ra cho vạn kiểu dáng phiên bản xài lẫn không xài chung AVX nhờ tận dụng trò phân tách CPU (CPU dispatching) thì làm ơn gọi ngay `_mm256_zeroupper()` trước cái thời khắc ly khai vũng mã xài AVX.
* Trừ phi một mẩu mã nguồn được dịch chung với AVX lại đi mò mẫm gọi một cụm hàm trốn ở phía một thư viện phi tiêu chuẩn không được bọc lót theo kèm trong cái trình biên dịch ấy, hơn hết cái góc thư viện đó vắng bóng hoàn toàn hơi thở của sự chống lưng đến từ AVX, thì chớ quên điểm danh `_mm256_zeroupper()` ngay tại thì tương lai trước lúc mò gọi tới đám hàm ở hệ thư viện xa lạ trên.

## 12.2 Tập lệnh AVX512 và các thanh ghi ZMM
Các thanh ghi dạng YMM 256-bit sẽ được bơm kích cỡ giãn nở ra thành ngưỡng 512-bit và mang cái danh xưng là ZMM mỗi khi hòa mình vào cùng tập lệnh AVX512. Quân số mảng thanh ghi thuộc hệ vectơ sẽ được kích thêm cho nhảy từ 16 lên trạm 32 ở trong loại chế độ 64-bit. Vỏn vẹn chỉ có lèo tèo 8 bộ thanh ghi nhóm vectơ giả sử xài chế độ 32-bit. Các nhóm thanh ghi chuẩn 128-bit XMM được bơm phồng lên loại 256-bit với pháp danh là hệ thanh ghi YMM lúc nhúng chung vào trong nhóm lệnh hệ AVX. Thế nên, chuỗi mã xài chung AVX512 tốt nhất nên được ngắm mục tiêu mà biên dịch cho hệ quy chiếu vận hành 64-bit.

Khối tập lệnh AVX512 cũng đính chung vào trong nó một tập hợp các thanh ghi mặt nạ (mask registers). Mấy thứ này được lôi ra dùng với vai trò tương tự với cấu trúc Boolean dưới dạng hệ vectơ. Gần như tất thảy các kiểu lệnh vectơ nào cũng có thể được che giấu cùng với bộ thanh ghi dán nhãn mặt nạ cốt để mỗi yếu tố cá thể ở trong dải vectơ sẽ chỉ có thể được đụng tay vào tính toán nếu như khối bit mang phận sự đối chiếu với cá thể ấy đang hiển thị là giá trị `1`. Trò đắp mặt nạ thế này nặn nhào tính vectơ hóa cho phần mã nguồn sở hữu các phân nhánh điều kiện mang theo cái vỏ bọc hiệu năng uyển chuyển lanh lẹ hơn.

Đồng thời lại mọc thêm vài cái chi nhánh phái sinh thuộc dạng ăn theo vào AVX512. Tất thảy bộ vi xử lý đã xài AVX512 kiểu gì cũng cõng một đống các mẩu phái sinh lan truyền này, nhưng tới thời điểm hiện tại thì chẳng có bộ não CPU nào chịu gánh trọn vẹn mọi cái nhánh lây lan kia vào trong lòng (tính thời điểm cuốn sách này được chắp bút năm 2016). Những nhánh biến thể có định danh lan rộng và thuộc vòng tính toán kế hoạch thuộc hệ AVX512 sẽ trải ra theo diện dưới đây:

* AVX512F. Nền móng (Foundation). Mọi khối xử lý bám theo dạng AVX512 đều hốt loại này. Gom trọn các phép xử lý số nguyên 32-bit và 64-bit, hệ dấu thập phân `float` với dạng `double` nằm bên trong vectơ 512-bit, bao hàm luôn thể loại toán tử mang hệ mặt nạ (masked operations).
* AVX512VL. Cũng ôm đồn y hệt những thao tác bên trên dải 128-bit cùng hệ 256-bit vectơ, gom luôn loại tác vụ hệ mặt nạ và 32 mảng thanh ghi nhóm vectơ.
* AVX512BW. Gồm các thao tác cho nhóm số nguyên 8-bit cùng 16-bit ở trong thân một vectơ 512-bit.
* AVX512DQ. Có cả lệnh tính phép nhân xen kẽ thao tác quy đổi dính tới kiểu số nguyên 64-bit. Vài thể loại hướng dẫn pha tạp khác dành riêng cho con bài `float` với kiểu `double`.
* AVX512ER. Các phương thức hỗ trợ xài mảng nghịch đảo siêu tốc (fast reciprocal), phép tính xài biến hàm số căn bậc hai nghịch đảo (reciprocal square root), cùng dạng toán hàm số mũ (exponential function). Chuẩn xác ở mảng loại `float`; còn bên `double` thì nằm ở mức chắp vá nhại theo (approximate).
* AVX512CD. Bộ dò tìm đụng độ (Conflict detection). Tranh thủ rà quét móc ra một đống các mảnh cá thể xài mảng bản sao trùng lặp ở phần ruột hệ cấu trúc vectơ.
* AVX512PF. Bộ phát tác chỉ lệnh gọi tính nạp trước dữ liệu (Prefetch) hòa trộn vào logic phân mảnh cùng với tóm gọn dữ liệu (gather/scatter logic).
* AVX512VBMI. Trò hoán vị sắp mâm (Permutation) đi liền dịch chuyển (shift) mang chỉ số 8-bit tính ở phương diện mức đo kích cỡ hạt (granularity).
* AVX512IFMA. Cơ chế hàn dính nén ép các phép nhân và phép cộng quyện vào nhau trên lưng điểm số nguyên 52-bit.
* AVX512_4VNNIW. Tích vô hướng lặp (Iterated dot product) cho dải số nguyên dạng 16-bit.
* AVX512_4FMAPS. Dạng lệnh thực thi vòng lặp ghép dính phép tính cộng và nhân, mang độ phân giải với ngưỡng chính xác đơn (single precision).

Bức tranh hổ lốn này nặn ra cái viễn cảnh phân luồng nhả lệnh (dispatching) cho CPU ngày một lằng nhằng rắc rối. Bạn đành phải chọn lọc ra những biến thể mang danh phụ trợ kia mà có công ích sinh được lời để nhào vô xử lý cho một góc bài toán nhất định rồi trích ra một lằn nhánh lệnh riêng để mà hiến tế phục vụ nhóm bộ xử lý mang trong thân những miếng mồi biến thể (extensions) này.

Cái trò móc lốp lôi thằng `_mm256_zeroupper()` ra thao tác ở vũng mã nguồn cho AVX512 chắc có lẽ vô thưởng vô phạt chả thiết dùng, thế nhưng rắc rối ở chỗ hố lầy này bấy lâu nay vẫn còn ngâm ở phần thảo luận cãi cọ chưa dứt. Mời lật sang sổ tay thứ 5, mục "Quy ước về kiểu gọi hàm (Calling conventions)", phân đoạn thứ 6.3 để tìm hiểu.

## 12.3 Tính năng tự động vectơ hóa (Automatic vectorization)
Số đông các trình biên dịch dạng hàng khủng tỷ như của phe Gnu, Clang rồi hệ Intel thừa xăng phô diễn kỹ nghệ tự động lấy phép tính hệ vectơ ra lót thảm những lúc tính năng song hành mang cái mác quá sức rõ ràng trước cặp mắt thiên hạ. Cố công lôi tài liệu hướng dẫn phẫu thuật trình biên dịch để tường tận mớ chỉ định dẫn đường chi li nhất. Đơn cử vài dòng mã:

```cpp
// Example 12.1a. Automatic vectorization 
const int size = 1024; 
int a[size], b[size]; 
// ... 
for (int i = 0; i < size; i++) { 
   a[i] = b[i] + 2; 
} 
```

Mấy loại trình biên dịch xịn sò sẽ vồ lấy cái thóp này đặng nhào nặn quá trình tối ưu bằng mưu mẹo tận dụng toán tử vectơ vào những thời khắc mà nhóm lệnh SSE2 (hoặc đàn em lứa sau) được gọi hồn tới. Cụm mã xử lý này mang khả năng đếm được một nhóm bốn, tám, hoặc bèo nhất mười sáu hạt nhân cấu thành từ mảng `b` đi giấu vào một cấu trúc chứa thanh ghi định theo hệ vectơ tùy thuộc theo thân thế cái danh sách chỉ lệnh (instruction set), từ đó bắt tay nặn ra hệ tính cộng chập với đám thanh ghi một thân cõng cả hệ vectơ khác mang cái mác `(2,2,2,...)` ở phần thân, sau rốt lôi bốn kết cục này đem chôn dưới mảng `a`. Trò thao túng này theo lẽ tự nhiên sẽ bị vướng vào luân hồi lặp đi lặp lại đủ số kiếp tính theo cái ranh kích cỡ của mảng sau khi chia đều lượng phần tử cắm trên mỗi khoang vectơ. Tốc lực thực thi theo cái nếp nhăn ấy cũng trồi mạnh mẽ lên theo. Đẹp nhãn tiền nhất chính là tình huống mức đếm của hệ thống vòng lặp đủ phép chia chẵn không dư cho tổng đại số hạt nhân phần tử nằm đè bên trên lớp vectơ. Bạn đôi phần vẫn nắm quyền cấy thêm vài cục hạt nhân độn vào (dummy elements) vứt nằm lăn lóc nơi vị trí khóa chốt cái dải mảng với ước vọng vỗ béo nặn to kích cỡ mảng cho chạm mốc tích số gấp vài lần con số thể hình của khối vectơ.

Tuy nhiên có chướng ngại nhỏ khi cố moi đám dải mảng thông qua ngõ ngách gọi biến con trỏ, lấy ví dụ:

```cpp
// Example 12.1b. Vectorization with alignment problem 
void AddTwo(int * __restrict aa, int * __restrict bb) { 
   for (int i = 0; i < size; i++) { 
      aa[i] = bb[i] + 2; 
   } 
} 
```

Các toán tử vectơ uyển chuyển lanh lợi nhất thường đòi hỏi các bộ mảng bắt buộc mang hình thái được ép lề (aligned) chia tỷ lệ với điểm kích cỡ bộ vectơ, điều này tương xứng với việc chứa những vùng lưu cất ngự trên những dải địa chỉ bộ nhớ hễ đem đếm tính phân nhỏ cho những số 16, 32 xen kẽ 64 thì chia trọn không sinh rác rưởi (chia hết). Nhìn vào ví dụ 12.1a, trình biên dịch có tiềm năng rà lại lề lối cho bộ mảng đạt ngưỡng được yêu sách như trên, cơ mà chệch sang trường hợp tại ví dụ 12.1b, thì khốn nỗi thằng trình biên dịch mù tịt không tài mọn ngửi thấu sự hiển hiện về việc bầy mảng đã được nắn chỉnh lề đàng hoàng ngay ngắn (properly aligned) hay lỡ chưa làm. Khâu chạy lặp dẫu thế mà nói vẫn có xác suất vớ được kiếp vectơ hóa (vectorized), lại khổ vì đoạn mã sẽ lọt thỏm về lại sự cồng kềnh ì ạch bởi vì trình biên dịch phải vắt chân lên cổ thao tác lót thêm đệm phòng hờ (extra precautions) đặng lấp đầy mớ hố rác lộn xộn sinh ra do các mảng thiếu xài canh lề (unaligned arrays). Có vô số chiêu trò bạn dư xăng làm được để xào nấu lại mảng mã cho nó phô trương được độ hiệu quả tối cao giữa dòng mớ rác mang tên mảng lùi xùi được lấy lên (accessed) thông suốt bằng mớ ma thuật con trỏ hay dẫn chứng chiếu dọi (references):

* Khi bạn giao phó mã thuật cho cái trình biên dịch từ nhà Intel nhào nặn, thì nhớ xài lệnh `#pragma vector aligned` hoặc gọi cái đạo bùa chỉ dẫn `__assume_aligned` báo với phía trình phiên dịch hay việc mớ mảng râu ria đã được xếp lề nghiêm ngắn, và phải cược cho chắc là điều đó đúng như vậy.
* Rạch ròi tuyên ngôn chức phận hàm này mang lằn ranh dạng nội tuyến (inline). Dòng động thái này khơi mở tài năng để cho trình phiên dịch giáng cấp trường hợp 12.1b quay về mức 12.1a.
* Tranh thủ bóp cò châm nổ dòng tập lệnh sở hữu dải hình bộ kích cỡ vectơ khổng lồ nhất trong khả năng tiềm tàng. Vũng AVX hay những hội tập lệnh đời hậu duệ vứt đi bớt ti tỉ hàng tá mớ xích xiềng cùm kẹp rắc rối về vụ canh nếp ngay lề cho nên bộ phận mã kết cục sẽ tuôn trào hiệu năng mặc kệ hễ đống mảng kia đã xếp nếp chỉnh tề hay chưa thèm ngó qua.

Quyền năng tự động biến đổi thành chuẩn vectơ sẽ khoác lên mình hình hài vận hành đỉnh sức mạnh nhất khi và chỉ khi hàng tá điều kiện sau được chu cấp thỏa đáng:
1. Đu bám dùng trình biên dịch biết chống lưng tính năng gọi hàm vectơ hóa tự động, rải rác như hội Gnu, Clang, Intel mọc lên cùng rễ PathScale.
2. Xài bản trình biên dịch đời mới nhất tinh xảo. Các công cụ dịch này càng ngày càng tỏ rõ thực lực thượng đẳng nơi trận mạc vectơ hóa.
3. Điền khéo các điểm tùy chọn trình biên dịch (compiler options) sao cho lọt thỏm ăn rơ khui nổ đúng cái bộ tập lệnh lăm le rắp tâm (/arch:SSE2, /arch:AVX hầm bà lằng cho xóm Windows, còn -msse2, -mavx, đồ nghề thì quăng cho Linux)
4. Canh chỉnh xếp lề bầy mảng đi với đống cấu trúc bề thế cho theo chuẩn 16 hễ vướng xài SSE2, tốt hơn là chọn 32 cho dòng AVX với đẹp nếp nhất là 64 khi đụng AVX512.
5. Tổng vòng lặp đếm nên yên tọa dán chặt theo dạng hằng số làm sao đem ra làm mồi chia chẵn đều cho cục phần tử tót lên cái vectơ thì hay.
6. Giả như hễ mấy hàng mảng tuồn ra chui vô lót đường cho bầy con trỏ qua mức ấy việc nếp nắn lề lại che khuất trong ranh giới phạm trù thân hàm nơi mà bạn thèm nhỏ dãi cái chức năng vectơ hóa thì làm ơn tuân theo đám lời khuyên tung ra phía trên kia giùm.
7. Nếu mảng hoặc bầy cấu trúc bị rờ gáy bới móc (accessed) mượn qua dàn con trỏ đi cặp chiếu dẫn, thì đánh tiếng hô to cho trình biên dịch rạch ròi rằng các con trỏ tuyệt nhiên đừng xài chung dạng mảng tham chiếu giả (alias), nếu cảm thấy tương xứng ăn nhập. Dở sách hướng dẫn cách chém thuật bằng trình dịch đặng hiểu rành rọt.
8. Tối giản triệt để ba trò múa may phân nhánh hễ xét tại bình diện thuộc phần tử vectơ
9. Né xa cái mảng tra cứu lật bảng tính ngay trên bình diện của hạt phần tử vectơ

Trợn mắt để ý dò la tờ phơi (listing) xuất trả mã hợp ngữ (assembly) hòng xác nhận lại dòng mã hệt vậy đã được tắm gội dưới lớp áo vectơ hóa hệt y đúc kịch bản chưa (lật trang 85 coi kỹ).

Thằng trình biên dịch lanh chanh còn thừa xăng chèn khâu toán tử vectơ vào những chốn vắng bóng hoàn toàn sự ngự trị của vòng lặp hễ mà chỉ một dạng thao tác phép toán rập khuôn diễn biến đè thẳng lên sống lưng chuỗi nối gót dài dằng dặc những mạng biến số. Ví như sau đây:

```cpp
// Example 12.2 
__declspec(align(16))     // Make all instances of S1 aligned 
struct S1 {               // Structure of 4 floats 
   float a, b, c, d; 
}; 
 
void Func() { 
   S1 x, y; 
   // ... 
   x.a = y.a + 1.; 
   x.b = y.b + 2.; 
   x.c = y.c + 3.; 
   x.d = y.d + 4.; 
}; 
```
