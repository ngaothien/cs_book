## 14.5 Phép chia số nguyên (Integer division)

Phép chia số nguyên tốn nhiều thời gian hơn phép cộng, phép trừ và phép nhân (27 - 80 chu kỳ xung nhịp cho số nguyên 32 bit, tùy thuộc vào bộ vi xử lý).

Phép chia số nguyên cho một lũy thừa của 2 có thể được thực hiện bằng một phép dịch bit (shift operation), cách này nhanh hơn rất nhiều.

Phép chia cho một hằng số nhanh hơn phép chia cho một biến số bởi vì các trình biên dịch tối ưu hóa có thể tính toán `a / b` thành `a * (2^n / b) >> n` với một lựa chọn $n$ phù hợp. Hằng số `(2^n / b)` được tính toán trước và phép nhân được thực hiện với số bit mở rộng. Phương pháp này phức tạp hơn một chút vì phải thêm vào nhiều sự điều chỉnh cho các lỗi về dấu và làm tròn. Phương pháp này được mô tả chi tiết hơn trong tài liệu 2: "Tối ưu hóa chương trình con trong hợp ngữ" (Optimizing subroutines in assembly language). Phương pháp này nhanh hơn nếu số bị chia (dividend) là không dấu.

Các nguyên tắc sau có thể được sử dụng để cải thiện mã có chứa phép chia số nguyên:

*   Phép chia số nguyên cho một hằng số thì nhanh hơn phép chia cho một biến. Hãy đảm bảo giá trị của số chia (divisor) được biết ở thời điểm biên dịch (compile time).
*   Phép chia số nguyên cho một hằng số sẽ nhanh hơn nếu hằng số là một lũy thừa của 2.
*   Phép chia số nguyên cho một hằng số sẽ nhanh hơn nếu số bị chia (dividend) là không dấu.

Ví dụ:

```cpp
// Ví dụ 14.10
int a, b, c;
a = b / c;                // Cách này chậm
a = b / 10;               // Chia cho một hằng số nhanh hơn
a = (unsigned int)b / 10; // Còn nhanh hơn nữa nếu không dấu
a = b / 16;               // Nhanh hơn nếu số chia là lũy thừa của 2
a = (unsigned int)b / 16; // Còn nhanh hơn nữa nếu không dấu
```

Các quy tắc tương tự áp dụng cho tính toán modulo (chia lấy dư):

```cpp
// Ví dụ 14.11
int a, b, c;
a = b % c;                // Cách này chậm
a = b % 10;               // Modulo cho một hằng số nhanh hơn
a = (unsigned int)b % 10; // Còn nhanh hơn nữa nếu không dấu
a = b % 16;               // Nhanh hơn nếu số chia là lũy thừa của 2
a = (unsigned int)b % 16; // Còn nhanh hơn nữa nếu không dấu
```

Bạn có thể tận dụng các quy tắc này bằng cách sử dụng một hằng số chia là lũy thừa của 2 nếu có thể và bằng cách đổi số bị chia thành không dấu (unsigned) nếu bạn chắc chắn rằng nó sẽ không âm.

Phương pháp mô tả ở trên vẫn có thể được sử dụng nếu giá trị của số chia không được biết tại thời điểm biên dịch, nhưng chương trình đang thực hiện phép chia lặp đi lặp lại với cùng một số chia. Trong trường hợp này, bạn phải thực hiện các tính toán cần thiết như `(2^n / b)`, v.v. tại thời điểm biên dịch. Thư viện hàm tại `www.agner.org/optimize/asmlib.zip` chứa nhiều hàm cho các tính toán này.

Có thể tránh việc chia một biến đếm vòng lặp cho một hằng số bằng cách trải vòng lặp (rolling out the loop) với cùng một hằng số đó. Ví dụ:

```cpp
// Ví dụ 14.12a
int list[300];
int i;
for (i = 0;  i < 300;  i++) {
   list[i] += i / 3;
}
```

Có thể được thay thế bằng:

```cpp
// Ví dụ 14.12b
int list[300];
int i, i_div_3;
for (i = i_div_3 = 0;  i < 300;  i += 3, i_div_3++) {
   list[i]   += i_div_3;
   list[i+1] += i_div_3;
   list[i+2] += i_div_3;
}
```

Một phương pháp tương tự có thể được sử dụng để tránh các phép toán modulo:

```cpp
// Ví dụ 14.13a
int list[300];
int i;
for (i = 0;  i < 300;  i++) {
   list[i] = i % 3;
}
```

Có thể được thay thế bằng:

```cpp
// Ví dụ 14.13b
int list[300];
int i;
for (i = 0;  i < 300;  i += 3) {
   list[i]   = 0;
   list[i+1] = 1;
   list[i+2] = 2;
}
```

Trải vòng lặp (loop unrolling) trong ví dụ 14.12b và 14.13b chỉ hoạt động nếu số đếm vòng lặp (loop count) chia hết cho hệ số trải (unroll factor). Nếu không, bạn phải thực hiện các phép toán bổ sung bên ngoài vòng lặp:

```cpp
// Ví dụ 14.13c
int list[301];
int i;
for (i = 0;  i < 301;  i += 3) {
   list[i]   = 0;
   list[i+1] = 1;
   list[i+2] = 2;
}
list[300] = 0;
```

## 14.6 Phép chia số thực (Floating point division)

Phép chia số thực tốn nhiều thời gian hơn phép cộng, phép trừ và phép nhân (20 - 45 chu kỳ xung nhịp).

Phép chia số thực cho một hằng số nên được thực hiện bằng cách nhân với số nghịch đảo của nó (reciprocal):

```cpp
// Ví dụ 14.14a
double a, b;
a = b / 1.2345;
```

Đổi thành:

```cpp
// Ví dụ 14.14b
double a, b;
a = b * (1. / 1.2345);
```

Trình biên dịch sẽ tính `(1./1.2345)` tại thời điểm biên dịch và chèn số nghịch đảo vào mã, vì vậy bạn sẽ không bao giờ mất thời gian thực hiện phép chia. Một số trình biên dịch sẽ tự động thay thế mã trong ví dụ 14.14a bằng 14.14b nhưng chỉ khi một số tùy chọn được thiết lập để nới lỏng độ chính xác của dấu phẩy động (xem trang 74). Do đó, an toàn hơn là tự thực hiện việc tối ưu hóa này một cách tường minh.

Đôi khi các phép chia có thể được loại bỏ hoàn toàn. Ví dụ:

```cpp
// Ví dụ 14.15a
if (a > b / c)
```

đôi khi có thể được thay thế bằng

```cpp
// Ví dụ 14.15b
if (a * c > b)
```

Nhưng hãy coi chừng những cạm bẫy ở đây: Dấu bất đẳng thức phải được đảo ngược nếu `c < 0`. Phép chia là không chính xác nếu `b` và `c` là số nguyên, trong khi phép nhân là chính xác.

Nhiều phép chia có thể được kết hợp. Ví dụ:

```cpp
// Ví dụ 14.16a
double y, a1, a2, b1, b2;
y = a1/b1 + a2/b2;  
```

Ở đây chúng ta có thể loại bỏ một phép chia bằng cách tạo một mẫu số chung (common denominator):

```cpp
// Ví dụ 14.16b
double y, a1, a2, b1, b2;
y = (a1*b2 + a2*b1) / (b1*b2);  
```

Thủ thuật sử dụng mẫu số chung thậm chí có thể được sử dụng trên các phép chia hoàn toàn độc lập với nhau. Ví dụ:

```cpp
// Ví dụ 14.17a
double a1, a2, b1, b2, y1, y2;
y1 = a1 / b1;
y2 = a2 / b2;
```

Có thể được đổi thành:

```cpp
// Ví dụ 14.17b
double a1, a2, b1, b2, y1, y2, reciprocal_divisor;
reciprocal_divisor = 1. / (b1 * b2);
y1 = a1 * b2 * reciprocal_divisor;
y2 = a2 * b1 * reciprocal_divisor;
```

## 14.7 Không trộn lẫn `float` và `double` (Don't mix float and double)

Các phép tính số thực dấu phẩy động thường mất lượng thời gian như nhau bất kể bạn đang sử dụng độ chính xác đơn (single precision - `float`) hay độ chính xác kép (double precision - `double`), nhưng sẽ có một khoản phạt (penalty) về hiệu năng cho việc trộn lẫn độ chính xác đơn và kép trong các chương trình được biên dịch cho hệ điều hành 64 bit và các chương trình được biên dịch cho tập lệnh SSE2 hoặc mới hơn. Ví dụ:

```cpp
// Ví dụ 14.18a
float a, b;
a = b * 1.2;       // Việc trộn lẫn float và double là không tốt
```

Tiêu chuẩn C/C++ chỉ định rằng tất cả các hằng số dấu phẩy động đều là độ chính xác kép theo mặc định, vì vậy `1.2` trong ví dụ này là một hằng số độ chính xác kép. Do đó, cần phải chuyển đổi `b` từ độ chính xác đơn sang độ chính xác kép trước khi nhân với hằng số độ chính xác kép và sau đó chuyển đổi kết quả trở lại độ chính xác đơn. Các chuyển đổi này tốn rất nhiều thời gian. Bạn có thể tránh các chuyển đổi này và làm cho đoạn mã nhanh hơn đến 5 lần, bằng cách biến hằng số thành độ chính xác đơn hoặc bằng cách biến `a` và `b` thành độ chính xác kép:

```cpp
// Ví dụ 14.18b
float a, b;
a = b * 1.2f;      // tất cả mọi thứ đều là float

// Ví dụ 14.18c
double a, b;
a = b * 1.2;       // tất cả mọi thứ đều là double
```

Không có mức phạt nào đối với việc trộn lẫn các độ chính xác của dấu phẩy động khác nhau khi mã được biên dịch cho các bộ xử lý cũ không có tập lệnh SSE2, nhưng tốt hơn là nên giữ cùng một độ chính xác trong tất cả các toán hạng để phòng trường hợp mã được chuyển sang (ported) một nền tảng khác sau này.

## 14.8 Chuyển đổi giữa số thực và số nguyên (Conversions between floating point numbers and integers)

**Chuyển đổi từ số thực sang số nguyên**
Theo tiêu chuẩn cho ngôn ngữ C++, tất cả các phép chuyển đổi từ số thực sang số nguyên đều sử dụng việc cắt xén (truncation) về phía 0, thay vì làm tròn (rounding). Điều này thật đáng tiếc bởi vì việc cắt xén tốn nhiều thời gian hơn làm tròn trừ khi tập lệnh SSE2 được sử dụng. Bạn nên kích hoạt tập lệnh SSE2 nếu có thể. SSE2 luôn được bật trong chế độ 64 bit.

Một phép chuyển đổi từ số thực sang số nguyên mà không có SSE2 thường mất khoảng 40 chu kỳ xung nhịp. Nếu bạn không thể tránh các chuyển đổi từ `float` hoặc `double` sang `int` trong phần tới hạn của mã, thì bạn có thể cải thiện hiệu quả bằng cách sử dụng làm tròn (rounding) thay vì cắt xén. Cách này nhanh hơn khoảng ba lần. Logic của chương trình có thể cần sửa đổi để bù đắp cho sự khác biệt giữa làm tròn và cắt xén.

Việc chuyển đổi hiệu quả từ `float` hoặc `double` sang số nguyên có thể được thực hiện bằng các hàm `lrintf` và `lrint`. Rất tiếc, các hàm này bị thiếu trong nhiều trình biên dịch thương mại do tranh cãi về tiêu chuẩn C99. Một bản triển khai của hàm `lrint` được đưa ra trong ví dụ 14.19 bên dưới. Hàm này làm tròn một số thực thành số nguyên gần nhất. Nếu hai số nguyên có khoảng cách bằng nhau thì số nguyên chẵn sẽ được trả về. Không có kiểm tra tràn số (overflow). Hàm này dành cho Windows 32 bit và Linux 32 bit với các trình biên dịch Microsoft, Intel và Gnu.

```cpp
// Ví dụ 14.19
static inline int lrint (double const x) { // Làm tròn tới số nguyên gần nhất 
   int n;
#if defined(__unix__) || defined(__GNUC__)
   // Linux 32-bit, Cú pháp Gnu/AT&T:
   __asm ("fldl %1 \n fistpl %0 " : "=m"(n) : "m"(x) : "memory" );
#else
   // Windows 32-bit, Cú pháp Intel/MASM:
   __asm fld qword ptr x;
   __asm fistp dword ptr n;
#endif
   return n;}
```

Mã này sẽ chỉ hoạt động trên các bộ vi xử lý tương thích với Intel/x86. Hàm này cũng có sẵn trong thư viện hàm tại `www.agner.org/optimize/asmlib.zip`.

Ví dụ sau cho thấy cách sử dụng hàm `lrint`:

```cpp
// Ví dụ 14.20
double d = 1.6;
int a, b;
a = (int)d;      // Cắt xén bị chậm. Giá trị của a sẽ là 1
b = lrint(d);    // Làm tròn thì nhanh. Giá trị của b sẽ là 2
```

Ở chế độ 64 bit hoặc khi tập lệnh SSE2 được bật, không có sự khác biệt về tốc độ giữa việc làm tròn và cắt xén. Các hàm bị thiếu có thể được triển khai như sau trong chế độ 64 bit hoặc khi tập lệnh SSE2 được bật:

```cpp
// Ví dụ 14.21.  // Chỉ dành cho SSE2 hoặc x64
#include <emmintrin.h>

static inline int lrintf (float const x) {
   return _mm_cvtss_si32(_mm_load_ss(&x));}

static inline int lrint (double const x) {
   return _mm_cvtsd_si32(_mm_load_sd(&x));}
```

Đoạn mã trong ví dụ 14.21 nhanh hơn các phương pháp làm tròn khác, nhưng không nhanh hơn cũng không chậm hơn so với phương pháp cắt xén khi tập lệnh SSE2 được bật.

**Chuyển đổi từ số nguyên sang số thực**
Chuyển đổi từ số nguyên sang số thực nhanh hơn chuyển đổi từ số thực sang số nguyên. Thời gian chuyển đổi thường là từ 5 đến 20 chu kỳ xung nhịp. Trong một số trường hợp, sẽ rất thuận lợi nếu thực hiện các phép tính số nguyên đơn giản ngay trong các biến dấu phẩy động để tránh việc phải chuyển đổi từ số nguyên sang số thực.

Chuyển đổi các số nguyên không dấu sang dấu phẩy động kém hiệu quả hơn so với các số nguyên có dấu. Sẽ hiệu quả hơn nếu chuyển các số nguyên không dấu thành số nguyên có dấu trước khi chuyển đổi thành dấu phẩy động nếu việc chuyển thành số nguyên có dấu đó không gây tràn số (overflow). Ví dụ:

```cpp
// Ví dụ 14.22a
unsigned int u;  double d;
d = u;
```

Nếu bạn chắc chắn rằng `u < 2^31` thì hãy chuyển đổi nó sang có dấu trước khi chuyển đổi sang số thực dấu phẩy động:

```cpp
// Ví dụ 14.22b
unsigned int u;  double d;
d = (double)(signed int)u;
```

## 14.9 Sử dụng các phép toán số nguyên để thao tác các biến số thực (Using integer operations for manipulating floating point variables)

Các số thực dấu phẩy động được biểu diễn bằng nhị phân theo tiêu chuẩn IEEE 754 (1985). Tiêu chuẩn này được sử dụng trong hầu hết tất cả các bộ vi xử lý và hệ điều hành hiện đại (nhưng không dùng ở một số trình biên dịch DOS rất cũ).

Việc biểu diễn `float`, `double` và `long double` phản ánh giá trị dấu phẩy động được viết dưới dạng $\pm 2^{eee} \cdot 1.fffff$, trong đó $\pm$ là dấu, $eee$ là số mũ (exponent), và $fffff$ là các số thập phân nhị phân của phần phân số (fraction). Dấu được lưu dưới dạng một bit duy nhất (là 0 cho số dương và 1 cho số âm). Số mũ được lưu dưới dạng một số nguyên nhị phân thiên vị (biased), và phần phân số được lưu dưới dạng các chữ số nhị phân. Số mũ luôn được chuẩn hóa (normalized), nếu có thể, để giá trị trước dấu thập phân là 1. Số '1' này không được đưa vào biểu diễn, ngoại trừ trong định dạng `long double`. Các định dạng có thể được biểu diễn như sau:

```cpp
struct Sfloat {
   unsigned int fraction : 23; // phần phân số
   unsigned int exponent :  8; // số mũ + 0x7F
   unsigned int sign     :  1; // bit dấu
};

struct Sdouble {
   unsigned int fraction : 52; // phần phân số
   unsigned int exponent : 11; // số mũ + 0x3FF
   unsigned int sign     :  1; // bit dấu
};

struct Slongdouble {
   unsigned int fraction : 63; // phần phân số
   unsigned int one      :  1; // luôn luôn là 1 nếu khác 0 và bình thường
   unsigned int exponent : 15; // số mũ + 0x3FFF
   unsigned int sign     :  1; // bit dấu
};
```

Giá trị của các số thực dấu phẩy động khác 0 có thể được tính như sau:

$$floatvalue = (-1)^{sign} \cdot (1 + fraction \cdot 2^{-23}) \cdot 2^{exponent - 127}$$
$$doublevalue = (-1)^{sign} \cdot (1 + fraction \cdot 2^{-52}) \cdot 2^{exponent - 1023}$$
$$longdoublevalue = (-1)^{sign} \cdot (one + fraction \cdot 2^{-63}) \cdot 2^{exponent - 16383}$$

Giá trị là 0 nếu tất cả các bit ngoại trừ bit dấu là 0. Zero có thể được biểu diễn có hoặc không có bit dấu.

Thực tế là định dạng dấu phẩy động được tiêu chuẩn hóa cho phép chúng ta thao tác trực tiếp các phần khác nhau của biểu diễn dấu phẩy động bằng cách sử dụng các phép toán số nguyên. Điều này có thể là một lợi thế vì phép toán số nguyên nhanh hơn phép toán dấu phẩy động. Bạn chỉ nên sử dụng các phương pháp này nếu bạn chắc chắn mình biết mình đang làm gì. Xem phần cuối của phần này để biết một số cảnh báo.

Chúng ta có thể thay đổi dấu của số dấu phẩy động một cách đơn giản bằng cách đảo ngược bit dấu:

```cpp
// Ví dụ 14.23
union {
   float f;
   int i;
} u;
u.i ^= 0x80000000; // đảo ngược bit dấu của u.f
```

Chúng ta có thể lấy giá trị tuyệt đối bằng cách đặt bit dấu về 0:

```cpp
// Ví dụ 14.24
union {
   float f;
   int i;
} u;
u.i &= 0x7FFFFFFF; // đặt bit dấu về 0
```
