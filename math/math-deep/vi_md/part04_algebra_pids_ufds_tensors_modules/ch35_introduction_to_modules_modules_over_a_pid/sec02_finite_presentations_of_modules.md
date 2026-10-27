# Hữu hạn các trình bày của Các môđun


<!-- PAGE 1282 -->
$a_{i}y_{i}$ có thể được biểu diễn dưới dạng tổ hợp tuyến tính (linear combination) của $(u_{1}, \dots  , u_{m})$. Nếu ta cho $a = a_{1} \dots  a_{n}$, thì $a_{1} \dots  a_{n}y_{i} \in Au_{1} \oplus \cdots  \oplus Au_{m}$ cho $i = 1, \dots  , n$, mà chỉ ra rằng
$$aM \subseteq Au_{1} \oplus \cdots  \oplus Au_{m}.$$
Bây giờ, $A$ là miền nguyên (integral domain), và vì $a_{i} \neq  0$ cho $i = 1, \dots  , n$, ta có $a = a_{1} \dots  a_{n} \neq  0$, và bởi vì $M$ là không xoắn (torsion-free), ánh xạ $x \mapsto$ ax là đơn ánh (injective). Suy ra rằng $M$ là đẳng cấu đến môđun con của môđun tự do (free module) $Au_{1} \oplus \cdots  \oplus Au_{m}$. Theo Mệnh đề 35.5, điều này môđun con nếu tự do, và do đó, $M$ là tự do. Mặc dù ta sẽ thu được kết quả này như hệ quả của cấu trúc định lý cho sinh hữu hạn (finitely generated) các môđun trên PID, ta là trong position đến cho quick chứng minh của sau đây định lý.

> **Định lý 35.7.** Cho $M$ là sinh hữu hạn (finitely generated) môđun trên PID. Thì $M/M_{tor}$ là tự do, và ở đó exit tự do môđun con $F$ của $M$ sao cho $M$ là tổng trực tiếp (direct sum)
$$M = M_{tor} \oplus F.$$
Số chiều của $F$ là một cách duy nhất được xác định.

*Chứng minh.* Theo Mệnh đề 35.4 $M/M_{tor}$ là không xoắn (torsion-free), và vì $M$ là sinh hữu hạn (finitely generated), nó là cũng sinh hữu hạn (finitely generated). Theo Mệnh đề 35.6, $M/M_{tor}$ là tự do. Ta có thương ánh xạ tuyến tính (linear map) $\pi$: $M \to M/M_{tor}$, mà là toàn ánh (surjective), và $M/M_{tor}$ là tự do, do đó theo Mệnh đề 35.2, có một môđun tự do (free module) $F$ đẳng cấu đến $M/M_{tor}$ sao cho
$$M = \mathrm{Ker} (\pi ) \oplus F = M_{tor} \oplus F.$$
Vì $F$ là đẳng cấu đến $M/M_{tor}$, số chiều của $F$ là một cách duy nhất được xác định. Định lý 35.7 rút gọn study của sinh hữu hạn (finitely generated) môđun trên PID đến study của sinh hữu hạn (finitely generated) xoắn (torsion) các môđun. Điều này là đường đi theo sau bởi Lang $[113]$ (Chương III, mục $7)$.

## 35.2 Hữu hạn các trình bày của Các môđun

Vì các môđun là một cách tổng quát không tự do, nó là tự nhiên đến nhìn cho các kỹ thuật cho dealing với nonfree các môđun. hint là rằng nếu $M$ là A-module và nếu $(u_{i})_{i\in I}$ là bất kỳ tập hợp của các phần tử sinh cho $M$, thì ta biết rằng có một toàn ánh (surjective) đồng cấu $\phi$: $A^{(I)} \to M$ từ môđun tự do (free module) $A^{(I)}$ được sinh bởi I lên $M$. Hơn nữa $M$ là đẳng cấu đến $A^{(I)}/Ker (\phi$). Thì, ta có thể chọn tập hợp của các phần tử sinh $(v_{j})_{j\in J}$ cho Ker $(\phi$), và một lần nữa có một toàn ánh (surjective) ánh xạ $\psi$: $A^{(J)} \to$ Ker $(\phi$) từ môđun tự do (free module) $A^{(J)}$ được sinh bởi $J$ lên Ker $(\phi$). ánh xạ $\psi$ có thể được được quan điểm ánh xạ tuyến tính (linear map) từ $A^{(J)}$ đến $A^{(I)}$, ta có
$$\mathrm{Im}(\psi ) = \mathrm{Ker} (\phi ),$$

<!-- PAGE 1283 -->
Và $\phi$ là toàn ánh (surjective). Lưu ý rằng $M$ là đẳng cấu đến $A^{(I)}/Im(\psi$). Trong như vậy tình huống ta nói rằng ta có chính xác dãy và điều này được ký hiệu bởi biểu đồ
$$\psi  A^{(I)}/\phi  M/ 0/$$
$$A^{(J)}.$$

> **Định nghĩa 35.6.** Cho trước A-module $M$, trình bày của $M$ là chính xác dãy
$$\psi  A^{(I)}/\phi  M/ 0/$$
$$A^{(J)}$$
Mà có nghĩa là $1. Im(\psi$) $=$ Ker $(\phi$). $2. \phi$ là toàn ánh (surjective). Hệ quả là, $M$ là đẳng cấu đến $A^{(I)}/Im(\psi$). Nếu I và $J$ là cả hai hữu hạn, ta nói rằng điều này là hữu hạn trình bày của $M$. Nhận thấy rằng trong trường hợp của hữu hạn trình bày, I và $J$ là hữu hạn, và nếu |J| $= n$ và |I| $= m$, thì $\psi$ là ánh xạ tuyến tính (linear map) $\psi$: $A^{n} \to A^{m}$, do đó nó được cho bởi một số $m \times  n$ ma trận $R$ với các hệ số trong $A$ được gọi là trình bày ma trận của $M$. Mọi cột $R^{j}$ của $R$ có thể thought của như quan hệ
$$a_{j1}e_{1} + \cdots  + a_{jm}e_{m} = 0$$
Trong số các phần tử sinh $e_{1}, \dots  , e_{m}$ của $A^{m}$, do đó ta có $n$ các quan hệ trong số các phần tử này các phần tử sinh. Cũng các ảnh của $e_{1}, \dots  , e_{m}$ trong $M$ là các phần tử sinh của $M$, do đó ta có thể nghĩ của ở trên các quan hệ như các quan hệ trong số các phần tử sinh của $M$. môđun con của $A^{m}$ được sinh (spanned) bởi các cột của $R$ là tập hợp của các quan hệ của $M$, và các cột của $R$ được gọi là đầy đủ tập hợp của các quan hệ cho $M$. các vectơ $e_{1}, \dots  , e_{m}$ được gọi là tập hợp của các phần tử sinh cho $M$. Ta có thể cũng nói rằng các phần tử sinh $e_{1}, \dots  , e_{m}$ và các quan hệ $R^{1}, \dots  , R^{n}$ (các cột của $R)$ là (hữu hạn) trình bày của môđun $M$. môđun $M$ được trình bày bởi $R$ là đẳng cấu đến $A^{m}/RA^{n}$, ở đâu ta ký hiệu bởi $RA^{n}$ ảnh (image) của $A^{n}$ bởi ánh xạ tuyến tính (linear map) được định nghĩa bởi $R$. Ví dụ, $the\mathbb{Z}-module$ được trình bày bởi ma trận cỡ $1 \times  1$ $R = (5)$ là thương, $\mathbb{Z}/5\mathbb{Z}$, của $\mathbb{Z}$ bởi môđun con $5\mathbb{Z}$ tương ứng với đơn lẻ quan hệ
$$5e_{1} = 0.$$
Nhưng $\mathbb{Z}/5\mathbb{Z}$ có khác các trình bày. Ví dụ, nếu ta xét ma trận của các quan hệ
$$R = \begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix} ,$$

<!-- PAGE 1284 -->
Trình bày môđun $M$, thì ta có các quan hệ
$$2e_{1} + e_{2} = 0$$
$$-e_{1} + 2e_{2} = 0.$$
Từ phương trình thứ nhất, ta thu được $e_{2} = -2e_{1}$, và thế vào phương trình thứ hai ta thu được
$$-5e_{1} = 0.$$
Suy ra rằng phần tử sinh $e_{2}$ có thể được được khử và $M$ được sinh bởi đơn lẻ phần tử sinh $e_{1}$ thỏa mãn quan hệ
$$5e_{1} = 0,$$
Mà chỉ ra rằng $M \approx \mathbb{Z}/5\mathbb{Z}$. ở trên ví dụ chỉ ra rằng nhiều khác nhau các ma trận có thể trình bày cùng môđun. Ở đây là một số hữu ích các quy tắc cho manipulating quan hệ ma trận mà không có thay đổi đẳng cấu lớp của môđun $M$ nó các trình bày.

> **Mệnh đề 35.8.** Nếu $R$ là một ma trận cỡ $m \times  n$ trình bày A-module $M$, thì các ma trận $S$ của tạo thành được liệt kê ở dưới trình bày cùng môđun (môđun đẳng cấu đến $M)$:
$(1) S = QRP^{-1}$, ở đâu $Q$ là $m \times  m$ ma trận khả nghịch (invertible matrix) và $P$ $n \times  n$ ma trận khả nghịch (invertible matrix) (cả hai trên $A)$.
$(2) S$ là thu được từ $R$ bởi xóa cột của các không điểm.
$(3)$ cột thứ $j$ của $R$ là $e_{i}$, và $S$ là thu được từ $R$ bởi xóa hàng thứ $i$ và cột thứ $j$.

*Chứng minh.* $(1)$ Theo Định nghĩa, ta có đẳng cấu $M \approx A^{m}/RA^{n}$, ở đâu ta ký hiệu bởi $RA^{n}$ ảnh (image) của $A^{n}$ bởi ánh xạ tuyến tính (linear map) được định nghĩa bởi $R$. Đi từ $R$ đến $QRP^{-1}$ tương ứng với tạo ra chuyển cơ sở (change of basis) trong $A^{m}$ và chuyển cơ sở (change of basis) trong $A^{n}$, và điều này cho ta thương môđun đẳng cấu đến $M$.
$(2) A$ không cột thực hiện không contribute đến sinh (span) của các cột của $R$, do đó nó có thể được được khử.
$(3)$ Nếu cột thứ $j$ của $R$ là $e_{i}$, thì khi lấy thương $A^{m}/RA^{n}$, phần tử sinh $e_{i}$ đi đến không. Điều này có nghĩa là phần tử sinh $e_{i}$ là redundant, và khi ta xóa nó, ta thu được ma trận của các quan hệ trong mà hàng thứ $i$ của $R$ và cột thứ $j$ của $R$ là deleted. các ma trận $P$ và $Q$ là thường các tích của sơ cấp các phép toán. Một nên là careful rằng các hàng của các không điểm cannnot được khử. Ví dụ, ma trận cỡ $2 \times  1$
$$R_{1} = \begin{pmatrix} 4 \\ 0 \end{pmatrix}$$

<!-- PAGE 1285 -->
Cho đơn lẻ quan hệ
$$4e_{1} = 0,$$
Nhưng thứ hai phần tử sinh $e_{2}$ không thể được khử. ma trận này các trình bày $module\mathbb{Z}/4\mathbb{Z}\times \mathbb{Z}$. Mặt khác, ma trận cỡ $1 \times  2$
$$R_{2} = \begin{pmatrix} 4 & 0 \end{pmatrix}$$
Cho hai các quan hệ
$$4e_{1} = 0,$$
$$0 = 0,$$
Do đó thứ hai phần tử sinh có thể được được khử và $R_{2}$ các trình bày môđun $\mathbb{Z}/4\mathbb{Z}$. các quy tắc của Mệnh đề 35.8 tạo nó khả dĩ/có thể để đơn giản hóa trình bày ma trận khá nhiều trong một số các trường hợp. Ví dụ, xét quan hệ ma trận
$$R = \begin{pmatrix} 3 & 8 & 7 & 9 \\ 2 & 4 & 6 & 6 \\ 1 & 2 & 2 & 1 \end{pmatrix} .$$
Bằng cách trừ $2$ lần hàng $3$ từ hàng $2$ và trừ $3$ lần hàng $3$ từ hàng $1$, ta thu được
$$\begin{pmatrix} 0 & 2 & 1 & 6 \\ 0 & 0 & 2 & 4 \\ 1 & 2 & 2 & 1 \end{pmatrix} .$$
Sau xóa cột $1$ và hàng $3$, ta thu được
$$\begin{pmatrix} 2 & 1 & 6 \\ 0 & 2 & 4 \end{pmatrix} .$$
Bằng cách trừ $2$ lần hàng $1$ từ hàng $2$, ta thu được
$$\begin{pmatrix} 2 & 1 & 6 \\ -4 & 0 & -8 \end{pmatrix} .$$
Sau xóa cột $2$ và hàng $1$, ta thu được
$$\begin{pmatrix} -4 & -8 \end{pmatrix} .$$
Bằng cách trừ $2$ lần cột $1$ từ cột $2$, ta thu được
$$\begin{pmatrix} -4 & 0 \end{pmatrix} .$$
Cuối cùng, ta có thể bỏ cột thứ hai và ta thu được
$$(4),$$

<!-- PAGE 1286 -->
Mà chỉ ra rằng $R$ các trình bày môđun $\mathbb{Z}/4\mathbb{Z}$. Không may là môđun con của môđun tự do (free module) của hữu hạn số chiều là không nhất thiết sinh hữu hạn (finitely generated) nhưng, theo Mệnh đề 35.5, nếu $A$ là PID, thì bất kỳ môđun con của sinh hữu hạn (finitely generated) môđun là sinh hữu hạn (finitely generated). tính chất này thực sự các đặc trưng hóa Các vành Noether. để chứng minh nó, ta cần slightly khác nhau phiên bản của Mệnh đề 35.2.

> **Mệnh đề 35.9.** Cho $f$: $E \to F$ là ánh xạ tuyến tính (linear map) giữa hai A-modules $E$ và $F$.
$(1)$ Cho trước bất kỳ tập hợp của các phần tử sinh $(v_{1}, \dots  , v_{r})$ của Im(f), với mọi $r$ các vectơ $u_{1}, \dots  , u_{r} \in E$ sao cho $f(u_{i}) = v_{i}$ cho $i = 1, \dots  , r$, nếu $U$ là sinh hữu hạn (finitely generated) môđun con của $E$ được sinh bởi $(u_{1}, \dots  , u_{r})$, thì môđun $E$ là tổng
$$E = \mathrm{Ker} (f) + U.$$
Hệ quả là, nếu cả hai Ker $(f)$ và Im(f) là sinh hữu hạn (finitely generated), thì $E$ là sinh hữu hạn (finitely generated).
$(2)$ Nếu $E$ là sinh hữu hạn (finitely generated), thì do đó là Im(f).

*Chứng minh.* $(1)$ Chọn bất kỳ $w \in E$, viết f(w) trên các phần tử sinh $(v_{1}, \dots  , v_{r})$ của Im(f) như f(w) $= a_{1}v_{1} + \cdots  + a_{r}v_{r}$, và cho $u = a_{1}u_{1} + \cdots  + a_{r}u_{r}$. Nhận thấy rằng
$$f(w -u) = f(w) -f(u)$$
$$= a_{1}v_{1} + \cdots  + a_{r}v_{r} -(a_{1}f(u_{1}) + \cdots  + a_{r}f(u_{r}))$$
$$= a_{1}v_{1} + \cdots  + a_{r}v_{r} -(a_{1}v_{1} + \cdots  + a_{r}v_{r})$$
$$= 0.$$
Vì vậy, $h = w$ - $u \in$ Ker $(f)$, và vì $w = h + u$ với $h \in$ Ker $(f)$ và $u \in U$, ta có $E =$ Ker $(f) + U$, như đã khẳng định. Nếu Ker $(f)$ là cũng sinh hữu hạn (finitely generated), bằng cách lấy hợp của hữu hạn tập hợp của các phần tử sinh cho Ker $(f)$ và $(v_{1}, \dots  , v_{r})$, ta thu được hữu hạn tập hợp của các phần tử sinh cho $E$.
$(2)$ Nếu $(u_{1}, \dots  , u_{n})$ sinh $E$, hiển nhiên là $(f(u_{1}), \dots  , f(u_{n}))$ sinh Im(f).

> **Định lý 35.10.** vành $A$ là Noetherian khi và chỉ khi mọi môđun con $N$ của sinh hữu hạn (finitely generated) A-module $M$ là chính nó sinh hữu hạn (finitely generated).

*Chứng minh.* Thứ nhất, giả sử rằng mọi môđun con $N$ của sinh hữu hạn (finitely generated) A-module $M$ là chính nó sinh hữu hạn (finitely generated). vành $A$ là môđun trên chính nó và nó được sinh bởi đơn lẻ phần tử $1$. Hơn nữa, mọi môđun con của $A$ là lý tưởng (ideal), do đó giả thiết suy ra rằng mọi lý tưởng (ideal) trong $A$ là sinh hữu hạn (finitely generated), mà chỉ ra rằng $A$ là Noetherian. Bây giờ, giả sử $A$ là Noetherian. Thứ nhất, nhận thấy rằng nó là đủ để chứng minh định lý cho sinh hữu hạn (finitely generated) các môđun tự do $A^{n}$ (với $n \ge 1)$. Thật vậy, giả sử rằng ta được chứng minh với mọi $n \ge 1$ rằng mọi môđun con của $A^{n}$ là sinh hữu hạn (finitely generated). Nếu $M$ là bất kỳ sinh hữu hạn (finitely generated) A-module, thì có một toàn ánh $\phi$: $A^{n} \to M$ với một số $n$ (ở đâu $n$ là số của các phần tử của hữu hạn sinh tập hợp cho $M)$. Cho trước bất kỳ môđun con $N$ của $M, L = \phi^{-1} (N)$ là

<!-- PAGE 1287 -->
Môđun con của $A^{n}$. Vì $A^{n}$ là sinh hữu hạn (finitely generated), môđun con $N$ của $A^{n}$ là sinh hữu hạn (finitely generated), và thì $N = \phi (L)$ là sinh hữu hạn (finitely generated). Nó vẫn còn để chứng minh định lý cho $M = A^{n}$. Ta tiến hành bằng quy nạp theo $n$. Cho $n = 1$, môđun con $N$ của $A$ là lý tưởng (ideal), và vì $A$ là Noetherian, $N$ là sinh hữu hạn (finitely generated). Cho quy nạp bước ở đâu $n > 1$, xét phép chiếu $\pi$: $A^{n} \to A^{n-1}$ cho trước bởi
$$\pi (a_{1}, \dots  , a_{n}) = (a_{1}, \dots  , a_{n-1}).$$
Hạt nhân (kernel) của $\pi$ là môđun
$$\mathrm{Ker} (\pi ) = {(0, \dots  , 0, a_{n}) \in A^{n}| a_{n} \in A} \approx A.$$
Với mọi môđun con $N$ của $A^{n}$, cho $\phi$: $N \to A^{n-1}$ là thu hẹp của $\pi$ đến $N$. Vì $\phi (N)$ là môđun con của $A^{n-1}$, theo giả thiết quy nạp, $Im(\phi$) $= \phi (N)$ là sinh hữu hạn (finitely generated). Cũng, Ker $(\phi$) $= N \cap$ Ker $(\pi$) là môđun con của Ker $(\pi$) $\approx A$, và do đó Ker $(\phi$) là đẳng cấu đến lý tưởng (ideal) của $A$, và do đó là sinh hữu hạn (finitely generated) (vì $A$ là Noetherian). Vì cả hai $Im(\phi$) và Ker $(\phi$) là sinh hữu hạn (finitely generated), theo Mệnh đề 35.9, môđun con $N$ là cũng sinh hữu hạn (finitely generated). Hệ quả là của Định lý 35.10, mọi sinh hữu hạn (finitely generated) A-module trên Vành Noether (Noetherian ring) $A$ là một cách hữu hạn được trình bày, bởi vì nếu $\phi$: $A^{n} \to M$ là toàn ánh lên sinh hữu hạn (finitely generated) môđun $M$, thì Ker $(\phi$) là sinh hữu hạn (finitely generated). Đặc biệt, nếu $A$ là PID, thì mọi sinh hữu hạn (finitely generated) môđun là một cách hữu hạn được trình bày. Nếu vành $A$ là không Noetherian, thì ở đó tồn tại sinh hữu hạn (finitely generated) A-modules rằng là không một cách hữu hạn được trình bày. Điều này là không do đó dễ để chứng minh. Ta sẽ chứng minh trong Mệnh đề 35.35 rằng nếu $A$ là PID thì ma trận $R$ có thể “được chéo hóa” như
$$R = QDP^{-1}$$
Ở đâu $D$ là ma trận đường chéo (diagonal matrix) (nhiều hơn/thêm tính toán các phiên bản của mệnh đề này là cho trước trong Định lý 36.18 và Định lý 36.21). Suy ra từ Mệnh đề 35.8 rằng mọi sinh hữu hạn (finitely generated) môđun $M$ trên PID có trình bày với $m$ các phần tử sinh và $r$ các quan hệ của tạo thành
$$\alpha_{i} e_{i} = 0,$$
Ở đâu $\alpha_{i}  \neq  0$ và $\alpha_{1}$ | $\alpha_{2}$ | $\cdots$ | $\alpha_{r}$, mà chỉ ra rằng $M$ là đẳng cấu đến tổng trực tiếp (direct sum)
$$M \approx A^{m-r}\oplus A/(\alpha_{1} A) \oplus \cdots  \oplus A/(\alpha_{r} A).$$
Điều này là phiên bản của Định lý 35.25 rằng sẽ được chứng minh trong Mục 35.5.
