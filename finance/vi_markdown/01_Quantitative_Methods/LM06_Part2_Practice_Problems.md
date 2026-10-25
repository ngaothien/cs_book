# Tập 1: Phương pháp Định lượng (*Quantitative Methods*)
## Học phần 6: Các Phương pháp Mô phỏng (*Simulation Methods*)
### Phần 2/2: Bài tập Thực hành (*Practice Problems*) (Trang PDF 199–200)

---

<!-- PDF Page 199 -->

# **BÀI TẬP THỰC HÀNH (*PRACTICE PROBLEMS*)** 

**1.** Giá đóng cửa hàng tuần của cổ phiếu Mordice Corporation như sau: 

**Minh họa 1: Cổ phiếu Mordice Corporation (*Exhibit 1: Mordice Corporation Shares*)** 

|**Ngày (*Date*)**|**Giá Đóng cửa (*Closing Price*) (euro)**|
|---|---|
|1 tháng 8 (*1 August*)|112|
|8 tháng 8 (*8 August*)|160|
|15 tháng 8 (*15 August*)|120|

Tỷ suất sinh lợi ghép lãi liên tục (*continuously compounded return*) của cổ phiếu Mordice Corporation trong giai đoạn từ ngày 1 tháng 8 đến ngày 15 tháng 8 _gần nhất_ với: 

- **A.** 6.90%. 
- **B.** 7.14%. 
- **C.** 8.95%. 

**2.** Trái ngược với phân phối chuẩn (*normal distributions*), phân phối log-chuẩn (*lognormal distributions*): 

- **A.** bị lệch trái (*skewed to the left*). 
- **B.** có các kết quả đầu ra không thể nhận giá trị âm (*cannot be negative*). 
- **C.** phù hợp để mô tả tỷ suất sinh lợi tài sản hơn là giá tài sản. 

**3.** Phân phối log-chuẩn là một mô hình chính xác hơn cho phân phối của giá cổ phiếu so với phân phối chuẩn bởi vì giá cổ phiếu: 

- **A.** có tính đối xứng (*symmetrical*). 
- **B.** không bị giới hạn (*unbounded*). 
- **C.** không âm (*non-negative*). 

**4.** Các nhà phân tích thực hiện phương pháp lấy mẫu tự thân (*bootstrap*): 

- **A.** tìm cách tạo ra các suy luận thống kê về các tham số tổng thể từ một mẫu duy nhất. 
- **B.** liên tục rút ra các mẫu có cùng kích thước, có hoàn lại (*with replacement*), từ tổng thể ban đầu. 
- **C.** phải chỉ định các phân phối xác suất cho các yếu tố rủi ro chính dẫn dắt các biến ngẫu nhiên cơ sở. 


<!-- PDF Page 200 -->

# **LỜI GIẢI (*SOLUTIONS*)** 

1. **A đúng.** Tỷ suất sinh lợi ghép lãi liên tục của một tài sản trong một kỳ bằng logarit tự nhiên của thay đổi giá tài sản trong kỳ đó. Trong trường hợp này, $\ln(120/112) = 6.90\%$. 

Lưu ý rằng tỷ suất sinh lợi ghép lãi liên tục từ kỳ $0$ đến kỳ $T$ là tổng của các tỷ suất sinh lợi ghép lãi liên tục tăng thêm trong từng kỳ đơn lẻ, mà trong trường hợp này là tỷ suất sinh lợi hàng tuần. Cụ thể: 

Tỷ suất sinh lợi Tuần 1: $\ln(160/112) = 35.67\%$. 

Tỷ suất sinh lợi Tuần 2: $\ln(120/160) = -28.77\%$. 

Tỷ suất sinh lợi ghép lãi liên tục $= 35.67\% + (-28.77\%) = 6.90\%$. 

2. **B đúng.** Theo định nghĩa, các biến ngẫu nhiên log-chuẩn không thể có giá trị âm (bị chặn dưới bởi 0) và có phân phối lệch phải (*skewed to the right*). 

3. **C đúng.** Một biến có phân phối log-chuẩn có cận dưới bằng không (*lower bound of zero*). Phân phối log-chuẩn cũng lệch phải, đây là một đặc tính hữu ích trong việc mô tả giá tài sản. 

4. **A đúng.** Phương pháp tự thân (*bootstrapping*) thông qua lấy mẫu ngẫu nhiên tạo ra biến quan sát từ việc lấy mẫu ngẫu nhiên với các tham số tổng thể chưa biết. Nhà phân tích không biết phân phối thực sự của tổng thể, nhưng thông qua việc lấy mẫu lại có thể suy luận ra các tham số tổng thể từ mẫu được tạo ngẫu nhiên. B sai bởi vì khi thực hiện bootstrap, nhà phân tích liên tục rút các mẫu từ *mẫu ban đầu* (*original sample*) chứ không phải từ *tổng thể* (*population*), trong đó mỗi mẫu lấy lại (*resample*) riêng lẻ có cùng kích thước với mẫu ban đầu và mỗi phần tử được rút ra đều được hoàn lại cho lần rút tiếp theo. C sai bởi vì khi thực hiện bootstrap, các nhà phân tích chỉ đơn giản sử dụng phân phối thực nghiệm quan sát được (*observed empirical distribution*) của các biến cơ sở. Ngược lại, trong mô phỏng Monte Carlo, nhà phân tích mới phải chỉ định các phân phối xác suất cho các yếu tố rủi ro chính dẫn dắt các biến cơ sở. 
