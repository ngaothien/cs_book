# Chứng minh của Định lý 8.5


<!-- PAGE 283 -->
$$⊛$$

## 8.6 Chứng minh của Định lý 8.5


*Chứng minh.* $(1)$ chỉ phần rằng có không đã được được chứng minh là tính duy nhất phần (khi $P =$ I). Giả sử rằng $A$ là khả nghịch và rằng $A = L_{1}U_{1} = L_{2}U_{2}$, với $L_{1}, L_{2}$ unit tam giác dưới (lower-triangular) và $U_{1}, U_{2}$ tam giác trên (upper-triangular). Thì ta có
$$L_{2}^{-1} L_{1} = U_{2}U_{1}^{-1} .$$
Tuy nhiên, hiển nhiên là $L_{2}^{-1}$ là tam giác dưới (lower-triangular) và rằng $U_{1}^{-1}$ là tam giác trên (upper-triangular), và do đó $L_{2}^{-1} L_{1}$ là tam giác dưới (lower-triangular) và $U_{2}U_{1}^{-1}$ là tam giác trên (upper-triangular). Vì đường chéo các phần tử (entries) của $L_{1}$ và $L_{2}$ là $1$, ở trên đẳng thức là chỉ khả dĩ/có thể nếu $U_{2}U_{1}^{-1} =$ I, nghĩa là, $U_{1} = U_{2}$, và do đó $L_{1} = L_{2}$.
$(2)$ Khi $P =$ I, ta có $L = E_{1}^{-1} E_{2}^{-1} \cdots  E_{n-1}^{-1}$, ở đâu $E_{k}$ là tích của $n$ - $k$ sơ cấp các ma trận của tạo thành $E_{i,k;-\ell i}$, ở đâu $E_{i,k;-\ell i}$ các trừ $\ell_{i}$ lần hàng $k$ từ hàng $i$, với $\ell_{ik}  = a_{ik}^{(k)} /a_{kk}^{(k)} , 1 \le k \le n$ - $1$, và $k + 1 \le i \le n$. Thì ta kiểm chứng được ngay rằng
$$E_{k} = \begin{pmatrix} 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & \cdots & -\ell_{k} & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\ 0 & \ell_{nk} & 0 & 1 \end{pmatrix} ,$$
$$\cdots -\cdots$$
Và rằng
$$E_{k}^{-1}= \begin{pmatrix} 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & \cdots & \ell_{k+1k} & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & \ell_{nk} & 0 & 1 \end{pmatrix} .$$
$$\cdots \cdots$$
Nếu ta định nghĩa $L_{k}$ bởi
$$L_{k} = \begin{pmatrix} 1 & 0 & 0 & 0 & 0 & \vdots & 0 \\ \ell_{21} & 1 & 0 & 0 & 0 & \vdots & 0 \\ \ell_{31} & \ell_{32} & \ddots & 0 & 0 & \vdots & 0 \\ \vdots & \vdots & \ddots & 1 & 0 & \vdots & 0 \\ \ell_{k+11} & \ell_{k+12} & \cdots & \ell_{k+1k} & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & 0 & \vdots & 0 \\ \ell_{n1} & \ell_{n2} & \ell_{nk} & 0 & 1 \end{pmatrix}$$
$$\cdots \cdots$$
Cho $k = 1, \dots  , n$ - $1$, ta dễ dàng kiểm tra rằng $L_{1} = E_{1}^{-1}$, và rằng
$$L_{k} = L_{k-1}E_{k}^{-1} ,2 \le k \le n -1,$$

<!-- PAGE 284 -->
Bởi vì phép nhân trên phải bởi $E_{k}^{-1}$ cộng $\ell_{i}$ lần cột $i$ đến cột $k$ (của ma trận $L_{k-1})$ với $i > k$, và cột $i$ của $L_{k-1}$ có chỉ khác không phần tử (entry) $1$ như của nó phần tử thứ $i$. Vì
$$L_{k} = E_{1}^{-1}\cdots  E_{k}^{-1} ,1 \le k \le n -1,$$
Ta kết luận rằng $L = L_{n-1}$, chứng minh của ta khẳng định về hình dạng của $L. (3)$ Bước $1$. Chứng minh $(\dagger_{1}$). Thứ nhất ta chứng minh bằng quy nạp theo $k$ rằng
$$A_{k+1} = E_{k}^{k} \cdots  E_{1}^{k}P_{k} \cdots  P_{1}A,k = 1, \dots  , n -2.$$
Cho $k = 1$, ta có $A_{2} = E_{1}P_{1}A = E_{1}^{1}P_{1}A$, vì $E_{1}^{1} = E_{1}$, do đó của ta assertion nghiệm đúng một cách tầm thường. Bây giờ nếu $k \ge 2$,
$$A_{k+1} = E_{k}P_{k}A_{k},$$
Và theo giả thiết quy nạp,
$$A_{k} = E_{k-1}^{k-1} \cdots  E_{2}^{k-1}E_{1}^{k-1}P_{k-1} \cdots  P_{1}A.$$
Bởi vì $P_{k}$ là hoặc đồng nhất thức hoặc phép chuyển vị, $P_{k}^{2}  =$ I, do đó bởi inserting occurrences của $P_{k}P_{k}$ như indicated ở dưới ta có thể viết
$$A_{k+1} = E_{k}P_{k}A_{k}$$
$$= E_{k}P_{k}E_{k-1}^{k-1} \cdots  E_{2}^{k-1}E_{1}^{k-1}P_{k-1} \cdots  P_{1}A$$
$$= E_{k}P_{k}E_{k-1}^{k-1}(P_{k}P_{k}) \cdots  (P_{k}P_{k})E_{2}^{k-1}(P_{k}P_{k})E_{1}^{k-1}(P_{k}P_{k})P_{k-1} \cdots  P_{1}A$$
$$= E_{k}(P_{k}E_{k-1}^{k-1}P_{k}) \cdots  (P_{k}E_{2}^{k-1}P_{k})(P_{k}E_{1}^{k-1}P_{k})P_{k}P_{k-1} \cdots  P_{1}A.$$
Nhận thấy rằng $P_{k}$ có đã được “moved” đến phải của phép khử các bước. Tuy nhiên, theo Định nghĩa,
$$E_{j}^{k} = P_{k}E_{j}^{k-1}P_{k},j = 1, \dots  , k -1$$
$$E_{k}^{k} = E_{k},$$
Do đó ta thu được
$$A_{k+1} = E_{k}^{k}E_{k-1}^{k} \cdots  E_{2}^{k}E_{1}^{k}P_{k} \cdots  P_{1}A,$$
Thiết lập giả thiết quy nạp (induction hypothesis). Cho $k = n$ - $2$, ta thu được
$$U = A_{n-1} = E_{n-1}^{n-1} \cdots  E_{1}^{n-1}P_{n-1} \cdots  P_{1}A,$$
Như đã khẳng định, và nhân tử hóa $PA = LU$ với
$$P = P_{n-1} \cdots  P_{1}$$
$$L = (E_{1}^{n-1})^{-1}\cdots  (E_{n-1}^{n-1})^{-1}$$

<!-- PAGE 285 -->
Là rõ ràng. Bước $2$. Chứng minh rằng các ma trận $(E_{j}^{k} )^{-1}$ là tam giác dưới (lower-triangular). Đến đạt được điều này, ta chứng minh rằng các ma trận $\mathcal{E}_{j}^{k}$ là chặt tam giác dưới (lower triangular) các ma trận của rất đặc biệt tạo thành. Vì cho $j = 1, \dots  , n$ - $2$, ta có $E_{j}^{j} = E_{j}$,
$$E_{j}^{k} = P_{k}E_{j}^{k-1}P_{k},k = j + 1, \dots  , n -1,$$
Vì $E_{n-1}^{n-1} = E_{n-1}$ và $P_{k}^{-1} = P_{k}$, ta thu được $(E_{j}^{j})^{-1} = E_{j}^{-1}$ cho $j = 1, \dots  , n$ - $1$, và cho $j = 1, \dots  , n$ - $2$, ta có
$$(E_{j}^{k} )^{-1}= P_{k}(E_{j}^{k-1})^{-1}P_{k},k = j + 1, \dots  , n -1.$$
Vì
$$(E_{j}^{k-1})^{-1}= I +\mathcal{E}_{j}^{k-1}$$
Và $P_{k} =$ P(k, $i)$ là phép chuyển vị hoặc $P_{k} =$ I, do đó $P_{k}^{2}  =$ I, và ta thu được $(E_{j}^{k} )^{-1} = P_{k}(E_{j}^{k-1})^{-1}P_{k} = P_{k}(I +\mathcal{E}_{j}^{k-1})P_{k} = P_{k}^{2} + P_{k} \mathcal{E}_{j}^{k-1} P_{k} =$ I $+ P_{k}\mathcal{E}_{j}^{k-1} P_{k}$. Vì vậy, ta có
$$(E_{j}^{k} )^{-1}= I + P_{k} \mathcal{E}_{j}^{k-1}P_{k},1 \le j \le n -2, j + 1 \le k \le n -1.$$
Ta chứng minh cho $j = 1, \dots  , n$ - $1$, rằng cho $k = j, \dots  , n$ - $1$, mỗi $\mathcal{E}_{j}^{k}$ là tam giác dưới (lower triangular) ma trận của tạo thành
$$\mathcal{E}_{j}^{k} = \begin{pmatrix} 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \cdots & \ell_{j+1j}^{(k)} & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & \ell_{nj}^{(k)} & 0 & 0 \end{pmatrix} ,$$
$$\cdots \cdots$$
Và rằng
$$\mathcal{E}_{j}^{k} = P_{k} \mathcal{E}_{j}^{k-1},1 \le j \le n -2, j + 1 \le k \le n -1,$$
Với $P_{k} =$ I hoặc $P_{k} =$ P(k, $i)$ với một số $i$ sao cho $k + 1 \le i \le n$. Với mỗi $j (1 \le j \le n$ - $1)$ ta tiến hành bằng quy nạp theo $k = j, \dots  , n$ - $1$. Vì $(E_{j}^{j})^{-1} = E_{j}^{-1}$ và vì $E_{j}^{-1}$ là của ở trên tạo thành, base trường hợp nghiệm đúng. Cho quy nạp bước, ta chỉ cần đến xét trường hợp ở đâu $P_{k} =$ P(k, $i)$ là phép chuyển vị, vì trường hợp ở đâu $P_{k} =$ I là tầm thường. Ta có đến hình ra những gì $P_{k}\mathcal{E}_{j}^{k-1} P_{k} =$

<!-- PAGE 286 -->
P(k, $i)\mathcal{E}_{j}^{k-1}$ P(k, $i)$ là. Tuy nhiên, vì
$$\mathcal{E}_{j}^{k-1}= \begin{pmatrix} 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \cdots & \ell_{j+1}^{(k-1)} & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\ 0 & \ell_{nj}^{(k-1)} & 0 & 0 \end{pmatrix} ,$$
$$\cdots \cdots$$
Và bởi vì $k + 1 \le i \le n$ và $j \le k$ - $1$, nhân $\mathcal{E}_{j}^{k-1}$ trên phải bởi P(k, $i)$ sẽ hoán vị các cột $i$ và $k$, mà là các cột của các không điểm, do đó
$$P(k, i)\mathcal{E}_{j}^{k-1}P(k, i) = P(k, i)\mathcal{E}_{j}^{k-1},$$
Và do đó,
$$(E_{j}^{k} )^{-1}= I + P(k, i)\mathcal{E}_{j}^{k-1}.$$
Nhưng vì
$$(E_{j}^{k} )^{-1}= I +\mathcal{E}_{j}^{k} ,$$
Ta suy ra rằng
$$\mathcal{E}_{j}^{k} = P(k, i)\mathcal{E}_{j}^{k-1}.$$
Ta cũng biết rằng nhân $\mathcal{E}_{j}^{k-1}$ trên trái bởi P(k, $i)$ sẽ hoán vị các hàng $i$ và $k$, mà chỉ ra rằng $\mathcal{E}_{j}^{k}$ có mong muốn tạo thành, như đã khẳng định. Vì tất cả $\mathcal{E}_{j}^{k}$ là chặt tam giác dưới (lower triangular), tất cả $(E_{j}^{k} )^{-1} =$ I $+\mathcal{E}_{j}^{k}$ là tam giác dưới (lower triangular), do đó tích
$$L = (E_{1}^{n-1})^{-1}\cdots  (E_{n-1}^{n-1})^{-1}$$
Là cũng tam giác dưới (lower triangular). Bước $3$. Biểu diễn $L$ như $L =$ I $+ \Lambda_{n-1}$, với $\Lambda_{n-1}  =\mathcal{E}_{1}^{1} + \cdots  +\mathcal{E}_{n-1}^{n-1}$. Từ Bước $1$ của Phần $(3)$, ta biết rằng
$$L = (E_{1}^{n-1})^{-1}\cdots  (E_{n-1}^{n-1})^{-1}.$$
Ta chứng minh bằng quy nạp theo $k$ rằng
$$\cdots$$
$$I + \Lambda_{k}  = (E_{1}^{k})^{-1} (E_{k}^{k})^{-1}$$
$$\Lambda_{k}  =\mathcal{E}_{1}^{k} + \cdots  +\mathcal{E}_{k}^{k},$$
Cho $k = 1, \dots  , n$ - $1$.

<!-- PAGE 287 -->
Nếu $k = 1$, ta có $E_{1}^{1} = E_{1}$ và
$$E_{1} = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ -\ell_{21}^{(1)} & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ \ell_{n1}^{(1)} & 0 & 1 \end{pmatrix} .$$
$$-\cdots$$
Ta cũng thu được
$$(E_{1}^{-1} )^{-1} = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ \ell_{21}^{(1)} & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ \ell_{n1}^{(1)} & 0 & 1 \end{pmatrix} = I + \Lambda_{1} .$$
$$\cdots$$
Vì $(E_{1}^{-1} )^{-1} =$ I $+\mathcal{E}_{1}^{1}$, ta tìm rằng ta thu được $\Lambda_{1}  =\mathcal{E}_{1}^{1}$, và base bước nghiệm đúng. Vì $(E_{j}^{k} )^{-1} =$ I $+\mathcal{E}_{j}^{k}$ với
$$\mathcal{E}_{j}^{k} = \begin{pmatrix} 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \cdots & \ell_{j+1j}^{(k)} & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & \ell_{nj}^{(k)} & 0 & 0 \end{pmatrix}$$
$$\cdots \cdots$$
Và $\mathcal{E}_{i}^{k} \mathcal{E}_{j}^{k} = 0$ nếu $i < j$, như trong phần $(2)$ cho phép tính liên quan đến các tích của $L_{k}’s$, ta thu được
$$(E_{1}^{k-1})^{-1}\cdots  (E_{k-1}^{k-1})^{-1}= I +\mathcal{E}_{1}^{k-1}+ \cdots  +\mathcal{E}_{k-1}^{k-1},2 \le k \le n.(*)$$
Tương tự, từ sự kiện rằng $\mathcal{E}_{j}^{k-1}$ P(k, $i) =\mathcal{E}_{j}^{k-1}$ nếu $i \ge k + 1$ và $j \le k$ - $1$ và vì
$$(E_{j}^{k} )^{-1}= I + P_{k}\mathcal{E}_{j}^{k-1},1 \le j \le n -2, j + 1 \le k \le n -1,$$
Ta thu được
$$\cdots$$
$$(E_{1}^{k})^{-1} (E_{k-1}^{k})^{-1}= I + P_{k}(\mathcal{E}_{1}^{k-1}+ \cdots  +\mathcal{E}_{k-1}^{k-1}),2 \le k \le n -1.(**)$$
Theo giả thiết quy nạp,
$$I + \Lambda_{k-1}  = (E_{1}^{k-1})^{-1}\cdots  (E_{k-1}^{k-1})^{-1},$$
Và từ (*), ta thu được
$$\Lambda_{k-1}  =\mathcal{E}_{1}^{k-1}+ \cdots  +\mathcal{E}_{k-1}^{k-1}.$$
Bằng cách sử dụng (**), ta suy ra rằng
$$\cdots$$
$$(E_{1}^{k})^{-1} (E_{k-1}^{k})^{-1}= I + P_{k}\Lambda_{k-1} .$$
