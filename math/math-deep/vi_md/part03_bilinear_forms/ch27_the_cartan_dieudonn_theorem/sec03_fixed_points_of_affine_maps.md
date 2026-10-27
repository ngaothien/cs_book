# Cố định Các điểm của Các ánh xạ afin


<!-- PAGE 985 -->
$$\longrightarrow$$
Với mọi $u \in E , f$ sẽ là afin nếu ta có thể chỉ ra rằng $g$ là tuyến tính, và $f$ sẽ là afin phép đẳng cự (isometry) nếu ta có thể chỉ ra rằng $g$ là tuyến tính phép đẳng cự (isometry). Nhận thấy rằng
$$--------\longrightarrow --------\longrightarrow$$
$$g(v) -g(u)=f(\Omega )f(\Omega + v) -f(\Omega )f(\Omega + u)$$
$$-----------\longrightarrow$$
$$=f(\Omega + u)f(\Omega + v).$$
Thì, giả thiết
$$----\longrightarrow \longrightarrow$$
$$\|f(a)f(b)\|= \|ab\|$$
Với mọi, $b \in E$, suy ra rằng
$$-----------\longrightarrow ---------\longrightarrow$$
$$\|g(v) -g(u)\|= \|f(\Omega + u)f(\Omega + v)\|= \|(\Omega + u)(\Omega + v)\|= \|v -u\|.$$
Do đó, $g$ bảo toàn khoảng cách. Cũng, theo Định nghĩa, ta có
$$g(0) = 0.$$
Do đó, ta có thể áp dụng Bổ đề 12.12, mà chỉ ra rằng $g$ là thật vậy tuyến tính phép đẳng cự (isometry), và do đó $f$ là afin phép đẳng cự (isometry). Trong thứ tự đến understand cấu trúc của afin các phép đẳng cự, nó là quan trọng đến investigate cố định các điểm của ánh xạ afin (affine map).

## 27.3 Cố định Các điểm của Các ánh xạ afin

$$\longrightarrow$$
$$Recall that E \begin{pmatrix} \longrightarrow \\ 1,f \end{pmatrix} denotes the eigenspace of the linear \longrightarrow mapf associated \longrightarrow  with the scalar$$
$1$, nghĩa là, không gian con bao gồm của tất cả các vectơ $u \in E$ sao cho $f (u) = u$. Rõ ràng,
$$\mathrm{Ker} \begin{pmatrix} \longrightarrow \\ f-id \end{pmatrix} = E \begin{pmatrix} \longrightarrow \\ 1,f \end{pmatrix} . Given some origin \Omega \in E, since$$
$$\longrightarrow  \longrightarrow \longrightarrow$$
$$f(a) = f(\Omega +\Omega a) = f(\Omega ) +f (\Omega a),$$
$$-----\longrightarrow  \longrightarrow \longrightarrow$$
Ta có $f(\Omega$)f() $= f (\Omega$), và do đó
$$--\longrightarrow  ---\longrightarrow  \longrightarrow \longrightarrow$$
$$\Omega f(a) =\Omega f(\Omega ) +f (\Omega a).$$
Từ ở trên, ta thu được
$$--\longrightarrow \longrightarrow  ---\longrightarrow  \longrightarrow \longrightarrow \longrightarrow$$
$$\Omega f(a) -\Omega a =\Omega f(\Omega ) +f (\Omega a) -\Omega a.$$
Bằng cách sử dụng điều này, ta chỉ ra sau đây bổ đề, mà nghiệm đúng cho tùy ý các không gian afin của hữu hạn số chiều và cho tùy ý các ánh xạ afin.

<!-- PAGE 986 -->

> **Mệnh đề 27.8.** Cho $E$ là bất kỳ không gian afin (affine space) của hữu hạn số chiều. Với mọi ánh xạ afin (affine map) $f$: $E \to E$, cho Fix(f) $= {a \in E$ | f() $= a}$ là tập hợp của cố định các điểm của $f$. Các tính chất sau đây đúng:
$(1)$ Nếu $f$ có một số cố định điểm, sao cho Fix(f) $\neq  \emptyset$, thì Fix(f) là không gian con afin (affine subspace) của $E$ sao cho
$$Fix(f) = a + E \begin{pmatrix} \longrightarrow \\ 1,f \\ linear \end{pmatrix} = a + \mathrm{Ker} \begin{pmatrix} \longrightarrow \\ f-id \\ forthe \end{pmatrix} ,$$
$$\longrightarrow$$
$$where E \begin{pmatrix} \longrightarrow \\ 1,f \end{pmatrix} is the eigenspace of the  mapf   eigenvalue 1.$$
$$(2) The affine map f has a unique fixed point iff E \begin{pmatrix} \longrightarrow \\ 1,f \end{pmatrix} = \mathrm{Ker} \begin{pmatrix} \longrightarrow \\ f-id \end{pmatrix} = {0}.$$

*Chứng minh.* $(1)$ Vì đồng nhất thức
$$--\longrightarrow \longrightarrow  ---\longrightarrow  \longrightarrow \longrightarrow \longrightarrow$$
$$\Omega f(b) -\Omega b =\Omega f(\Omega ) +f (\Omega b) -\Omega b$$
$$--\longrightarrow$$
Nghiệm đúng với mọi $\Omega , b \in E$, nếu f() $= a$, thì af() $= 0$, và do đó, đặt $\Omega = a$, với mọi $b \in E$ ta có
$$--\longrightarrow \longrightarrow  --\longrightarrow  \longrightarrow \longrightarrow \longrightarrow  \longrightarrow \longrightarrow \longrightarrow$$
$$af(b) -ab =af(a) +f (ab) -ab =f (ab) -ab,$$
Và do đó
$$f(b) = b$$
Khi và chỉ khi
$$--\longrightarrow \longrightarrow$$
$$af(b) -ab = 0$$
Khi và chỉ khi
$$\longrightarrow \longrightarrow \longrightarrow$$
$$f (ab) -ab = 0$$
Khi và chỉ khi
$$\longrightarrow$$
$$ab \in E \begin{pmatrix} \longrightarrow \\ 1,f \end{pmatrix} = \mathrm{Ker} \begin{pmatrix} \longrightarrow \\ f-id \end{pmatrix} ,$$
Mà chứng tỏ rằng
$$Fix(f) = a + E \begin{pmatrix} \longrightarrow \\ 1,f \end{pmatrix} = a + \mathrm{Ker} \begin{pmatrix} \longrightarrow \\ f-id \end{pmatrix} .$$
$(2)$ Một lần nữa, fix một số gốc $\Omega$. Một số thỏa mãn f() $= a$ khi và chỉ khi
$$--\longrightarrow \longrightarrow$$
$$\Omega f(a) -\Omega a = 0$$
Khi và chỉ khi
$$---\longrightarrow  \longrightarrow \longrightarrow \longrightarrow$$
$$\Omega f(\Omega ) +f (\Omega a) -\Omega a = 0,$$
Mà có thể được được viết lại như
$$\longrightarrow ---\longrightarrow$$
$$\begin{pmatrix} \longrightarrow \\ f-id \\ = & 0 \end{pmatrix} (\Omega a) = -\Omega f(\Omega ).$$
$$\longrightarrow  \longrightarrow$$
$$We have E \begin{pmatrix} \longrightarrow \\ 1,f \\ \longrightarrow \\ f- \end{pmatrix} = \mathrm{Ker} \begin{pmatrix} \longrightarrow \\ f-id \\ surjective, \end{pmatrix} {} iff f -id is injective, and sinceE has finite$$
Số chiều, id là cũng và do đó, ở đó là thật vậy một số $a \in E$ sao cho
$$\longrightarrow ---\longrightarrow$$
$$\begin{pmatrix} \longrightarrow \\ f-id \end{pmatrix} (\Omega a) = -\Omega f(\Omega ),$$
