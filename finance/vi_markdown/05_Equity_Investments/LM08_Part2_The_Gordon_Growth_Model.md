# Tập 5: Đầu tư Cổ phiếu (Volume 5: Equity Investments)
## Học phần 8: Định giá Cổ phiếu: Các Khái niệm và Công cụ Cơ bản (Equity Valuation: Concepts and Basic Tools)
### Phần 2/4: Mô hình Tăng trưởng Gordon (The Gordon Growth Model) (Trang PDF 360–372)

---

<!-- PDF Page 360 -->

# **<mark>7</mark>** 

## **MÔ HÌNH TĂNG TRƯỞNG GORDON (THE GORDON GROWTH MODEL)** 

tính toán và diễn giải giá trị nội tại của một chứng khoán vốn dựa trên mô hình chiết khấu cổ tức tăng trưởng đều Gordon (*Gordon (constant) growth dividend discount model*) hoặc mô hình chiết khấu cổ tức hai giai đoạn (*two-stage dividend discount model*), tùy trường hợp phù hợp 

xác định các đặc điểm của những công ty phù hợp để áp dụng mô hình chiết khấu cổ tức tăng trưởng đều hoặc đa giai đoạn (*multistage dividend discount model*)
giải thích các ưu điểm và nhược điểm của từng nhóm mô hình định giá 

Một vấn đề khá hiển nhiên khi cố gắng áp dụng Phương trình 1 cho vốn chủ sở hữu phổ thông là phương trình này đòi hỏi chuyên gia phân tích phải ước tính một chuỗi vô hạn các khoản cổ tức dự kiến. Để đơn giản hóa quá trình này, các chuyên gia phân tích thường đưa ra những giả định về cách thức cổ tức sẽ tăng trưởng hoặc thay đổi theo thời gian. Mô hình tăng trưởng (đều) Gordon (*Gordon (constant) growth model* – Gordon, 1962) là một mô hình chiết khấu cổ tức (DDM) đơn giản và được công nhận rộng rãi. Mô hình này giả định cổ tức tăng trưởng vô thời hạn ở một tốc độ không đổi. 

Bởi vì giả định tốc độ tăng trưởng không đổi, mô hình tăng trưởng Gordon đặc biệt phù hợp để định giá vốn chủ sở hữu của các công ty có trả cổ tức, tương đối ít nhạy cảm với chu kỳ kinh doanh (*business cycle*) và đang ở giai đoạn tăng trưởng trưởng thành/bão hòa (*mature growth phase*). Các ví dụ có thể bao gồm một công ty tiện ích điện lực phục vụ một khu vực tăng trưởng chậm hoặc một nhà sản xuất mặt hàng thực phẩm thiết yếu (ví dụ: bánh mì). Lịch sử tăng cổ tức ở một tốc độ tăng trưởng ổn định là một tiêu chí thực tiễn khác nếu chuyên gia phân tích tin rằng khuôn mẫu đó sẽ tiếp tục duy trì trong tương lai. 

Với giả định tăng trưởng không đổi, Phương trình 1 có thể được viết lại thành Phương trình 8, trong đó $g$ là tốc độ tăng trưởng không đổi (*constant growth rate*): 

![](assets/Equity_Investments.pdf-0360-10.png)

<!-- Formula Text: V 0  =  ∑ t=1 ∞ D 0 (1 + g) t _ (1 + r) t    =  D 0 [ (1 + g) _ (1 + r)  + (1 + g) 2 _ (1 + r) 2  + ... + (1 + g) ∞ _ (1 + r) ∞ ] (8) -->

$$V_0 = \sum_{t=1}^{\infty} \frac{D_0(1 + g)^t}{(1 + r)^t} = D_0 \left[ \frac{(1 + g)}{(1 + r)} + \frac{(1 + g)^2}{(1 + r)^2} + \cdots + \frac{(1 + g)^\infty}{(1 + r)^\infty} \right] \tag{8}$$

Nếu tỷ suất sinh lợi yêu cầu $r$ được giả định là lớn hơn nghiêm ngặt so với tốc độ tăng trưởng $g$ ($r > g$), thì biểu thức trong ngoặc vuông ở Phương trình 8 là một cấp số nhân lùi vô hạn (*infinite geometric series*) và có tổng bằng $[(1 + g)/(r - g)]$. Thay vào Phương trình 8 sẽ tạo ra mô hình tăng trưởng Gordon như được trình bày trong Phương trình 9: 

![](assets/Equity_Investments.pdf-0360-12.png)

<!-- Formula Text: V 0  = D 0 (1 + g) _ r − g    = D 1 _ r − g (9) -->

$$V_0 = \frac{D_0(1 + g)}{r - g} = \frac{D_1}{r - g} \tag{9}$$

Để minh họa cho biểu thức này, giả sử cổ tức hàng năm hiện tại (gần đây nhất) của một cổ phiếu là €5.00 và cổ tức dự kiến sẽ tăng trưởng ở mức 4 phần trăm mỗi năm. Tỷ suất sinh lợi yêu cầu đối với vốn chủ sở hữu là 8 phần trăm. Do đó, ước tính giá trị nội tại theo mô hình tăng trưởng Gordon là $€5.00(1.04)/(0.08 - 0.04) = €5.20/0.04 = €130$ trên mỗi cổ phiếu. Lưu ý rằng tử số là $D_1$ chứ không phải $D_0$. (Sử dụng sai tử số là một lỗi phổ biến.) 

Mô hình tăng trưởng Gordon ước tính giá trị nội tại như là giá trị hiện tại của một niên kim vĩnh cửu tăng trưởng đều (*growing perpetuity*). Nếu tốc độ tăng trưởng, $g$, được giả định bằng 0, Phương trình 8 sẽ rút gọn về biểu thức tính giá trị hiện tại của một niên kim vĩnh cửu không đổi, đã được cho trước đó ở Phương trình 6. 

Khi ước tính tốc độ tăng trưởng dài hạn, các chuyên gia phân tích sử dụng nhiều phương pháp khác nhau, bao gồm việc đánh giá mức tăng trưởng của cổ tức hoặc thu nhập theo thời gian, sử dụng tốc độ tăng trưởng trung vị của ngành, và sử dụng mối quan hệ được trình bày trong Phương trình 10 để ước tính tốc độ tăng trưởng bền vững (*sustainable growth rate*): 

![](assets/Equity_Investments.pdf-0360-16.png)

<!-- Formula Text: g = b × ROE (10) -->

$$g = b \times \text{ROE} \tag{10}$$


<!-- PDF Page 361 -->

##### trong đó 

$g =$ tốc độ tăng trưởng cổ tức (*dividend growth rate*) 

$b =$ tỷ lệ lợi nhuận giữ lại (*earnings retention rate*) $= (1 - \text{Tỷ lệ chi trả cổ tức } [\text{Dividend payout ratio}])$ 

$\text{ROE} =$ tỷ suất sinh lợi trên vốn chủ sở hữu (*return on equity*) 

Ví dụ 7 minh họa việc áp dụng mô hình tăng trưởng Gordon đối với cổ phiếu của một công ty sản xuất công nghiệp lớn. Chuyên gia phân tích tin rằng công ty sẽ tiếp tục tăng trưởng ở tốc độ mà nó đã đạt được trong ba năm trước đó và duy trì ổn định trong tương lai. Ví dụ này đặt câu hỏi rằng giả định tăng trưởng cổ tức đóng góp bao nhiêu vào ước tính giá trị nội tại. Câu hỏi này có ý nghĩa liên quan đến việc định giá bởi vì nếu con số này cao xét theo tỷ lệ phần trăm, thì một phần lớn giá trị của cổ phiếu phụ thuộc vào việc hiện thực hóa ước tính tăng trưởng đó. Người ta có thể trả lời câu hỏi này bằng cách lấy ước tính giá trị nội tại được xác định bởi Phương trình 9 trừ đi giá trị được xác định bởi Phương trình 6 (vốn giả định cổ tức không tăng trưởng).<sup>3</sup> 

##### **VÍ DỤ 7 (EXAMPLE 7)** 

### **Áp dụng Mô hình Tăng trưởng Gordon (Applying the Gordon Growth Model)** 

Siemens AG hoạt động trong lĩnh vực tư liệu sản xuất (*capital goods*) và công nghệ. Công ty tham gia vào các lĩnh vực kỹ thuật, sản xuất chế tạo, tự động hóa, năng lượng và giao thông vận tải. Công ty hoạt động trên phạm vi toàn cầu và là một trong những tập đoàn lớn nhất trong các lĩnh vực mà mình tham gia. Đây là một nhà tuyển dụng lớn cả ở thị trường nội địa Đức nguyên bản lẫn tại hàng chục quốc gia trên khắp thế giới. Thông tin tài chính chọn lọc của Siemens xuất hiện trong Bảng minh họa 3 (Exhibit 3). 

**Bảng minh họa 3: Thông tin Tài chính Chọn lọc của Siemens AG (Exhibit 3: Selected Financial Information for Siemens AG)** 

|**Năm (Year)**|**2017**|**2016**|**2015**|**2014**|**2013**|
|---|---|---|---|---|---|
|EPS|€7.45|€6.74|€8.85|€6.37|€5.08|
|DPS|€3.7|€3.6|€3.5|€3.3|€3.0|
|Tỷ lệ chi trả cổ tức (*Payout ratio*)|50%|53%|40%|52%|59%|
|ROE|15.6%|15.9%|22.3%|18.2%|14.6%|
|Giá cổ phiếu (*Share price*)<br>(XETRA - Frankfurt)|€119.2|€104.2|€79.94|€94.37|€89.06|

_Lưu ý:_ DPS viết tắt của "cổ tức trên mỗi cổ phiếu (*dividends per share*)." 

_Nguồn:_ Morningstar, www.siemens.com. 

Chuyên gia phân tích ước tính tốc độ tăng trưởng vào khoảng 5.4 phần trăm dựa trên tốc độ tăng trưởng cổ tức trong giai đoạn từ năm 2013 đến năm 2017 $[3(1 + g)^4 = 3.7$, suy ra $g = 5.4\%]$. Để xác minh rằng tốc độ tăng trưởng ước tính 5.4 phần trăm là khả thi trong tương lai, chuyên gia phân tích cũng sử dụng mức trung bình của tỷ lệ lợi nhuận giữ lại và ROE của Siemens trong năm năm trước đó $(g \approx 0.49 \times 17.3\% \approx 8.5\%)$ để ước tính tốc độ tăng trưởng bền vững. 

Sử dụng một số cách tiếp cận, bao gồm việc cộng một phần bù rủi ro vào trái phiếu chính phủ Đức dài hạn và sử dụng mô hình CAPM, chuyên gia phân tích ước tính tỷ suất sinh lợi yêu cầu là 7.5 phần trăm. Khoản cổ tức gần nhất là €3.70 được sử dụng cho $D_0$. 


<!-- PDF Page 362 -->

1. Sử dụng mô hình tăng trưởng Gordon để ước tính giá trị nội tại của Siemens. 

#### **Lời giải:** 

![](assets/Equity_Investments.pdf-0362-05.png)

<!-- Formula Text: V 0  =   €3.70 (1 + 0.054) _____________ 0.075 − 0.054    =  €185.70 -->

$$V_0 = \frac{€3.70(1 + 0.054)}{0.075 - 0.054} = €185.70$$

2. Giả định tăng trưởng cổ tức đóng góp bao nhiêu vào ước tính giá trị nội tại? 

#### **Lời giải:** 

![](assets/Equity_Investments.pdf-0362-08.png)

<!-- Formula Text: €185.70 −  €3.70 _ 0.075   =  €136.37 -->

$$€185.70 - \frac{€3.70}{0.075} = €136.37$$

3. Dựa trên giá trị nội tại ước tính, một cổ phiếu của Siemens đang bị định giá thấp, định giá cao, hay định giá hợp lý? 

#### **Lời giải:** 

Một cổ phiếu của Siemens dường như đang bị định giá thấp (*undervalued* – vì giá thị trường năm 2017 là €119.2 thấp hơn €185.70). Trước khi đưa ra khuyến nghị, chuyên gia phân tích có thể cân nhắc xem các dữ liệu đầu vào ước tính có thực tế hay không và kiểm tra độ nhạy của giá trị ước tính đối với những thay đổi trong các dữ liệu đầu vào. 

4. Giá trị nội tại là bao nhiêu nếu ước tính tốc độ tăng trưởng được hạ xuống mức 4.4 phần trăm? 

#### **Lời giải:** 

![](assets/Equity_Investments.pdf-0362-14.png)

<!-- Formula Text: V 0  =   €3.70 (1 + 0.044) _____________ 0.075 − 0.044    =  €124.61 -->

$$V_0 = \frac{€3.70(1 + 0.044)}{0.075 - 0.044} = €124.61$$

5. Giá trị nội tại là bao nhiêu nếu ước tính tốc độ tăng trưởng được hạ xuống mức 4.4 phần trăm và ước tính tỷ suất sinh lợi yêu cầu được tăng lên mức 8.5 phần trăm? 

#### **Lời giải:** 

![](assets/Equity_Investments.pdf-0362-17.png)

<!-- Formula Text: V 0  =   €3.70 (1 + 0.044) _____________ 0.085 − 0.044    =  €94.21 -->

$$V_0 = \frac{€3.70(1 + 0.044)}{0.085 - 0.044} = €94.21$$

Ước tính giá trị nội tại theo mô hình tăng trưởng Gordon cực kỳ nhạy cảm với việc lựa chọn tỷ suất sinh lợi yêu cầu $r$ và tốc độ tăng trưởng $g$. Có khả năng là giả định tốc độ tăng trưởng và giả định tỷ suất sinh lợi yêu cầu được sử dụng ban đầu đã quá cao. Tăng trưởng kinh tế toàn cầu thường chỉ ở mức một chữ số thấp, điều này có thể đồng nghĩa với việc một công ty lớn như Siemens sẽ phải chật vật mới có thể tăng trưởng cổ tức ở mức 5.4 phần trăm mãi mãi. Bảng minh họa 4 (Exhibit 4) trình bày một phân tích độ nhạy sâu hơn đối với giá trị nội tại của Siemens theo các ước tính tỷ suất sinh lợi yêu cầu và tốc độ tăng trưởng. 

**Bảng minh họa 4: Phân tích Độ nhạy đối với Ước tính Giá trị Nội tại của Siemens AG (Exhibit 4: Sensitivity Analysis of the Intrinsic-Value Estimate for Siemens AG)** 

||**$g = 2.5\%$**|**$g = 3.5\%$**|**$g = 4.5\%$**|**$g = 5.5\%$**|**$g = 6.5\%$**|
|---|---|---|---|---|---|
|$r = 6\%$|€108.4|€153.2|€257.8|€780.7|—|
|$r = 7\%$|€84.3|€109.4|€154.7|€260.2|€788.1|
|$r = 8\%$|€69.0|€85.1|€110.5|€156.1|€262.7|


<!-- PDF Page 363 -->

||**$g = 2.5\%$**|**$g = 3.5\%$**|**$g = 4.5\%$**|**$g = 5.5\%$**|**$g = 6.5\%$**|
|---|---|---|---|---|---|
|$r = 9\%$|€58.3|€69.6|€85.9|€111.5|€157.6|
|$r = 10\%$|€50.6|€58.9|€70.3|€86.7|€112.6|

Lưu ý rằng không có giá trị nào được hiển thị khi tốc độ tăng trưởng vượt quá tỷ suất sinh lợi yêu cầu. Mô hình tăng trưởng Gordon giả định rằng tốc độ tăng trưởng không thể lớn hơn tỷ suất sinh lợi yêu cầu. 

Các giả định của mô hình Gordon bao gồm: 

- Cổ tức là thước đo chính xác để sử dụng cho mục đích định giá. 

- Tốc độ tăng trưởng cổ tức là mãi mãi: Nó là vĩnh cửu và không bao giờ thay đổi. 

- Tỷ suất sinh lợi yêu cầu cũng không đổi theo thời gian. 

- Tốc độ tăng trưởng cổ tức nhỏ hơn nghiêm ngặt so với tỷ suất sinh lợi yêu cầu ($g < r$). 

Một chuyên gia phân tích có thể không hài lòng với những giả định này vì nhiều lý do. Các cổ phiếu đang được xem xét có thể hiện tại không trả cổ tức. Các giả định của Gordon có thể quá đơn giản hóa nên không phản ánh được đặc điểm của các công ty đang được đánh giá. Một số phương án thay thế cho việc sử dụng mô hình Gordon như sau: 

- Sử dụng một mô hình DDM mạnh mẽ/linh hoạt hơn cho phép các khuôn mẫu tăng trưởng thay đổi khác nhau. 

- Sử dụng một thước đo dòng tiền khác ngoài cổ tức cho mục đích định giá. 

- Sử dụng một cách tiếp cận định giá khác (chẳng hạn như phương pháp bội số). 

Việc áp dụng DDM sẽ gặp khó khăn nếu công ty đang được phân tích hiện tại không trả cổ tức. Một công ty có thể không trả cổ tức nếu: 1) các cơ hội đầu tư mà công ty có được đều hấp dẫn đến mức việc giữ lại và tái đầu tư nguồn vốn là tốt hơn, xét dưới góc độ tỷ suất sinh lợi, so với việc phân phối cổ tức cho các cổ đông, hoặc 2) công ty đang ở trong tình trạng tài chính bấp bênh đến mức không đủ khả năng chi trả cổ tức. Một chuyên gia phân tích vẫn có thể sử dụng DDM để định giá các công ty như vậy bằng cách giả định rằng cổ tức sẽ bắt đầu được chi trả tại một thời điểm nào đó trong tương lai. Chuyên gia phân tích có thể giả định thêm rằng sự tăng trưởng không đổi sẽ diễn ra sau ngày đó và sử dụng mô hình tăng trưởng Gordon để định giá. Tuy nhiên, việc ngoại suy từ chỗ hiện tại chưa có cổ tức nhìn chung sẽ mang lại những dự báo có độ bất định rất cao. Các chuyên gia phân tích thường chọn sử dụng một hoặc nhiều phương án thay thế thay cho hoặc để bổ trợ cho mô hình tăng trưởng Gordon. 

##### **VÍ DỤ 8 (EXAMPLE 8)** 

### **Mô hình Tăng trưởng Gordon trong Trường hợp Hiện tại Không có Cổ tức (Gordon Growth Model in the Case of No Current Dividend)** 

1. Một công ty hiện tại không trả cổ tức nhưng dự kiến sẽ bắt đầu trả cổ tức sau 5 năm nữa (tại $t = 5$). Khoản cổ tức đầu tiên dự kiến là $4.00 và sẽ nhận được sau 5 năm kể từ hôm nay. Khoản cổ tức đó dự kiến sẽ tăng trưởng ở mức 6 phần trăm mãi mãi. Tỷ suất sinh lợi yêu cầu là 10 phần trăm. Giá trị nội tại hiện tại ước tính là bao nhiêu? 

### **Lời giải:** 

Chuyên gia phân tích có thể định giá cổ phiếu này thành hai phần: 

**1.** Chuyên gia phân tích sử dụng mô hình tăng trưởng Gordon để ước tính giá trị tại $t = 5$; trong mô hình này, khoản cổ tức của năm kế tiếp (năm 6) là $\$4(1.06)$. Sau đó chuyên gia phân tích tìm giá trị hiện tại của mức giá trị này tính tại thời điểm $t = 0$. 


<!-- PDF Page 364 -->

**2.** Chuyên gia phân tích tìm giá trị hiện tại của khoản cổ tức $4 chưa được "tính" trong ước tính ở Phần 1 (vốn chỉ định giá các khoản cổ tức từ $t = 6$ trở đi). Lưu ý rằng đề bài ngụ ý rằng $D_0, D_1, D_2, D_3,$ và $D_4$ đều bằng 0.

Phần 1: Giá trị của phần này là $65.818:

$$V_n = \frac{D_n(1 + g)}{r - g} = \frac{D_{n+1}}{r - g}$$

$$V_5 = \frac{\$4(1 + 0.06)}{0.10 - 0.06} = \frac{\$4.24}{0.04} = \$106$$

$$V_0 = \frac{\$106}{(1 + 0.10)^5} = \$65.818$$

Phần 2: Giá trị của phần này là $2.484:

$$V_0 = \frac{\$4}{(1 + 0.10)^5} = \$2.484$$

Tổng của hai phần là $\$65.818 + \$2.484 = \$68.30$. Cách khác, chuyên gia phân tích có thể định giá cổ phiếu tại thời điểm $t = 4$, thời điểm mà cổ tức dự kiến sẽ được chi trả vào năm kế tiếp (năm 5) và từ thời điểm đó chúng dự kiến sẽ tăng trưởng với tốc độ không đổi:

$$V_4 = \frac{\$4.00}{0.10 - 0.06} = \frac{\$4.00}{0.04} = \$100$$

$$V_0 = \frac{\$100}{(1 + 0.10)^4} = \$68.30$$

Phần tiếp theo giải quyết việc áp dụng DDM với các giả định linh hoạt hơn về tốc độ tăng trưởng cổ tức. 

# **<mark>8</mark> CÁC MÔ HÌNH CHIẾT KHẤU CỔ TỨC ĐA GIAI ĐOẠN (MULTISTAGE DIVIDEND DISCOUNT MODELS)** 

tính toán và diễn giải giá trị nội tại của một chứng khoán vốn dựa trên mô hình chiết khấu cổ tức tăng trưởng đều Gordon hoặc mô hình chiết khấu cổ tức hai giai đoạn, tùy trường hợp phù hợp 

xác định các đặc điểm của những công ty phù hợp để áp dụng mô hình chiết khấu cổ tức tăng trưởng đều hoặc đa giai đoạn
giải thích các ưu điểm và nhược điểm của từng nhóm mô hình định giá 

Các mô hình tăng trưởng đa giai đoạn (*multistage growth models*) thường được sử dụng để mô hình hóa các công ty đang tăng trưởng nhanh. _Mô hình DDM hai giai đoạn (two-stage DDM)_ giả định rằng tại một thời điểm nào đó công ty sẽ bắt đầu trả cổ tức tăng trưởng với tốc độ không đổi, nhưng trước thời điểm đó công ty sẽ trả cổ tức đang tăng trưởng ở một tốc độ cao hơn mức có thể duy trì bền vững trong dài hạn. Nghĩa là, công ty được giả định sẽ trải qua một giai đoạn tăng trưởng cao ban đầu và hữu hạn, có lẽ là trước khi có sự gia nhập của các đối thủ cạnh tranh, theo sau bởi một giai đoạn tăng trưởng bền vững vô hạn. Do đó, DDM hai giai đoạn sử dụng hai tốc độ tăng trưởng: một tốc độ tăng trưởng cao cho giai đoạn hữu hạn ban đầu, theo sau là một tốc độ tăng trưởng bền vững thấp hơn kéo dài mãi mãi. Mô hình tăng trưởng Gordon được sử dụng để ước tính giá trị kết thúc (*terminal value*) tại thời điểm $n$, phản ánh giá trị hiện tại tại thời điểm $n$ của các khoản cổ tức nhận được trong suốt giai đoạn tăng trưởng bền vững. 

Phương trình 11 sẽ được sử dụng ở đây làm điểm khởi đầu cho mô hình định giá hai giai đoạn. Mô hình định giá hai giai đoạn tương tự như Ví dụ 8 ngoại trừ việc thay vì giả định cổ tức bằng 0 trong giai đoạn đầu, chuyên gia phân tích giả định rằng cổ tức sẽ thể hiện một 


<!-- PDF Page 365 -->

tốc độ tăng trưởng cao trong suốt giai đoạn đầu. Phương trình 11 định giá các khoản cổ tức trong giai đoạn tăng trưởng cao ngắn hạn và giá trị kết thúc vào cuối giai đoạn tăng trưởng cao đó. Tốc độ tăng trưởng ngắn hạn, $g_S$, kéo dài trong $n$ năm. Giá trị nội tại trên mỗi cổ phiếu vào năm $n$, $V_n$, đại diện cho giá trị tại năm $n$ của các khoản cổ tức nhận được trong giai đoạn tăng trưởng bền vững hay chính là giá trị kết thúc tại thời điểm $n$. $V_n$ có thể được ước tính bằng cách sử dụng mô hình tăng trưởng Gordon như được trình bày trong Phương trình 12, trong đó $g_L$ là tốc độ tăng trưởng dài hạn hay bền vững (*long-term or sustainable growth rate*). Cổ tức trong năm $n + 1$, $D_{n+1}$, có thể được xác định bằng cách sử dụng Phương trình 13: 

![](assets/Equity_Investments.pdf-0365-04.png)

<!-- Formula Text: V 0  =  ∑ t=1 n D 0 (1 + g S) t _ (1 + r) t   + V n _ (1 + r) n (11) V n  = D n+1 _ r − g L (12) D n+1  =  D 0 (1 + g S) n (1 + g L) (13) -->

$$V_0 = \sum_{t=1}^{n} \frac{D_0(1 + g_S)^t}{(1 + r)^t} + \frac{V_n}{(1 + r)^n} \tag{11}$$

$$V_n = \frac{D_{n+1}}{r - g_L} \tag{12}$$

$$D_{n+1} = D_0(1 + g_S)^n(1 + g_L) \tag{13}$$

##### **VÍ DỤ 9 (EXAMPLE 9)** 

### **Áp dụng Mô hình Chiết khấu Cổ tức Hai giai đoạn (Applying the Two-Stage Dividend Discount Model)** 

1. Cổ tức hiện tại, $D_0$, là $5.00. Tốc độ tăng trưởng dự kiến là 10 phần trăm một năm trong ba năm và sau đó là 5 phần trăm. Tỷ suất sinh lợi yêu cầu là 15 phần trăm. Hãy ước tính giá trị nội tại. 

### **Lời giải:** 

$$D_1 = \$5.00(1 + 0.10) = \$5.50$$

$$D_2 = \$5.00(1 + 0.10)^2 = \$6.05$$

$$D_3 = \$5.00(1 + 0.10)^3 = \$6.655$$

$$D_4 = \$5.00(1 + 0.10)^3(1 + 0.05) = \$6.98775$$

$$V_3 = \frac{\$6.98775}{0.15 - 0.05} = \$69.8775$$

$$V_0 = \frac{\$5.50}{(1 + 0.15)} + \frac{\$6.05}{(1 + 0.15)^2} + \frac{\$6.655}{(1 + 0.15)^3} + \frac{\$69.8775}{(1 + 0.15)^3} \approx \$59.68$$

Mô hình DDM có thể được mở rộng ra nhiều giai đoạn tùy theo mức độ phù hợp. Đối với hầu hết các công ty đại chúng (tức là các công ty đã vượt qua giai đoạn khởi nghiệp), những người hành nghề giả định tốc độ tăng trưởng rốt cuộc sẽ rơi vào ba giai đoạn: 1) tăng trưởng (*growth*), 2) chuyển tiếp (*transition*), và 3) trưởng thành/bão hòa (*maturity*). Giả định này củng cố việc sử dụng _mô hình DDM ba giai đoạn (three-stage DDM)_, vốn sử dụng ba tốc độ tăng trưởng: một tốc độ tăng trưởng cao cho giai đoạn hữu hạn đầu tiên, theo sau là một tốc độ tăng trưởng thấp hơn cho giai đoạn hữu hạn thứ hai, và tiếp theo là một tốc độ tăng trưởng bền vững thấp hơn kéo dài mãi mãi. 

Người ta có thể lập luận rằng DDM ba giai đoạn sẽ phù hợp nhất đối với một công ty khá non trẻ, một công ty vừa mới bước vào giai đoạn tăng trưởng. Mô hình DDM hai giai đoạn sẽ phù hợp để ước tính giá trị của một công ty lâu đời hơn đã đi qua giai đoạn tăng trưởng của mình và hiện đang ở giai đoạn chuyển tiếp (một giai đoạn có tốc độ tăng trưởng cao hơn tốc độ tăng trưởng bền vững) trước khi tiến tới giai đoạn trưởng thành (giai đoạn có tốc độ tăng trưởng bền vững thấp hơn). 

Tuy nhiên, việc lựa chọn DDM hai giai đoạn không nhất thiết chỉ dựa vào tuổi đời của công ty. Các công ty đã thành lập lâu năm đôi khi vẫn xoay sở để tái khởi động mức tăng trưởng trên trung bình thông qua, chẳng hạn như, đổi mới sáng tạo, mở rộng sang các thị trường mới, hoặc mua lại và sáp nhập (*acquisitions*). 


<!-- PDF Page 366 -->

Hoặc tốc độ tăng trưởng dài hạn của một công ty có thể bị gián đoạn bởi một giai đoạn hoạt động kém hơn mức bình thường. Nếu tốc độ tăng trưởng dự kiến sẽ dịu lại (trong trường hợp thứ nhất) hoặc cải thiện (trong trường hợp thứ hai) hướng về một tốc độ tăng trưởng dài hạn nào đó, thì DDM hai giai đoạn có thể sẽ phù hợp. Do đó, chúng ta đã chọn DDM hai giai đoạn để định giá Tập đoàn International Business Machines (IBM) trong Ví dụ 10. 

##### **VÍ DỤ 10 (EXAMPLE 10)** 

### **Mô hình Chiết khấu Cổ tức Hai giai đoạn: Tập đoàn International Business Machines (Two-Stage Dividend Discount Model: International Business Machines Corporation)** 

Tập đoàn International Business Machines (IBM) là một công ty công nghệ hàng đầu có trụ sở tại Hoa Kỳ. IBM được thành lập vào năm 1911, ban đầu là một công ty sản xuất máy móc để bán và cho thuê, từ cân thương mại và máy chấm công công nghiệp, máy thái thịt và phô mai, cho đến thẻ đục lỗ. IBM đã giới thiệu máy tính cá nhân vào năm 1981; tuy nhiên, đến thập niên 1990, công ty bắt đầu chịu thua lỗ trong mảng kinh doanh sản xuất máy tính cốt lõi của mình và đến thập niên 2000, công ty đã bắt đầu đa dạng hóa sang lĩnh vực tư vấn kinh doanh, quá trình này được hoàn tất vào năm 2005 khi hãng bán mảng kinh doanh máy tính cá nhân của mình cho công ty Trung Quốc Lenovo. IBM hiện hoạt động thông qua năm phân khúc: Giải pháp Nhận thức (*Cognitive Solutions*), Dịch vụ Kinh doanh Toàn cầu (*Global Business Services* – GBS), Dịch vụ Công nghệ & Nền tảng Đám mây (*Technology Services & Cloud Platforms*), Hệ thống (*Systems*), và Tài chính Toàn cầu (*Global Financing*). Phân khúc Giải pháp Nhận thức cung cấp một dải năng lực từ phân tích mô tả, dự đoán và đề xuất (*descriptive, predictive, and prescriptive analytics*) cho đến các hệ thống nhận thức. Giải pháp Nhận thức bao gồm Watson, một nền tảng điện toán nhận thức có khả năng tương tác bằng ngôn ngữ tự nhiên, xử lý dữ liệu lớn (*big data*), và học hỏi từ các tương tác với con người và máy tính. Phân khúc GBS cung cấp cho khách hàng dịch vụ tư vấn, dịch vụ quản lý ứng dụng và dịch vụ quy trình toàn cầu. Phân khúc Dịch vụ Công nghệ & Nền tảng Đám mây cung cấp các dịch vụ cơ sở hạ tầng công nghệ thông tin. Phân khúc Hệ thống cung cấp cho khách hàng các công nghệ cơ sở hạ tầng. Phân khúc Tài chính Toàn cầu bao gồm tài trợ khách hàng, tài trợ thương mại, cùng tái sản xuất và tiếp thị lại. 

Báo cáo _Value Line_ ngày 30 tháng 7 năm 2018 về IBM xuất hiện trong Bảng minh họa 5 (Exhibit 5). IBM đã tăng cổ tức hàng năm trong suốt 15 năm qua. Thông tin từ _Value Line_ cho thấy mức tăng trưởng cổ tức vào khoảng 17.0 phần trăm trong 10 năm qua, 13.5 phần trăm trong 5 năm qua, và ước tính ở mức 4.5 phần trăm cho giai đoạn từ năm 2015 đến năm 2023. Sau một thời kỳ tăng trưởng thông qua mua lại và sáp nhập, khuôn mẫu này cho thấy IBM có thể đang chuyển tiếp sang giai đoạn tăng trưởng trưởng thành. 

Mô hình DDM hai giai đoạn có thể nói là một lựa chọn tốt để định giá IBM bởi vì công ty dường như đang chuyển tiếp từ giai đoạn tăng trưởng cao (lưu ý mức tăng trưởng cổ tức 13.5 phần trăm trong 5 năm qua) sang giai đoạn tăng trưởng thấp hơn (lưu ý mức dự báo tăng trưởng cổ tức 4.5 phần trăm cho giai đoạn 2015–2023). 

Mô hình CAPM có thể được sử dụng để ước tính tỷ suất sinh lợi yêu cầu, $r$, cho IBM. Báo cáo _Value Line_ (ở góc trên bên trái) ước tính hệ số beta là 0.95. Sử dụng lợi suất khoảng 2.0 phần trăm của trái phiếu Kho bạc Hoa Kỳ kỳ hạn 10 năm làm đại diện (*proxy*) cho lãi suất phi rủi ro và giả định phần bù rủi ro vốn chủ sở hữu là 5.0 phần trăm, chúng ta tìm được ước tính cho $r$ sẽ là 6.75 phần trăm $[2.0\% + 0.95(5.0\%)]$. 

Để ước tính giá trị nội tại vào cuối năm 2018, chúng ta sử dụng mức cổ tức năm 2018 là US$6.21 từ báo cáo _Value Line_. Cổ tức được giả định sẽ tăng trưởng ở tốc độ 5.0 phần trăm trong một năm và sau đó là 2.33 phần trăm. Giả định tốc độ tăng trưởng cho giai đoạn đầu nhất quán với dự báo của _Value Line_ cho 


<!-- PDF Page 367 -->

cổ tức năm 2018 và năm 2019. Giả định của chúng ta về tốc độ tăng trưởng vĩnh cửu 2.33 phần trăm tạo ra một giả định tốc độ tăng trưởng 8 năm gần mức 4.5%,<sup>4</sup> nhất quán với dự báo của _Value Line_ về mức tăng trưởng 4.5 phần trăm từ năm 2015–2022. Do đó: 

$$D_{2019} = \text{US}\$6.21(1 + 0.05) = \text{US}\$6.5205$$

$$D_{2020} = \text{US}\$6.21(1 + 0.05)(1 + 0.0233) = \text{US}\$6.6724$$

$$D_{2021} = \text{US}\$6.21(1 + 0.05)(1 + 0.0233)^2 = \text{US}\$6.8279$$

$$V_{2020} = \frac{\text{US}\$6.8279}{0.0675 - 0.0233} = \text{US}\$154.4774$$

$$V_{2018} = \frac{\text{US}\$6.5205}{(1 + 0.0675)} + \frac{\text{US}\$6.6724}{(1 + 0.0675)^2} + \frac{\text{US}\$154.4774}{(1 + 0.0675)^2} \approx \text{US}\$147.523$$

Với mức giá gần đây là US$148.56, như được ghi chú ở góc trên bên trái của báo cáo _Value Line_, ước tính giá trị nội tại US$147.523 cho thấy rằng IBM đang được định giá xấp xỉ mức hợp lý (*approximately fairly valued*). 


<!-- PDF Page 368 -->

##### **Bảng minh họa 5: Báo cáo _Value Line_ về IBM (Exhibit 5: _Value Line_ Report on IBM)** 

![](assets/Equity_Investments.pdf-0368-05.png)

_Nguồn:_ © 2018 Value Line, Inc. Bảo lưu mọi quyền trên toàn thế giới. “Value Line” là nhãn hiệu đã đăng ký của Value Line, Inc. Các Chỉ số Trung bình Nhân và Trung bình Cộng của Value Line được tính toán bởi Thomson Reuters. Thông tin được cung cấp bởi Thomson Reuters. 


<!-- PDF Page 369 -->

## **CÁC MÔ HÌNH BỘI SỐ VÀ MỐI QUAN HỆ GIỮA BỘI SỐ GIÁ, MÔ HÌNH GIÁ TRỊ HIỆN TẠI, VÀ CÁC YẾU TỐ CƠ BẢN (MULTIPLIER MODELS AND RELATIONSHIP AMONG PRICE MULTIPLES, PRESENT VALUE MODELS, AND FUNDAMENTALS)** 

# **<mark>9</mark>** 

giải thích cơ sở lý luận của việc sử dụng các bội số giá để định giá cổ phiếu, mối liên hệ giữa bội số giá trên thu nhập với các yếu tố cơ bản, và việc sử dụng các bội số dựa trên phương pháp so sánh
tính toán và diễn giải các bội số sau: giá trên thu nhập, giá trên ước tính dòng tiền hoạt động, giá trên doanh thu, và giá trên giá trị sổ sách 

giải thích các ưu điểm và nhược điểm của từng nhóm mô hình định giá 

Thuật ngữ **bội số giá (*price multiple*)** đề cập đến một tỷ số so sánh giá cổ phiếu với một dòng tiền tệ hoặc giá trị nào đó nhằm cho phép đánh giá giá trị tương đối của cổ phiếu một công ty. Một số người hành nghề sử dụng các tỷ số giá như một cơ chế sàng lọc (*screening mechanism*). Nếu tỷ số này thấp hơn một giá trị xác định, cổ phiếu sẽ được xác định là ứng viên để mua, và nếu tỷ số này vượt quá một giá trị xác định, cổ phiếu sẽ được xác định là ứng viên để bán. Nhiều người hành nghề sử dụng các tỷ số khi xem xét một nhóm hoặc một khu vực ngành các cổ phiếu và coi những cổ phiếu có tỷ số tương đối thấp là những chứng khoán có mức định giá hấp dẫn. 

Các bội số giá được các chuyên gia phân tích chứng khoán sử dụng bao gồm: 

- Tỷ số giá trên thu nhập (*Price-to-earnings ratio* – P/E). Thước đo này là tỷ số giữa giá cổ phiếu trên thu nhập mỗi cổ phiếu (EPS). P/E có thể nói là bội số giá được giới truyền thông trích dẫn thường xuyên nhất và được các chuyên gia phân tích cũng như các nhà đầu tư sử dụng nhiều nhất (Block 1999). Các công trình nền tảng của McWilliams (1966), Miller và Widmann (1966), Nicholson (1968), Dreman (1977), và Basu (1977) đã trình bày bằng chứng về lợi thế tỷ suất sinh lợi của các cổ phiếu có P/E thấp. 

- Tỷ số giá trên giá trị sổ sách (*Price-to-book ratio* – P/B). Tỷ số giữa giá cổ phiếu trên giá trị sổ sách mỗi cổ phiếu. Nhiều bằng chứng đáng kể cho thấy các bội số P/B có mối quan hệ nghịch biến với tỷ suất sinh lợi tương lai (Fama và French 1995). 

- Tỷ số giá trên doanh thu (*Price-to-sales ratio* – P/S). Thước đo này là tỷ số giữa giá cổ phiếu trên doanh thu mỗi cổ phiếu. O’Shaughnessy (2005) đã cung cấp bằng chứng cho thấy bội số P/S thấp là bội số hữu ích nhất để dự đoán tỷ suất sinh lợi tương lai. 

- Tỷ số giá trên dòng tiền (*Price-to-cash-flow ratio* – P/CF). Thước đo này là tỷ số giữa giá cổ phiếu trên một thước đo dòng tiền tính trên mỗi cổ phiếu nào đó. Các thước đo dòng tiền bao gồm dòng tiền tự do (*free cash flow* – FCF) và dòng tiền hoạt động (*operating cash flow* – OCF). 

Một lời chỉ trích phổ biến đối với tất cả các bội số này là chúng không tính đến tương lai. Lời chỉ trích này là đúng nếu bội số được tính toán từ các giá trị quá khứ (*trailing*) hoặc hiện tại của mẫu số. Những người hành nghề tìm cách khắc phục lời chỉ trích này bằng nhiều kỹ thuật khác nhau, bao gồm việc dự báo các giá trị cơ bản (mẫu số) cho một hoặc nhiều năm trong tương lai. Các bội số giá dự phóng (*forward*, *leading*, hoặc *prospective price multiples*) thu được có thể khác biệt rõ rệt so với các bội số giá quá khứ (*trailing price multiples*). Trong trường hợp không có dự báo tường minh về các giá trị cơ bản, chuyên gia phân tích đang đưa ra một dự báo ngầm định về tương lai khi triển khai các mô hình như vậy. Việc lựa chọn bội số giá—quá khứ (*trailing*) hay dự phóng (*forward*)—cần phải được sử dụng nhất quán cho các công ty đang được đem ra so sánh. 

Bên cạnh các bội số giá truyền thống được sử dụng trong định giá vừa được trình bày, các chuyên gia phân tích cần biết cách tính toán và diễn giải các tỷ số khác. Những tỷ số đó bao gồm các tỷ số được sử dụng để phân tích hiệu quả hoạt động kinh doanh và tình trạng tài chính dựa trên dữ liệu được báo cáo trong báo cáo tài chính. Ngoài ra, nhiều ngành còn có các thước đo chuyên biệt về 


<!-- PDF Page 370 -->

hiệu quả hoạt động kinh doanh mà các chuyên gia phân tích phụ trách những ngành đó cần phải nắm vững. Ví dụ, khi phân tích các công ty truyền hình cáp, tỷ số giữa tổng giá trị thị trường của công ty trên tổng số lượng thuê bao thường được sử dụng. Một thước đo phổ biến khác là doanh thu trên mỗi thuê bao. Trong ngành dầu khí, một tỷ số thường được trích dẫn là trữ lượng đã được chứng minh (*proved reserves*) trên mỗi cổ phiếu phổ thông. Các tỷ số đặc thù theo ngành hoặc lĩnh vực như thế này có thể được sử dụng để hiểu các biến số kinh doanh cốt lõi trong một ngành hoặc lĩnh vực cũng như để làm nổi bật các chứng khoán có mức định giá hấp dẫn. 

### **Mối quan hệ giữa các Bội số Giá, Mô hình Giá trị Hiện tại, và các Yếu tố Cơ bản (Relationships among Price Multiples, Present Value Models, and Fundamentals)** 

Các bội số giá thường được sử dụng độc lập với các mô hình giá trị hiện tại. Một cách tiếp cận định giá theo bội số giá, phương pháp so sánh (*method of comparables*), không bao gồm việc dự báo dòng tiền hay chiết khấu về giá trị hiện tại. Tuy nhiên, một bội số giá thường có liên hệ với các yếu tố cơ bản thông qua một mô hình dòng tiền chiết khấu, chẳng hạn như mô hình tăng trưởng Gordon. Việc hiểu rõ những mối liên kết như vậy có thể làm sâu sắc thêm sự thấu hiểu của chuyên gia phân tích về các nhân tố tác động đến giá trị của một bội số và thường có thể giúp giải thích nguyên nhân dẫn đến sự khác biệt trong các bội số mà không liên quan đến việc định giá sai. Các biểu thức được xây dựng có thể được diễn giải là _giá trị hợp lý (justified value)_ của một bội số—tức là giá trị được biện minh bởi (dựa trên) các yếu tố cơ bản hoặc một tập hợp các dự đoán dòng tiền. Những biểu thức này là một cách thức thay thế để trình bày các ước tính giá trị nội tại. 

Ví dụ, sử dụng mô hình tăng trưởng Gordon đã xác định trước đó trong Phương trình 9 và giả định rằng giá bằng với giá trị nội tại ($P_0 = V_0$), chúng ta có thể phát biểu lại Phương trình 9 như sau: 

![](assets/Equity_Investments.pdf-0370-07.png)

<!-- Formula Text: P 0  = D 1 _ r − g (14) -->

$$P_0 = \frac{D_1}{r - g} \tag{14}$$

Để đi đến mô hình cho hệ số P/E dự phóng hợp lý (*justified forward P/E*) được cho trong Phương trình 15, chúng ta chia cả hai vế của Phương trình 14 cho dự báo thu nhập của năm tới, $E_1$. Trong Phương trình 15, tỷ lệ chi trả cổ tức (*dividend payout ratio*), $p$, là tỷ số giữa cổ tức trên thu nhập: 

![](assets/Equity_Investments.pdf-0370-09.png)

<!-- Formula Text: P 0 _ E 1   = D 1 / E 1 _ r − g   = p _ r − g (15) -->

$$\frac{P_0}{E_1} = \frac{D_1 / E_1}{r - g} = \frac{p}{r - g} \tag{15}$$

Phương trình 15 chỉ ra rằng hệ số P/E có mối quan hệ nghịch biến với tỷ suất sinh lợi yêu cầu và đồng biến với tốc độ tăng trưởng; nghĩa là, khi tỷ suất sinh lợi yêu cầu tăng lên thì P/E giảm xuống, và khi tốc độ tăng trưởng tăng lên thì P/E tăng lên. Hệ số P/E và tỷ lệ chi trả cổ tức bề ngoài dường như có mối quan hệ đồng biến. Tuy nhiên, mối quan hệ này có thể không đúng, bởi vì tỷ lệ chi trả cổ tức cao hơn có thể hàm ý một tốc độ tăng trưởng chậm hơn do công ty giữ lại một tỷ trọng thu nhập thấp hơn để tái đầu tư. Hiện tượng này được gọi là sự đánh đổi giữa cổ tức và thu nhập (*dividend displacement of earnings*). 

##### **VÍ DỤ 11 (EXAMPLE 11)** 

### **Ước tính Giá trị Dựa trên các Yếu tố Cơ bản (Value Estimate Based on Fundamentals)** 

1. Petroleo Brasileiro SA, thường được biết đến với tên gọi Petrobras, từng có lần bị Bloomberg.com gắn mác là "công ty dầu khí đắt đỏ nhất". Dữ liệu của Petrobras và ngành dầu khí, bao gồm hệ số P/E 12 tháng gần nhất (*trailing twelve-month* – TTM) và tỷ lệ chi trả cổ tức, xuất hiện dưới đây. 

||**Petrobras**|**Ngành (Industry)**|
|---|---|---|
|Tỷ số P/E (TTM)|39.61|13.0|
|Tỷ suất sinh lợi trên tài sản – ROA (TTM) (%)|3.0|3.2|


<!-- PDF Page 371 -->

||**Petrobras**|**Ngành (Industry)**|
|---|---|---|
|Tốc độ tăng trưởng EPS 3 năm (%)|NM|66.00|
|EPS (MRQ) so với Quý cách đây 1 năm (% thay đổi)|138.96|−12.0|

_Lưu ý:_ NM viết tắt của không thể định lượng (*non-quantifiable*). EPS của Petrobras đã chuyển biến từ mức lỗ 1.14 BRL trên mỗi cổ phiếu sang mức lãi 0.16 BRL trên mỗi cổ phiếu trong kỳ gần nhất. MRQ viết tắt của "quý gần nhất (*most recent quarter*)." 

_Nguồn:_ Reuters. 

Hãy giải thích làm thế nào thông tin được hiển thị lại củng cố cho một hệ số P/E của Petrobras cao hơn so với của ngành. 

### **Lời giải:** 

Dữ liệu củng cố cho mức P/E cao hơn đối với Petrobras bởi vì tốc độ tăng trưởng EPS quý gần nhất (MRQ) của công ty vượt trội so với ngành. Phương trình 15 ngụ ý một mối quan hệ đồng biến giữa tỷ lệ chi trả cổ tức và bội số P/E. Petrobras đã có EPS âm trong giai đoạn từ năm 2014 đến năm 2017, và không trả cổ tức trong suốt giai đoạn đó. Tỷ lệ chi trả cổ tức cao hơn sẽ hỗ trợ cho mức P/E cao hơn. Hơn nữa, trong chừng mực mà mức tăng trưởng EPS cao hơn hàm ý một tốc độ tăng trưởng cao về cổ tức, thì tốc độ tăng trưởng EPS cao sẽ hỗ trợ cho một mức P/E cao. Tỷ số P/E cao hơn là do sự cải thiện trong hiệu quả hoạt động tài chính cơ bản của công ty và tiềm năng tăng trưởng dự kiến cao hơn của cổ phiếu này so với các công ty trung vị trong ngành. 

##### **VÍ DỤ 12 (EXAMPLE 12)** 

### **Xác định P/E Dự phóng Hợp lý (Determining Justified Forward P/E)** 

Heinrich Gladisch, CFA, đang ước tính hệ số P/E dự phóng hợp lý cho Nestlé, một trong những công ty dinh dưỡng và sức khỏe hàng đầu thế giới. Gladisch ghi nhận rằng doanh thu năm 2017 là 89.78 tỷ SFr (90.3 tỷ US$) và thu nhập ròng là 7.18 tỷ SFr (7.25 tỷ US$). Ông sắp xếp dữ liệu về EPS, cổ tức trên mỗi cổ phiếu, và tỷ lệ chi trả cổ tức cho các năm 2013–2017 trong bảng sau: 

||**2013**|**2014**|**2015**|**2016**|**2017**|
|---|---|---|---|---|---|
|Thu nhập trên mỗi cổ phiếu (*Earnings per share*)|SFr3.24|SFr4.54|SFr2.90|SFr2.76|SFr2.32|
|_% thay đổi so với năm trước (Year over year % change)_||44.6%|–36.1%|–4.8%|–15.9%|
|Cổ tức trên mỗi cổ phiếu (*Dividend per share*)|SFr2.15|SFr2.2|SFr2.25|SFr2.3|SFr2.35|
|_% thay đổi so với năm trước (Year over year % change)_||2.3%|2.3%|2.2%|2.2%|
|Tỷ lệ chi trả cổ tức (*Dividend payout ratio*)|68.5%|48.5%|77.6%|83.3%|99.2%|

Gladisch tính toán rằng ROE đạt trung bình 15.5 phần trăm trong giai đoạn 2013−2017 nhưng đã xuống dưới mức đó ở 11.7 phần trăm vào năm 2017. Tuy nhiên, trong năm đó, thu nhập ròng báo cáo của Nestlé bao gồm một khoản mục không thường xuyên (*nonrecurring component*) lớn. Công ty đã báo cáo "thu nhập cơ bản (*underlying earnings*)" năm 2017, được định nghĩa là thu nhập ròng "từ các hoạt động kinh doanh liên tục trước các khoản suy giảm giá trị tài sản (*impairments*), chi phí tái cấu trúc, kết quả từ việc thanh lý và các khoản mục bất thường một lần (*one-off items*) đáng kể," ở mức SFr2.93, mang lại mức ROE điều chỉnh là 14.8%. Dự đoán sự cải thiện ngày càng tăng trong biên lợi nhuận của Nestlé nhờ sự tăng trưởng tại các thị trường sản phẩm của hãng, Gladisch ước tính mức ROE dài hạn là 21.5 phần trăm. 


<!-- PDF Page 372 -->

Gladisch quyết định rằng các tỷ lệ chi trả cổ tức của giai đoạn 2013–2016—đạt trung bình 67.7 phần trăm—đại diện tốt hơn cho tỷ lệ chi trả cổ tức trong tương lai của Nestlé so với tỷ lệ chi trả cổ tức cao của năm 2017 (khi tính dựa trên thu nhập báo cáo). Tỷ lệ chi trả cổ tức năm 2017 cao hơn bởi vì ban lãnh đạo rõ ràng đã dựa vào các cấu phần thu nhập ròng dự kiến sẽ tiếp diễn trong tương lai để ấn định mức cổ tức năm 2017. Nhưng việc dựa vào thu nhập ròng bao gồm cả các khoản mục không thường xuyên để trả cổ tức sẽ tạo ra nhu cầu tiềm tàng phải tăng cổ tức trong tương lai. Làm tròn mức trung bình giai đoạn 2013−2016 lên, Gladisch chốt mức ước tính 68 phần trăm cho tỷ lệ chi trả cổ tức để sử dụng trong việc tính toán hệ số P/E dự phóng hợp lý bằng Phương trình 15. 

Công ty của Gladisch ước tính rằng tỷ suất sinh lợi yêu cầu đối với cổ phiếu của Nestlé là 9 phần trăm mỗi năm. Gladisch cũng tìm thấy dữ liệu sau đây ở hai đầu thái cực của dải phổ dự báo từ các chuyên gia phân tích nghiên cứu bên ngoài: 

||**2018E**|**2019E**|
|---|---|---|
|Dự báo của chuyên gia phân tích lạc quan nhất:|||
|EPS|SFr3.99|SFr4.33|
|_% thay đổi so với năm trước_|71.9%|8.5%|
|P/E (dựa trên mức giá mục tiêu SFr105)|26.3|24.2|
|Dự báo của chuyên gia phân tích kém lạc quan nhất:|||
|EPS|SFr3.52|SFr3.59|
|_% thay đổi so với năm trước_|51.7%|2.0%|
|P/E (dựa trên mức giá mục tiêu SFr68)|19.3|18.9|

1. Chỉ dựa trên thông tin và các ước tính do Gladisch cùng công ty của ông xây dựng, hãy ước tính hệ số P/E dự phóng hợp lý của Nestlé. 

#### **Lời giải:** 

Ước tính hệ số P/E dự phóng hợp lý là 32.38. Tốc độ tăng trưởng cổ tức có thể được ước tính bằng cách sử dụng Phương trình 10 là $(1 - \text{Tỷ lệ chi trả cổ tức}) \times \text{ROE} = (1 - 0.68) \times 0.215 = 0.069$, hay 6.9 phần trăm. Do đó, 

![](assets/Equity_Investments.pdf-0372-09.png)

<!-- Formula Text: P 0 _ E 1   = Payout _ r − g   = 0.68 _ 0.09 − 0.069   =  32.38 -->

$$\frac{P_0}{E_1} = \frac{\text{Payout}}{r - g} = \frac{0.68}{0.09 - 0.069} = 32.38$$

2. So sánh và đối chiếu ước tính P/E dự phóng hợp lý từ Câu hỏi 1 với các ước tính từ mỗi đầu thái cực trong dải phổ dự báo của các chuyên gia phân tích nghiên cứu bên ngoài. 

#### **Lời giải:** 

Hệ số P/E dự phóng hợp lý ước tính là 32.38 cao hơn so với các ước tính P/E năm 2018 hợp lý ở mức 26.3 và 19.3 của hai chuyên gia phân tích kia. Việc sử dụng tỷ suất sinh lợi yêu cầu 9.5 phần trăm thay vì 9 phần trăm sẽ dẫn đến ước tính P/E dự phóng hợp lý là $26.2 = 0.68 / (0.095 - 0.069)$. Việc sử dụng mức ROE 16.5 phần trăm (mức ROE trung bình của giai đoạn 2013–2016) thay vì 21.5 phần trăm sẽ dẫn đến ước tính P/E dự phóng hợp lý là $18.4 = 0.68 / [0.09 - (0.32)(0.165)] = 0.68 / (0.09 - 0.053)$. Hệ số P/E dự phóng hợp lý rất nhạy cảm với những thay đổi trong các dữ liệu đầu vào. 

Các ước tính P/E dự phóng hợp lý có thể nhạy cảm với những thay đổi nhỏ trong các giả định. Do đó, các chuyên gia phân tích có thể hưởng lợi từ việc thực hiện phân tích độ nhạy, như được trình bày trong Bảng minh họa 6 (Exhibit 6), vốn được dựa trên Ví dụ 12. Bảng minh họa 6 cho thấy hệ số P/E dự phóng hợp lý 
