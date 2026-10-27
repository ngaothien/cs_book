# Sơ cấp Các ma trận và Hàng Các phép toán


<!-- PAGE 266 -->
Phụ thuộc và $A_{k}$ sẽ không là khả nghịch, một mâu thuẫn. tình huống này được minh họa bởi sau đây ma trận cho $n = 5$ và $k = 3$:
$$\begin{pmatrix} a_{1 1}^{(3)} & a_{1 2}^{(3)} & a_{1 3}^{(3)} & a_{1 3}^{(3)} & a_{1 5}^{(3)} \\ 0 & a_{2 2}^{(3)} & a_{2 3}^{(3)} & a_{2 4}^{(3)} & a_{2 5}^{(3)} \\ 0 & 0 & 0 & a_{3 4}^{(3)} & a_{3 5}^{(3)} \\ 0 & 0 & 0 & a_{4 4}^{(3)} & a_{4n}^{(3)} \\ 0 & 0 & 0 & a_{5 4}^{(3)} & a_{5 5}^{(3)} \end{pmatrix} .$$
Thứ nhất ba các cột của ở trên ma trận là phụ thuộc tuyến tính (linearly dependent). Do đó một của các phần tử (entries) $a_{i k}^{(k)}$ với $k \le i \le n$ có thể được được chọn như phần tử trụ (pivot), và ta hoán vị hàng thứ $k$ với hàng thứ $i$, thu được ma trận $\alpha^{(k)} = (\alpha_{j l}^{(k)}$). mới phần tử trụ (pivot) là $\pi_{k}  = \alpha_{k k}^{(k)}$, và ta không các phần tử (entries) $i = k + 1, \dots  , n$ trong cột $k$ bằng cách cộng $-\alpha_{i k}^{(k)}  /\pi_{k}$ lần hàng $k$ đến hàng $i$. Tại kết thúc/cuối của bước này, ta có $A_{k+1}$. Nhận thấy rằng thứ nhất $k$ - $1$ các hàng của $A_{k}$ là đồng nhất đến thứ nhất $k$ - $1$ các hàng của $A_{k+1}$. process của Phép khử Gauss (Gaussian elimination) được minh họa trong schematic tạo thành ở dưới:
$$\begin{pmatrix} \times & \times & \times & \times \\ \times & \times & \times & \times \\ \times & \times & \times & \times \end{pmatrix} =\Rightarrow \begin{pmatrix} \times & \times & \times & \times \\ 0 & \times & \times & \times \\ 0 & \times & \times & \times \\ 0 & \times & \times & \times \end{pmatrix} =\Rightarrow \begin{pmatrix} \times & \times & \times & \times \\ 0 & \times & \times & \times \\ 0 & 0 & \times & \times \\ 0 & 0 & \times & \times \end{pmatrix} =\Rightarrow \begin{pmatrix} \times & \times & \times & \times \\ 0 & \times & \times & \times \\ 0 & 0 & \times & \times \\ 0 & 0 & 0 & \times \end{pmatrix} .$$
$\times \times \times \times$

## 8.3 Sơ cấp Các ma trận và Hàng Các phép toán

Nó là dễ đến hình ra những gì loại của các ma trận perform các phép biến đổi sơ cấp trên hàng được sử dụng during Phép khử Gauss (Gaussian elimination). then chốt điểm là rằng nếu $A = PB$, ở đâu $A, B$ là $m \times  n$ các ma trận và $P$ là ma trận vuông (square matrix) có số chiều $m$, nếu (như thông thường) ta ký hiệu các hàng của $A$ và $B$ bởi $A_{1}, \dots  , A_{m}$ và $B_{1}, \dots  , B_{m}$, thì công thức
$$a_{ij} = \sum_{k=1}^{m}  p_{ik}b_{kj}$$
Cho $(i$, j)th phần tử (entry) trong $A$ chỉ ra rằng hàng thứ $i$ của $A$ là tổ hợp tuyến tính (linear combination) của các hàng của $B$:
$$A_{i} = p_{i1}B_{1} + \cdots  + p_{im}B_{m}.$$
Vì vậy, phép nhân của ma trận trên trái bởi ma trận vuông (square matrix) performs hàng các phép toán. Tương tự, phép nhân của ma trận trên phải bởi ma trận vuông (square matrix) performs cột các phép toán hoán vị của hàng thứ $k$ với hàng thứ $i$ là đạt được bằng cách nhân $A$ trên trái bởi phép chuyển vị ma trận P(i, $k)$, mà là ma trận thu được từ ma trận đơn vị (identity matrix)

<!-- PAGE 267 -->
Bởi hoán vị các hàng $i$ và $k$, i.e.,
$$P(i, k) = \begin{pmatrix} 1 \\ 1 \\ 0 & 1 \\ 1 \\ \ddots \\ 1 \\ 1 & 0 \\ 1 \\ 1 \end{pmatrix} .$$
Ví dụ, nếu $m = 3$,
$$P(1, 3) = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix} ,$$
Thì
$$P(1, 3)B = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} b_{11} & b_{12} & \cdots & \cdots & \cdots  b_{1n} \\ b_{21} & b_{22} & \cdots & \cdots & \cdots  b_{2n} \\ b_{31} & b_{32} & b_{3n} \end{pmatrix} = \begin{pmatrix} b_{31} & b_{32} & \cdots & \cdots & \cdots  b_{3n} \\ b_{21} & b_{22} & \cdots & \cdots & \cdots  b_{2n} \\ b_{11} & b_{12} & b_{1n} \end{pmatrix} .$$
$$\cdots \cdots \cdots \cdots \cdots \cdots$$
Nhận thấy rằng det(P(i, $k)) = -1$. Hơn nữa, P(i, $k)$ là đối xứng (P(i, $k)^{\top} =$ P(i, $k))$, và
$$P(i, k)^{-1}= P(i, k).$$
During hoán vị Bước $(2)$, nếu hàng $k$ và hàng $i$ cần là permuted, ma trận $A$ được nhân trên trái bởi ma trận $P_{k}$ sao cho $P_{k} =$ P(i, $k)$, khác ta tập hợp $P_{k} =$ I. Cộng $\beta$ lần hàng $j$ đến hàng $i$ (với $i \neq  j)$ là đạt được bằng cách nhân $A$ trên trái bởi sơ cấp ma trận,
$$E_{i,j;\beta} = I + \beta e_{i j},$$
Ở đâu
$$1if k = i and l = j$$
$$(e_{i j})_{k l} =$$
$$0if k \neq  i or l \neq  j,$$
I.e.,
$$E_{i,j;\beta} = \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \\ \ddots \\ 1 \\ \beta & 1 \\ 1 \\ 1 \end{pmatrix} orE_{i,j;\beta} = \begin{pmatrix} 1 \\ 1 \\ 1 & \beta \\ 1 \\ \ddots \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} ,$$

<!-- PAGE 268 -->
Trên trái, $i > j$, và trên phải, $i < j$. chỉ số $i$ là chỉ số của hàng rằng là đã thay đổi bởi phép nhân. Ví dụ, nếu $m = 3$ và ta muốn đến cộng hai lần hàng $1$ đến hàng $3$, vì $\beta  = 2, j = 1$ và $i = 3$, ta tạo thành
$$E_{3,1;2} = I + 2e_{31} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} + \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 2 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & 0 & 1 \end{pmatrix} ,$$
Và tính toán
$$100 \begin{pmatrix} b_{11} & b_{12} & \cdots & \cdots & \cdots  b_{1n} \\ b_{21} & b_{22} & \cdots & \cdots & \cdots  b_{2n} \\ b_{31} & b_{32} & b_{3n} \end{pmatrix}$$
$$E_{3,1;2}B =010$$
$$$$
$$201\cdots \cdots \cdots$$
$$b_{11}b_{12}\cdots \cdots \cdots  b_{1n}$$
$$=b_{21}b_{22}\cdots \cdots \cdots  b_{2n}.$$
$$$$
$$2b_{11} + b_{31}2b_{12} + b_{32}\cdots \cdots \cdots  2b_{1n} + b_{3n}$$
Nhận thấy rằng nghịch đảo của $E_{i,j;\beta} =$ I $+ \beta e_{i j}$ là $E_{i,j;-\beta} =$ I - $\beta e_{i j}$ và rằng $det(E_{i,j;\beta}) = 1$. Vì vậy, during Bước $3$ (phép khử bước), ma trận $A$ được nhân trên trái bởi tích $E_{k}$ của các ma trận của tạo thành $E_{i,k;\beta i,k}$, với $i > k$. Hệ quả là, ta xem rằng
$$A_{k+1} = E_{k}P_{k}A_{k},$$
Và thì
$$A_{k} = E_{k-1}P_{k-1} \cdots  E_{1}P_{1}A.$$
Điều này justifies khẳng định được tạo trước đó rằng $A_{k} = M_{k}A$ với một số ma trận khả nghịch (invertible matrix) $M_{k}$; ta có thể chọn
$$M_{k} = E_{k-1}P_{k-1} \cdots  E_{1}P_{1},$$
Tích của các ma trận khả nghịch. sự kiện rằng det(P(i, $k)) = -1$ và rằng $det(E_{i,j;\beta}) = 1$ suy ra ngay lập tức sự kiện được khẳng định ở trên: Ta luôn luôn có
$$\det(A_{k}) = \pm  \det(A).$$
Hơn nữa, vì
$$A_{k} = E_{k-1}P_{k-1} \cdots  E_{1}P_{1}A$$
Và vì Phép khử Gauss (Gaussian elimination) các dừng cho $k = n$, ma trận
$$A_{n} = E_{n-1}P_{n-1} \cdots  E_{2}P_{2}E_{1}P_{1}A$$
Là tam giác trên (upper-triangular). Cũng lưu ý rằng nếu ta cho $M = E_{n-1}P_{n-1} \cdots  E_{2}P_{2}E_{1}P_{1}$, thì det(M) $= \pm 1$, và
$$\det(A) = \pm  \det(A_{n}).$$
Các ma trận P(i, $k)$ và $E_{i,j;\beta}$ được gọi là sơ cấp các ma trận. Ta có thể summarize ở trên thảo luận trong sau đây định lý:
