# Tính toán Efficiency của Đơn hình (simplex) Phương pháp


<!-- PAGE 1634 -->
Là luôn luôn khả dĩ/có thể. Ngược lại, $(\gamma_{K*} )_{i}^{j} = 0$ với mọi non-slack các biến, do đó ta detected rằng phương trình thứ $i$ là redundant và ta có thể xóa nó. Khác các trình bày của bảng đơn hình (tableau) phương pháp có thể được tìm thấy trong Bertsimas và Tsitsiklis $[21]$ và Papadimitriou và Steiglitz $[139]$.

## 46.5 Tính toán Efficiency của Đơn hình (simplex) Phương pháp

Cho chúng ta kết luận với một vài comments về efficiency của thuật toán đơn hình (simplex algorithm). Trong thực tế, nó đã được quan sát bởi Dantzig rằng cho các bài toán quy hoạch tuyến tính với $m < 50$ và $m+n < 200$, đơn hình (simplex) các thuật toán typically đòi hỏi ít hơn $3m/2$ các vòng lặp, nhưng nhiều nhất 3m các vòng lặp. sự kiện này agrees với nhiều hơn/thêm recent empirical experiments với nhiều lớn hơn các bài toán quy hoạch rằng chỉ ra rằng số các vòng lặp là bị chặn bởi 3m. Do đó, nó đã là somewhat của shock trong $1972$ khi Klee và Minty tìm thấy bài toán quy hoạch tuyến tính (linear program) với $n$ các biến và $n$ các phương trình cho mà thuật toán đơn hình (simplex algorithm) với Dantzig’s phần tử trụ (pivot) quy tắc đòi hỏi đòi hỏi $2^{n}$ - $1$ các vòng lặp. Điều này bài toán quy hoạch (được lấy từ Chvatal $[40]$, trang $47)$ là reproduced ở dưới:
$$maximize \sum_{j=1}^{n}  10^{n-j}x_{j}$$
$$subject to$$
$$\begin{pmatrix} 2 & 10^{i-j}x_{j} \end{pmatrix} \sum_{j=1}^{i-1}  + x_{i} \le 100^{i-1}$$
$$x_{j} \ge 0,$$
Cho $i = 1, \dots  , n$ và $j = 1, \dots  , n$. Nếu $p =$ max(m, $n)$, thì, theo tệ hơn trường hợp behavior, với mọi currently đã biết phần tử trụ (pivot) các quy tắc, thuật toán đơn hình (simplex algorithm) có hàm mũ complexity trong $p$. Tuy nhiên, như ta được nói trước đó, trong thực tế, nasty các ví dụ chẳng hạn như Klee–Minty ví dụ dường như là rare, và số của các vòng lặp xuất hiện là tuyến tính trong $m$. Liệu có hay không phần tử trụ (pivot) quy tắc (clairvoyant quy tắc) cho mà đơn hình (simplex) các thuật toán chạy trong đa thức time theo $m$ là vẫn mở bài toán. Hirsch giả thuyết các khẳng định rằng tồn tại một phần tử trụ (pivot) quy tắc sao cho thuật toán đơn hình (simplex algorithm) tìm nghiệm tối ưu (optimal solution) trong O(p) các bước. tốt nhất cận đã biết do đó far do Kalai và Kleitman là $m^{1+lnn} = (2n)^{lnm}$. Cho nhiều hơn/thêm trên điều này topic, xem Matousek và Gardner $[127]$ (Mục 5.9) và Bertsimas và Tsitsiklis $[21]$ (Mục 3.7). Researchers có investigated bài toán của việc tìm trên các cận trên được kỳ vọng số của chọn phần tử trụ các bước nếu randomized phần tử trụ (pivot) quy tắc được sử dụng. Các cận tốt hơn hơn $2^{m}$ (nhưng của course, không đa thức) có đã được tìm thấy.
