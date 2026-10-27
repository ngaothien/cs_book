# Cơ bản QR Thuật toán


<!-- PAGE 663 -->
Hơn $m)$ ý tưởng là đến sinh $n \times  n$ Hessenberg ma trận con $H_{n}$ của đầy đủ Ma trận Hessenberg $H$ (sao cho $A = UHU^{*}$) bao gồm của của nó thứ nhất $n$ các hàng và $n$ các cột; ma trận $U_{n}$ bao gồm của thứ nhất $n$ các cột của $U$ là cũng produced. Rayleigh–Ritz phương pháp bao gồm trong việc tính toán các trị riêng (eigenvalues) của $H_{n}$ bằng cách sử dụng QR- phương pháp với shifts. các trị riêng (các trị riêng (eigenvalues)) này, được gọi là Ritz các giá trị, là các xấp xỉ của các trị riêng (eigenvalues) của $A$. Typically, extreme các trị riêng (eigenvalues) là tìm thấy thứ nhất. Phép lặp Arnoldi (Arnoldi iteration) có thể cũng được quan điểm như cách của việc tính toán cơ sở trực chuẩn (orthonormal basis) của Krylov không gian con, cụ thể là $subspace\mathcal{K}_{n}(A, b)$ được sinh (spanned) bởi $(b$, Ab, $\dots  , A^{n}b)$. Ta có thể cũng sử dụng Phép lặp Arnoldi (Arnoldi iteration) để tìm xấp xỉ nghiệm của phương trình tuyến tính Ax $= b$ bởi cực tiểu hóa $\|b$ - $Ax_{n}\|_{2}$ với mọi $x_{n}$ là Krylov $space\mathcal{K}_{n}(A, b)$. phương pháp này named GMRES được thảo luận trong Mục 18.5. đặc biệt trường hợp ở đâu $H$ là đối xứng (hoặc Hermite) ma trận ba đường chéo (tridiagonal matrix) được thảo luận trong Mục 18.6. Trong trường hợp này, Arnoldi’s thuật toán trở thành Lanczos’ thuật toán. Nó là nhiều nhiều hơn/thêm efficient hơn Phép lặp Arnoldi (Arnoldi iteration). Ta close điều này chương bởi thảo luận hai cổ điển các phương pháp cho việc tính toán đơn lẻ vectơ riêng (eigenvector) và đơn lẻ trị riêng (eigenvalue): lũy thừa vòng lặp và nghịch đảo (lũy thừa) vòng lặp; xem Mục 18.7.

## 18.1 Cơ bản QR Thuật toán

Cho $A$ là một ma trận cỡ $n \times  n$ mà được giả sử là chéo hóa được (diagonalizable) và khả nghịch. cơ bản QR thuật toán làm cho sử dụng của hai rất đơn giản các bước. Bắt đầu với $A_{1} = A$, ta xây dựng các dãy của các ma trận $(A_{k}), (Q_{k}) (R_{k})$ và $(P_{k})$ như sau:
$$FactorA_{1} = Q_{1}R_{1}$$
$$SetA_{2} = R_{1}Q_{1}$$
$$FactorA_{2} = Q_{2}R_{2}$$
$$SetA_{3} = R_{2}Q_{2}$$
$$\vdots$$
$$FactorA_{k} = Q_{k}R_{k}$$
$$SetA_{k+1} = R_{k}Q_{k}$$
$$\vdots$$
Do đó, $A_{k+1}$ là thu được từ Nhân tử hóa QR (QR-factorization) $A_{k} = Q_{k}R_{k}$ của $A_{k}$ bởi swapping $Q_{k}$ và $R_{k}$. Định nghĩa $P_{k}$ bởi
$$P_{k} = Q_{1}Q_{2} \cdots  Q_{k}.$$
Vì $A_{k} = Q_{k}R_{k}$, ta có $R_{k} = Q_{k}^{*}A_{k}$, và vì $A_{k+1} = R_{k}Q_{k}$, ta thu được
$$A_{k+1} = Q_{k}^{*}A_{k}Q_{k}.(*_{1})$$

<!-- PAGE 664 -->
Hiển nhiên quy nạp chỉ ra rằng
$$A_{k+1} = Q_{k}^{*} \cdots  Q_{1}^{*}A_{1}Q_{1} \cdots  Q_{k} = P_{k}^{*} AP_{k},$$
Rằng là
$$A_{k+1} = P_{k}^{*}  AP_{k}.(*_{2})$$
Vì vậy, $A_{k+1}$ và $A$ là đồng dạng, do đó chúng có cùng các trị riêng (eigenvalues). cơ bản QR vòng lặp phương pháp bao gồm trong việc tính toán dãy của các ma trận $A_{k}$, và trong lý tưởng (ideal) tình huống, đến kỳ vọng rằng $A_{k}$ “hội tụ” đến tam giác trên (upper triangular) ma trận, chính xác hơn rằng phần của $A_{k}$ ở dưới chính đường chéo đi đến không, và đường chéo các phần tử (entries) hội tụ đến các trị riêng (eigenvalues) của $A$. lý tưởng (lý tưởng (ideal)) này tình huống là chỉ đạt được trong khá đặc biệt các trường hợp. Cho một thing, nếu $A$ là unita (hoặc trực giao trong thực trường hợp), vì trong QR phân rã ta có $R =$ I, ta thu được $A_{2} = IQ = Q = A_{1}$, do đó phương pháp thực hiện không tạo bất kỳ progress. Cũng, nếu $A$ là thực ma trận, vì $A_{k}$ là cũng thực, nếu $A$ có phức các trị riêng (eigenvalues), thì phần của $A_{k}$ ở dưới chính đường chéo có thể’t đi đến không. một cách tổng quát, phương pháp chạy vào troubles bất cứ khi nào $A$ có phân biệt các trị riêng (eigenvalues) với cùng môđun/độ lớn. sự hội tụ của dãy $(A_{k})$ là chỉ đã biết dưới một số fairly restrictive các giả thiết. Chẵn/ngay cả dưới như vậy các giả thiết, điều này là không một cách thực genuine sự hội tụ. Thật vậy, nó có thể được được hiển thị rằng phần của $A_{k}$ ở dưới chính đường chéo đi đến không, và đường chéo các phần tử (entries) hội tụ đến các trị riêng (eigenvalues) của $A$, nhưng phần của $A_{k}$ ở trên đường chéo có thể không hội tụ. Tuy nhiên, cho mục đích của việc tìm các trị riêng (eigenvalues) của $A$, điều này thực hiện không matter. sau đây sự hội tụ kết quả được chứng minh trong Ciarlet $[41]$ (Chương $6$, Định lý 6.3.10 và Serre $[162]$ (Chương $13$, Định lý 13.2). Nó là rarely applicable trong thực tế, ngoại trừ cho đối xứng (hoặc Hermite) xác định dương (positive definite) các ma trận, như ta sẽ xem một cách ngắn.

> **Định lý 18.1.** Giả sử (phức) $n\times n$ ma trận $A$ là khả nghịch, chéo hóa được (diagonalizable), và rằng của nó các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{n}$ có khác nhau moduli, sao cho
$$|\lambda_{1} | > |\lambda_{2} | > \cdots  > |\lambda_{n} | > 0.$$
Nếu $A = P\Lambda P^{-1}$, ở đâu $\Lambda  = diag(\lambda_{1} , \dots  , \lambda_{n}$), và nếu $P^{-1}$ có Nhân tử hóa LU (LU-factorization), thì chặt tam giác dưới (lower-triangular) phần của $A_{k}$ hội tụ đến không, và đường chéo của $A_{k}$ hội tụ đến $\Lambda$.

*Chứng minh.* Ta reproduce chứng minh trong Ciarlet $[41]$ (Chương $6$, Định lý 6.3.10). chiến lược là đến study asymptotic behavior của các ma trận $P_{k} = Q_{1}Q_{2} \cdots  Q_{k}$. Cho điều này, hóa ra là ta cần đến xét các lũy thừa $A^{k}$. Bước $1$. Cho $\mathcal{R}_{k} = R_{k} \cdots  R_{2}R_{1}$. Ta khẳng định rằng
$$A^{k}= (Q_{1}Q_{2} \cdots  Q_{k})(R_{k} \cdots  R_{2}R_{1}) = P_{k}\mathcal{R}_{k}.(*_{3})$$

<!-- PAGE 665 -->
Ta tiến hành bởi quy nạp. base trường hợp $k = 1$ là tầm thường. Cho quy nạp bước, từ $(*_{2})$, ta có
$$P_{k}A_{k+1} = AP_{k}.$$
Vì $A_{k+1} = R_{k}Q_{k} = Q_{k+1}R_{k+1}$, ta có
$$P_{k+1}\mathcal{R}_{k+1} = P_{k}Q_{k+1}R_{k+1}\mathcal{R}_{k} = P_{k}A_{k+1}\mathcal{R}_{k} = AP_{k}\mathcal{R}_{k} = AA^{k}= A^{k+1}$$
Thiết lập quy nạp bước. Bước $2$. Ta sẽ biểu diễn ma trận $P_{k}$ như $P_{k} = QQ_{k}D_{k}$, theo ma trận đường chéo (diagonal matrix)
$$e$$
$D_{k}$ với unit các phần tử (entries), với $Q$ và $Q_{k}$ unita.
$$e$$
Cho $P = QR$, Nhân tử hóa QR (QR-factorization) của $P$ (với $R$ tam giác trên (upper triangular) ma trận với dương đường chéo các phần tử (entries)), và $P^{-1} = LU$, Nhân tử hóa LU (LU-factorization) của $P^{-1}$. Vì $A = P\Lambda P^{-1}$, ta có
$$A^{k}= P\Lambda^{k} P^{-1}= QR\Lambda^{k} LU = QR(\Lambda^{k} L\Lambda^{-k} )\Lambda^{k} U.(*_{4})$$
Ở đây, $\Lambda^{-k}$ là ma trận đường chéo (diagonal matrix) với các phần tử (entries) $\lambda_{i}^{-k}$. lý do cho giới thiệu ma trận $\Lambda^{k} L\Lambda^{-k}$ là rằng của nó asymptotic behavior là dễ để xác định. Thật vậy, ta có
$$0if i < j$$
$$$$
$$$$
$$1if i = j$$
$$$$
$$(\Lambda^{k} L\Lambda^{-k} )_{ij} =$$
$$L_{ij}if i > j.$$
$$ \begin{pmatrix} \lambda_{i}^{k} \\ \lambda_{j} \end{pmatrix}$$
Giả thiết rằng $|\lambda_{1}$ | $> |\lambda_{2}$ | $> \cdots  > |\lambda_{n}$ | $> 0$ suy ra rằng
$$lim\Lambda^{k} L\Lambda^{-k} = I.(\dagger )$$
$$k\mapsto \infty$$
Lưu ý rằng nó là để thu được điều này giới hạn rằng ta được tạo giả thiết trên moduli của các trị riêng (eigenvalues). Ta có thể viết
$$\Lambda^{k} L\Lambda^{-k} = I + F_{k},withlimF_{k} = 0,$$
$$k\mapsto \infty$$
Và hệ quả là, vì $R(\Lambda^{k} L\Lambda^{-k}$) $=$ R(I $+ F_{k}) = R + RF_{k}R^{-1}R =$ (I $+ RF_{k}R^{-1})R$, ta có
$$R(\Lambda^{k} L\Lambda^{-k} ) = (I + RF_{k}R^{-1})R.(*_{5})$$
Theo Mệnh đề 9.12(1), vì $lim_{k\mapsto \infty} F_{k} = 0$, và do đó $lim_{k\mapsto \infty} RF_{k}R^{-1} = 0$, các ma trận I $+ RF_{k}R^{-1}$ là khả nghịch cho $k$ lớn đủ. Hệ quả là cho $k$ lớn đủ, ta có Nhân tử hóa QR (QR-factorization)
$$I + RF_{k}R^{-1}=Q_{k}R_{k},(*_{6})$$
$$ee$$
$$e$$
Với $(R_{k})_{ii} > 0$ cho $i = 1, \dots  , n$. Vì các ma trận $Q_{k}$ là unita, ta có $Q_{k}  = 1, e  e$
$$2$$
Do đó dãy $(Q_{k})$ là bị chặn. Suy ra rằng nó có convergent dãy con $(Q_{\ell})$ rằng
$$e e$$
Hội tụ đến một số ma trận $Q$, mà là cũng unita. Vì
$$e$$
$$R_{\ell}= (Q_{\ell})^{*}(I + RF_{\ell}R^{-1}),$$
$$e e$$

<!-- PAGE 666 -->
Ta suy ra rằng dãy con $(R_{\ell})$ cũng hội tụ đến một số ma trận $R$, mà là cũng trên
$$e e$$
Tam giác với dương đường chéo các phần tử (entries). Bởi chuyển đến giới hạn (bằng cách sử dụng các dãy con), ta thu được $R = (Q)^{*}$, nghĩa là, $e  e$
$$I =QR.$$
$$e e$$
Bởi tính duy nhất của Phân rã QR (QR-decomposition) (khi đường chéo các phần tử (entries) của $R$ là dương), ta thu được
$$Q =R = I.$$
$$e e$$
Vì ở trên lập luận áp dụng đến bất kỳ các dãy con của $(Q_{k})$ và $(R_{k})$, bởi tính duy nhất
$$e e$$
Của các giới hạn, ta kết luận rằng “đầy đủ” các dãy $(Q_{k})$ và $(R_{k})$ hội tụ:
$$e e$$
$$limQ_{k} = I,limR_{k} = I.$$
$$ee$$
$$k\mapsto \infty k\mapsto \infty$$
Vì bởi $(*_{4})$,
$$A^{k}= QR(\Lambda^{k} L\Lambda^{-k} )\Lambda^{k} U,$$
Bởi $(*_{5})$,
$$R(\Lambda^{k} L\Lambda^{-k} ) = (I + RF_{k}R^{-1})R,$$
Và bởi $(*_{6})$
$$I + RF_{k}R^{-1}=Q_{k}R_{k},$$
$$ee$$
Ta được chứng minh rằng
$$A^{k}= (QQ_{k})(R_{k}R\Lambda^{k} U).(*_{7})$$
$$e e$$
Nhận thấy rằng $QQ_{k}$ là ma trận unita (unitary matrix), và $R_{k}R\Lambda^{k} U$ là tam giác trên (upper triangular) ma trận, như
$$e e$$
Tích của tam giác trên (upper triangular) các ma trận. Tuy nhiên, một số các phần tử (entries) trong $\Lambda$ có thể là âm, do đó ta có thể’t khẳng định rằng $R_{k}R\Lambda^{k} U$ có dương đường chéo các phần tử (entries). Tuy nhiên, ta có một cái khác
$$e$$
Phân rã QR (QR-decomposition) của $A^{k}$,
$$A^{k}= (QQ_{k})(R_{k}R\Lambda^{k} U) = P_{k}\mathcal{R}_{k}.$$
$$e e$$
Nó là dễ để chứng minh rằng ở đó là ma trận đường chéo (diagonal matrix) $D_{k}$ với $|(D_{k})_{ii}| = 1$ cho $i = 1, \dots  , n$, sao cho
$$P_{k} = QQ_{k}D_{k}.(*_{8})$$
$$e$$
Sự tồn tại của $D_{k}$ là hệ quả của sau đây sự kiện: Nếu ma trận khả nghịch (invertible matrix) $B$ có hai QR các nhân tử hóa $B = Q_{1}R_{1} = Q_{2}R_{2}$, thì có một ma trận đường chéo (diagonal matrix) $D$ với unit các phần tử (entries) sao cho $Q_{2} = DQ_{1}$. biểu thức cho $P_{k}$ trong $(*_{8})$ là rằng mà ta đã là seeking. Bước $3$. Asymptotic behavior của các ma trận $A_{k+1} = P_{k}^{*}  AP_{k}$. Vì $A = P\Lambda P^{-1} = QR\Lambda R^{-1}Q^{-1}$ và bởi $(*_{8}), P_{k} = QQ_{k}D_{k}$, ta thu được
$$e$$
$$A_{k+1} = D_{k}^{*}(Q_{k})^{*}Q^{*}QR\Lambda R^{-1}Q^{-1}QQ_{k}D_{k} = D_{k}^{*}(Q_{k})^{*}R\Lambda R^{-1}Q_{k}D_{k}.(*_{9})$$
$$e e e e$$

<!-- PAGE 667 -->
Vì $lim_{k\mapsto \infty} Q_{k} =$ I, ta suy ra rằng
$$e$$
$$lim(Q_{k} e)^{*}R\Lambda R^{-1} eQ_{k} = R\Lambda R^{-1} = \begin{pmatrix} \lambda_{1} & * & \cdots & * \\ 0 & \lambda_{2} & \cdots & * \\ \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_{n} \end{pmatrix} ,$$
$$k\mapsto \infty$$
Tam giác trên (upper triangular) ma trận với các trị riêng (eigenvalues) của $A$ trên đường chéo. Vì $R$ là tam giác trên (upper triangular), thứ tự của các trị riêng (eigenvalues) được bảo toàn. Nếu ta cho
$$\mathcal{D}_{k} = (Q_{k})^{*}R\Lambda R^{-1}Q_{k},(*_{10})$$
$$e e$$
Thì bởi $(*_{9})$ ta có $A_{k+1} = D_{k}^{*}\mathcal{D}_{k}D_{k}$, và vì các ma trận $D_{k}$ là các ma trận đường chéo, ta có
$$(A_{k+1})_{jj} = (D_{k}^{*}\mathcal{D}_{k}D_{k})_{ij} \overline{= (}\overline{D}_{k}\overline{)}_{ii}(D_{k})_{jj}(\mathcal{D}_{k})_{ij},$$
Mà suy ra rằng
$$(A_{k+1})_{ii} = (\mathcal{D}_{k})_{ii},i = 1, \dots  , n,(*_{11})$$
Vì $|(D_{k})_{ii}| = 1$ cho $i = 1, \dots  , n$. Vì $lim_{k\mapsto \infty} \mathcal{D}_{k} = R\Lambda R^{-1}$, ta kết luận rằng chặt tam giác dưới (lower-triangular) phần của $A_{k+1}$ hội tụ đến không, và đường chéo của $A_{k+1}$ hội tụ đến $\Lambda$. Nhận thấy rằng nếu ma trận $A$ là thực, thì giả thiết rằng các trị riêng (eigenvalues) có phân biệt moduli suy ra rằng các trị riêng (eigenvalues) là tất cả thực và đơn giản. sau đây Matlab bài toán quy hoạch các cài đặt cơ bản QR-method bằng cách sử dụng hàm qrv4 từ Mục 12.8. hàm $T =$ qreigen(,m) $T = A$; cho $k =$ 1:m $[Q R] =$ qrv4(T); $T =$ R*Q; kết thúc/cuối kết thúc/cuối

> **Ví dụ 18.1.** Nếu ta chạy hàm qreigen với $100$ các vòng lặp trên $8 \times  8$ ma trận đối xứng (symmetric matrix)
$$A = \begin{pmatrix} 4 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 1 & 4 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 4 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 4 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 4 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 4 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 & 4 & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 4 \end{pmatrix} ,$$

<!-- PAGE 668 -->
Ta tìm ma trận
$$T = \begin{pmatrix} 5.8794 & 0.0015 & 0.0000 & -0.0000 & 0.0000 & -0.0000 & 0.0000 & -0.0000 \\ 0.0015 & 5.5321 & 0.0001 & 0.0000 & -0.0000 & 0.0000 & 0.0000 & 0.0000 \\ 0 & 0.0001 & 5.0000 & 0.0000 & -0.0000 & 0.0000 & 0.0000 & 0.0000 \\ 0 & 0 & 0.0000 & 4.3473 & 0.0000 & 0.0000 & 0.0000 & 0.0000 \\ 0 & 0 & 0 & 0.0000 & 3.6527 & 0.0000 & 0.0000 & -0.0000 \\ 0 & 0 & 0 & 0 & 0.0000 & 3.0000 & 0.0000 & -0.0000 \\ 0 & 0 & 0 & 0 & 0 & 0.0000 & 2.4679 & 0.0000 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0.0000 & 2.1206 \end{pmatrix} .$$
Đường chéo các phần tử (entries) match các trị riêng (eigenvalues) tìm thấy bởi chạy Matlab hàm eig(). Nếu một vài các trị riêng (eigenvalues) có cùng môđun/độ lớn, thì chứng minh breaks xuống, ta có thể không có dài hơn khẳng định $(\dagger$), cụ thể là rằng
$$lim\Lambda^{k} L\Lambda^{-k} = I.$$
$$k\mapsto \infty$$
Nếu ta giả sử rằng $P^{-1}$ có phù hợp “khối Nhân tử hóa LU (LU-factorization),” nó có thể được được hiển thị rằng các ma trận $A_{k+1}$ hội tụ đến khối tam giác trên (upper-triangular) ma trận, ở đâu mỗi khối tương ứng với các trị riêng (eigenvalues) có cùng môđun/độ lớn. Ví dụ, nếu $A$ là một ma trận cỡ $9 \times  9$ với các trị riêng (eigenvalues) $\lambda_{i}$ sao cho $|\lambda_{1}$ | $= |\lambda_{2}$ | $= |\lambda_{3}$ | $> |\lambda_{4}$ | $> |\lambda_{5}$ | $= |\lambda_{6}$ | $= |\lambda_{7}$ | $= |\lambda_{8}$ | $= |\lambda_{9}$ |, thì $A_{k}$ hội tụ đến khối ma trận đường chéo (diagonal matrix) (với ba các khối, $3 \times  3$ khối, $1 \times  1$ khối, và $5 \times  5$ khối) của tạo thành
$$\begin{pmatrix} ⋆ & ⋆ & ⋆ & * & * & * & * & * & * \\ ⋆ & ⋆ & ⋆ & * & * & * & * & * & * \\ ⋆ & ⋆ & ⋆ & * & * & * & * & * & * \\ 0 & 0 & 0 & ⋆ & * & * & * & * & * \\ 0 & 0 & 0 & 0 & ⋆ & ⋆ & ⋆ & ⋆ & ⋆ \\ 0 & 0 & 0 & 0 & ⋆ & ⋆ & ⋆ & ⋆ & ⋆ \\ 0 & 0 & 0 & 0 & ⋆ & ⋆ & ⋆ & ⋆ & ⋆ \\ 0 & 0 & 0 & 0 & ⋆ & ⋆ & ⋆ & ⋆ & ⋆ \\ 0 & 0 & 0 & 0 & ⋆ & ⋆ & ⋆ & ⋆ & ⋆ \end{pmatrix} .$$
Xem Ciarlet $[41]$ (Chương $6$ Mục 6.3) cho nhiều hơn/thêm chi tiết. Dưới các điều kiện của Định lý 18.1, đặc biệt, nếu $A$ là đối xứng (hoặc Hermite) xác định dương (positive definite) ma trận, các vectơ riêng (eigenvectors) của $A$ có thể được approximated. Tuy nhiên, khi $A$ là không ma trận đối xứng (symmetric matrix), vì tam giác trên (upper triangular) phần của $A_{k}$ thực hiện không nhất thiết hội tụ, một có là cautious rằng chặt chẽ justification là lacking. Giả sử ta áp dụng QR thuật toán đến ma trận $A$ thỏa mãn các giả thiết của Định lý

> **Định lý 18.1.** Cho $k$ lớn đủ, $A_{k+1} = P_{k}^{*}  AP_{k}$ là gần như tam giác trên (upper triangular) và đường chéo các phần tử (entries) của $A_{k+1}$ là tất cả phân biệt, do đó ta có thể xét rằng chúng là các trị riêng (eigenvalues) của $A_{k+1}$, và do đó của $A$. để tránh cũng nhiều các chỉ số dưới, viết $T$ cho tam giác trên (upper triangular) ma trận
