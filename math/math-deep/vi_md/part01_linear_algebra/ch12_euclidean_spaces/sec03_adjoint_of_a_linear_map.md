# Liên hợp (adjoint) của Ánh xạ tuyến tính (linear map)


<!-- PAGE 469 -->
Ở đâu $A = (a_{ij})$. Ta kiểm chứng được ngay rằng $s$ là dạng tuyến tính (linear form). Nó là dễ để kiểm tra rằng duy nhất ma trận $Z$ sao cho
$$\langle Z, A\rangle = s(A)for all A \in M_{n}(\mathbb{R})$$
Là ma trận $Z =$ các một(n, $n)$ có các phần tử (entries) là tất cả bằng $1$.

## 12.3 Liên hợp (adjoint) của Ánh xạ tuyến tính (linear map)

Sự tồn tại của đẳng cấu $\flat$: $E \to E^{*}$ là then chốt đến sự tồn tại của liên hợp (adjoint) các ánh xạ. importance của liên hợp (adjoint) các ánh xạ stems từ sự kiện rằng các ánh xạ tuyến tính (linear maps) phát sinh trong vật lý các bài tập là thường tự liên hợp (self-adjoint), mà có nghĩa là $f = f^{*}$. Hơn thế nữa, tự liên hợp (self-adjoint) các ánh xạ có thể được được chéo hóa trên các cơ sở trực chuẩn của các vectơ riêng (eigenvectors). Điều này là then chốt đến nghiệm của nhiều các bài tập trong cơ học và kỹ thuật nói chung (xem Strang $[175])$. Cho $E$ là Không gian Euclid (Euclidean space) của hữu hạn số chiều $n$, và cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map). Với mọi $u \in E$, ánh xạ
$$v \mapsto u \cdot  f(v)$$
Là rõ ràng dạng tuyến tính (linear form) trong $E^{*}$, và theo Định lý 12.6, tồn tại duy nhất một vectơ trong $E$ được ký hiệu bởi $f^{*} (u)$ sao cho
$$f^{*} (u) \cdot  v = u \cdot  f(v),$$
Với mọi $v \in E$. sau đây đơn giản mệnh đề chỉ ra rằng ánh xạ $f^{*}$ là tuyến tính.

> **Mệnh đề 12.8.** Cho trước Không gian Euclid (Euclidean space) $E$ của hữu hạn số chiều, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f^{*}$: $E \to E$ sao cho
$$f^{*} (u) \cdot  v = u \cdot  f(v),for all u, v \in E.$$

*Chứng minh.* Cho trước $u_{1}, u_{2} \in E$, vì tích vô hướng (inner product) là song tuyến tính, ta có
$$(u_{1} + u_{2}) \cdot  f(v) = u_{1} \cdot  f(v) + u_{2} \cdot  f(v),$$
Với mọi $v \in E$, và
$$(f^{*} (u_{1}) + f^{*} (u_{2})) \cdot  v = f^{*} (u_{1}) \cdot  v + f^{*} (u_{2}) \cdot  v,$$
Với mọi $v \in E$, và vì bởi giả định,
$$f^{*} (u_{1}) \cdot  v = u_{1} \cdot  f(v)andf^{*} (u_{2}) \cdot  v = u_{2} \cdot  f(v),$$
Với mọi $v \in E$. Do đó ta thu được
$$(f^{*} (u_{1}) + f^{*} (u_{2})) \cdot  v = (u_{1} + u_{2}) \cdot  f(v) = f^{*} (u_{1} + u_{2}) \cdot  v,$$
Với mọi $v \in E$. Vì của ta tích vô hướng (inner product) là xác định dương (positive definite), điều này suy ra rằng
$$f^{*} (u_{1} + u_{2}) = f^{*} (u_{1}) + f^{*} (u_{2}).$$

<!-- PAGE 470 -->
Tương tự,
$$(\lambda u) \cdot  f(v) = \lambda (u \cdot  f(v)),$$
Với mọi $v \in E$, và
$$(\lambda f^{*} (u)) \cdot  v = \lambda (f^{*} (u) \cdot  v),$$
Với mọi $v \in E$, và vì bởi giả định,
$$f^{*} (u) \cdot  v = u \cdot  f(v),$$
Với mọi $v \in E$, ta thu được
$$(\lambda f^{*} (u)) \cdot  v = \lambda (u \cdot  f(v)) = (\lambda u) \cdot  f(v) = f^{*} (\lambda u) \cdot  v$$
Với mọi $v \in E$. Vì $\flat$ là song ánh (bijective), điều này suy ra rằng
$$f^{*} (\lambda u) = \lambda f^{*} (u).$$
Do đó, $f^{*}$ là thật vậy ánh xạ tuyến tính (linear map), và nó là duy nhất vì $\flat$ là song ánh.

> **Định nghĩa 12.4.** Cho trước Không gian Euclid (Euclidean space) $E$ của hữu hạn số chiều, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, duy nhất ánh xạ tuyến tính (linear map) $f^{*}$: $E \to E$ sao cho
$$f^{*} (u) \cdot  v = u \cdot  f(v),for all u, v \in E$$
Cho trước theo Mệnh đề 12.8 được gọi là liên hợp (adjoint) của $f$ (w.r.t. đến tích vô hướng (inner product)). Các ánh xạ tuyến tính (linear maps) $f$: $E \to E$ sao cho $f = f^{*}$ được gọi là tự liên hợp (self-adjoint) các ánh xạ. Tự liên hợp (self-adjoint) các ánh xạ tuyến tính (linear maps) đóng rất quan trọng vai trò bởi vì chúng có thực các trị riêng (eigenvalues), và bởi vì các cơ sở trực chuẩn phát sinh từ các vectơ riêng (các vectơ riêng (eigenvectors)) của chúng. Hơn nữa, nhiều vật lý các bài tập dẫn đến đến tự liên hợp (self-adjoint) các ánh xạ tuyến tính (linear maps) (trong tạo thành của các ma trận đối xứng).
Nhận xét: Mệnh đề 12.8 vẫn nghiệm đúng nếu tích vô hướng (inner product) trên $E$ được thay thế bởi không suy biến dạng song tuyến tính đối xứng $\phi$. Các ánh xạ tuyến tính (linear maps) sao cho $f^{-1} = f^{*}$, hoặc tương đương
$$f^{*} \circ f = f \circ f^{*} = id,$$
Cũng đóng quan trọng vai trò. Chúng là tuyến tính các phép đẳng cự, hoặc các phép đẳng cự. Các phép quay là đặc biệt các loại của các phép đẳng cự. Một cái khác quan trọng lớp của các ánh xạ tuyến tính (linear maps) là các ánh xạ tuyến tính (linear maps) thỏa mãn tính chất
$$f^{*} \circ f = f \circ f^{*} ,$$
Được gọi là chuẩn tắc/bình thường các ánh xạ tuyến tính (linear maps). Ta sẽ xem sau này rằng chuẩn tắc/bình thường các ánh xạ có thể luôn luôn được chéo hóa trên các cơ sở trực chuẩn của các vectơ riêng (eigenvectors), nhưng điều này sẽ đòi hỏi bằng cách sử dụng Hermite tích vô hướng (inner product) (trên $\mathbb{C})$.
