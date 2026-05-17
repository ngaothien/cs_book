# 18 Tổng quan về các tùy chọn của trình biên dịch (Overview of compiler options)

Bảng 18.1. Các tùy chọn dòng lệnh (command line options) liên quan đến tối ưu hóa

| | Trình biên dịch MS (Windows) | Trình biên dịch Gnu (Linux) | Trình biên dịch Intel (Windows) | Trình biên dịch Intel (Linux) |
|---|---|---|---|---|
| Tối ưu hóa cho tốc độ (Optimize for speed) | `/O2` hoặc `/Ox` | `-O3` hoặc `-Ofast` | `/O3` | `-O3` |
| Tối ưu hóa liên thủ tục (Interprocedural optimization) | `/Og` | | | |
| Tối ưu hóa toàn chương trình (Whole program optimization) | `/GL` | `--combine`, `-fwhole-program` | `/Qipo` | `-ipo` |
| Không xử lý ngoại lệ (No exception handling) | `/EHs-` | | | |
| Không dùng khung ngăn xếp (No stack frame) | `/Oy` | `-fomit-frame-pointer` | | `-fomit-frame-pointer` |
| Không nhận dạng kiểu tại thời điểm chạy (No RTTI) | `/GR-` | `-fno-rtti` | `/GR-` | `-fno-rtti` |
| Giả định không có bí danh con trỏ (Assume no pointer aliasing) | `/Oa` | | | `-fno-alias` |
| Phép toán dấu phẩy động không nghiêm ngặt (Non-strict floating point) | | `-ffast-math` | `/fp:fast`, `/fp:fast=2` | `-fp-model fast`, `-fp-model fast=2` |
| Các con trỏ thành viên đơn giản (Simple member pointers) | `/vms` | | | |
| Các hàm Fastcall | `/Gr` | | | |
| Liên kết mức hàm (Function level linking - loại bỏ hàm không được tham chiếu) | `/Gy` | `-ffunction-sections` | `/Gy` | `-ffunction-sections` |
| Tập lệnh SSE (vector float 128 bit) | `/arch:SSE` | `-msse` | `/arch:SSE` | `-msse` |
| Tập lệnh SSE2 (vector số nguyên hoặc double 128 bit) | `/arch:SSE2` | `-msse2` | `/arch:SSE2` | `-msse2` |
| Tập lệnh SSE3 | | `-msse3` | `/arch:SSE3` | `-msse3` |
| Tập lệnh Suppl. SSE3 | | `-mssse3` | `/arch:SSSE2` | `-mssse3` |
| Tập lệnh SSE4.1 | | `-msse4.1` | `/arch:SSE4.1` | `-msse4.1` |
| Tập lệnh AVX | `/arch:AVX` | `-mAVX` | `/arch:AVX` | `-mAVX` |
| Tự động điều phối CPU (Automatic CPU dispatch) | | | `/QaxSSE3`, v.v. (Chỉ cho CPU Intel) | `-axSSE3`, v.v. (Chỉ cho CPU Intel) |
| Tự động véc-tơ hóa (Automatic vectorization) | | `-O3` hoặc tốt hơn: `-Ofast -mveclibabi` | (không yêu cầu tùy chọn cụ thể) | (không yêu cầu tùy chọn cụ thể) |
| Tự động song song hóa (Automatic parallelization) bằng đa luồng | | | `/Qparallel` | `-parallel` |
| Song song hóa bằng các chỉ thị OpenMP | `/openmp` | `-fopenmp` | `/Qopenmp` | `-openmp` |
| Mã 32 bit | | `-m32` | | |
| Mã 64 bit | | `-m64` | | |
| Liên kết tĩnh (Static linking - đa luồng) | `/MT` | `-static` | `/MT` | `-static` |
| Sinh tệp tin liệt kê hợp ngữ (Generate assembly listing) | `/FA` | `-S -masm=intel` | `/FA` | `-S` |
| Sinh tệp tin bản đồ (Generate map file) | `/Fm` | | | |
| Sinh báo cáo tối ưu hóa (Generate optimization report) | | | `/Qopt-report` | `-opt-report` |


Bảng 18.2. Các chỉ thị trình biên dịch và từ khóa liên quan đến tối ưu hóa

| | Trình biên dịch MS (Windows) | Trình biên dịch Gnu (Linux) | Trình biên dịch Intel (Windows) | Trình biên dịch Intel (Linux) |
|---|---|---|---|---|
| Căn lề theo byte thứ 16 (Align by 16) | `__declspec(align(16))` | `__attribute((aligned(16)))` | `__declspec(align(16))` | `__attribute((aligned(16)))` |
| Giả định con trỏ được căn lề (Assume pointer is aligned) | | | `#pragma vector aligned` | `#pragma vector aligned` |
| Giả định con trỏ không có bí danh (Assume pointer not aliased) | `#pragma optimize("a", on)`, `__restrict` | `__restrict` | `__declspec(noalias)`, `__restrict`, `#pragma ivdep` | `__restrict`, `#pragma ivdep` |
| Giả định hàm là thuần túy (Assume function is pure) | | `__attribute((const))` | | `__attribute((const))` |
| Giả định hàm không ném ngoại lệ (Assume function does not throw exceptions) | `throw()` | `throw()` | `throw()` | `throw()` |
| Giả định hàm chỉ được gọi từ cùng một module | `static` | `static` | `static` | `static` |
| Giả định hàm thành viên chỉ được gọi từ cùng một module | | `__attribute__((visibility("internal")))` | | `__attribute__((visibility("internal")))` |
| Véc-tơ hóa (Vectorize) | | | `#pragma vector always` | `#pragma vector always` |
| Tối ưu hóa hàm | `#pragma optimize(...)` | | | |
| Hàm Fastcall | `__fastcall` | `__attribute((fastcall))` | `__fastcall` | |
| Ghi không lưu trữ (Noncached write) | | | `#pragma vector nontemporal` | `#pragma vector nontemporal` |


Bảng 18.3. Các macro được định nghĩa sẵn (Predefined macros)

| | Trình biên dịch MS (Windows) | Trình biên dịch Gnu (Linux) | Trình biên dịch Intel (Windows) | Trình biên dịch Intel (Linux) |
|---|---|---|---|---|
| Nhận dạng trình biên dịch (Compiler identification) | `_MSC_VER` và không có `__INTEL_COMPILER` | `__GNUC__` và không có `__INTEL_COMPILER` | `__INTEL_COMPILER` | `__INTEL_COMPILER` |
| Nền tảng 16 bit | không có `_WIN32` | n.a. | n.a. | n.a. |
| Nền tảng 32 bit | không có `_WIN64` | | không có `_WIN64` | |
| Nền tảng 64 bit | `_WIN64` | `_LP64` | `_WIN64` | `_LP64` |
| Nền tảng Windows | `_WIN32` | | `_WIN32` | |
| Nền tảng Linux | n.a. | `__unix__`, `__linux__` | | `__unix__`, `__linux__` |
| Nền tảng x86 | `_M_IX86` | | `_M_IX86` | |
| Nền tảng x86-64 | `_M_IX86` và `_WIN64` | | `_M_X64` | `_M_X64` |
