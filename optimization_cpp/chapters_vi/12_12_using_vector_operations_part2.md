```cpp
// Example 12.1c. Vectorization with intrinsic functions 
#include <emmintrin.h> // Header file for SSE2 intrinsic functions 
 
void AddTwo(int * aa, int * bb) { 
   const int size = 1024; 
   __m128i * a = (__m128i*)aa;  // Make a vector pointer to aa 
   __m128i * b = (__m128i*)bb;  // Make a vector pointer to bb 
   __m128i two = _mm_set1_epi32(2); // Make a vector of (2,2,2,2) 
   for (int i = 0; i < size/4; i++) { 
      // Do the addition. The loop count is reduced by a factor of 4 
      a[i] = _mm_add_epi32(b[i], two); 
   } 
} 
```

Đẩy lên cái ví dụ nhích nếp phức tạp lên chút đỉnh chính là sự phân nhánh nương nhờ dòng chảy của dữ liệu. Cấu trúc C++ ngắm qua chắc mẩm có điệu bộ như vầy:

```cpp
// Example 12.4a. Branching based on data 
void SelectAddMul(short int aa[], short int bb[], short int cc[]) { 
   for (int i = 0; i < 256; i++) { 
      if (bb[i] > 0) { 
         aa[i] = cc[i] + 2; 
      } 
      else { 
         aa[i] = bb[i] * cc[i]; 
      } 
   } 
} 
```

Hệ vòng lặp này dư sức ôm mộng vectơ hóa bằng cái mẹo tung đòn tính toán đè ra đập nát cả hai phân nhánh rồi sáp nhập tất thảy kết quả về một mối xài thứ ngón đòn nhào nặn lớp mặt nạ cộm bit (bit mask). Mẩu mã rờ tới bộ vectơ 128-bit với bầy hàm nội tại rập khuôn vầy nè:

```cpp
// Example 12.4b. Same example, using intrinsic functions 
#include <emmintrin.h>            // Define intrinsic functions 
 
// Function to load unaligned integer vector from array 
static inline __m128i LoadVector(void const * p) { 
   return _mm_loadu_si128((__m128i const*)p);} 
 
// Function to store unaligned integer vector into array 
static inline void StoreVector(void * d, __m128i const & x) { 
   _mm_storeu_si128((__m128i *)d, x);} 
 
void SelectAddMul(short int aa[], short int bb[], short int cc[]) { 
  // Make a vector of (0,0,0,0,0,0,0,0) 
  __m128i zero = _mm_setzero_si128(); 
 
  // Make a vector of (2,2,2,2,2,2,2,2) 
  __m128i two = _mm_set1_epi16(2); 
 
  // Roll out loop by eight to fit the eight-element vectors: 
  for (int i = 0; i < 256; i += 8) { 
    // Load eight consecutive elements from bb into vector b: 
    __m128i b = LoadVector(bb + i); 
    // Load eight consecutive elements from cc into vector c: 
    __m128i c = LoadVector(cc + i); 
    // result1 = c + 2; 
    __m128i result1 = _mm_add_epi16(c, two); 
    // result2 = b * c; 
    __m128i result2 = _mm_mullo_epi16(b, c); 
    // condition = b > 0; 
    __m128i condition = _mm_cmpgt_epi16(b, zero); 
    // a = condition ? result1 : result2; 
    // (This works by taking result1 AND condition,  
    // result2 AND NOT condition, and finally OR the two limits). 
    // The SSE4.1 instruction set has a blend instruction that  
    // can do this, but here we show a method that works on all: 
    __m128i a = _mm_or_si128( 
        _mm_and_si128(condition, result1), 
        _mm_andnot_si128(condition, result2)); 
    // Store the result vector in eight consecutive elements in aa: 
    StoreVector(aa + i, a); 
  } 
} 
```

Bạn chớ quên phải cấy ghép thêm mấy mẩu tệp tiêu đề (header file) ăn rơ với dàn biến hàm nội tại này. Bảng tên họ của cái đám tệp tiêu đề nhẵn mặt sẽ lộ diện hệt như vầy:

| Tập lệnh (Instruction set) | Tệp tiêu đề (Header file) |
| --- | --- |
| MMX | mmintrin.h |
| SSE | xmmintrin.h |
| SSE2 | emmintrin.h |
| SSE3 | pmmintrin.h |
| Suppl. SSE3 | tmmintrin.h |
| SSE4.1 | smmintrin.h |
| SSE4.2 | nmmintrin.h (MS), smmintrin.h (Gnu) |
| AES, PCLMUL | wmmintrin.h |
| AVX | immintrin.h |
| AMD SSE4A | ammintrin.h |
| AMD XOP | ammintrin.h (MS), xopintrin.h (Gnu) |
| AMD FMA4 | fma4intrin.h (Gnu) |
| Tất cả (all) | intrin.h (MS), x86intrin.h (Gnu) |
*Bảng 12.2. Các tệp tiêu đề dành cho các hàm nội tại*

Cái nùi tệp tiêu đề `zintrin.h` nhồi nhét cả mấy mảnh dị dạng về hàm nội tại do tôi tự chắp tay nhào nặn bù vô mấy ngóc ngách bị lãng quên trong mớ tệp tiêu đề đẻ từ trình biên dịch (mời qua chốn www.agner.org/optimize/cppexamples.zip dòm cho rõ).

Nhớ kỹ cái thóp là vài thằng trình biên dịch có thói chứa chấp kiểu lót duy nhất một mảng tệp tiêu đề độc cô cầu bại, mang cái mác là `intrin.h` hay nhãn `x86intrin.h`, gom hốt trọn ổ mọi thứ rác. Danh sách cộm cán đếm hết mặt hội hàm nội tại bị đào lên từ quyển *Intel Intrinsics Guide*, một báu vật tung hê trôi dạt dưới dạng công cụ tra cứu hay một mớ ứng dụng (ngự ở link này https://software.intel.com/sites/landingpage/IntrinsicsGuide/).

Bạn cần cược chắc chắn cho vụ bộ xử lý trung tâm (CPU) thực sự nâng đỡ chống lưng bộ chỉ lệnh tương ứng với nó. Hễ mà bạn cố đấm ăn xôi nhét thêm một tệp tiêu đề chuyên biệt dành riêng cho một bộ tập lệnh cao siêu nào đó vượt mặt tầm với của bộ CPU thì y như rằng bạn đang đánh cược chèn thêm một cái chỉ lệnh mà CPU chả thèm ngó ngàng hỗ trợ, dẫn tới chuyện khối mã sẽ đổ sụp (crash). Đọc qua trang 125 đặng biết mánh khóe tra dò đám tập lệnh nào đang được hậu thuẫn.

### Căn chỉnh dữ liệu (Aligning data)
Công đoạn bốc hàng dữ liệu chất lên một chiếc xe vectơ sẽ lao vút đi lẹ làng hơn nếu như các cục dữ liệu này được canh chỉnh lề ép góc (aligned) vô cho khớp với một khu vực địa chỉ nào đó chia được vẹn toàn cho tổng kích thước của cỗ xe vectơ (tầm 16 hay 32 byte). Khâu làm trò này có khả năng mang đến hiệu ứng cực kỳ đáng nể bên trên nếp gấp não của những bộ CPU lứa già cỗi cũng như hệ xử lý Intel Atom, song lại chẳng mang nhiều ý nghĩa sống còn trước mấy bộ xử lý thế hệ non trẻ. Tỉ dụ ngay bên dưới đây sẽ mách nước cách uốn nắn xếp mảng cho thẳng hàng.

```cpp
// Example 12.5. Aligned arrays 
 
// Define macro for aligning data 
#ifdef _MSC_VER              // If Microsoft compiler 
#define Alignd(X) __declspec(align(16)) X 
#else                        // Gnu compiler, etc. 
#define Alignd(X) X __attribute__((aligned(16))) 
#endif 
 
const int size = 256;           // Array size 
 
Alignd ( short int aa[size] );  // Make three aligned arrays 
Alignd ( short int bb[size] ); 
Alignd ( short int cc[size] ); 
 
// Function to load aligned integer vector from array 
static inline __m128i LoadVectorA(void const * p) { 
   return _mm_load_si128((__m128i const*)p); 
} 
 
// Function to store aligned integer vector into array 
static inline void StoreVectorA(void * d, __m128i const & x) { 
   _mm_store_si128((__m128i *)d, x); 
} 
```

### Tính năng rà bảng tính mang vỏ bọc vectơ hóa (Vectorized table lookup)
Các mảng tra cứu (Lookup tables) tỏ ra vô vàn hữu ích cho chuyện tuốt tát lại dòng mã, tựa như được phơi bày cặn kẽ trên trang 135. Ngặt một nỗi, bảng tra cứu thi thoảng lại đóng trọn vai diễn chướng ngại vật chắn ngang con đường vectơ hóa. Các bè phái tập lệnh tối tân nhất có chắp nối thêm vài chiêu trò để xài vào dịp dò quét bảng tính dưới vỏ bọc vectơ. Mớ lệnh lạ này được dồn lại trong một bảng tổng hợp dưới đây.

| Hàm nội tại (Intrinsic function) | Số lượng phần tử tối đa trong bảng | Kích thước mỗi phần tử bảng | Số lần tra cứu đồng thời | Tập lệnh yêu cầu (Instruction set needed) |
| --- | --- | --- | --- | --- |
| _mm_shuffle_epi8 | 16 | 1 byte = char | 16 | SSSE3 |
| _mm_perm_epi8 | 16 | 1 byte = char | 16 | XOP, chỉ có trên AMD |
| _mm_permutevar_ps | 8 | 4 bytes = float hay int | 8 | AVX |
| _mm256_permutevar_ps | 8 | 4 bytes = float hay int | 8 | AVX2 |
| _mm_i32gather_epi32 | không giới hạn | 4 bytes = int | 4 | AVX2 |
| _mm256_i32gather_epi32 | không giới hạn | 4 bytes = int | 8 | AVX2 |
| _mm_i64gather_epi32 | không giới hạn | 8 bytes = int64_t | 2 | AVX2 |
| _mm256_i64gather_epi32 | không giới hạn | 8 bytes = int64_t | 4 | AVX2 |
| _mm_i32gather_ps | không giới hạn | 4 bytes = float | 4 | AVX2 |
| _mm256_i32gather_ps | không giới hạn | 4 bytes = float | 8 | AVX2 |
| _mm_i64gather_pd | không giới hạn | 8 bytes = double | 2 | AVX2 |
| _mm256_i64gather_pd | không giới hạn | 8 bytes = double | 4 | AVX2 |
*Bảng 12.3. Các hàm nội tại dành riêng cho việc tra cứu trên những mảng dữ liệu đã được vectơ hóa*

Giở bài rờ đầu đám hàm nội tại dăm khi phát rồ sinh chứng vướng víu với cồng kềnh, bộ mã lúc này phình to ra và cũng rối rắm tới độ hộc máu mới đọc xuôi. Cho nên, thường thì luồn lách bằng cụm lớp chức năng vectơ (vector classes) dễ thở hơn chán vạn, đằng nào cũng được vạch trần ở tiết mục ngay bên dưới.

## 12.5 Tận dụng nhóm lớp vectơ (Using vector classes)
Nặn ra mấy dòng mã rập khuôn theo đường đi nước bước bên mục ví dụ 12.4b với 12.4c ắt hẳn mang tiếng nhọc xác lôi thôi vô cùng. Chúng ta thừa khả năng viết y chang nhưng ở vào cái dáng vẻ mạch lạc rạch ròi đi vào nếp hơn bằng mẹo nén ép bao bọc hội vectơ lọt thỏm vào mấy chủng lớp C++ (C++ classes) xen lẫn sử dụng mánh lới dùng đám toán tử có chức năng nạp chồng (overloaded operators) phục vụ cho đủ trò như tính phép cộng giữa các hệ vectơ với nhau. Mấy gã toán tử kia thảy được rải dạng nội tuyến (inlined) cốt ngõ hầu cho chuỗi mã rác đầu ra của nó quay về hình thù bản mã máy y xì đúc không có nửa điểm sai biệt như thể bạn vừa dùng tới đám hàm chức năng nội tại vây. Nó chỉ là giúp cho người đời viết gọn lỏn `a + b` thay vì phải bưng cái nùi `_mm_add_epi16(a,b)` gõ vào.

Rải rác hàng lố hệ thư viện đính kèm cụm lớp (class) vectơ dựng sẵn có tiếng tăm lúc này, điểm mặt thì vớ được một đám từ Intel còn cái mớ lặt vặt nữa nằm ở thư mục của chính chủ tôi. Khu thư viện gói cả mảng lớp vectơ (hay gọi nôm na là VCL) mà do tôi chắp bút giấu diếm một bầy tính năng đồ sộ, ráng nhìn qua thử http://www.agner.org/optimize/#vectorclass. Bên kia chiến tuyến thì bầy thư viện hội vectơ của phe Intel có bề ạch đụi mốc meo lâu đời chẳng đặng ngó qua nên tự nhiên đóng cái xác chết nhét xó cho là lỗi thời phế trất (obsolete).

| Thư viện lớp chức năng vectơ (Vector class library) | Intel | VCL (Agner) |
| --- | --- | --- |
| Có mặt ở chốn (Available from) | Trình biên dịch C++ của Intel và Microsoft | www.agner.org/optimize/#vectorclass |
| Tệp cần chèn vào (Include file) | dvec.h | vectorclass.h |
| Cụm trình dịch chống lưng (Supported compilers) | Intel, Microsoft | Intel, Microsoft, Gnu, Clang |
| Vận hành dưới trướng HĐH (Supported operating systems) | Windows, Linux, Mac | Windows, Linux, Mac, BSD |
| Quyền kiểm soát hệ tập lệnh (Instruction set control) | Không | Có |
| Bản quyền (License) | Giấy phép nằm lọt thỏm gói chung theo giá bán trình biên dịch | Dạng phát hành mã nguồn mở (GNU General Public License), lót kèm tùy chọn giấy phép dân buôn chuyên dụng (commercial) |
*Bảng 12.4. Các thư viện gói gọn hệ lớp vectơ*

Cái bảng rải rác dưới đây bóc mẽ phơi bày hội lớp chức năng mang hơi hướm vectơ đang mọc rễ nhan nhản. Chèn vào chốn gốc mớ tệp tiêu đề (header file) phù hợp sẽ châm nổ khả năng đánh tiếng gọi tắt mở khóa tới mọi cỗ lớp chức năng vừa kể tới.

| Kích thước mỗi phần tử, bits | Số lượng phần tử trong vectơ | Loại phần tử (Type) | Tổng kích thước vectơ, bits | Lớp vectơ (Intel) | Lớp vectơ (VCL) |
| --- | --- | --- | --- | --- | --- |
| 8 | 8 | char | 64 | Is8vec8 | |
| 8 | 8 | unsigned char | 64 | Iu8vec8 | |
| 16 | 4 | short int | 64 | Is16vec4 | |
| 16 | 4 | unsigned short int | 64 | Iu16vec4 | |
| 32 | 2 | int | 64 | Is32vec2 | |
| 32 | 2 | unsigned int | 64 | Iu32vec2 | |
| 64 | 1 | int64_t | 64 | I64vec1 | |
| 8 | 16 | char | 128 | Is8vec16 | Vec16c |
| 8 | 16 | unsigned char | 128 | Iu8vec16 | Vec16uc |
| 16 | 8 | short int | 128 | Is16vec8 | Vec8s |
| 16 | 8 | unsigned short int | 128 | Iu16vec8 | Vec8us |
| 32 | 4 | int | 128 | Is32vec4 | Vec4i |
| 32 | 4 | unsigned int | 128 | Iu32vec4 | Vec4ui |
| 64 | 2 | int64_t | 128 | I64vec2 | Vec2q |
| 64 | 2 | uint64_t | 128 | | Vec2uq |
| 8 | 32 | char | 256 | | Vec32c |
| 8 | 32 | unsigned char | 256 | | Vec32uc |
| 16 | 16 | short int | 256 | | Vec16s |
| 16 | 16 | unsigned short int | 256 | | Vec16us |
| 32 | 8 | int | 256 | | Vec8i |
| 32 | 8 | unsigned int | 256 | | Vec8ui |
| 64 | 4 | int64_t | 256 | | Vec4q |
| 64 | 4 | uint64_t | 256 | | Vec4uq |
| 32 | 16 | int | 512 | | Vec16i |
| 32 | 16 | unsigned int | 512 | | Vec16ui |
| 64 | 8 | int64_t | 512 | | Vec8q |
| 64 | 8 | uint64_t | 512 | | Vec8uq |
| 32 | 4 | float | 128 | F32vec4 | Vec4f |
| 64 | 2 | double | 128 | F64vec2 | Vec2d |
| 32 | 8 | float | 256 | F32vec8 | Vec8f |
| 64 | 4 | double | 256 | F64vec4 | Vec4d |
| 32 | 16 | float | 512 | | Vec16f |
| 64 | 8 | double | 512 | | Vec8d |
*Bảng 12.5. Lớp tính năng vectơ nằm vắt vẻo bên trong cả thảy hai kho thư viện*

Kể ra không khuyên đám đông đâm đầu xài mấy kiểu vectơ mang mốc thể hình nén nhồi tròn trịa 64-bit cho cam, cũng bởi đám này khắc tinh với các khối mã mang dạng dấu thập phân động. Hễ cố đấm ăn xôi dùng đống biến vectơ 64-bit ấy cho bằng được thì buộc lòng phải khui hàm `_mm_empty()` nhảy múa ở khúc lết cuối màn vọc phép tính vectơ 64-bit trước bến đổ lúc nhào vô vũng mã tính toán số thập phân động lơ lửng. Cỡ vectơ to bự chảng sẽ chẳng đụng gót vô mấy phiền phức khỉ ho cò gáy thế này.

Bọn vectơ cõng mức dung tích chứa ở tầm 256 và 512 bit thì sẽ chỉ chịu ban ân xuất đầu lộ diện hễ có sự bợ đỡ ngầm phía sau từ chốn CPU kèm hệ điều hành tráo bài qua (nhìn sang trang 109 rõ mười mươi). Đứa con đẻ bầy đàn lớp thư viện VCL ngầm bên dưới trướng tôi có kỹ xảo xài bản nhái lột xác (emulate) giả mù sa mưa diễn vai vectơ 256-bit bọc trong cái lốt là một đôi vectơ 128-bit chập lại hoặc nặn cục vectơ 512-bit giả cầy đắp thành từ cái vỏ đôi khối 256-bit đồ nhái hoặc cấy ghép 4 mảng 128-bit chắp nối lại.

Đoạn dẫn chứng mượn tạm dưới đây phơi bày mảng mã lột ra rập khuôn đúng cái lốt gương mặt điển hình số 12.4b, cơ mà được xào nấu nặn bóp lại có rờ gáy tận dụng mớ lớp hệ vectơ bên nhà Intel:

```cpp
// Example 12.4d. Same example, using Intel vector classes 
#include <dvec.h>  // Define vector classes 
 
// Function to load unaligned integer vector from array 
static inline __m128i LoadVector(void const * p) { 
   return _mm_loadu_si128((__m128i const*)p);} 
 
// Function to store unaligned integer vector into array 
static inline void StoreVector(void * d, __m128i const & x) { 
   _mm_storeu_si128((__m128i *)d, x);} 
 
void SelectAddMul(short int aa[], short int bb[], short int cc[]) { 
 
   // Make a vector of (0,0,0,0,0,0,0,0) 
   Is16vec8 zero(0,0,0,0,0,0,0,0); 
   // Make a vector of (2,2,2,2,2,2,2,2) 
   Is16vec8 two(2,2,2,2,2,2,2,2); 
 
   // Roll out loop by eight to fit the eight-element vectors: 
   for (int i = 0; i < 256; i += 8) { 
      // Load eight consecutive elements from bb into vector b: 
      Is16vec8 b = LoadVector(bb + i); 
      // Load eight consecutive elements from cc into vector c: 
      Is16vec8 c = LoadVector(cc + i); 
      // result = b > 0 ? c + 2 : b * c; 
      Is16vec8 a = select_gt(b, zero, c + two, b * c); 
      // Store the result vector in eight consecutive elements in aa: 
      StoreVector(aa + i, a); 
   } 
} 
```

Kéo luôn vệt mẫu ví dụ tương đương nhưng đổi vai mượn mớ lớp vectơ từ hệ VCL tự tay nặn ra thì trông cái mặt bộ dạng hệt nhường này:

```cpp
// Example 12.4e. Same example, using VCL 
#include "vectorclass.h"     // Define vector classes 
 
void SelectAddMul(short int aa[], short int bb[], short int cc[]) { 
   // Define vector objects 
   Vec16s a, b, c; 
 
   // Roll out loop by 16 to fit the 16-element vectors: 
   for (int i = 0; i < 256; i += 16) { 
      // Load 16 consecutive elements from bb into vector b: 
      b.load(bb+i); 
      // Load 16 consecutive elements from cc into vector c: 
      c.load(cc+i); 
      // result = b > 0 ? c + 2 : b * c; 
      a = select(b > 0, c + 2, b * c); 
      // Store the result vector in 16 consecutive elements in aa: 
      a.store(aa+i); 
   } 
} 
```

Thằng trình biên dịch từ cái lò ấp Microsoft bế quan tỏa cảng chẳng thèm chứa chấp cái việc quăng đống tạo tác lớp vectơ vào lòng làm biến thông số đi chung (function parameters) cốt lỗi bắt rễ từ mấy khúc mắc ở khâu dọn nếp xếp lề lủng. Cho đặng êm đẹp, người ta dòm ngó với mớm lời khuyên nên đu bám mượn đám mã dẫn xuất (reference) loại nhãn hằng số (constant) mà phang vào thay chỗ:

```cpp
// Example 12.6. Function with vector parameters 
Vec4f polynomial (Vec4f const & x) { 
   // polynomial(x) = 2.5*x^2 - 8*x + 2 
   return (2.5f * x - 8.0f) * x + 2.0f; 
} 
```
