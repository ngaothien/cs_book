# Các bài tập


<!-- PAGE 689 -->
$\bullet$ Unreduced và rút gọn Hessenberg các ma trận. $\bullet$ Deflation. $\bullet$ Shift. $\bullet$ Wilkinson shift. $\bullet$ Gấp đôi shift. $\bullet$ Francis shift. $\bullet$ Ẩn shifting. $\bullet$ Ẩn Q-theorem. $\bullet$ Phép lặp Arnoldi (Arnoldi iteration). $\bullet$ Breakdown của Phép lặp Arnoldi (Arnoldi iteration). $\bullet$ Krylov không gian con. $\bullet$ Rayleigh–Ritz phương pháp. $\bullet$ Ritz các giá trị, Arnoldi estimates. $\bullet$ Phần dư (residual). $\bullet$ GMRES $\bullet$ Phép lặp Lanczos (Lanczos iteration). $\bullet$ Lũy thừa vòng lặp. $\bullet$ Nghịch đảo lũy thừa vòng lặp. $\bullet$ Rayleigh tỉ số.

## 18.9 Các bài tập

Bài toán 18.1. Chứng minh Định lý 18.2; xem Bài toán 13.7.
Bài toán 18.2. Chứng minh rằng nếu ma trận $A$ là Hermite (hoặc thực đối xứng), thì bất kỳ Ma trận Hessenberg $H$ đồng dạng đến $A$ là Hermite ba đường chéo (thực đối xứng ba đường chéo).
Bài toán 18.3. Với mọi ma trận (thực hoặc phức) $A$, nếu $A = QR$ là Phân rã QR (QR-decomposition) của $A$ bằng cách sử dụng Householder các phép đối xứng, chứng minh rằng nếu $A$ là trên Hessenberg thì do đó là $Q$.

<!-- PAGE 690 -->
Bài toán 18.4. Chứng minh rằng nếu $A$ là trên Hessenberg, thì các ma trận $A_{k}$ thu được bằng cách áp dụng QR-algorithm là cũng trên Hessenberg.
Bài toán 18.5. Chứng minh ẩn $Q$ định lý. định lý này nói rằng rằng nếu $A$ là rút gọn đến trên Hessenberg tạo thành như $A = UHU^{*}$ và nếu $H$ là unreduced $(h_{i+1i} \neq  0$ cho $i = 1, \dots  , n -1)$, thì các cột của chỉ số $2, \dots  , n$ của $U$ được xác định bởi cột thứ nhất của $U$ sai khác dấu;
Bài toán 18.6. Read Mục 7.5 của Golub và Van Loan $[83]$ và cài đặt của chúng phiên bản của QR-algorithm với shifts.
Bài toán 18.7. Nếu Phép lặp Arnoldi (Arnoldi iteration) có breakdown tại giai đoạn $n$, nghĩa là, $h_{n+1} = 0$, thì ta tìm thấy thứ nhất unreduced khối của Ma trận Hessenberg $H$. Chứng minh rằng các trị riêng (eigenvalues) của $H_{n}$ là các trị riêng (eigenvalues) của $A$.
Bài toán 18.8. Chứng minh Định lý 18.6.
Bài toán 18.9. Cài đặt GRMES và test nó trên một số các hệ phương trình tuyến tính.
Bài toán 18.10. Phát biểu và chứng minh các phiên bản của Mệnh đề 18.5 và Định lý 18.6 cho Phép lặp Lanczos (Lanczos iteration).
Bài toán 18.11. Chứng minh các kết quả về lũy thừa vòng lặp phương pháp được phát biểu trong Mục 18.7.
Bài toán 18.12. Chứng minh các kết quả về nghịch đảo lũy thừa vòng lặp phương pháp được phát biểu trong Mục 18.7.
Bài toán 18.13. Cài đặt và test lũy thừa vòng lặp phương pháp và nghịch đảo lũy thừa vòng lặp phương pháp.
Bài toán 18.14. Read Lecture $27$ trong Trefethen và Bau $[182]$ và cài đặt và test Rayleigh thương vòng lặp phương pháp.
