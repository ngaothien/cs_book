# Tập 6: Thu nhập Cố định (Fixed Income)
## Học phần 9: Cấu trúc Kỳ hạn của Lãi suất: Đường cong Lãi suất Giao ngay, Đường cong Lãi suất Ngang giá và Đường cong Lãi suất Kỳ hạn (The Term Structure of Interest Rates: Spot, Par, and Forward Curves)
### Phần 1/3: Giới thiệu (Trang PDF 221–230)

---

<!-- PDF Page 221 -->

#### H Ọ C P H Ầ N 

# **<mark>9</mark>** 

### **Cấu trúc Kỳ hạn của Lãi suất: Đường cong Lãi suất Giao ngay, Đường cong Lãi suất Ngang giá và Đường cong Lãi suất Kỳ hạn (*The Term Structure of Interest Rates: Spot, Par, and Forward Curves*)** 

###### **<mark>MỤC TIÊU HỌC TẬP (*LEARNING OUTCOMES*)</mark>** 

|**_Mức độ thành thạo_**|**_Ứng viên cần có khả năng:_**|
|---|---|
||định nghĩa lãi suất giao ngay (*spot rates*) và đường cong lãi suất giao ngay (*spot curve*), đồng thời tính giá của một trái phiếu bằng cách sử dụng lãi suất giao ngay|
||định nghĩa lãi suất ngang giá (*par rates*) và lãi suất kỳ hạn (*forward rates*), đồng thời tính lãi suất ngang giá, lãi suất kỳ hạn từ lãi suất giao ngay, lãi suất giao ngay từ lãi suất kỳ hạn, và giá của một trái phiếu bằng cách sử dụng lãi suất kỳ hạn|
||so sánh đường cong lãi suất giao ngay (*spot curve*), đường cong lãi suất ngang giá (*par curve*), và đường cong lãi suất kỳ hạn (*forward curve*)|



##### **GIỚI THIỆU (*INTRODUCTION*)** 

**<mark>1</mark>** 

Các bài học trước đã định giá các công cụ thu nhập cố định bằng cách chiết khấu tất cả các dòng tiền tương lai theo một mức lãi suất duy nhất, chẳng hạn như lợi suất đáo hạn (*yield-to-maturity*) hoặc lãi suất tham chiếu thị trường (*market reference rate* – MRR) cộng với biên độ chiết khấu (*discount margin*). Ba bài học tiếp theo sẽ nới lỏng giả định này bằng cách giới thiệu **cấu trúc kỳ hạn của lãi suất (*term structure of interest rates*)**, hay thực tế là lãi suất thay đổi theo thời gian đáo hạn. Dữ liệu lý tưởng để sử dụng cho việc phân tích cấu trúc kỳ hạn là các trái phiếu không trả lãi định kỳ (*zero-coupon bonds*) phi rủi ro vỡ nợ, được gọi là **lãi suất giao ngay (*spot rates*)** hoặc **đường cong lãi suất giao ngay (*spot curve*)**. Vì những dữ liệu này nhìn chung không thể quan sát trực tiếp được, nên nhiều kỹ thuật ước tính khác nhau được sử dụng. Đường cong lãi suất giao ngay được sử dụng để suy ra hai đường cong lợi suất quan trọng khác: **đường cong lãi suất ngang giá (*par curve*)** và **đường cong lãi suất kỳ hạn (*forward curve*)**. Đường cong lãi suất ngang giá liên quan đến lợi suất trái phiếu của các chứng khoán chuẩn giả định được định giá ngang mệnh giá (*at par*), trong khi đường cong lãi suất kỳ hạn liên quan đến lãi suất cho các kỳ tính lãi bắt đầu trong tương lai. Cả ba đường cong này đều là nền tảng cho phân tích thu nhập cố định và các ứng dụng khác bởi vì chúng đại diện cho các tỷ suất sinh lợi phi rủi ro vỡ nợ cho các khoảng thời gian bắt đầu từ ngày hôm nay và trong tương lai. Chúng tôi sẽ trình bày việc định giá trái phiếu bằng cách sử dụng các mức lãi suất khác nhau này và thiết lập mối quan hệ giữa chúng. 

Hầu hết các ví dụ và bảng biểu được sử dụng xuyên suốt bài đọc có thể được tải xuống dưới dạng sổ làm việc Microsoft Excel. Mỗi trang tính trong sổ làm việc được gắn nhãn với số ví dụ hoặc số bảng biểu tương ứng trong văn bản. 


<!-- PDF Page 222 -->

###### **TỔNG QUAN HỌC PHẦN (*LEARNING MODULE OVERVIEW*)** 

- **Lãi suất giao ngay (*spot rates*)** là lãi suất chiết khấu thị trường trên các trái phiếu không trả lãi định kỳ (*zero-coupon bonds*) phi rủi ro vỡ nợ, đôi khi được gọi là **lãi suất zero (*zero rates*)**. Bằng cách sử dụng một chuỗi các lãi suất giao ngay trong việc tính giá trái phiếu, ta thu được mức giá trái phiếu không có chênh lệch giá (*no-arbitrage bond price*). 

- **Lãi suất ngang giá (*par rate*)** là lãi suất chiết khấu thị trường cho một kỳ hạn cụ thể dẫn đến việc một trái phiếu được định giá ngang mệnh giá (*at par*). Lãi suất ngang giá được suy ra từ các lãi suất giao ngay tính đến và bao gồm cả ngày đáo hạn. 

- **Lãi suất kỳ hạn hàm ý (*implied forward rates*)** được tính bằng cách sử dụng lãi suất giao ngay và có thể được diễn giải là tỷ suất sinh lợi tăng thêm, hay cận biên (*incremental, or marginal, return*), cho việc kéo dài thời gian đáo hạn thêm một kỳ nữa. Do đó, chúng phản ánh một **lãi suất tái đầu tư hòa vốn (*breakeven reinvestment rate*)**. 

- Vì lãi suất ngang giá và lãi suất kỳ hạn có thể được suy ra từ lãi suất giao ngay, nên hình dạng của đường cong lãi suất giao ngay có mối liên hệ chặt chẽ với hình dạng của đường cong lãi suất ngang giá và đường cong lãi suất kỳ hạn. 

- Trong các cấu trúc kỳ hạn dốc lên (*upward-sloping term structures*), lãi suất ngang giá sẽ thấp hơn lãi suất giao ngay tương ứng của chúng và lãi suất kỳ hạn sẽ lớn hơn lãi suất giao ngay. Trong các cấu trúc kỳ hạn dốc xuống (*downward-sloping term structures*), lãi suất ngang giá sẽ lớn hơn lãi suất giao ngay và lãi suất kỳ hạn sẽ thấp hơn lãi suất giao ngay. 

###### **TỰ ĐÁNH GIÁ HỌC PHẦN (*LEARNING MODULE SELF-ASSESSMENT*)** 

Các câu hỏi ban đầu này nhằm giúp bạn tự đánh giá mức độ hiểu biết hiện tại của mình về học phần này. 

1. Tính giá và lợi suất đáo hạn (YTM) của một trái phiếu kỳ hạn 3 năm, lãi suất coupon 1% có mệnh giá là 100 với các lãi suất giao ngay sau đây: 

|1 năm|1,0%|
|---|---|
|2 năm|1,5%|
|3 năm|2,0%|



###### **Lời giải:** 

Mức giá là 97,135: 

![](assets/Fixed_Income.pdf-0222-14.png)

<!-- Formula Text: PV  =    PMT _ (1 + Z 1) 1  +   PMT _ (1 + Z 2) 2  + ⋯  +  PMT + FV _ (1 + Z N) N PV  = 1 _ (1 + 0.01) 1  + 1 _ (1 + 0.015) 2  + 101 _ (1 + 0.02) 3 PV = 97.135 The YTM is 1.993%: PV  =    PMT _ (1 + r) 1  +   PMT _ (1 + r) 2  + ⋯  +  PMT + FV _ (1 + r) N 97.135  = 1 _ (1 + r) 1  + 1 _ (1 + r) 2  +   101 _ (1 + r) 3 r = 0.01993 = 1.993% -->
$$PV = \frac{PMT}{(1 + Z_1)^1} + \frac{PMT}{(1 + Z_2)^2} + \dots + \frac{PMT + FV}{(1 + Z_N)^N}$$
$$PV = \frac{1}{(1 + 0.01)^1} + \frac{1}{(1 + 0.015)^2} + \frac{101}{(1 + 0.02)^3}$$
$$PV = 97.135$$

YTM là 1,993%:

$$PV = \frac{PMT}{(1 + r)^1} + \frac{PMT}{(1 + r)^2} + \dots + \frac{PMT + FV}{(1 + r)^N}$$
$$97.135 = \frac{1}{(1 + r)^1} + \frac{1}{(1 + r)^2} + \frac{101}{(1 + r)^3}$$
$$r = 0.01993 = 1.993\%$$


<!-- PDF Page 223 -->

2. Định nghĩa những gì mà lãi suất ngang giá (*par rate*) đại diện trong bối cảnh định giá trái phiếu. 

###### **Lời giải:** 

   - Lãi suất ngang giá là lợi suất đáo hạn làm cho giá trị hiện tại của các dòng tiền của một trái phiếu (tức là giá của nó) bằng với mệnh giá (*par or face value*) của nó. 

3. Tính lãi suất kỳ hạn 1 năm hàm ý sau hai năm kể từ bây giờ (tức là 2y1y) với các lãi suất giao ngay sau đây, giả định ghép lãi hàng năm: 

|1 năm|1,0%|
|---|---|
|2 năm|1,5%|
|3 năm|2,0%|



###### **Lời giải:** 

- $$(1 + Z_A)^A \times (1 + IFR_{A,B-A})^{B-A} = (1 + Z_B)^B$$

$$(1 + 0.015)^2 \times (1 + IFR_{2,1})^1 = (1 + 0.02)^3 \implies IFR_{2,1} = 3.01\%$$
*(Lưu ý: Bản gốc ở câu 3 viết nhầm phép tính của 1y2y: $(1 + 0.01)^1 \times (1 + IFR_{2,1})^2 = (1 + 0.02)^3 \implies IFR_{2,1} = 2.50\%$, trong khi Câu 4 ngay bên dưới sử dụng kết quả đúng của 2y1y là $3.01\%$).*

4. Giải thích ý nghĩa kinh tế của kết quả lãi suất kỳ hạn được tính trong Câu hỏi 3. 

###### **Lời giải:** 

Lãi suất kỳ hạn 1 năm sau hai năm kể từ bây giờ (2y1y) ở mức 3,01% ngụ ý rằng các nhà đầu tư kỳ vọng lãi suất 1 năm sẽ là 3,01% vào cuối năm thứ hai. Điều này phản ánh mức lãi suất mà tại đó việc tái đầu tư sẽ mang lại kết quả như nhau trong thời hạn đầu tư 3 năm bất kể nhà đầu tư ban đầu mua một trái phiếu kỳ hạn 2 năm hay một trái phiếu kỳ hạn 3 năm. 

5. Đối chiếu lãi suất giao ngay (*spot rates*) và lãi suất kỳ hạn (*forward rates*). 

###### **Lời giải:** 

Lãi suất giao ngay phản ánh lãi suất đi vay và đầu tư đối với nguồn vốn ngay lập tức (hoặc trong vài ngày tới) trong kỳ hạn đã xác định, trong khi lãi suất kỳ hạn phản ánh lãi suất áp dụng cho các thỏa thuận đi vay hoặc đầu tư bắt đầu vào một ngày trong tương lai cho một kỳ hạn đã xác định. 

6. Đúng hay sai: Lãi suất kỳ hạn 1 năm cao hơn so với lãi suất giao ngay tương ứng của chúng khi đường cong lãi suất giao ngay dốc xuống (*downward sloping*). 

   - **A.** Đúng (*True*) 

   - **B.** Sai (*False*) 

###### **Lời giải:** 

Sai (*False*). Khi đường cong lãi suất giao ngay dốc xuống, đường cong lãi suất kỳ hạn 1 năm sẽ nằm bên dưới đường cong lãi suất giao ngay. Lãi suất giao ngay giảm dần đối với các kỳ hạn dài hơn ngụ ý rằng các nhà đầu tư nên kỳ vọng mức lãi suất tái đầu tư thấp hơn trong những năm tương lai, và đường cong lãi suất kỳ hạn phản ánh những kỳ vọng này. 


<!-- PDF Page 224 -->

## **<mark>2</mark>** 

##### **CẤU TRÚC KỲ HẠN CỦA LÃI SUẤT VÀ LÃI SUẤT GIAO NGAY (*MATURITY STRUCTURE OF INTEREST RATES AND SPOT RATES*)** 

định nghĩa lãi suất giao ngay và đường cong lãi suất giao ngay, đồng thời tính giá của một trái phiếu bằng cách sử dụng lãi suất giao ngay 

###### **Cấu trúc Kỳ hạn của Lãi suất (*Maturity Structure of Interest Rates*)** 

Giả sử lợi suất đáo hạn của một trái phiếu cao hơn so với một trái phiếu khác. Có một số lý do khả dĩ giải thích cho sự khác biệt này, bao gồm rủi ro tín dụng, các đồng tiền khác nhau, tính thanh khoản, sự khác biệt về thuế, và giả định về định kỳ (*periodicity*) được sử dụng trong phép tính lợi suất. Sự khác biệt về rủi ro tín dụng và tiền tệ đã được chứng minh trong các bài học trước, nơi các trái phiếu định danh bằng đồng euro kỳ hạn 30 năm của Romania (Bộ Tài chính) được phát hành ở mức lợi suất đáo hạn 4,657%, tức mức chênh lệch 411 bp so với trái phiếu của Cộng hòa Liên bang Đức. Một lý do khác khiến các trái phiếu có thể có lợi suất đáo hạn khác nhau là chúng có thời gian đáo hạn khác nhau. Nhân tố giải thích sự khác biệt về lợi suất này được gọi là **cấu trúc đáo hạn của lãi suất (*maturity structure of interest rates*)** hay **cấu trúc kỳ hạn của lãi suất (*term structure of interest rates*)**. 

Cấu trúc kỳ hạn được phân tích tốt nhất bằng cách sử dụng các trái phiếu có tất cả các đặc tính giống nhau _ngoại trừ_ thời gian đáo hạn; nghĩa là, các trái phiếu phải được định danh bằng cùng một đồng tiền và có cùng rủi ro tín dụng, tính thanh khoản, tình trạng thuế, và giả định về định kỳ, đồng thời chúng phải có cùng lãi suất coupon để mỗi trái phiếu có cùng mức độ rủi ro tái đầu tư coupon (*coupon reinvestment risk*). Bộ dữ liệu lý tưởng này sẽ là lợi suất đáo hạn trên một chuỗi các trái phiếu _không trả lãi định kỳ_ (*zero-coupon bonds*) phi rủi ro vỡ nợ, được gọi là **lãi suất giao ngay (*spot rates*)**, cho đầy đủ các kỳ hạn. Trái phiếu chính phủ của các thị trường phát triển thường được sử dụng cho mục đích này, bởi vì chúng đại diện cho mức rủi ro vỡ nợ thấp nhất trong số các tổ chức phát hành trên một thị trường nhất định. Tập hợp lại, bộ dữ liệu này là **đường cong lãi suất giao ngay (*spot curve*)** của trái phiếu chính phủ, đôi khi được gọi là đường cong zero hoặc đường cong “strip” (bởi vì các khoản thanh toán coupon bị “tách” – *“stripped”* – ra khỏi trái phiếu). 

Đường cong lãi suất giao ngay của trái phiếu chính phủ là lý tưởng để phân tích cấu trúc đáo hạn bởi vì nó đáp ứng tốt nhất giả định “các yếu tố khác không đổi” (*“other things being equal”*). Các trái phiếu chính phủ này được cho là có cùng đồng tiền, rủi ro tín dụng, tính thanh khoản, và tình trạng thuế. Quan trọng nhất, với tư cách là trái phiếu không trả lãi định kỳ, chúng không có rủi ro tái đầu tư coupon. Đường cong lãi suất giao ngay của trái phiếu chính phủ được minh họa trong Bảng 1 cho các kỳ hạn từ 1 đến 30 năm. Lợi suất hàng năm được biểu thị trên cơ sở trái phiếu trả lãi nửa năm một lần (*semiannual bond basis*), giúp thuận tiện cho việc so sánh với các trái phiếu trả coupon thực hiện thanh toán nửa năm một lần, giống như trái phiếu doanh nghiệp ở nhiều thị trường. 


<!-- PDF Page 225 -->

**Bảng 1: Đường cong Lãi suất Giao ngay (Zero) của Trái phiếu Chính phủ (*Exhibit 1: Government Bond Spot (Zero) Curve*)** 

![](assets/Fixed_Income.pdf-0225-03.png)

<!-- Picture Text: Yield-to-Maturity (%)<br>6<br>5<br>4<br>3<br>2<br>1<br>0<br>0 5 10 15 20 25 30<br>Time-to-Maturity (years)<br> -->
> **Chú thích hình ảnh:**
> - **Trục tung:** Lợi suất đáo hạn (*Yield-to-Maturity*) (%) (từ 0 đến 6)
> - **Trục hoành:** Thời gian đáo hạn (*Time-to-Maturity*) (năm) (từ 0 đến 30)

Đường cong lãi suất giao ngay trong Bảng 1 dốc lên và phẳng dần ở các thời gian đáo hạn dài hơn, có nghĩa là các trái phiếu chính phủ dài hạn hơn có lợi suất cao hơn so với các trái phiếu ngắn hạn hơn. Mô hình này là điển hình trong các điều kiện thị trường bình thường. Đôi khi, đường cong lãi suất giao ngay lại dốc xuống ở chỗ lợi suất ngắn hạn hơn lại cao hơn lợi suất dài hạn hơn. Những đường cong lãi suất giao ngay dốc xuống như vậy được gọi là **đường cong lợi suất đảo ngược (*inverted yield curves*)**. Các lý thuyết tìm cách giải thích hình dạng của đường cong lợi suất và những hàm ý của nó đối với các điều kiện thị trường tài chính trong tương lai sẽ được đề cập sau. 

Mặc dù một đường cong lãi suất giao ngay bao gồm các trái phiếu chính phủ không trả lãi định kỳ là lý tưởng cho việc phân tích, nhưng có một số vấn đề thực tiễn cần phải giải quyết. Thứ nhất, hầu hết các trái phiếu chính phủ được giao dịch sôi động đều thực hiện thanh toán coupon. Các trái phiếu trả coupon này có thể không có cùng tính thanh khoản và tình trạng thuế. Các trái phiếu cũ hơn (đã lưu hành lâu – *“seasoned”*) có xu hướng kém thanh khoản hơn so với các khoản nợ mới phát hành bởi vì chúng thuộc sở hữu của các nhà đầu tư tổ chức và cá nhân theo chiến lược “mua và nắm giữ” (*“buy-and-hold”*). Các chính phủ phát hành nợ mới cho các thời gian đáo hạn định kỳ—chẳng hạn, trái phiếu kỳ hạn 5 năm và 10 năm. Trái phiếu kỳ hạn 6 năm hiện tại có thể là một trái phiếu kỳ hạn 10 năm đã được phát hành cách đây 4 năm. Ngoài ra, bởi vì lãi suất biến động, các trái phiếu cũ hơn có thể được định giá ở mức chiết khấu hoặc phần trội so với mệnh giá, điều này có thể dẫn đến sự khác biệt về thuế bởi vì một số khu vực tài phán thuế phân biệt giữa lãi và lỗ vốn (*capital gains and losses*) với thu nhập tiền lãi (*interest income*). 

Do đó, trên thực tế, chỉ những trái phiếu chính phủ mới được phát hành gần đây nhất và được giao dịch sôi động nhất mới được sử dụng để xây dựng đường cong lợi suất. Những trái phiếu này có tính thanh khoản tương tự nhau, và bởi vì chúng được định giá gần với mệnh giá hơn, nên chúng có ít tác động về thuế hơn. Thêm vào đó, bởi vì có dữ liệu hạn chế cho đầy đủ các kỳ hạn, phương pháp nội suy (*interpolation*) được sử dụng để hoàn thiện đường cong. Bảng 2 minh họa một đường cong lợi suất cho một chính phủ phát hành các trái phiếu kỳ hạn 2 năm, 3 năm, 5 năm, 7 năm, 10 năm, và 30 năm thực hiện thanh toán coupon nửa năm một lần. Phương pháp nội suy tuyến tính (*straight-line interpolation*) được sử dụng giữa các điểm đó trên đường cong lợi suất. 


<!-- PDF Page 226 -->

**Bảng 2: Đường cong Lợi suất Trái phiếu Chính phủ Trả lãi Coupon (*Exhibit 2: Government Coupon Bond Yield Curve*)** 

![](assets/Fixed_Income.pdf-0226-03.png)

<!-- Picture Text: Yield-to-Maturity (%)<br>3.0<br>2.5<br>2.0<br>1.5<br>1.0<br>0.5<br>0<br>0 5 10 15 20 25 30<br>Time-to-Maturity (years)<br>Yield-to-Maturity (%)<br>0.20<br>0.15<br>0.10<br>0.05<br>0<br>1 3 6 12<br>Time-to-Maturity (months)<br> -->
> **Chú thích hình ảnh:**
> - **Biểu đồ chính:** Trục tung: Lợi suất đáo hạn (*Yield-to-Maturity*) (%) (0 đến 3,0); Trục hoành: Thời gian đáo hạn (*Time-to-Maturity*) (năm) (0 đến 30).
> - **Biểu đồ phóng to (góc dưới):** Trục tung: Lợi suất đáo hạn (*Yield-to-Maturity*) (%) (0 đến 0,20); Trục hoành: Thời gian đáo hạn (*Time-to-Maturity*) (tháng) (1, 3, 6, 12).

Bảng 2 cũng bao gồm lợi suất cho các chứng khoán chính phủ ngắn hạn có thời gian đáo hạn là 1 tháng, 3 tháng, 6 tháng, và 12 tháng. Mặc dù các công cụ thị trường tiền tệ này được phát hành và giao dịch trên cơ sở lãi suất chiết khấu, nhưng chúng được chuyển đổi sang lợi suất tương đương trái phiếu (*bond equivalent yields* – tức là lãi suất cộng thêm với một năm 365 ngày). Tất cả các trái phiếu trên đường cong lợi suất cũng cần được chuyển đổi sang cùng một định kỳ (*periodicity*) nhằm tạo thuận lợi cho việc so sánh giữa các thời gian đáo hạn khác nhau. Việc chuyển đổi từ lãi suất chiết khấu sang lợi suất tương đương trái phiếu và giữa các định kỳ đã được trình bày trong các bài học trước. 

###### **Định giá Trái phiếu Sử dụng Lãi suất Giao ngay (*Bond Pricing Using Spot Rates*)** 

Vì lãi suất thay đổi theo kỳ hạn và có cấu trúc kỳ hạn, chúng ta có thể định giá trái phiếu bằng cách sử dụng một chuỗi các lãi suất chiết khấu tương ứng với các ngày phát sinh dòng tiền. Một chuỗi như vậy, đại diện cho các mức lãi suất phi rủi ro vỡ nợ, chính là đường cong lãi suất giao ngay (*spot curve*). Giá trái phiếu được xác định bằng cách sử dụng lãi suất giao ngay sẽ thiết lập các mức giá “không có chênh lệch giá” (*“no-arbitrage” prices*); nếu giá của một trái phiếu khác với giá trị không có chênh lệch giá của nó, một cơ hội kinh doanh chênh lệch giá (*arbitrage opportunity*) sẽ tồn tại trong điều kiện không có chi phí giao dịch. 


<!-- PDF Page 227 -->

Giả sử lãi suất giao ngay 1 năm là 2%, lãi suất giao ngay 2 năm là 3%, và lãi suất giao ngay 3 năm là 4%. Khi đó, giá của một trái phiếu kỳ hạn 3 năm thanh toán coupon hàng năm ở mức 5% là 102,960: 

![](assets/Fixed_Income.pdf-0227-04.png)

<!-- Formula Text: 5 _ (1.02) 1  + 5 _ (1.03) 2  +   105 _ (1.04) 3  = -->
$$\frac{5}{(1.02)^1} + \frac{5}{(1.03)^2} + \frac{105}{(1.04)^3} =$$

###### $4.902 + 4.713 + 93.345 = 102.960$. 

Trái phiếu kỳ hạn 3 năm này được định giá ở mức phần trội (*at a premium*), vì vậy lợi suất đáo hạn của nó phải thấp hơn mức lãi suất coupon 5% của nó. Sử dụng công thức định giá trái phiếu cơ bản, lợi suất đáo hạn là 3,935%: 

![](assets/Fixed_Income.pdf-0227-07.png)

<!-- Formula Text: 102.960  = 5 _ (1 + r) 1  + 5 _ (1 + r) 2  +   105 _ (1 + r) 3 ; r  =  0.03935. -->
$$102.960 = \frac{5}{(1 + r)^1} + \frac{5}{(1 + r)^2} + \frac{105}{(1 + r)^3}; \quad r = 0.03935$$

Nếu các dòng tiền được chiết khấu bằng cách sử dụng lợi suất đáo hạn, ta cũng thu được mức giá tương tự: 

![](assets/Fixed_Income.pdf-0227-09.png)

<!-- Formula Text: 5 _ (1.03935) 1  + 5 _ (1.03935) 2  + 105 _ (1.03935) 3  = -->
$$\frac{5}{(1.03935)^1} + \frac{5}{(1.03935)^2} + \frac{105}{(1.03935)^3} =$$

$4.811 + 4.629 + 93.520 = 102.960$. 

Hãy chú ý rằng giá trị hiện tại của từng dòng tiền riêng lẻ được chiết khấu bằng lãi suất giao ngay khác với khi được chiết khấu bằng lợi suất đáo hạn. Giá trị hiện tại của khoản thanh toán coupon đầu tiên là 4,902 khi được chiết khấu ở mức 2%, nhưng là 4,811 khi được chiết khấu ở mức 3,935%. Giá trị hiện tại của dòng tiền cuối cùng, bao gồm cả khoản hoàn trả tiền gốc, là 93,345 ở mức 4% và 93,520 ở mức 3,935%. Tuy nhiên, tổng giá trị hiện tại khi sử dụng một trong hai phương pháp đều là 102,960. 

Phương trình 1 là một công thức tổng quát để tính giá trái phiếu khi biết chuỗi các lãi suất giao ngay. Lưu ý rằng để định giá một trái phiếu có hồ sơ rủi ro khác với đường cong lãi suất giao ngay (chẳng hạn như rủi ro tín dụng, ví dụ như đối với trái phiếu doanh nghiệp), một mức chênh lệch (*spread*) sẽ phải được cộng thêm vào các lãi suất giao ngay. 

![](assets/Fixed_Income.pdf-0227-13.png)

<!-- Formula Text: PV  =    PMT _ (1 + Z 1) 1  +   PMT _ (1 + Z 2) 2  + ⋯  +  PMT + FV _ (1 + Z N) N , (1) -->
$$PV = \frac{PMT}{(1 + Z_1)^1} + \frac{PMT}{(1 + Z_2)^2} + \dots + \frac{PMT + FV}{(1 + Z_N)^N} \tag{1}$$

trong đó: 

- $Z_1$ là lãi suất giao ngay (*spot rate*), hay lợi suất trái phiếu không trả lãi định kỳ (*zero-coupon yield*) hoặc lãi suất zero (*zero rate*), cho kỳ 1 

- $Z_2$ là lãi suất giao ngay, hay lợi suất trái phiếu không trả lãi định kỳ hoặc lãi suất zero, cho kỳ 2 

- $Z_N$ là lãi suất giao ngay, hay lợi suất trái phiếu không trả lãi định kỳ hoặc lãi suất zero, cho kỳ $N$ 

Chúng ta sẽ sử dụng lãi suất giao ngay trên trái phiếu chính phủ Canada và Úc để minh họa việc định giá trái phiếu bằng lãi suất giao ngay. 


<!-- PDF Page 228 -->

**Bảng 3: Lãi suất Giao ngay của Trái phiếu Chính phủ: Canada và Úc (*Exhibit 3: Government Bond Spot Rates: Canada and Australia*)** 

![](assets/Fixed_Income.pdf-0228-03.png)

<!-- Picture Text: Spot Rates (%)<br>3.0<br>2.5<br>2.0<br>1.5<br>1.0<br>0.5<br>0<br>1 2 3 4 5 7 10 20 30<br>Years until Maturity<br>Canada Australia<br> -->
> **Chú thích hình ảnh:**
> - **Trục tung:** Lãi suất giao ngay (*Spot Rates*) (%) (từ 0 đến 3,0)
> - **Trục hoành:** Số năm cho đến khi đáo hạn (*Years until Maturity*) (1, 2, 3, 4, 5, 7, 10, 20, 30)
> - **Đường biểu diễn:** Canada và Úc (*Australia*)

![](assets/Fixed_Income.pdf-0228-04.png)

<!-- Picture Text: Maturity<br>(Years) 1 2 3 4 5 7 10 20 30<br>Canada 0.31% 0.57% 0.80% 0.96% 1.11% 1.30% 1.58% 1.98% 2.06%<br>Australia 0.03% 0.07% 0.30% 0.59% 0.81% 1.17% 1.52% 2.35% 2.47%<br> -->

| Kỳ hạn (*Maturity*) (Năm) | 1 | 2 | 3 | 4 | 5 | 7 | 10 | 20 | 30 |
|---|---|---|---|---|---|---|---|---|---|
| **Canada** | 0,31% | 0,57% | 0,80% | 0,96% | 1,11% | 1,30% | 1,58% | 1,98% | 2,06% |
| **Úc (*Australia*)** | 0,03% | 0,07% | 0,30% | 0,59% | 0,81% | 1,17% | 1,52% | 2,35% | 2,47% |

###### **VÍ DỤ 1** 

###### **Giá Trái phiếu và Lợi suất Đáo hạn Dựa trên Lãi suất Giao ngay (*Bond Prices and Yields-to-Maturity Based on Spot Rates*)** 

1. Tính giá (trên mỗi 100 đơn vị mệnh giá) của một trái phiếu chính phủ Canada kỳ hạn 5 năm có lãi suất coupon 1,00% với các lãi suất giao ngay được hiển thị trong Bảng 3. 

###### **Lời giải:** 

99,50. Để tính giá của trái phiếu, chúng ta sử dụng Phương trình 1 và các lãi suất giao ngay được cung cấp cho từng dòng tiền. 

![](assets/Fixed_Income.pdf-0228-10.png)

<!-- Formula Text: PV  =    PMT _ (1 + Z 1) 1  +   PMT _ (1 + Z 2) 2  + ⋯  +  PMT + FV _ (1 + Z N) N . PV  = 1 _ (1 + 0.0031) 1  + 1 _ (1 + 0.0057) 2  + 1 _ (1 + 0.0080) 3  + 1 _ (1 + 0.0096) 4  + 101 _ (1 + 0.0111) 5 . PV = 99.50. -->
$$PV = \frac{PMT}{(1 + Z_1)^1} + \frac{PMT}{(1 + Z_2)^2} + \dots + \frac{PMT + FV}{(1 + Z_N)^N}$$
$$PV = \frac{1}{(1 + 0.0031)^1} + \frac{1}{(1 + 0.0057)^2} + \frac{1}{(1 + 0.0080)^3} + \frac{1}{(1 + 0.0096)^4} + \frac{101}{(1 + 0.0111)^5}$$
$$PV = 99.50$$

2. Tính giá (trên mỗi 100 đơn vị mệnh giá) của một trái phiếu chính phủ Úc kỳ hạn 5 năm có lãi suất coupon 0,80% với các lãi suất giao ngay được hiển thị trong Bảng 3. 

###### **Lời giải:** 

99,99. Để tính giá của trái phiếu, chúng ta sử dụng Phương trình 1 và các lãi suất giao ngay được cung cấp cho từng dòng tiền. 

![](assets/Fixed_Income.pdf-0228-14.png)

<!-- Formula Text: PV  =    PMT _ (1 + Z 1) 1  +   PMT _ (1 + Z 2) 2  + ⋯  +  PMT + FV _ (1 + Z N) N . PV  = 0.80 _ (1 + 0.0003) 1  + 0.80 _ (1 + 0.0007) 2  + 0.80 _ (1 + 0.0030) 3  + 0.80 _ (1 + 0.0059) 4  + 100.80 _ (1 + 0.0081) 5 . -->
$$PV = \frac{PMT}{(1 + Z_1)^1} + \frac{PMT}{(1 + Z_2)^2} + \dots + \frac{PMT + FV}{(1 + Z_N)^N}$$
$$PV = \frac{0.80}{(1 + 0.0003)^1} + \frac{0.80}{(1 + 0.0007)^2} + \frac{0.80}{(1 + 0.0030)^3} + \frac{0.80}{(1 + 0.0059)^4} + \frac{100.80}{(1 + 0.0081)^5}$$


<!-- PDF Page 229 -->

###### $PV = 99.99$ 

3. Tính YTM của trái phiếu chính phủ Canada kỳ hạn 5 năm, sử dụng mức giá thu được trong Câu hỏi 1. 

###### **Lời giải:** 

1,104%. Thay vì giải tìm giá, chúng ta sử dụng Phương trình 1 để giải tìm YTM, tức IRR làm cân bằng mức giá được tính trong Câu hỏi 1 với giá trị hiện tại của các dòng tiền tương lai. Trong Microsoft Excel hoặc Google Sheets, hàm RATE hoặc IRR có thể được sử dụng để giải tìm $r$. 

![](assets/Fixed_Income.pdf-0229-06.png)

<!-- Formula Text: PV  =    PMT _ (1 + r) 1  +   PMT _ (1 + r) 2  + ⋯  +  PMT + FV _ (1 + r) N 99.50  = 1 _ (1 + r) 1  + 1 _ (1 + r) 2  + 1 _ (1 + r) 3  + 1 _ (1 + r) 4  +   101 _ (1 + r) 5 = r = 0.011036 = 1.104% -->
$$PV = \frac{PMT}{(1 + r)^1} + \frac{PMT}{(1 + r)^2} + \dots + \frac{PMT + FV}{(1 + r)^N}$$
$$99.50 = \frac{1}{(1 + r)^1} + \frac{1}{(1 + r)^2} + \frac{1}{(1 + r)^3} + \frac{1}{(1 + r)^4} + \frac{101}{(1 + r)^5}$$
$$r = 0.011036 = 1.104\%$$

Hãy chú ý rằng lợi suất của trái phiếu trả coupon thấp hơn một chút so với lãi suất giao ngay 5 năm. 

###### **BỘ CÂU HỎI (*QUESTION SET*)** 

1. Đúng hay sai: Trên thực tế, đường cong lãi suất giao ngay (*spot curve*) được tạo ra bằng cách tính lợi suất đáo hạn trên các trái phiếu chính phủ trả coupon mới được phát hành gần đây có các kỳ hạn khác nhau. 

   - **A.** Đúng (*True*) 

   - **B.** Sai (*False*) 

###### **Lời giải:** 

Đúng (*True*). Mặc dù các trái phiếu chính phủ phi rủi ro không trả lãi định kỳ sẽ được ưu tiên hơn, nhưng trên thực tế, đường cong lãi suất giao ngay được tạo ra bằng cách sử dụng lợi suất trên các trái phiếu chính phủ trả coupon mới được phát hành gần đây và phương pháp nội suy tuyến tính. Những trái phiếu này thỏa mãn tốt nhất các điều kiện cho việc phân tích cấu trúc kỳ hạn. 

2. Xác định từ còn thiếu trong câu sau: Bởi vì thường có dữ liệu hạn chế để tính lợi suất cho đầy đủ các kỳ hạn, nên thông thường cần phải __________ giữa các lợi suất quan sát được để hoàn thiện dữ liệu đường cong. 

###### **Lời giải:** 

Bởi vì thường có dữ liệu hạn chế để tính lợi suất cho đầy đủ các kỳ hạn, nên thông thường cần phải **nội suy (*interpolate*)** giữa các lợi suất quan sát được để hoàn thiện dữ liệu đường cong. 

3. Tính giá và lợi suất đáo hạn của một trái phiếu kỳ hạn 5 năm, lãi suất coupon 2,5% với các lãi suất giao ngay sau đây. Giả định ghép lãi hàng năm. 

|1 năm|3,000%|
|---|---|
|2 năm|2,800%|
|3 năm|2,600%|


<!-- PDF Page 230 -->

![](assets/Fixed_Income.pdf-0230-03.png)

<!-- Picture Text: 4-year                   2.400%<br>5-year                   2.200%<br>Solution:<br> -->

|4 năm|2,400%|
|---|---|
|5 năm|2,200%|

###### **Lời giải:**

Mức giá là 101,314 (hoặc 101,34 theo làm tròn bên dưới). 

![](assets/Fixed_Income.pdf-0230-05.png)

<!-- Formula Text: PV  =    PMT _ (1 + Z 1) 1  +   PMT _ (1 + Z 2) 2  + ⋯  +  PMT + FV _ (1 + Z N) N . PV  = 2.50 _ (1 + 0.03) 1  + 2.50 _ (1 + 0.028) 2  + 2.50 _ (1 + 0.026) 3  + 2.50 _ (1 + 0.024) 4  + 102.50 _ (1 + 0.022) 5 . PV = 101.34 The YTM is 2.22%. PV  =    PMT _ (1 + r) 1  +   PMT _ (1 + r) 2  + ⋯  +  PMT + FV _ (1 + r) N 101.34  =    2.50 _ (1 + r) 1  +   2.50 _ (1 + r) 2  +   2.50 _ (1 + r) 3  +   2.50 _ (1 + r) 4  +  102.50 _ (1 + r) 5 r = 0.022195 = 2.22% -->
$$PV = \frac{PMT}{(1 + Z_1)^1} + \frac{PMT}{(1 + Z_2)^2} + \dots + \frac{PMT + FV}{(1 + Z_N)^N}$$
$$PV = \frac{2.50}{(1 + 0.03)^1} + \frac{2.50}{(1 + 0.028)^2} + \frac{2.50}{(1 + 0.026)^3} + \frac{2.50}{(1 + 0.024)^4} + \frac{102.50}{(1 + 0.022)^5}$$
$$PV = 101.34$$

YTM là 2,22%.

$$PV = \frac{PMT}{(1 + r)^1} + \frac{PMT}{(1 + r)^2} + \dots + \frac{PMT + FV}{(1 + r)^N}$$
$$101.34 = \frac{2.50}{(1 + r)^1} + \frac{2.50}{(1 + r)^2} + \frac{2.50}{(1 + r)^3} + \frac{2.50}{(1 + r)^4} + \frac{102.50}{(1 + r)^5}$$
$$r = 0.022195 = 2.22\%$$

4. Giả sử chúng ta quan sát thấy cấu trúc kỳ hạn sau đây đối với trái phiếu chính phủ Canada. Hãy tính giá của một trái phiếu chính phủ Canada kỳ hạn 3 năm, lãi suất coupon 0,50%. 

|**Kỳ hạn (*Maturity*)**|**Lợi suất đáo hạn (*Yield-to-maturity*)**|
|---|---|
|1 năm (*1-Year*)|1,1000%|
|2 năm (*2-Year*)|0,9500%|
|3 năm (*3-Year*)|0,7951%|
|4 năm (*4-Year*)|0,5700%|
|5 năm (*5-Year*)|0,3100%|



![](assets/Fixed_Income.pdf-0230-08.png)

<!-- Formula Text: Solution: The price is 99.126. PV  =    PMT _ (1 + Z 1) 1  +   PMT _ (1 + Z 2) 2  + ⋯  +  PMT + FV _ (1 + Z N) N . PV  = 0.50 _ (1 + 0.011) 1  + 0.50 _ (1 + 0.095) 2  + 100.50 ____________ (1 + 0.007951) 3 PV = 99.126 -->
###### **Lời giải:**

Mức giá là 99,126.

$$PV = \frac{PMT}{(1 + Z_1)^1} + \frac{PMT}{(1 + Z_2)^2} + \dots + \frac{PMT + FV}{(1 + Z_N)^N}$$
$$PV = \frac{0.50}{(1 + 0.011)^1} + \frac{0.50}{(1 + 0.0095)^2} + \frac{100.50}{(1 + 0.007951)^3}$$
$$PV = 99.126$$

5. Ví dụ 1 (trong sổ làm việc Excel đi kèm) có bao gồm một câu hỏi cho một trái phiếu chính phủ Canada kỳ hạn 3 năm, lãi suất coupon 0,50%, trong đó giá của trái phiếu cũng giống như mức giá 99,126 trong Câu hỏi 4 ở trên. Hãy đối chiếu các đường cong lãi suất giao ngay của Canada trong Ví dụ 1 và Câu hỏi 4, đồng thời giải thích tại sao hai đường cong lợi suất khác nhau này lại tạo ra cùng một kết quả định giá. 

###### **Lời giải:** 

Ví dụ 1 có một cấu trúc kỳ hạn dốc lên (*upward-sloping*), trong khi ở Câu hỏi 4, cấu trúc kỳ hạn lại dốc xuống (*downward sloping*). Một điểm tương đồng quan trọng là, bất chấp sự khác biệt rất lớn về <u>điểm xuất phát (tức là lãi suất giao ngay 1 năm)</u> 
