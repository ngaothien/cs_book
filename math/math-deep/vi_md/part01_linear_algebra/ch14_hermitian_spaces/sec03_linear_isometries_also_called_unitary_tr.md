# Tuyến tính Các phép đẳng cự (Cũng Được gọi là Unita Các phép biến đổi)


<!-- PAGE 544 -->

## 14.3 Tuyến tính Các phép đẳng cự (Cũng Được gọi là Unita Transfor-

$$mations)$$
Trong mục này ta xét các ánh xạ tuyến tính (linear maps) giữa Các không gian Hermite rằng bảo toàn Hermite chuẩn (norm). Tất cả các định nghĩa cho trước cho Các không gian Euclid trong Mục 12.5 mở rộng đến Các không gian Hermite, ngoại trừ rằng trực giao các phép biến đổi được gọi là unita phép biến đổi, nhưng Mệnh đề 12.12 mở rộng chỉ với được sửa đổi Điều kiện $(2)$. Thật vậy, old chứng minh rằng $(2)$ suy ra
$(3)$ thực hiện không hoạt động/công trình, và implication là thực ra sai! Nó có thể được repaired bởi strengthening Điều kiện $(2)$. Cho sake của tính đầy đủ, ta phát biểu Hermite phiên bản của Định nghĩa 12.5.

> **Định nghĩa 14.7.** Cho trước bất kỳ hai không tầm thường Các không gian Hermite $E$ và $F$ của cùng hữu hạn số chiều $n$, hàm $f$: $E \to F$ là unita phép biến đổi, hoặc tuyến tính phép đẳng cự (isometry), nếu nó là tuyến tính và
$$\|f(u)\|= \|u\|,for all u \in E.$$
Mệnh đề 12.12 có thể được salvaged bởi strengthening Điều kiện $(2)$.

> **Mệnh đề 14.14.** Cho trước bất kỳ hai không tầm thường Các không gian Hermite $E$ và $F$ của cùng hữu hạn số chiều $n$, với mọi hàm $f$: $E \to F$, các tính chất sau đây là tương đương:
$(1) f$ là ánh xạ tuyến tính (linear map) và $\|f(u)\| = \|u\|$, với mọi $u \in E$;
$(2) \|f(v)$ - $f(u)\| = \|v$ - $u\|$ và f(iu) $=$ nếu(u), với mọi $u, v \in E$.
$(3)$ f(u) $\cdot$ f(v) $= u \cdot  v$, với mọi $u, v \in E$. Hơn nữa, như vậy ánh xạ là song ánh (bijective).

*Chứng minh.* chứng minh rằng $(2)$ suy ra $(3)$ cho trước trong Mệnh đề 12.12 cần là revised như sau. Ta sử dụng phân cực đồng nhất thức
$$2\phi (u, v) = (1 + i)(\|u\|^{2}+ \|v\|^{2}) -\|u -v\|^{2}-i\|u -iv\|^{2}.$$
Vì f(iv) $=$ nếu(v), ta thu được f(0) $= 0$ bằng cách đặt $v = 0$, do đó hàm $f$ bảo toàn khoảng cách và chuẩn (norm), và ta thu được
$$2\phi (f(u), f(v)) = (1 + i)(\|f(u)\|^{2}+ \|f(v)\|^{2}) -\|f(u) -f(v)\|^{2}$$
$$-i\|f(u) -if(v)\|^{2}$$
$$= (1 + i)(\|f(u)\|^{2}+ \|f(v)\|^{2}) -\|f(u) -f(v)\|^{2}$$
$$-i\|f(u) -f(iv)\|^{2}$$
$$= (1 + i)(\|u\|^{2}+ \|v\|^{2}) -\|u -v\|^{2}-i\|u -iv\|^{2}$$
$$= 2\phi (u, v),$$
Mà chỉ ra rằng $f$ bảo toàn Hermite tích vô hướng (inner product) như mong muốn. rest của chứng minh là unchanged.
