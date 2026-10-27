# Tuyến tính Các phép đẳng cự (Trực giao Các phép biến đổi)


<!-- PAGE 479 -->
Các đa thức được sử dụng trong xấp xỉ lý thuyết và trong vật lý phát sinh bởi phù hợp lựa chọn của trọng số hàm $W$. Ngoài ra trước đó hai các ví dụ, Hermite các đa thức tương ứng với W(x) $= e^{-x2}$, Laguerre các đa thức đến W(x) $= e^{-x}$, và Jacobi các đa thức đến W(x) $= (1$ - $x)^{\alpha}(1 + x)^{\beta}$, với $\alpha , \beta  > -1$. Toàn diện treatments của trực giao các đa thức có thể được tìm thấy trong Lebedev $[118]$, Sansone $[150]$, và Andrews, Askey và Roy $[3]$. Ta có thể cũng chứng minh sau đây mệnh đề regarding trực giao các không gian.

> **Mệnh đề 12.11.** Cho trước bất kỳ không tầm thường Không gian Euclid (Euclidean space) $E$ của hữu hạn số chiều $n \ge 1$, với mọi không gian con $F$ có số chiều $k$, phần bù trực giao (orthogonal complement) $F^{\perp}$ của $F$ có số chiều $n$ - $k$, và $E = F \oplus F^{\perp}$. Hơn nữa, ta có $F^{\perp \perp} = F$.

*Chứng minh.* Từ Mệnh đề 12.9, không gian con $F$ có một số cơ sở trực chuẩn (orthonormal basis) $(u_{1}, \dots  , u_{k})$. Điều này độc lập tuyến tính (linearly independent) họ $(u_{1}, \dots  , u_{k})$ có thể được được mở rộng đến cơ sở (basis) $(u_{1}, \dots  , u_{k}, v_{k+1}, \dots  , v_{n})$, và theo Mệnh đề 12.10, nó có thể được được chuyển đổi đến cơ sở trực chuẩn (orthonormal basis) $(u_{1}, \dots  , u_{n})$, mà chứa $(u_{1}, \dots  , u_{k})$ như cơ sở trực chuẩn (orthonormal basis) của $F$. Bây giờ bất kỳ vectơ $w = w_{1}u_{1}+\cdots +w_{n}u_{n} \in E$ là trực giao đến $F$ khi và chỉ khi $w \cdot  u_{i} = 0$, với mọi $i$, ở đâu $1 \le i \le k$, khi và chỉ khi $w_{i} = 0$ với mọi $i$, ở đâu $1 \le i \le k$. Rõ ràng, điều này chỉ ra rằng $(u_{k+1}, \dots  , u_{n})$ là cơ sở (basis) của $F^{\perp}$, và do đó $E = F \oplus F^{\perp}$, và $F^{\perp}$ có số chiều $n$ - $k$. Tương tự, bất kỳ vectơ $w = w_{1}u_{1} + \cdots  + w_{n}u_{n} \in E$ là trực giao đến $F^{\perp}$ khi và chỉ khi $w \cdot  u_{i} = 0$, với mọi $i$, ở đâu $k + 1 \le i \le n$, khi và chỉ khi $w_{i} = 0$ với mọi $i$, ở đâu $k + 1 \le i \le n$. Do đó, $(u_{1}, \dots  , u_{k})$ là cơ sở (basis) của $F^{\perp \perp}$, và $F^{\perp \perp} = F$.

## 12.5 Tuyến tính Các phép đẳng cự (Trực giao Các phép biến đổi)

Trong mục này ta xét các ánh xạ tuyến tính (linear maps) giữa Các không gian Euclid rằng bảo toàn Euclidean chuẩn (norm). Các phần tử này các phép biến đổi, đôi khi được gọi là cứng motions, đóng quan trọng vai trò trong hình học.

> **Định nghĩa 12.5.** Cho trước bất kỳ hai không tầm thường Các không gian Euclid $E$ và $F$ của cùng hữu hạn số chiều $n$, hàm $f$: $E \to F$ là trực giao phép biến đổi, hoặc tuyến tính phép đẳng cự (isometry), nếu nó là tuyến tính và
$$\|f(u)\|= \|u\|,for all u \in E.$$
Các nhận xét:
$(1) A$ tuyến tính phép đẳng cự (isometry) là thường được định nghĩa như ánh xạ tuyến tính (linear map) sao cho
$$\|f(v) -f(u)\|= \|v -u\|,$$
Với mọi $u, v \in E$. Vì ánh xạ $f$ là tuyến tính, hai các định nghĩa là tương đương. thứ hai định nghĩa chỉ focuses trên bảo toàn khoảng cách giữa các vectơ.
$(2)$ Đôi khi, ánh xạ tuyến tính (linear map) thỏa mãn điều kiện của Định nghĩa 12.5 được gọi là một mêtric ánh xạ, và tuyến tính phép đẳng cự (isometry) được định nghĩa như song ánh (bijective) mêtric ánh xạ.

<!-- PAGE 480 -->
Phép đẳng cự (isometry) (mà không có word tuyến tính) đôi khi được định nghĩa như hàm $f$: $E \to F$ (không nhất thiết tuyến tính) sao cho
$$\|f(v) -f(u)\|= \|v -u\|,$$
Với mọi $u, v \in E$, i.e., như hàm rằng bảo toàn khoảng cách. Điều này requirement hóa ra là rất mạnh. Thật vậy, tiếp theo mệnh đề chỉ ra rằng tất cả các phần tử này các định nghĩa là tương đương khi $E$ và $F$ là của hữu hạn số chiều, và cho các hàm sao cho f(0) $= 0$.

> **Mệnh đề 12.12.** Cho trước bất kỳ hai không tầm thường Các không gian Euclid $E$ và $F$ của cùng hữu hạn số chiều $n$, với mọi hàm $f$: $E \to F$, các tính chất sau đây là tương đương:
$(1) f$ là ánh xạ tuyến tính (linear map) và $\|f(u)\| = \|u\|$, với mọi $u \in E$;
$(2) \|f(v)$ - $f(u)\| = \|v$ - $u\|$, với mọi $u, v \in E$, và f(0) $= 0$;
$(3)$ f(u) $\cdot$ f(v) $= u \cdot  v$, với mọi $u, v \in E$. Hơn nữa, như vậy ánh xạ là song ánh (bijective).

*Chứng minh.* Rõ ràng, $(1)$ suy ra $(2)$, vì trong $(1)$ nó được giả sử rằng $f$ là tuyến tính. Giả sử rằng $(2)$ nghiệm đúng. Thực ra, ta sẽ chứng minh slightly mạnh hơn kết quả. Ta chứng minh rằng nếu
$$\|f(v) -f(u)\|= \|v -u\|$$
Với mọi $u, v \in E$, thì với mọi vectơ $\tau  \in E$, hàm $g: E \to F$ được định nghĩa sao cho
$$g(u) = f(\tau  + u) -f(\tau )$$
Với mọi $u \in E$ là ánh xạ thỏa mãn Điều kiện $(2)$, và rằng $(2)$ suy ra $(3)$. Rõ ràng, g(0) $= f(\tau$) - $f(\tau$) $= 0$. Lưu ý rằng từ giả thiết
$$\|f(v) -f(u)\|= \|v -u\|$$
Với mọi $u, v \in E$, ta kết luận rằng
$$\|g(v) -g(u)\|= \|f(\tau  + v) -f(\tau ) -(f(\tau  + u) -f(\tau ))\|,$$
$$= \|f(\tau  + v) -f(\tau  + u)\|,$$
$$= \|\tau  + v -(\tau  + u)\|,$$
$$= \|v -u\|,$$
Với mọi $u, v \in E$. Vì g(0) $= 0$, bằng cách đặt $u = 0$ trong
$$\|g(v) -g(u)\|= \|v -u\|,$$

<!-- PAGE 481 -->
Ta thu được
$$\|g(v)\|= \|v\|$$
Với mọi $v \in E$. Nói cách khác, $g$ bảo toàn cả hai khoảng cách và chuẩn (norm). để chứng minh rằng $g$ bảo toàn tích vô hướng (inner product), ta sử dụng đơn giản sự kiện rằng
$$2u \cdot  v = \|u\|^{2}+ \|v\|^{2}-\|u -v\|^{2}$$
Với mọi $u, v \in E$. Khi đó vì $g$ bảo toàn khoảng cách và chuẩn (norm), ta có
$$2g(u) \cdot  g(v) = \|g(u)\|^{2}+ \|g(v)\|^{2}-\|g(u) -g(v)\|^{2}$$
$$= \|u\|^{2}+ \|v\|^{2}-\|u -v\|^{2}$$
$$= 2u \cdot  v,$$
Và do đó $g(u)\cdot$ g(v) $= u\cdot v$, với mọi $u, v \in E$, mà là $(3)$. Đặc biệt, nếu f(0) $= 0$, bởi đặt $\tau  = 0$, ta có $g = f$, và $f$ bảo toàn vô hướng (scalar) tích, i.e., $(3)$ nghiệm đúng. Bây giờ giả sử rằng $(3)$ nghiệm đúng. Vì $E$ là của hữu hạn số chiều, ta có thể chọn cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$ cho $E$. Vì $f$ bảo toàn trong các tích, $(f(e_{1}), \dots , f(e_{n}))$ là cũng trực chuẩn, và vì $F$ cũng có số chiều $n$, nó là cơ sở (basis) của $F$. Thì lưu ý rằng vì $(e_{1}, \dots  , e_{n})$ và $(f(e_{1}), \dots  , f(e_{n}))$ là các cơ sở trực chuẩn, với mọi $u \in E$ ta có
$$u = \sum_{i=1}^{n}  (u \cdot  e_{i})e_{i} = \sum_{i=1}^{n}  u_{i}e_{i}$$
Và
$$f(u) = \sum_{i=1}^{n}  (f(u) \cdot  f(e_{i}))f(e_{i}),$$
Và vì $f$ bảo toàn trong các tích, điều này chỉ ra rằng
$$f(u) = \sum_{i=1}^{n}  (f(u) \cdot  f(e_{i}))f(e_{i}) = \sum_{i=1}^{n}  (u \cdot  e_{i})f(e_{i}) = \sum_{i=1}^{n}  u_{i}f(e_{i}),$$
Mà chứng tỏ rằng $f$ là tuyến tính. Hiển nhiên, $f$ bảo toàn Euclidean chuẩn (norm), và $(3)$ suy ra $(1)$. Cuối cùng, nếu f(u) $=$ f(v), thì bởi tính tuyến tính f(v - $u) = 0$, sao cho $\|f(v$ - $u)\| = 0$, và vì $f$ bảo toàn các chuẩn, ta phải có $\|v$ - $u\| = 0$, và do đó $u = v$. Do đó, $f$ là đơn ánh (injective), và vì $E$ và $F$ có cùng hữu hạn số chiều, $f$ là song ánh (bijective).
Các nhận xét:
$(i)$ số chiều giả định là cần thiết chỉ để chứng minh rằng $(3)$ suy ra $(1)$ khi $f$ là không đã biết là tuyến tính, và để chứng minh rằng $f$ là toàn ánh (surjective), nhưng chứng minh chỉ ra rằng $(1)$ suy ra rằng $f$ là đơn ánh (injective).
