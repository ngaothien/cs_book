### Phân luồng CPU khi đính với các nhóm lớp vectơ (CPU dispatching with vector classes)
Bộ thư viện gom nhóm lớp vectơ VCL khơi mào cái viễn cảnh gò ép nhào nặn quá trình biên dịch (compile) chĩa vào hàng tá các bộ tập lệnh tạp nham bắt nguồn từ trên đúng một cục mã nguồn (source code) y hệt nhau. Dạng thư viện này có ngậm sẵn mớ chỉ thị tiền xử lý (preprocessing directives) để rờ gáy bấu víu vào lôi ra cái dạng bản thực thi tối ưu số zách dâng hiến cho một tập lệnh chỉ định (instruction set).

Bằng chứng ở lề dưới phơi bày cái ngón đòn nhào nặn cái bản `SelectAddMul` (số 12.4e) độn thêm tính năng nhả luồng phân vùng CPU (CPU dispatching) tự động rành rọt. Đoạn mã chui rúc ở hình thù này nên được chích thuốc ép biên dịch làm hẳn 3 màn 3 lớp, một vòng hiến cho hệ tập lệnh SSE2, mâm thứ 2 cho phe SSE4.1 rồi lớp chót là về với hội AVX2; lại còng thêm cái gông buộc chặt 3 dạng sinh linh kể trên đan cài thắt bím tụ chung lọt vào đúng một khoang thực thi duy nhất (same executable). Phe SSE2 chễm chệ đoạt cái ngai vàng là hạng tập lệnh lót đường hạng bét vừa vặn đủ ngưỡng được hệ thư viện cưu mang, phe SSE4.1 bù lại đẻ ra đôi chút mưu lợi trong mảng biến hàm `select`, và dải lệnh dạng AVX2 lại hiến tế món hời đến từ bộ thanh ghi nhét chứa vectơ mang thể hình vạm vỡ. Mớ thư viện lớp chứa vectơ đành nhắm mắt lấy xài 1 cục thanh ghi kích thước 256-bit cống cho cái lớp tên là `Vec16s` những lúc nhào nặn mã cho trạm AVX2, không thì rút xài hai con thanh ghi thể 128-bit hễ biên dịch đổ ngược dốc về đống tập lệnh mâm dưới lùn hơn. Phép xài cái cờ hiệu (macro) tiền xử lý mang danh `INSTRSET` bợ đỡ chức năng ban cái vỏ bọc định danh xéo sắc đôi đường dành ra cho vạn biến thể của tập lệnh. Bộ nhả luồng CPU (CPU dispatcher) khi tới nước ấy sẽ tự xắn tay đóng chốt cho một cụm biến con trỏ hệ hàm (function pointer) hướng thẳng về cái tạo vật mang phom dáng trác tuyệt nhất. Mò mẫm qua trang cẩm nang hướng dẫn `vectorclass` ngõ hầu tường tận sâu xa.

```cpp
// Example 12.7. Vector class code with automatic CPU dispatching 
#include "vectorclass.h"  // vector class library 
#include <stdio.h>        // define fprintf 
 
// define function type 
typedef void FuncType(short int aa[], short int bb[], short int cc[]); 
 
// function prototypes for each version 
FuncType SelectAddMul, SelectAddMul_SSE2, SelectAddMul_SSE41, 
SelectAddMul_AVX2, SelectAddMul_dispatch;  
 
// Define function name depending on instruction set 
#if   INSTRSET == 2                    // SSE2 
#define FUNCNAME SelectAddMul_SSE2 
#elif INSTRSET == 5                    // SSE4.1 
#define FUNCNAME SelectAddMul_SSE41 
#elif INSTRSET == 8                    // AVX2 
#define FUNCNAME SelectAddMul_AVX2 
#endif 
 
// specific version of the function. Compile once for each version 
void FUNCNAME(short int aa[], short int bb[], short int cc[]) { 
   Vec16s a, b, c; // Define biggest possible vector objects 
   // Roll out loop by 16 to fit the biggest vectors: 
   for (int i = 0; i < 256; i += 16) { 
      b.load(bb+i); 
      c.load(cc+i); 
      a = select(b > 0, c + 2, b * c); 
      a.store(aa+i); 
   } 
} 
 
#if INSTRSET == 2 
// make dispatcher in only the lowest of the compiled versions 
#include "instrset_detect.cpp" // instrset_detect function 
 
// Function pointer initially points to the dispatcher. 
// After first call it points to the selected version 
FuncType * SelectAddMul_pointer = &SelectAddMul_dispatch; 
  
// Dispatcher 
void SelectAddMul_dispatch(short int aa[], short int bb[], 
   short int cc[]) { 
   // Detect supported instruction set 
   int iset = instrset_detect(); 
   // Set function pointer 
   if      (iset >= 8) SelectAddMul_pointer = &SelectAddMul_AVX2; 
   else if (iset >= 5) SelectAddMul_pointer = &SelectAddMul_SSE41; 
   else if (iset >= 2) SelectAddMul_pointer = &SelectAddMul_SSE2; 
   else { 
      // Error: lowest instruction set not supported 
      fprintf(stderr, "\nError: Instruction set SSE2 not supported"); 
      return; 
    } 
   // continue in dispatched version 
   return (*SelectAddMul_pointer)(aa, bb, cc); 
} 
 
// Entry to dispatched function call 
inline void SelectAddMul(short int aa[], short int bb[], 
   short int cc[]) { 
   // go to dispatched version 
   return (*SelectAddMul_pointer)(aa, bb, cc); 
} 
 
#endif  // INSTRSET == 2 
```

## 12.6 Luân chuyển mảng mã tính toán dây chuyền (serial code) nhét vào hố vectơ hóa (Transforming serial code for vectorization)
Đâu phải vũng mã chằng chịt nào cũng đèo trọn cái cấu trúc song song có khả năng nặn ra nhét vừa khít vô mảng vectơ lanh lẹ êm xuôi được. Hằng hà sa số đám mã vốn phơi ra cái bản tính thâm căn là chạy theo kiểu dây chuyền (serial) hễ móc vào ý niệm một chuỗi phép tính luôn giẫm đạp đè gãy dựa dẫm vô cục tính kế tiếp vừa được phôi thai nặn xong. Biết đâu chừng ở cõi nào đấy việc thu vén đống mã ấy sao cho chúng phô ra dưới lốt vectơ hóa lại rẽ sang màng thành quả vẹn toàn miến là mớ luồng mã ấy có độ chịu lặp lại xoay vòng. Trường hợp lôi thôi mà đơn giản lột xác nhất chắc mẩm xoay quanh chuỗi tính nhẩm cộng gộp một danh sách hầm bà lằng những mảng số má với nhau:

```cpp
// Example 12.8a. Sum of a list 
float a[100]; 
float sum = 0; 
for (int i = 0; i < 100; i++) sum += a[i]; 
```

Nùi mã trôi tuột ở lằn bên trên bộc bạch cái chất dây chuyền là tại mốc hệ số tính gộp nào của biến `sum` cũng thảy đều phải bú mớm dựa vào vũng số liệu đoạt được của thằng `sum` chạy sát nách chắp tay tạo ra. Mẹo lách luật là phải quăng xé vòng lặp lột bung tháo trần nó với kích cỡ mức `n` cộng dồn với chuyện xếp nếp bài trí lại kết cấu hòng nặn ra cái viễn cảnh mà mỗi mốc biến đẻ ra đều chỉ ngó về hệ số bỏ xó ở vị trí cách đó những `n` vạch đi lùi, trong đó điểm `n` là xưng danh cho lượng phần tử cuộn trong mâm vectơ. Thử lôi số `n = 4` ra xài xể, thì vớ được:

```cpp
// Example 12.8b. Sum of a list, rolled out by 4 
float a[100]; 
float s0 = 0, s1 = 0, s2 = 0, s3 = 0, sum; 
for (int i = 0; i < 100; i += 4) { 
   s0 += a[i]; 
   s1 += a[i+1]; 
   s2 += a[i+2]; 
   s3 += a[i+3]; 
} 
sum = (s0+s1)+(s2+s3); 
```

Rồi rốt cục mớ `s0, s1, s2` xen kẽ `s3` có cửa được trộn lẫn sáp nhập thành đúng một quả vectơ nặn tới tận 128-bit đặng nặn ra màn phô diễn cả bốn mảng phép tính cộng nhét chật trong vỏn vẹn một toán tử thi triển. Một đứa trình dịch ranh mãnh sẽ nhào nặn rước cái ví dụ 12.8a chắp lốt cho ra đời thằng 12.8b một cách rành rành tự động mớm luôn chiêu vectơ hóa cái vũng mã trên miễn bạn đành lòng hiến tế dọn cho mớ tùy biến ép toán cực tốc độ (fast math) phang chung cái phe tập lệnh đẻ từ khuôn SSE đồ lên.

Mớ chuyện dính vào ca lắt léo quẹo vòng thì lại bó chiếu trước khâu vectơ hóa tự động lười biếng. Tỉ như lội mổ qua ngắm thử góc khuất của một chùm chuỗi xài thuật Taylor. Gã hàm số mũ thừa sức bị lôi ra mần nhẩm bởi phép dãn dòng chuỗi sau:
```
e^x = sum (x^n / n!)
```

Mảng mã C++ được nhào ra sẽ hiện hình thành khuôn mẫu nhường vầy:

```cpp
// Example 12.9a. Taylor series 
float Exp(float x) {       // Approximate exp(x) for small x 
   float xn = x;           // x^n 
   float sum = 1.f;        // sum, initialize to x^0/0! 
   float nfac = 1.f;       // n factorial 
   for (int n = 1; n <= 16; n++) { 
      sum += xn / nfac; 
      xn *= x; 
      nfac *= n+1; 
   } 
   return sum; 
} 
```

Nhìn chõ vào đây, có ngửi thấy cái mùi rằng mỗi mức mảng giá trị `xn` bị lôi đầu ra tính hệt vào cái mốc nấc số kế sát ở vạch lùi hệt y khuôn cấu trúc `xn = x * xn-1`, còn đống `n!` cũng đè đầu cưỡi cổ lên cái vạch đi dạt ra sau y lột cái vỏ `n! = n * (n-1)!`. Đứng ở thế lỡ muốn chẻ cái nhánh vòng lặp bung bét tách làm tư, ta đành phải gạt nước mắt cắn răng tính nhẩm hệt mọi cái cột mốc theo cái mảng số lết đi lùi đúng bốn bực lùi ra sau. Bởi rứa, ta mần chiêu tính cho `xn` khoác lốt rập khuôn mảng `x4 * xn-4`. Ngặt nỗi mò hộc tốc cũng chả rờ gáy nổi ngón đòn ranh ma nào đặng khui bung cái công đoạn xử lý phép giai thừa, hên thay làm trò này vớ vẩn rảnh rỗi bởi bầy giai thừa kia vốn chả ngả rễ dính dấp tới thằng `x` tẹo nào thành thử cứ chưng cất tuốt cái đám biến số đấy cất gọn giấu trong một quyển bảng tính nặn sẵn chực chờ lôi ra xài (pre-calculated table). Hay ho hơn nữa: nhồi nhét cất luôn cái mớ giai thừa nghịch đảo (reciprocal factorials) cốt rũ bỏ đống nợ nần dây vào phép toán chia (trò tính chia bao đời nay vốn lề mề, như thiên hạ đồn đại). Cái nùi mã bấy giờ đã được nặn nắn trọn kiếp vectơ theo bộ dáng thế này (dùng tới đám lớp vectơ của Intel):

```cpp
// Example 12.9b. Taylor series, vectorized 
#include <dvec.h>          // Define vector classes (Intel) 
#include <pmmintrin.h>     // SSE3 required 
 
// This function adds the elements of a vector, uses SSE3. 
// (This is faster than the function add_horizontal) 
static inline float add_elements(__m128 const & x) { 
   __m128 s; 
   s = _mm_hadd_ps(x, x); 
   s = _mm_hadd_ps(s, s); 
   return _mm_cvtss_f32(s); 
} 
 
float Exp(float x) {       // Approximate exp(x) for small x 
   __declspec(align(16))   // align table by 16 
   const float coef[16] = {      // table of 1/n! 
      1., 1./2., 1./6., 1./24., 1./120., 1./720., 1./5040., 
      1./40320., 1./362880., 1./3628800., 1./39916800.,  
      1./4.790016E8, 1./6.22702E9, 1./8.71782E10, 
      1./1.30767E12, 1./2.09227E13}; 
   float x2 = x * x;              // x^2 
   float x4 = x2 * x2;            // x^4 
   // Define vectors of four floats 
   F32vec4 xxn(x4, x2*x, x2, x);  // x^1, x^2, x^3, x^4 
   F32vec4 xx4(x4);               // x^4 
   F32vec4 s(0.f, 0.f, 0.f, 1.f); // initialize sum 
   for (int i = 0; i < 16; i += 4) {  // Loop by 4 
      s += xxn * _mm_load_ps(coef+i); // s += x^n/n! 
      xxn *= xx4;                     // next four x^n 
   } 
   return add_elements(s);            // add the four sums 
} 
```

Đoạn vòng chạy lặp cuộn liền tù tì một nhát dồn nén bốn cái phân mảnh dính chùm liên hoàn gói vào một cái vectơ tròn trịa. Có lẽ nó cũng bõ công xứng sức nếu ta tháo xích mớ vòng lặp nặn giãn cự li xa vời thêm nếu trúng lúc vòng lặp kéo quá dông dài do cữ tốc độ mần việc ngự chốn này rất có cơ may bị bóp nghẹt lún phanh bởi cái đống gánh cồng kềnh tới từ thứ độ trễ (latency) của cái toán tử nhân chập `xxn` hơn là khâu thông lượng thoát (throughput) (lật xem thêm ở trang 105). Quyển bảng tính liệt kê rải rác đống hệ số được mần phép nhẩm ngấm ngầm tại khoảng thời khắc biên dịch gác mái nơi đây. Hoặc giả lại bộc lộ vẻ tiện lợi hơn chán hễ tự tính ra cái bảng tại thời điểm mã đã vô luồng chạy thời gian thực (runtime), chừng nào bạn chắc mẩm cược một phen đảm bảo rằng bảng kia thảy bị kêu réo tính đúng có duy nhất một chập, chẳng phải theo cái thói hàm lôi ra xài lần nào tính dồn lần đó.

## 12.7 Các biến hàm toán học chực bợ đỡ cho nhóm vectơ (Mathematical functions for vectors)
Bày biện ra hằng hà sa số các kho thư viện chức năng nhằm nhẩm tính nặn ra các nhóm hàm toán học đủ thể loại lấy ví như hàm hệ logarit, dạng hàm số chứa dấu mũ, dải hàm lượng giác lằng nhằng, hầm bà lằng hở tí xài vectơ chêm vào. Bầy thư viện hốt trọn chức phận hàm nhường này mang theo mình thứ công dụng to tát phục vụ khâu vác đống mã thuần toán nhét vô máy vectơ hóa.

Lòi ra đến tận hai phe cánh thư viện toán dính tới vectơ dị biệt trái phe: kho thư viện vectơ đuôi dài lê thê (long vector libraries) cùng cụm thư viện gốc vectơ chắp vá dạng ngắn (short vector libraries). Khui cái điểm gợn sóng khác biệt, lấy rập khuôn câu chuyện giả tưởng rằng bạn hầm hè mần thịt duy nhất một dạng hàm nặn toán đập lặp lại liên hoàn vạn kiếp trên sống lưng hàng ngàn đầu con số. Níu xài chưởng của phe thư viện hệ vectơ dài, bạn tự lấy rơm buộc vào bụng mang nguyên lốc dải mảng chứa ngàn đứa phần tử lót ổ dưới lốt một cái thông số ban cho biến hàm dâng chốn thư viện ấy, mớ hàm kia sau lại thảy chôn trọn vẹn cả thảy ngàn mảnh kết cục đào mương giấu sâu bên dưới bụng một dải mảng lai tạp khác. Điểm lép vế tồi tệ đến từ cái trò moi thư viện xài loại vectơ cồng kềnh dài nhằng này chui đầu vào hốc nếu bạn buộc dây mần liên tù tì cả dãy các nhát cắn tính nhẩm thì bạn đành gánh thêm quả nợ tốn đất chứa dồn nhét mớ kết quả ngã ba đường đâm chồi từ dăm góc luồng chạy chôn nơi cái mảng dã chiến tạm thời trước chập lôi gọi mẩu hàm tính phần đoạn tiếp. Kẻ xài đòn dùng hệ thư viện đẻ ra cái mảng vectơ ngắn ngủn, thì có chiêu xé dọc xé ngang cụm dữ liệu phân nát nó văng thành từng cọc vectơ phái sinh con trẻ (sub-vectors) nặn sao lọt lỏn luồn khít qua ngách kích thước của kho thanh ghi vectơ (vector registers) tọa trong ruột CPU. Nếu rủi thanh ghi lứa vectơ ấy thừa sức chống gánh nhồi nhét, cho dụ bốn tay số, thì rốt cục bạn cắn răng gõ cổng mảng hàm số phía thư viện tròn chĩnh 250 lượt lặp với thù lao bốn tên lính số mỗi chuyến lèn chặt cứng dưới cái mai rùa chở bởi cụm thanh ghi vectơ. Bộ hàm nằm ườn nơi thư viện bấy giờ trút trả về cọc số kết xuất tuồn qua dạng thanh ghi vectơ thế chỗ nhét mồi ngay vào miệng bước rẽ nhánh liên phanh nối gót thuộc luồng chuỗi tính nhẩm chẳng bận công phải nhồi ép nhét kho giấu lũ số liệu nửa mùa trôi tuột xuống lòng huyệt trí nhớ RAM làm chi cho rối. Độc chiêu lắt léo này vớ vẩn nhả tốc nhanh hơn chán chê mặc xác cái việc thâm hụt rác rưởi bởi những cú gõ hàm lách chéo đẻ thêm tại cái thói CPU dư hơi chép mồm nhai ngấu nghiến thực thi vũng mã mà chân thì đập nhịp lén la lén lút tuồn mồi nhử tải mớ luồng mã đi kèm biến hàm lứa sau vô chực chờ móc ra xử lý ngay tức thì (prefetching). Đời vốn nghiệt ngã, chiêu tung đòn hệ vectơ cụt ngủn dễ sinh chuyện hụt chân nếu khâu dàn hàng đống dây chuyền mớ phép tính rập nặn trổ ra một dải sương mù đan đan bện chặt kết dính thành chuỗi phụ thuộc (dependency chain) kéo phơi lây lết. Người phàm khao khát CPU thảy mình xắn tay nhảy nhót vờn trên luồng chạy hệ vectơ phái sinh con trẻ chuyến số hai sớm hẳn một khắc lúc chưa thèm phủi đít kết thúc cho trót khâu luân hồi toán học đè nén trên lưng lũ vectơ chắt con phe đầu tiên. Rủi vướng cái hố chuỗi bám đuôi lê thê nặn mớ gánh nặng ập tới hốt trọn bãi đáp hàng chờ đợi của vũng rác lệnh tắc ứ chưa tiêu hóa lấp phình trong lòng ruột CPU rồi phang thẳng cái hãm nhịp phanh kìm trói tay bóp cổ cơ chế bấu víu đoạt mớ sức mạnh ranh mãnh nặn trổ từ cỗ máy xử lý phi tuần tự (out-of-order calculation).

Khều đại ra bảng danh sách vớ vẩn mấy xó chứa thư viện thuần toán chắp cánh cho phe vectơ lê thê dài dọc:
* Khối thư viện toán nằm nôi hệ vectơ cộp mác Intel (VML, MKL). Múa may êm xuôi qua mọi hệ sân bãi chơi quy chiếu x86. Nùi thư viện này thót tim nặn cái performance ghẻ lở trên xác mấy dòng CPU hất cẳng cái lốt Intel trừ phi bạn ngửa bài ăn gian bẻ ngoặt cướp quyền (overriding) nhóm bộ nhả lệnh phân luồng (dispatcher) CPU nòi Intel đẻ ra. Ngó sang trang 134 cho kỹ.
* Bộ móng Intel Performance Primitives (IPP). Trơn tru qua vạn dải x86. Ngậm êm chạy luột ngay cả xài CPU loại ngoài Intel. Vác theo nguyên bầy biến hàm chuyên rờ tới số liệu thống kê, mớ xử lý nắn bóp tín hiệu lẫn cả múa may xào nấu ảnh họa.
* Thư viện mở Yeppp. Mở cửa tung mã ngầm. Nâng nách chống lưng cho đám nền đất x86 cắp theo ARM với đẻ đống cửa sập nương nhờ đủ trò luồng ngôn ngữ xào nấu code lủng. Web ngự trị tại: www.yeppp.info

Đẩy xuống cái bầy danh sách đẻ cho đám lứa thư viện chuyên mần toán xài hệ vectơ mẩu ngắn:
* Thư viện hệ toán chuyên trị vectơ đoạn cắn cụt lủn đẻ từ Intel (SVML). Đám râu ria này thảy được bán bia kèm lạc tuồn chung với cụm dịch Intel và bị ập lôi hồn lên lúc xài phép vectơ hóa tự phơi diễn tự động. Thằng trình dịch phe Gnu có ngón đòn bẻ nặn ra xài cụm thư viện này mượn ngả lệnh `-mveclibabi=svml`. Thư viện loại này nhiều khi giật lùi thọt chân mất tốc nếu nằm trên xó CPU phi Intel trừ lúc bạn đánh thó giật dây bẻ quyền trói cái mớ phân nhả lệnh (dispatcher) cộp mác Intel. Dở trang 134 ngóng thêm.
* Góc thư viện mác AMD LIBM. Lè ra vớ bở xài trên độc có mấy khu đất 64-bit của nền Linux với Windows. Đống thư viện ghẻ này nặn cái hiệu suất tụt huyết áp trên xác cỗ CPU lỡ thiếu cái vũng rác tập lệnh FMA4. (Đống chùm lệnh đó xửa xưa vốn do bàn tay phe Intel chắp vẽ cơ mà chả hiểu sao giờ chỉ duy nhất dàn CPU của hội AMD chứa chấp bợ đỡ cho nằm chơi). Gã trình biên dịch Gnu đủ khả năng bấu bám vô ngách thư viện chốn này nương nhờ cái thẻ bài nhúng tùy chọn `-mveclibabi=acml`.
* Cụm thư viện lứa lớp vectơ cộp dấu ngầm VCL nặn từ tôi. Loại mở mã ngầm tự do. Bênh vực che lấp rải qua mọi hóc x86. Chứa chấp mớ trình dịch thuộc dải Microsoft, Intel, hệ Gnu cùng phe Clang. Cả vũng mã thảy bị nội tuyến hóa hất văng (inlined) - rảnh nợ cái khoản nhọc xác kết dính lôi xéo rờ cụm thư viện hóng hớt từ dải ngoài nhét vô. Xem link www.agner.org/optimize/#vectorclass

Tất thảy mọi khu rác thư viện vừa gõ đầu ấy chễm chệ đoạt được một luồng hiệu năng cực mượt chắp thêm cái độ chuẩn xác miễn bàn. Ngưỡng cữ thời gian bay nhả tốc đi với tốc lực phải lẹ hơn ngàn lần xài lót cái phe đám thư viện dạng mác phi vectơ (non-vector).

Đống thẻ bài danh xưng chằng chịt cho phe nhóm biến hàm ngự bên chốn thư viện lứa SVML lẫn hội LIBM phải chăng do lười biếng mà đâm ra mù mịt thiếu khâu dọn nếp tài liệu cẩn thận. Cái nùi ví dụ chôn trong bảng dưới đây ắt hẳn tạo phước hễ bạn có máu vớ liều mò kêu réo đống hàm thư viện rành rọt không mượn cớ trung gian xỏ lá:

| Thư viện (Library) | Hàm `exp` dành cho 4 số `float` | Hàm `exp` dành cho 2 số `double` |
| --- | --- | --- |
| Intel SVML bản 10.2 trở về trước | vmlsExp4 | vmldExp2 |
| Intel SVML bản 10.3 trở về sau | __svml_expf4 | __svml_exp2 |
| Intel SVML + ia32intrin.h | _mm_exp_ps | _mm_exp_pd |
| AMD Core Math Library | __vrs4_expf | __vrd2_exp |
| AMD LIBM Library | amd_vrs4_expf | amd_vrd2_exp |
| VCL vector class library | exp | exp |

## 12.8 Căn lề ép góc cho góc bộ nhớ vọt sinh lắt léo kiểu động (Aligning dynamically allocated memory)
Một mảng bộ nhớ vốn phôi thai bằng thuật phép nhúng lệnh `new` hay rờ `malloc` thường theo lệ bị đóng khuôn xếp theo chia nếp lề con số 8 thay rập vì số 16. Thứ này mới nghe đã lồi mầm gieo rắc đại họa đụng vô cái đám thao tác hệ vectơ hễ mảng ốc vít lề góc chia mốc 16 bị gông cùm ép chỉ định. Cụm biên dịch kho Intel đã lách thóp dọn sạch sành sanh khúc mắc ấy thông qua màn định hình tung ra cặp đao `_mm_malloc` kề kề cái đục `_mm_free`.

Kiếm miếng võ lạt mềm buộc chặt trơn láng phổ biến hơn thì chùm kín giấu biệt dải mảng vừa khoét lấy ngự dạt vô trong ruột một vũng thùng chứa giả lớp (container class) thằng lứa này nhúng tay hốt xác dọn dẹp nguyên cụm phiền nhiễu vụ lề lủng. Mò chõ sang www.agner.org/optimize/cppexamples.zip để soi thấu đống mánh lới nhào nặn dải mảng ép lề lọt với mác hở đường moi xài vectơ.

## 12.9 Xếp góc căn lề rập khuôn cho lứa phim RGB hay mảng vectơ chạy 3 chiều (Aligning RGB video or 3-dimensional vectors)
Đám thông tin chứa dữ kiện hệ màu ảnh RGB ôm đồn lấy tới cả ba cụm hệ số đè vào lót lọt từng chấm điểm. Thằng nhãi rách này vớ vẩn nhét không vừa vặn lọt thỏm vào khuôn ngự của hố vectơ đơn cử như đám gánh tận bốn cục biến `float` dại dột. Trò hệt vậy cũng rập khuôn nhét cho cái phe nhóm hình học vẽ hình 3 chiều mang theo đám số má vectơ cõng cái bộ dạng lệch pha (odd-sized) tạp nham tương tự. Rổ thông tin bắt buộc phải bị bóp méo vặn ép cho nằm thẳng nếp rập khuôn mảng thể hình kích thước cỗ vectơ để qua chót lọt trót lọt đong đếm mót nhặt xíu hơi hám hiệu suất sinh lời. Cứ mù quáng lao vào mần màn vọc lấy lệnh nạp móc vô trút ra đọc ghi hố dữ liệu xài mảng xộc xệch lệch nếp (unaligned) dăm chập xui xẻo kéo cái tốc lực cày bừa rớt mốc tồi tàn tận đáy hố tới bực khó coi đến nhường cái lợi ích rút được từ món xài toán tử vectơ bỗng nhạt phai trôi về không. Bạn được quyền rút vội quơ vào một trong số mấy rổ kế bẩn phô diễn lắt léo rải ra hệt bên dưới, nương tựa hễ nén được cục lọt vô trúng ý khâu giải thuật lằng nhằng nặn vướng chướng ngại này:

* Ném chèn thêm nhồi nặn tọng luôn vô một quả hạt nhân hệ số nhét thứ tư vớ vẩn đóng vai thừa thãi lót đệm bù chắp cho bầy rác dữ liệu căng phình nhét chặt kín trót lọt khuôn khối vectơ. Đẩy lên xem hệt mớ lách luật nhàn rỗi nhẹ bộp, cơ mà đành tốn thêm dăm mảng bãi bộ nhớ ngấu nghiến gặm mòn (memory used) bị khoét thủng xài hao uổng phí. Bạn tốt hơn nên chôn sống trốn biệt cái hệ giải này giả dụ công cuộc cày ải đào xới nhét trút mảng hệ bộ nhớ đóng vai làm quả chốt cổ chai kìm hãm luồng hiệu năng (bottleneck).
* Tranh thủ xào bài dọn dẹp nhồi mảng dữ kiện chia gom thảy về thành bầy cụm mang thể 4 (hay 8) điểm chấm rạch ròi hễ mà bốn số R vứt trọn ổ trong duy nhất một hệ vectơ, nguyên dải bốn mạng hệ G tống lót vào bộ vectơ tiếp bước chầu chực, cộng gộp bốn tên cộm cán mạng B nằm chết dí nơi cuối đuôi hốc vectơ cuối chót.
* Gom mớ rác dọn trơn tru vũng thông tin ép lót chăn mọi đầu số vế R tranh nằm hốc đầu nhát cắn, kế lôi gót rập hàng dải toàn bộ nùi G bò trườn vô theo đuôi, lùi lại đóng đít gom hốt đống số phe nhóm phế thải tàn tích dăm cái đầu bậu B.

Đoán định ngã giá lôi đầu chọn vứt đâu cái thứ chiêu trò múa may lắt léo nào ập vào phải chăng đành ủy thác dựa nhờ nơi đống độ dẻo dai bám ăn đứt vô ruột cái mạng lưới hình dạng toán học bấu xé xoay quanh. Người trần mắt thịt như bạn mần chi ngó lảng cứ quơ mướn vội cái ngón đòn phôi thai sinh được luồng nhánh mã êm ái trơn mượt không dính chướng ngại là chót lọt.

Nếu lỡ cái rổ số lượng các chấm điểm trớ trêu rúc nhầm cái số chẳng thể chia hốt cho vừa vặn cái bộ chia hệ thể hình vectơ thì cứ đành đánh thó nhét vứt chêm đại dăm ba nốt mạng hạt câm cọc phế phẩm chôn trút vào đuôi chót cốt tóm cho trọn lấy khối tròn trĩnh nguyên mẫu mang phận cỗ xe vectơ.

## 12.10 Lời chốt tóm lại (Conclusion)
Cày cuốc ôm một mớ lời vươn nách hiệu tốc độ siêu trơn nhờ bám áo nương vào phao vectơ giả dụ đống mã luồn được cái dòng máu mạch song song chực trào tự thuở lọt lòng. Lộc nhặt thu hồi ăn theo rớt lọt nằm trong sự móc nối tới sỉ số tổng đàn hạt phần tử rải lên mặt một cỗ vectơ. Đường dọn sạch bóp lách khôn ngoan không chê được chắc nịch quy về trút dựa thác bóng phó mệnh vào gánh tự thao túng trổ phép vectơ hóa (automatic vectorization) nhờ gã thợ đụng tay trình dịch lót nặn. Đứa thợ trình biên dịch vờn chép miệng nhét mã tuôn vào móng vectơ hóa trong chớp mắt nơi góc khuất cõi vũng ví dụ hạng nhẹ lọt phơi ra vũng mạch chạy song song (parallelism) ló ngó tới chướng mắt hay cái hố nùi mã ôm khư khư lèo tèo vài hạt bụi hệ toán thao túng nhạt phai dăm vạch lề lối trơn trượt (simple standard operations). Mọi món bạn nặn công hất vào chỉ xoay quanh gỡ cái bóp cò khai hỏa khui ngàm vũng tập lệnh mác SSE2 đồ hậu sinh xài.

Khốn nỗi, vẫn hở ra mớ rắc rối nơi chốn gã múa tay trình biên dịch giơ tay xin hàng chối vứt đi vụ vectơ hóa nhão nhão qua kiểu chạy rề rề tự động phế thải hoặc quăng lót thứ rác sản phẩm rỗng tuếch dạng lết chưa tối ưu (suboptimal way). Chui vô xó này người trần buộc xắn tay vạch trần lôi mã nhào ra đánh cho nhuyễn chừa lối vectơ hóa phơi mình vạch nếp lộ rõ (explicitly). Phơi sương nhan nhản nùi mánh trò khui nhồi thủ công nặn ra bầy mớ này:
* Nương tựa vùi lấp xài vũng móng hợp ngữ (assembly language)
* Moi móc rút ruột bầy hội hàm nội tại (intrinsic functions)
* Nhặt xài sẵn đống mạng cấu trúc lớp vectơ (vector classes) đúc đổ khuôn từ rốn

Ngón bài mềm mượt qua dễ dãi bậc nhất để giáng thủ xài chiêu vạch nếp vectơ hóa là nhờ xài cướp lấy kho thư viện lứa nhóm lớp vectơ (vector class library). Tranh thủ rảnh tay bạn dồn hất pha trộn đống này đi theo hàm nhào nặn nội tại nếu khao khát chọc đống đồ nặn chưa khoét chôn trong nôi thư viện chứa lớp chức năng vectơ. Bất kể bạn đắn đo móc nùi đống chùm hàm phôi thai lọt hốc nội tại lút góc hay chuộng vọc vào xóm lớp tính vectơ phơi mình thì đấy cũng vỏn vẹn lằn ranh nằm trong góc xó chữ tùy tâm (convenience) - hai loại đẻ ra y hệt chẳng vướng vết cắt ly giáo đo ở thước đo tốc độ hiệu năng xử lý (performance). Gã tay ngang trình biên dịch biết cách bợ đít mớm thả ra đúng một phôi mã (same code) ngự ở chót vạch ranh dù rơi vô màn lật bài rớt lọng nào đi chăng nữa. Dạng hàm bọc lót nội tại có mang cái vẻ chắp vá rỗng tuếch với cục kịch xồ xề hầm bà lằng. Đoạn mã biến hóa dễ ngửi mướt mắt khi vọc vô đám lứa lớp nặn vectơ đính chung đám chùm hàm nạp chồng đè (overloaded operators).

Chàng trình dịch tốt mã thi thoảng vớt vát lôi kéo thao túng bóp mã luồn lách phô tút lại bầy nếp góc đẩy hiệu suất (optimize the code) sâu hun hút vớt sau chót vụ bạn mới rờ gáy nắn nhóp thủ công hất vô nôi hệ vectơ. Gã này đâm chồi bới mổ móc chước mánh lới nhào ép tỷ như ngón băm gọt nạp trét dạng nội tuyến cho mảng hàm (function inlining), bài chém bay biến hội diễn đạt giả dối nạp lại (common subexpression elimination), mẹo rải phát tán cái cọc nhãn hằng số văng vô tội vạ (constant propagation), với chiêu độ vòng lặp (loop optimization), đồ. Mớ tuyệt chiêu nhào nặn kia thỉnh thoảng hiếm muộn bĩ cực lắm mới thó ra moi trong hầm rác thao túng mảng hợp ngữ thủ công lầm lũi do chưng cái trò đè ấy rớt bóp làm bộ mã lú đú kẹt cồng kềnh (unwieldy), dễ sập chướng hố ngập rác lỗi (error prone), còng luôn chuyện đành khoanh tay đứng chầu chực nhượng bộ chẳng vớ ra đường vá lọt khe mà bảo trì nổi. Đòn lai pha phôi trộn vụ bẻ nắn ngón lách nương tay vectơ hóa bằng ngón chưởng thủ công đi chung hớt vớt đẩy nắn đùn trình nặn ép mượt mã từ tay biên dịch (compiler) nặn bóp rốt cục lại dễ nhổ mọc nhả trái quả cực bốc ở vạn lần màn chạm trán nhan nhản. Lũ trình đúc vọc biên dịch dẫu bôn ba bao chốn nay hiếm hoi đâm chọt xài trò nhồi lan phát tán mác dạng hằng số trơn tru cùng dăm đường nhào nắn đâm thọc độ lướt trên phe lũ ruột lót luồng mã hệ vectơ. Lần khân lại thấy chốt đành có lỡ dở đôi lúc tự mượn áo giấu mảng nhúng bứt tay buông giao đứt cho màn xài thuật nhả vectơ tự động (automatic vectorization) hất qua phe cái máy biên dịch rỗng hễ nó gánh lót nhả kèo chẳng rờ thấy vết bợn nhơ. Góp dăm cọc thời gian mò ngửa chọc ngoáy vọc vạch (experimentation) phơi mình cũng mang nghĩa cứu rỗi cào xới đặng mò rút về ngón bám mạn trượt tối đa phước lộc (best solution).

Mớ nùi mã đè lót nhồi vô bao vectơ tréo ngoe thay hay lòi chui ra ngậm nén cả lố những chỉ thị độn bù thêm đặng dằn lấy ép chóp mảng biến đổi số lót vạt (converting the data) dọn vào cái rương định dạng ngậm phom đúng đắn rồi mới xới ùa gom hất đẩy đi vào vũng vị trí (right positions) tròn trịa đo ni đóng giày lọt ruột mấy lớp vectơ. Cái mảng lôi mồi quy đổi dữ kiện lẫn trò nắn xào tráo đổi rác xoay vòng chong chóng (shuffling) kiểu này lác đác kéo ghì lụt hụt thời gian mòn mỏi trôi tuột còn lắm hơn khâu lôi mảng phép toán (actual calculations) chân chính vồ vập xử lý. Mảng mâm trút bã này đáng bị điểm mặt nhớ kỹ moi xét cặn kẽ chập nào nặn bộ óc dòm chừng cắn đắn lường cân thiệt hơn chuyện vớ bám bợ vectơ rờ gáy có lụm được quả ngọt ngào tơm tất chăng (profitable).

Tôi rắp tâm kéo màn bế mạc trút dấu chốt hạ phân mảng mẩu ở đây lấy vạch mốc đánh tóm lược nguyên cái đám cội nguồn nhân tố (factors) đè đầu rạch phán ngón chưởng vung xài thuật kéo chèn rúc vào lót lớp vectơ hóa phô trương bao món hơi sức điểm bốc lên chốn lợi điểm thần thông (advantageous) ra đặng.

Mớ nhân tố nặn ra mảng vectơ hóa chiếm rợp chiếu vớt lộc hời (favorable):
* Hệ hạt giống lứa mang mác dữ liệu teo tóp vụn vặt: `char`, `short int`, `float`.
* Đắp lặp đè cùng một dạng toán thao tác luân chuyển liên tục rải mâm trút ập qua nguyên bầy thông tin ngâm trong đống vũng mảng khổng lồ dài lết.
* Khoảng độ lớn của mảng rỗng chia đều nhẵn vớt không sót điểm cho tổng thể hình nặn cục thuộc hệ vectơ.
* Đám quặt luồng nhánh phơi màn chẳng dò ra bóng đường chọc nết chọn gỡ (select) một mảng phe bên trong cái hố nùi cặp đôi mớ tính nhẩm (expressions) dạng dọn chóp giản đơn.
* Trò thao túng mảng lệnh (operations) tréo ngoe chỉ bám rễ ló mặt rành rành hễ kẹp chung đi xài dăm gã toán hạng dính dấp rễ vectơ (vector operands): rà độ mốc bé đứt (minimum), đếm vũng điểm to phình (maximum), thuật nhồi nặn cộng chập trào bão hòa (saturated addition), luân hồi nạp rút hệ nghịch đảo lẹ tay lanh mắt phán (fast approximate reciprocal), rút xài đường phép lôi căn bậc hai phang xéo nghịch đảo rướn ranh lẹ chóp (fast approximate reciprocal square root), rồi mảng moi lỗi sai sắc phân pha vũng màu RGB (RGB color difference).
* Cái hố dàn tập lệnh dính phần vectơ ló mặt mở sẵn chờ ăn (available), như cọc AVX, hội AVX2, phe AVX-512.
* Nùi mảng chứa thư viện bám cục chức phận chuyên gánh phép vectơ toán học đèo bồng (Mathematical vector function libraries).
* Bám váy chắp xài gã dịch hệ Gnu, rờ nách Clang chêm vào nôi Intel sinh lời.
* Mượn gã phu bốc vác CPU ngậm ôm chứa cái cọc rổ đẻ thực thi ngự mức thể trạng chắp vá đè ướm khớp khuôn đúc kích cỡ thằng thanh ghi vectơ (vector register).

Đống cội rễ đẻ nặn làm trò gọi hồn vectơ hóa quay lọt hố trượt lùi văng xa phần mòn mỏi (less favorable):
* Phe hạt mầm thông tin mác lứa to xác uốn éo cồng kềnh: kiểu `int64_t`, hệ `double`.
* Cọc thông tin dữ liệu chạy trật đường lề không canh vứt xó xệch trượt (misaligned).
* Mang đống phế phụ nhồi nhét cữ lót thao túng lùi chuyển định dạng dữ kiện đục lọt (conversion), xáo bài bốc luân hồi (shuffling), đắp bó (packing), vạch xé nới (unpacking) ập vào chằng chịt cần ngó móc.
* Mớ chia nhánh lươn lẹo nắm thóp bắt phai (predictable branches) dư sức hất nhảy bật vượt nhát đè băng rào lọt mớ cụm lệnh lớn xác (large expressions) dăm ba chập vắng bóng phiếu lụm chọn chọc vào vũng mã ấy.
* Rốn trình dịch bù trất ôm bụng rỗng thiếu khuyết trầm trọng mớ bãi rác chỉ lệnh vọc mạch báo lề lối (alignment) chắp vũng của gã nhõng nhẽo con trỏ cộng lót điểm mớ mác xài chui biệt danh mảng chiếu dọi (aliasing).
