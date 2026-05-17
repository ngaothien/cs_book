# 15 Siêu lập trình (Metaprogramming)

Siêu lập trình có nghĩa là tạo ra mã để tạo ra mã. Ví dụ, trong các ngôn ngữ kịch bản thông dịch (interpreted script languages), thường có thể tạo ra một đoạn mã tạo ra một chuỗi (string) và sau đó thông dịch chuỗi đó thành mã.

Siêu lập trình có thể hữu ích trong các ngôn ngữ biên dịch (compiled languages) như C++ để thực hiện một số tính toán tại thời điểm biên dịch (compile time) thay vì tại thời điểm chạy (runtime) nếu tất cả các đầu vào (inputs) cho các tính toán đều có sẵn tại thời điểm biên dịch. (Tất nhiên không có lợi thế như vậy trong các ngôn ngữ thông dịch vì mọi thứ đều diễn ra ở thời điểm chạy).

Các kỹ thuật sau đây có thể được coi là siêu lập trình trong C++:

*   **Các chỉ thị tiền xử lý (Preprocessor directives).** Ví dụ sử dụng `#if` thay vì `if`. Đây là một cách rất hiệu quả để loại bỏ các đoạn mã thừa, nhưng có những hạn chế nghiêm trọng đối với những gì bộ tiền xử lý (preprocessor) có thể làm bởi vì nó chạy trước trình biên dịch và nó chỉ hiểu các biểu thức và toán tử đơn giản nhất.
*   **Tạo một chương trình C++ sinh ra một chương trình C++ khác (hoặc một phần của nó).** Điều này có thể hữu ích trong một số trường hợp, ví dụ như để tạo ra các bảng của các hàm toán học mà bạn muốn làm các mảng tĩnh trong chương trình cuối cùng. Tất nhiên, điều này đòi hỏi bạn phải biên dịch đầu ra của chương trình thứ nhất.
*   **Trình biên dịch tối ưu hóa** có thể cố gắng làm càng nhiều càng tốt tại thời điểm biên dịch. Ví dụ, tất cả các trình biên dịch tốt sẽ rút gọn `int x = 2 * 5;` thành `int x = 10;`.
*   **Các template (khuôn mẫu) được khởi tạo (instantiated) tại thời điểm biên dịch.** Một bản sao của template (template instance) sẽ có các tham số của nó được thay thế bằng các giá trị thực tế của chúng trước khi nó được biên dịch. Đây là lý do tại sao hầu như không có chi phí (cost) nào khi sử dụng template (xem tr. 58). Có thể thể hiện bất kỳ thuật toán nào bằng template metaprogramming (siêu lập trình template), nhưng phương pháp này cực kỳ phức tạp và vụng về (clumsy), như bạn sẽ thấy ngay sau đây.

Các ví dụ sau đây giải thích cách siêu lập trình có thể được sử dụng để tăng tốc việc tính toán hàm lũy thừa (power function) khi số mũ (exponent) là một số nguyên đã biết tại thời điểm biên dịch.

```cpp
// Ví dụ 15.1a. Tính x lũy thừa 10
double xpow10(double x) {
   return pow(x,10);
}
```

Hàm `pow` sử dụng logarit trong trường hợp chung, nhưng trong trường hợp này, nó sẽ nhận ra rằng 10 là một số nguyên, nên kết quả có thể được tính toán bằng cách chỉ sử dụng các phép nhân. Thuật toán sau đây được sử dụng bên trong hàm `pow` khi số mũ là một số nguyên dương:

```cpp
// Ví dụ 15.1b. Tính lũy thừa nguyên bằng vòng lặp
double ipow (double x, unsigned int n) {
   double y = 1.0;               // dùng cho phép nhân
   while (n != 0) {              // lặp qua mỗi bit của n
      if (n & 1) y *= x;         // nhân nếu bit = 1
      x *= x;                    // bình phương x
      n >>= 1;                   // lấy bit tiếp theo của n
   }
   return y;                     // trả về y = pow(x,n)
}

double xpow10(double x) {
   return ipow(x,10);            // ipow nhanh hơn pow
}
```

Phương pháp được sử dụng trong ví dụ 15.1b sẽ dễ hiểu hơn khi chúng ta trải (roll out) vòng lặp và tổ chức lại:

```cpp
// Ví dụ 15.1c. Tính lũy thừa nguyên, vòng lặp đã trải ra
double xpow10(double x) {
   double x2  = x *x;            // x^2
   double x4  = x2*x2;           // x^4
   double x8  = x4*x4;           // x^8
   double x10 = x8*x2;           // x^10
   return x10;                   // trả về x^10
}
```

Như chúng ta có thể thấy, có thể tính toán `pow(x,10)` với chỉ bốn phép nhân. Làm thế nào để có thể đi từ ví dụ 15.1b sang 15.1c? Chúng ta đã tận dụng việc $n$ được biết tại thời điểm biên dịch để loại bỏ mọi thứ chỉ phụ thuộc vào $n$, bao gồm vòng lặp `while`, câu lệnh `if` và tất cả các phép tính số nguyên. Mã trong ví dụ 15.1c nhanh hơn 15.1b, và trong trường hợp này nó cũng có thể nhỏ hơn.

Việc chuyển đổi từ ví dụ 15.1b sang 15.1c được tôi thực hiện thủ công, nhưng nếu chúng ta muốn tạo ra một đoạn mã hoạt động cho bất kỳ hằng số thời gian biên dịch (compile-time constant) $n$ nào, thì chúng ta cần siêu lập trình. Không có trình biên dịch nào tôi đã thử nghiệm có thể chuyển đổi ví dụ 15.1a sang 15.1c một cách tự động, và chỉ có trình biên dịch Gnu sẽ chuyển đổi ví dụ 15.1b sang 15.1c. Chúng ta chỉ có thể hy vọng rằng các trình biên dịch trong tương lai sẽ tự động thực hiện các tối ưu hóa như vậy, nhưng chừng nào điều này chưa thành hiện thực, chúng ta có thể cần siêu lập trình.

Ví dụ tiếp theo cho thấy phép tính này được triển khai bằng template metaprogramming. Đừng hoảng sợ nếu bạn không hiểu nó. Tôi đưa ra ví dụ này chỉ để cho thấy template metaprogramming ngoằn ngoèo và phức tạp như thế nào.

```cpp
// Ví dụ 15.1d. Lũy thừa số nguyên sử dụng template metaprogramming

// Template cho pow(x,N) trong đó N là một hằng số nguyên dương.
// Trường hợp tổng quát, N không phải là lũy thừa của 2:
template <bool IsPowerOf2, int N>
class powN {
public:
   static double p(double x) {
   // Xóa bit 1 ngoài cùng bên phải trong biểu diễn nhị phân của N:
   #define N1 (N & (N-1))
      return powN<(N1&(N1-1))==0,N1>::p(x) * powN<true,N-N1>::p(x);
   #undef N1
   }
};

// Partial template specialization (đặc tả template một phần) cho N là lũy thừa của 2
template <int N>
class powN<true,N> {
public:
   static double p(double x) {
      return powN<true,N/2>::p(x) * powN<true,N/2>::p(x);
   }
};

// Full template specialization (đặc tả template đầy đủ) cho N = 1. Điều này kết thúc đệ quy
template<>
class powN<true,1> {
public:
   static double p(double x) {
      return x;
   }
};

// Full template specialization cho N = 0
// Điều này chỉ được dùng để tránh lặp vô hạn nếu powN bị
// gọi nhầm với IsPowerOf2 = false trong khi nó đáng ra phải là true.
template<>
class powN<true,0> {
public:
   static double p(double x) {
      return 1.0;
   }
};

// Function template cho x lũy thừa N
template <int N>
static inline double IntegerPower (double x) {
   // (N & N-1)==0 nếu N là lũy thừa của 2
   return powN<(N & N-1)==0,N>::p(x);
}

// Dùng template để tính x lũy thừa 10
double xpow10(double x) {
   return IntegerPower<10>(x);
}
```

Nếu bạn muốn biết mã này hoạt động như thế nào, đây là phần giải thích. Vui lòng bỏ qua phần giải thích sau đây nếu bạn không chắc là mình cần nó.

Trong C++ template metaprogramming, các vòng lặp được triển khai dưới dạng các template đệ quy (recursive templates). Template `powN` đang tự gọi chính nó để giả lập vòng lặp `while` trong ví dụ 15.1b. Việc rẽ nhánh (Branches) được triển khai bằng đặc tả template (một phần) - partial template specialization. Đây là cách rẽ nhánh `if` trong ví dụ 15.1b được triển khai. Sự đệ quy phải luôn kết thúc bằng một template specialization không đệ quy, chứ không phải bằng một sự rẽ nhánh bên trong template.

Template `powN` là một class template thay vì một function template bởi vì partial template specialization chỉ được cho phép đối với các class. Việc chia nhỏ `N` thành các bit riêng lẻ trong biểu diễn nhị phân của nó là đặc biệt phức tạp (tricky). Tôi đã sử dụng thủ thuật `N1 = N&(N-1)` để lấy giá trị của N với bit 1 ngoài cùng bên phải đã được loại bỏ. Nếu N là lũy thừa của 2 thì `N&(N-1)` bằng 0. Hằng số `N1` có thể được định nghĩa bằng các cách khác ngoài dùng macro, nhưng phương pháp được sử dụng ở đây là cách duy nhất hoạt động trên tất cả các trình biên dịch mà tôi đã thử nghiệm.

Các trình biên dịch Microsoft, Intel và Gnu trên thực tế đang rút gọn ví dụ 15.1d thành 15.1c như dự định, trong khi trình biên dịch Borland và Digital Mars tạo ra đoạn mã kém tối ưu hơn vì chúng thất bại trong việc loại bỏ các biểu thức con phổ biến (common sub-expressions).

Tại sao template metaprogramming lại phức tạp đến vậy? Bởi vì tính năng template của C++ chưa bao giờ được thiết kế cho mục đích này. Nó chỉ tình cờ là có thể làm được. Template metaprogramming phức tạp đến mức tôi cho rằng sử dụng nó là không khôn ngoan. Mã phức tạp tự nó là một yếu tố rủi ro, và chi phí để xác minh (verifying), gỡ lỗi (debugging) và bảo trì loại mã như vậy cao đến mức hiếm khi bào chữa (justifies) được cho phần hiệu suất đạt được tương đối nhỏ.

Tuy nhiên, có những trường hợp mà template metaprogramming là cách duy nhất để đảm bảo rằng các tính toán nhất định được thực hiện tại thời điểm biên dịch. (Các ví dụ có thể được tìm thấy trong thư viện vector class của tôi).

Ngôn ngữ D cho phép các câu lệnh `if` tại thời điểm biên dịch (được gọi là `static if`), nhưng không có các vòng lặp tại thời điểm biên dịch hoặc việc sinh ra các tên định danh (identifier names) tại thời điểm biên dịch. Chúng ta chỉ có thể hy vọng rằng tính năng như vậy sẽ có sẵn trong tương lai. Nếu một phiên bản tương lai của C++ cho phép các vòng lặp `while` và `if` tại thời điểm biên dịch, thì việc chuyển đổi từ ví dụ 15.1b sang siêu lập trình sẽ rất đơn giản. Hợp ngữ MASM (MASM assembly language) có các tính năng siêu lập trình đầy đủ, bao gồm cả khả năng định nghĩa tên hàm và tên biến bằng macro từ các hàm chuỗi. Một bản triển khai siêu lập trình tương tự như ví dụ 15.1b và d bằng hợp ngữ được cung cấp như một ví dụ trong chương "Vòng lặp Macro" (Macro loops) trong tài liệu 2: "Tối ưu hóa chương trình con bằng hợp ngữ".

Trong khi chờ đợi các công cụ siêu lập trình tốt hơn khả dụng, chúng ta có thể chọn các trình biên dịch tốt nhất trong việc thực hiện các phép rút gọn (reductions) tương đương theo sáng kiến riêng của chúng bất cứ khi nào có thể. Một trình biên dịch tự động rút gọn ví dụ 15.1a thành 15.1c tất nhiên sẽ là giải pháp dễ dàng nhất và đáng tin cậy nhất. (Trong các thử nghiệm của tôi, trình biên dịch Intel đã rút gọn 15.1a thành một 15.1b nội tuyến (inlined) và trình biên dịch Gnu đã rút gọn 15.1b thành 15.1c, nhưng không có trình biên dịch nào rút gọn 15.1a thành 15.1c).
