# Tóm tắt


<!-- PAGE 733 -->
$$Figure 20.7: A weighted graph and its partition into two clusters.$$
Cách để thu được xung quanh bài toán này là đến chuẩn hóa cuts bằng cách chia bởi một số measure của mỗi tập con $A_{i}$. nghiệm bằng cách sử dụng thể tích $vol(A_{i})$ của $A_{i}$ (cho $K = 2)$ đã là proposed và investigated trong seminal paper của Shi và Malik $[166]$. Subsequently, Yu (trong her dissertation $[197])$ và Yu và Shi $[199]$ được mở rộng phương pháp đến $K > 2$ clusters. ý tưởng là để cực tiểu hóa chi phí hàm
$$Ncut(A_{1}, \dots  , A_{K}) = \sum_{i=1}^{K}  \frac{links(A_{i}\overline{, A}_{i})}{vol(A_{i})} = \sum_{i=1}^{K}  \frac{cut(A_{i})}{vol(A_{i})} .$$
Tiếp theo bước là đến biểu diễn của ta tối ưu hóa bài toán trong ma trận tạo thành, và điều này có thể được được thực hiện theo Rayleigh các tỉ số liên quan đến toán tử Laplace của đồ thị (graph Laplacian) trong numerators. Điều này lý thuyết là rất đẹp, nhưng ta thực hiện không có không gian đến trình bày nó ở đây. interested độc giả là referred đến Gallier $[75]$.

## 20.5 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ được trực tiếp các đồ thị, undirected các đồ thị. $\bullet$ Liên thuộc các ma trận, kề các ma trận. $\bullet$ được trọng số các đồ thị. $\bullet$ Ma trận bậc (degree matrix). $\bullet$ Toán tử Laplace của đồ thị (graph Laplacian) (chưa chuẩn hóa).
