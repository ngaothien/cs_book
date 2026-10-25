# Tập 5: Đầu tư Cổ phiếu (Volume 5: Equity Investments)
## Học phần 3: Hiệu quả Thị trường (Learning Module 3: Market Efficiency)
### Phần 2/3: Các Bất thường Định giá trên Thị trường - Theo Chuỗi thời gian và Chéo (Market Pricing Anomalies - Time Series and Cross-Sectional) (Trang PDF 149–161)

---

<!-- PDF Page 149 -->

### **CÁC BẤT THƯỜNG ĐỊNH GIÁ TRÊN THỊ TRƯỜNG - THEO CHUỖI THỜI GIAN VÀ CHÉO (MARKET PRICING ANOMALIES - TIME SERIES AND CROSS-SECTIONAL)**

# **<mark>6</mark>**

mô tả các bất thường thị trường (*market anomalies*)

Mặc dù có rất nhiều bằng chứng cho thấy các thị trường là hiệu quả, các nhà nghiên cứu đã xác định được một số sự kém hiệu quả hoặc bất thường bề ngoài của thị trường. Những bất thường thị trường này, nếu tồn tại dai dẳng (*persistent*), sẽ là những ngoại lệ đối với khái niệm hiệu quả thị trường. Các nhà nghiên cứu kết luận rằng một **bất thường thị trường (*market anomaly*)** có thể hiện diện nếu sự thay đổi trong giá của một tài sản hoặc chứng khoán không thể được liên kết trực tiếp với thông tin liên quan hiện tại đã được biết đến trên thị trường hoặc với việc công bố thông tin mới vào thị trường.

Giá trị hiệu lực của bất kỳ bằng chứng nào ủng hộ sự tồn tại tiềm tàng của một sự kém hiệu quả hoặc bất thường thị trường phải _nhất quán_ qua các khoảng thời gian đủ dài. Nếu không, một bất thường thị trường được phát hiện có thể phần lớn chỉ là một sản phẩm ngẫu nhiên (*artifact*) của giai đoạn mẫu được chọn. Trong cuộc tìm kiếm rộng khắp nhằm khám phá các bất thường có khả năng sinh lời, nhiều phát hiện có thể chỉ đơn giản là sản phẩm của một quá trình được gọi là **khai phá dữ liệu (*data mining*)**, còn được gọi là **sục sạo dữ liệu (*data snooping*)**. Trong thông lệ nghiên cứu được chấp nhận chung, một giả thuyết ban đầu được xây dựng dựa trên cơ sở lý luận kinh tế (*economic rationale*). Sau đó, các kiểm định được tiến hành trên dữ liệu được lựa chọn một cách khách quan để xác nhận hoặc bác bỏ giả thuyết ban đầu. Tuy nhiên, với việc khai phá dữ liệu, quy trình này thường bị đảo ngược: dữ liệu được kiểm tra với mục đích xây dựng một giả thuyết, thay vì xây dựng giả thuyết trước. Điều này được thực hiện bằng cách phân tích dữ liệu theo nhiều cách khác nhau, và thậm chí sử dụng các phương pháp thực nghiệm khác nhau cho đến khi bạn tìm thấy sự ủng hộ cho một kết quả mong muốn, trong trường hợp này là một bất thường có khả năng sinh lời.

Liệu các nhà nghiên cứu có thể nhìn lại dữ liệu trong quá khứ và tìm ra một chiến lược giao dịch lẽ ra đã mang lại tỷ suất sinh lợi bất thường hay không? Chắc chắn là có. Việc sục sạo dữ liệu đủ nhiều thường có thể phát hiện ra một chiến lược giao dịch lẽ ra đã hoạt động hiệu quả trong quá khứ chỉ đơn thuần nhờ sự tình cờ ngẫu nhiên. Nhưng trong một thị trường hiệu quả, một chiến lược như vậy ít có khả năng tạo ra tỷ suất sinh lợi bất thường một cách nhất quán trong tương lai. Ngoài ra, mặc dù các bất thường được xác định có vẻ tạo ra tỷ suất sinh lợi vượt trội, nhưng nhìn chung rất khó để khai thác các bất thường đó một cách có lời sau khi đã tính đến rủi ro, chi phí giao dịch, v.v.

Một số bất thường nổi tiếng được liệt kê trong Bảng minh họa 3. Danh sách này hoàn toàn không phải là toàn diện, nhưng nó cung cấp thông tin về độ rộng của các bất thường. Một vài trong số các bất thường này được thảo luận chi tiết hơn trong các phần tiếp theo. Các bất thường được xếp vào các nhóm dựa trên phương pháp nghiên cứu đã xác định ra bất thường đó. Các bất thường theo chuỗi thời gian (*time-series anomalies*) được xác định bằng cách sử dụng dữ liệu chuỗi thời gian. Các bất thường chéo (*cross-sectional anomalies*) được xác định dựa trên việc phân tích một lát cắt ngang các công ty khác nhau ở một số đặc điểm then chốt. Các bất thường khác được xác định bằng nhiều phương pháp khác nhau, bao gồm cả các nghiên cứu sự kiện (*event studies*).

**Bảng minh họa 3: Mẫu các Bất thường Định giá Quan sát được (Exhibit 3: Sampling of Observed Pricing Anomalies)**

|**Chuỗi thời gian (Time Series)**|**Chéo (Cross-Sectional)**|**Khác (Other)**|
|---|---|---|
|Hiệu ứng tháng Giêng (*January effect*)|Hiệu ứng quy mô (*Size effect*)|Chiết khấu quỹ đóng (*Closed-end fund discount*)|
|Hiệu ứng ngày trong tuần (*Day-of-the-week effect*)|Hiệu ứng giá trị (*Value effect*)|Bất ngờ lợi nhuận (*Earnings surprise*)|
|Hiệu ứng cuối tuần (*Weekend effect*)|Tỷ số giá trị sổ sách trên giá trị thị trường (*Book-to-market ratios*)|Phát hành lần đầu ra công chúng (*Initial public offerings*)|
|Hiệu ứng chuyển giao tháng (*Turn-of-the-month effect*)|Hiệu ứng tỷ số P/E (*P/E ratio effect*)|Hiệu ứng chứng khoán kiệt quệ tài chính (*Distressed securities effect*)|
|Hiệu ứng ngày lễ (*Holiday effect*)|Bí ẩn Value Line (*Value Line enigma*)|Chia tách cổ phiếu (*Stock splits*)|
|Hiệu ứng thời điểm trong ngày (*Time-of-day effect*)| |Siêu cúp Bóng bầu dục Mỹ (*Super Bowl*)|

<!-- PDF Page 150 -->

|**Chuỗi thời gian (Time Series)**|**Chéo (Cross-Sectional)**|**Khác (Other)**|
|---|---|---|
|Đà tăng trưởng (*Momentum*)|||
|Phản ứng thái quá (*Overreaction*)|||

#### **Các Bất thường theo Chuỗi thời gian (Time-Series Anomalies)**

Hai trong số các nhóm bất thường theo chuỗi thời gian chính đã được ghi nhận là 1) các bất thường theo lịch (*calendar anomalies*) và 2) các bất thường về đà tăng trưởng và phản ứng thái quá (*momentum and overreaction anomalies*).

##### **_Các Bất thường theo Lịch (Calendar Anomalies)_**

Vào những năm 1980, một số nhà nghiên cứu đã báo cáo rằng tỷ suất sinh lợi của thị trường chứng khoán trong tháng Giêng cao hơn đáng kể so với các tháng còn lại trong năm, với phần lớn tỷ suất sinh lợi bất thường được ghi nhận trong năm ngày giao dịch đầu tiên của tháng Giêng. Kể từ lần đầu tiên được ghi nhận vào những năm 1980, quy luật này, được gọi là **hiệu ứng tháng Giêng (*January effect*)**, đã được quan sát thấy ở hầu hết các thị trường cổ phiếu trên thế giới. Bất thường này còn được gọi là **hiệu ứng chuyển giao năm (*turn-of-the-year effect*)**, hoặc thậm chí thường được gọi là “hiệu ứng công ty nhỏ vào tháng Giêng” (*“small firm in January effect”*) bởi vì nó thường được quan sát thấy nhất đối với tỷ suất sinh lợi của các cổ phiếu có vốn hóa thị trường nhỏ.<sup>23</sup>

Hiệu ứng tháng Giêng mâu thuẫn với giả thuyết thị trường hiệu quả bởi vì tỷ suất sinh lợi vượt trội trong tháng Giêng không bắt nguồn từ bất kỳ thông tin hay tin tức mới và liên quan nào. Một số lý do đã được đề xuất cho bất thường này, bao gồm việc bán cắt lỗ để giảm thuế (*tax-loss selling*). Các nhà nghiên cứu đã suy đoán rằng, để giảm nghĩa vụ thuế của mình, các nhà đầu tư bán các chứng khoán “thua lỗ” (*“loser” securities*) của họ vào tháng Mười Hai với mục đích tạo ra các khoản lỗ vốn (*capital losses*), sau đó có thể được dùng để khấu trừ vào bất kỳ khoản lãi vốn (*capital gains*) nào. Một lời giải thích có liên quan là những cổ phiếu thua lỗ này có xu hướng là các cổ phiếu vốn hóa nhỏ có độ biến động cao.<sup>24</sup> Nguồn cung cổ phiếu tăng lên trong tháng Mười Hai này làm giảm giá của chúng, và sau đó những cổ phiếu này được mua lại vào đầu tháng Giêng ở mức giá tương đối hấp dẫn. Nhu cầu mua này sau đó lại đẩy giá của chúng tăng trở lại. Nhìn chung, bằng chứng chỉ ra rằng việc bán cắt lỗ để giảm thuế có thể giải thích một phần tỷ suất sinh lợi bất thường trong tháng Giêng, nhưng không giải thích được toàn bộ hiện tượng này.

Một lời giải thích khả dĩ khác cho bất thường này là cái gọi là “làm đẹp báo cáo danh mục” (*“window dressing”*), một thông lệ trong đó các nhà quản lý danh mục đầu tư bán đi các chứng khoán rủi ro hơn của họ trước ngày 31 tháng Mười Hai. Lời giải thích như sau: nhiều nhà quản lý danh mục đầu tư lập báo cáo thường niên về các khoản nắm giữ trong danh mục của họ tính đến ngày 31 tháng Mười Hai. Việc bán các chứng khoán rủi ro hơn là một nỗ lực nhằm làm cho danh mục của họ trông có vẻ ít rủi ro hơn. Sau ngày 31 tháng Mười Hai, nhà quản lý danh mục đầu tư sau đó sẽ chỉ đơn giản là mua lại các chứng khoán rủi ro hơn nhằm cố gắng kiếm được tỷ suất sinh lợi cao hơn. Tuy nhiên, tương tự như giả thuyết bán cắt lỗ để giảm thuế, bằng chứng nghiên cứu ủng hộ giả thuyết làm đẹp báo cáo giải thích được một phần, nhưng không phải toàn bộ, bất thường này.

Bằng chứng gần đây đối với cả tỷ suất sinh lợi cổ phiếu và trái phiếu cho thấy rằng hiệu ứng tháng Giêng không tồn tại dai dẳng và do đó không phải là một bất thường định giá. Một khi thực hiện điều chỉnh phù hợp cho rủi ro, “hiệu ứng” tháng Giêng không tạo ra tỷ suất sinh lợi bất thường.<sup>25</sup>

Một số hiệu ứng theo lịch khác, bao gồm hiệu ứng ngày trong tuần (*day-of-the-week*) và hiệu ứng cuối tuần (*weekend effects*),<sup>26</sup> đã được tìm thấy. Các bất thường này được tóm tắt trong Bảng minh họa 4.<sup>27</sup> Nhưng giống như hiệu ứng quy mô sẽ được mô tả sau, hầu hết các bất thường này đã bị loại bỏ

> 23 Cũng có bằng chứng về hiệu ứng tháng Giêng trong tỷ suất sinh lợi trái phiếu vốn phổ biến hơn ở các trái phiếu doanh nghiệp lợi suất cao (*high-yield corporate bonds*), tương tự như hiệu ứng công ty nhỏ đối với cổ phiếu.

> 24 Xem Roll (1983).

> 25 Xem, ví dụ, Kim (2006).

> 26 Để xem thảo luận về một số quy luật bất thường này, xem Jacobs và Levy (1988).

> 27 Hiệu ứng cuối tuần bao gồm một quy luật của tỷ suất sinh lợi xoay quanh dịp cuối tuần: tỷ suất sinh lợi dương bất thường vào các ngày thứ Sáu tiếp nối bởi tỷ suất sinh lợi âm bất thường vào các ngày thứ Hai. Đây là một hiệu ứng ngày trong tuần liên kết cụ thể tỷ suất sinh lợi của ngày thứ Sáu và ngày thứ Hai. Điều thú vị cần lưu ý là vào năm 2009, hiệu ứng cuối tuần tại Hoa Kỳ đã bị đảo ngược, với 80 phần trăm mức tăng từ tháng 3 năm 2009 trở đi đến từ

<!-- PDF Page 151 -->

theo thời gian. Một quan điểm cho rằng các bất thường đã bị khai thác đến mức hiệu ứng đó đã bị kinh doanh chênh lệch giá triệt tiêu (*arbitraged away*). Tuy nhiên, một quan điểm khác cho rằng các phương pháp luận thống kê ngày càng tinh vi hơn đã không còn phát hiện ra những sự kém hiệu quả trong định giá nữa.

**Bảng minh họa 4: Các Bất thường Dựa trên Lịch (Exhibit 4: Calendar-Based Anomalies)**

|**Bất thường (Anomaly)**|**Quan sát (Observation)**|
|---|---|
|Hiệu ứng chuyển giao tháng (*Turn-of-the-month effect*)|Tỷ suất sinh lợi có xu hướng cao hơn vào ngày giao dịch cuối cùng của tháng và ba ngày giao dịch đầu tiên của tháng tiếp theo.|
|Hiệu ứng ngày trong tuần (*Day-of-the-week effect*)|Tỷ suất sinh lợi trung bình vào ngày thứ Hai là số âm và thấp hơn tỷ suất sinh lợi trung bình của bốn ngày còn lại trong tuần, vốn đều là số dương.|
|Hiệu ứng cuối tuần (*Weekend effect*)|Tỷ suất sinh lợi vào dịp cuối tuần có xu hướng thấp hơn tỷ suất sinh lợi vào các ngày làm việc trong tuần.|
|Hiệu ứng ngày lễ (*Holiday effect*)|Tỷ suất sinh lợi của cổ phiếu vào ngày trước các kỳ nghỉ lễ của thị trường có xu hướng cao hơn các ngày khác.|

##### **_Các Bất thường về Đà tăng trưởng và Phản ứng thái quá (Momentum and Overreaction Anomalies)_**

Các bất thường về đà tăng trưởng (*Momentum anomalies*) liên quan đến các mô hình giá cổ phiếu trong ngắn hạn. Một trong những nghiên cứu đầu tiên xác định loại bất thường này được thực hiện bởi Werner DeBondt và Richard Thaler, những người lập luận rằng các nhà đầu tư phản ứng thái quá (*overreact*) trước việc công bố thông tin đại chúng ngoài kỳ vọng.<sup>28</sup> Do đó, giá cổ phiếu sẽ bị thổi phồng quá mức (hoặc bị dìm giá quá mức) đối với những công ty công bố thông tin tốt (hoặc xấu). Bất thường này đã được biết đến với tên gọi là hiệu ứng phản ứng thái quá (*overreaction effect*). Sử dụng hiệu ứng phản ứng thái quá, họ đã đề xuất một chiến lược bao gồm việc mua các danh mục “thua cuộc” (*“loser” portfolios*) và bán các danh mục “chiến thắng” (*“winner” portfolios*). Họ định nghĩa các cổ phiếu là người chiến thắng hay kẻ thua cuộc dựa trên tổng tỷ suất sinh lợi của chúng trong giai đoạn từ ba đến năm năm trước đó. Họ phát hiện ra rằng trong giai đoạn tiếp theo, các danh mục thua cuộc có thành quả vượt trội hơn thị trường, trong khi các danh mục chiến thắng có thành quả kém hơn thị trường. Các quy luật tương tự đã được ghi nhận ở nhiều, dù không phải tất cả, các thị trường cổ phiếu toàn cầu cũng như trên các thị trường trái phiếu. Một lời chỉ trích là bất thường quan sát được có thể là kết quả của các vấn đề thống kê trong quá trình phân tích.

Một sự mâu thuẫn với hiệu quả dạng yếu xảy ra khi các chứng khoán đã trải qua mức tỷ suất sinh lợi cao trong ngắn hạn có xu hướng tiếp tục tạo ra tỷ suất sinh lợi cao hơn trong các kỳ tiếp theo.<sup>29</sup> Bằng chứng thực nghiệm ủng hộ sự tồn tại của đà tăng trưởng (*momentum*) trong tỷ suất sinh lợi cổ phiếu ở hầu hết các thị trường chứng khoán trên thế giới đã được ghi nhận rất đầy đủ. Nếu các nhà đầu tư có thể giao dịch dựa trên đà tăng trưởng và kiếm được lợi nhuận bất thường, thì bất thường này mâu thuẫn với dạng yếu của giả thuyết thị trường hiệu quả bởi vì nó đại diện cho một mô hình trong giá cả có thể được khai thác chỉ đơn giản bằng cách sử dụng thông tin giá lịch sử.<sup>30</sup>

Các nhà nghiên cứu đã lập luận rằng sự tồn tại của đà tăng trưởng là hợp lý (*rational*) và không đi ngược lại hiệu quả thị trường bởi vì hoàn toàn hợp lý khi có những cú sốc đối với tốc độ tăng trưởng kỳ vọng của dòng tiền dành cho cổ đông và những cú sốc này tạo ra một

> ngày giao dịch đầu tiên của tuần.

> 28 DeBondt và Thaler (1985).

> 29 Lưu ý rằng quy luật này hoàn toàn trái ngược với quy luật đảo chiều của DeBondt và Thaler vốn xuất hiện trong các khoảng thời gian dài hơn. Về mặt lý thuyết, hai quy luật này có thể có liên hệ với nhau. Nói cách khác, hoàn toàn có khả năng giá cả bị đẩy lên cực kỳ cao, có lẽ là quá cao, trong ngắn hạn đối với các công ty đang ăn nên làm ra. Trong dài hạn hơn (từ ba đến năm năm), giá của những cổ phiếu chiến thắng trong ngắn hạn này tự điều chỉnh lại và chúng có thành quả kém đi.

> 30 Jegadeesh và Titman (2001).

<!-- PDF Page 152 -->

sự tự tương quan hợp lý và tồn tại trong thời gian ngắn.<sup>31</sup> Nói cách khác, việc các cổ phiếu có một mức độ đà tăng trưởng nhất định trong tỷ suất sinh lợi chứng khoán của chúng có thể không hàm ý sự phi lý trí mà thay vào đó có thể phản ánh việc giá cả đang điều chỉnh trước một cú sốc về tốc độ tăng trưởng.

#### **Các Bất thường Chéo (Cross-Sectional Anomalies)**

Hai trong số các bất thường chéo được nghiên cứu nhiều nhất trên các thị trường tài chính là hiệu ứng quy mô (*size effect*) và hiệu ứng giá trị (*value effect*).

##### **_Hiệu ứng Quy mô (Size Effect)_**

Hiệu ứng quy mô xuất phát từ quan sát cho thấy cổ phiếu của các công ty vốn hóa nhỏ (*small-cap companies*) có xu hướng có thành quả vượt trội hơn cổ phiếu của các công ty vốn hóa lớn (*large-cap companies*) trên cơ sở điều chỉnh theo rủi ro. Nhiều nhà nghiên cứu đã ghi nhận hiệu ứng công ty nhỏ ngay sau khi nghiên cứu ban đầu được công bố vào năm 1981. Tuy nhiên, hiệu ứng này không còn rõ ràng trong các nghiên cứu tiếp theo.<sup>32</sup> Một phần lý do khiến hiệu ứng quy mô không được xác nhận bởi các nghiên cứu tiếp theo có thể là do thực tế rằng nếu nó thực sự là một bất thường, các nhà đầu tư hành động dựa trên hiệu ứng này sẽ làm giảm bất kỳ tỷ suất sinh lợi tiềm năng nào. Nhưng một phần lời giải thích có thể chỉ đơn giản là hiệu ứng được quan sát thấy ban đầu là một kết quả ngẫu nhiên tình cờ và do đó thực chất không phải là một sự kém hiệu quả.

##### **_Hiệu ứng Giá trị (Value Effect)_**

Một số nghiên cứu thực nghiệm toàn cầu đã chỉ ra rằng các cổ phiếu giá trị (*value stocks*), vốn thường được hiểu là các cổ phiếu có tỷ số giá trên thu nhập (P/E) và tỷ số giá trị thị trường trên giá trị sổ sách (M/B) thấp hơn mức trung bình, cùng tỷ suất cổ tức (*dividend yields*) cao hơn mức trung bình, đã có thành quả vượt trội một cách nhất quán so với các cổ phiếu tăng trưởng (*growth stocks*) trong những khoảng thời gian dài.<sup>33</sup> Nếu hiệu ứng này tồn tại dai dẳng, bất thường cổ phiếu giá trị mâu thuẫn với hiệu quả thị trường dạng bán mạnh bởi vì tất cả các thông tin được sử dụng để phân loại cổ phiếu theo cách này đều là thông tin công khai hiện có.

Fama và French đã phát triển một mô hình ba nhân tố (*three-factor model*) để dự đoán tỷ suất sinh lợi cổ phiếu.<sup>34</sup> Ngoài việc sử dụng tỷ suất sinh lợi thị trường như được chỉ định bởi mô hình định giá tài sản vốn (CAPM), mô hình Fama và French còn đưa thêm quy mô của công ty được đo lường bằng giá trị thị trường của vốn chủ sở hữu và giá trị sổ sách của vốn chủ sở hữu chia cho giá trị thị trường của vốn chủ sở hữu của công ty, vốn là một thước đo giá trị. Mô hình Fama và French nắm bắt các chiều kích rủi ro liên quan đến tỷ suất sinh lợi cổ phiếu mà mô hình CAPM không xem xét. Fama và French nhận thấy rằng khi họ áp dụng mô hình ba nhân tố thay vì CAPM, bất thường cổ phiếu giá trị biến mất.

# **<mark>7</mark>**

### **CÁC BẤT THƯỜNG KHÁC, HÀM Ý CỦA CÁC BẤT THƯỜNG ĐỊNH GIÁ TRÊN THỊ TRƯỜNG (OTHER ANOMALIES, IMPLICATIONS OF MARKET PRICING ANOMALIES)**

mô tả các bất thường thị trường (*market anomalies*)

> 31 Johnson (2002).

> 32 Mặc dù một số lượng lớn các nghiên cứu ghi nhận hiệu ứng công ty nhỏ, các nghiên cứu này tập trung vào một giai đoạn tương tự như giai đoạn của nghiên cứu ban đầu và do đó sử dụng một bộ dữ liệu tương tự. Chìa khóa để xác định xem một hiện tượng có phải là bất thường thực sự hay không là sự tồn tại dai dẳng trong các kiểm định ngoài mẫu (*out-of-sample tests*). Fama và French (2008) ghi nhận rằng hiệu ứng quy mô chỉ thể hiện rõ ở các cổ phiếu vốn hóa siêu nhỏ (*microcap stocks*) chứ không phải ở các cổ phiếu vốn hóa nhỏ và lớn, và những cổ phiếu vốn hóa siêu nhỏ này có thể có ảnh hưởng đáng kể trong các nghiên cứu ghi nhận hiệu ứng quy mô.

> 33 Ví dụ, xem Capaul, Rowley, và Sharpe (1993) cùng Fama và French (1998).

> 34 Fama và French (1995).

<!-- PDF Page 153 -->

Một số bất thường bổ sung đã được ghi nhận trên các thị trường tài chính, bao gồm sự tồn tại của các khoản chiết khấu quỹ đầu tư đóng (*closed-end investment fund discounts*), các phản ứng giá trước việc công bố thông tin lợi nhuận, tỷ suất sinh lợi của các đợt phát hành lần đầu ra công chúng (IPO), và khả năng dự đoán tỷ suất sinh lợi dựa trên thông tin trước đó.

#### **Chiết khấu Quỹ Đầu tư Đóng (Closed-End Investment Fund Discounts)**

Một quỹ đầu tư đóng (*closed-end investment fund*) phát hành một số lượng cổ phiếu cố định tại thời điểm thành lập và không bán thêm bất kỳ cổ phiếu nào sau đợt chào bán ban đầu. Do đó, vốn hóa của quỹ là cố định trừ khi có một đợt chào bán ra công chúng thứ cấp được thực hiện. Cổ phiếu của các quỹ đóng được giao dịch trên thị trường chứng khoán giống như bất kỳ cổ phiếu nào khác trên thị trường vốn cổ phần (tức là giá của chúng được xác định bởi cung và cầu).

Về mặt lý thuyết, những cổ phiếu này lẽ ra phải được giao dịch ở mức giá xấp xỉ bằng với giá trị tài sản ròng (*net asset value* – NAV) trên mỗi cổ phiếu của chúng, vốn chỉ đơn giản là tổng giá trị thị trường của các chứng khoán mà quỹ đang nắm giữ trừ đi mọi khoản nợ phải trả rồi chia cho số lượng cổ phiếu đang lưu hành. Tuy nhiên, có vô số nghiên cứu đã ghi nhận rằng, tính trung bình, các quỹ đóng được giao dịch ở mức chiết khấu (*discount*) so với NAV. Hầu hết các nghiên cứu đã ghi nhận mức chiết khấu trung bình nằm trong khoảng 4–10 phần trăm, mặc dù có những quỹ riêng lẻ đã giao dịch ở mức chiết khấu vượt quá 50 phần trăm và những quỹ khác lại giao dịch ở mức phần bù (*premiums*) lớn.<sup>35</sup>

Khoản chiết khấu quỹ đóng đặt ra một câu đố hóc búa bởi vì về mặt khái niệm, một nhà đầu tư có thể mua tất cả cổ phiếu trong quỹ, thanh lý quỹ, và cuối cùng thu được một khoản lợi nhuận. Một số nhà nghiên cứu đã cho rằng các khoản chiết khấu này bắt nguồn từ phí quản lý hoặc kỳ vọng về thành quả hoạt động của các nhà quản lý, nhưng những lời giải thích này không được ủng hộ bởi bằng chứng thực tế.<sup>36</sup> Một lời giải thích thay thế cho khoản chiết khấu là các nghĩa vụ thuế gắn liền với các khoản lãi và lỗ vốn chưa thực hiện (*unrealized capital gains and losses*) vốn đã tồn tại trước thời điểm nhà đầu tư mua cổ phiếu, và do đó, nhà đầu tư không có quyền kiểm soát hoàn toàn đối với thời điểm hiện thực hóa các khoản lãi và lỗ đó.<sup>37</sup> Mặc dù bằng chứng ủng hộ giả thuyết này ở một mức độ nhất định, hiệu ứng thuế không đủ lớn để giải thích toàn bộ khoản chiết khấu. Cuối cùng, người ta thường lập luận rằng các khoản chiết khấu tồn tại do các vấn đề về thanh khoản và những sai sót trong việc tính toán NAV. Lời giải thích về sự kém thanh khoản là hợp lý nếu các cổ phiếu trong danh mục được ghi nhận ở cùng mức giá như các cổ phiếu giao dịch công khai có tính thanh khoản cao hơn; một số bằng chứng ủng hộ khẳng định này. Nhưng cũng giống như các lý do về thuế, các vấn đề thanh khoản chỉ giải thích được một phần của hiệu ứng chiết khấu.

Liệu các khoản chiết khấu này có thể được khai thác để kiếm tỷ suất sinh lợi bất thường nếu tính đến chi phí giao dịch hay không? Không. Thứ nhất, chi phí giao dịch liên quan đến việc khai thác khoản chiết khấu—mua tất cả cổ phiếu và thanh lý quỹ—sẽ xóa sạch mọi khoản lợi nhuận.<sup>38</sup> Thứ hai, các khoản chiết khấu này có xu hướng quay trở về mức không theo thời gian. Do đó, một chiến lược giao dịch dựa trên các khoản chiết khấu này sẽ ít có khả năng sinh lời.<sup>39</sup>

#### **Bất ngờ Lợi nhuận (Earnings Surprise)**

Mặc dù hầu hết các nghiên cứu sự kiện đều ủng hộ hiệu quả thị trường dạng bán mạnh, một số nhà nghiên cứu đã cung cấp bằng chứng đặt dấu hỏi về hiệu quả thị trường dạng bán mạnh. Một trong những nghiên cứu này liên quan đến sự điều chỉnh đã được kiểm tra sâu rộng của giá cổ phiếu

> 35 Xem Dimson và Minio-Kozerski (1999) để xem tổng thuật về các tài liệu nghiên cứu này.

> 36 Xem Lee, Shleifer, và Thaler (1990).

> 37 Tỷ suất sinh lợi cho những người sở hữu cổ phiếu quỹ đóng có ba phần: 1) sự tăng giá hoặc giảm giá của bản thân các cổ phiếu quỹ đó, 2) cổ tức kiếm được và được quỹ phân phối cho những người sở hữu, và 3) các khoản lãi và lỗ vốn kiếm được bởi quỹ và được quỹ phân phối. Lời giải thích cho việc định giá bất thường này có liên quan đến thời điểm phân phối các khoản lãi vốn.

> 38 Xem, ví dụ, nghiên cứu của Pontiff (1996), chỉ ra cách chi phí kinh doanh chênh lệch giá trên các khoản chiết khấu này triệt tiêu lợi nhuận.
> 39 Xem Pontiff (1995).

<!-- PDF Page 154 -->

trước các thông báo lợi nhuận.<sup>40</sup> Phần ngoài kỳ vọng của thông báo lợi nhuận, hay **bất ngờ lợi nhuận (*earnings surprise*)**, là phần lợi nhuận không được các nhà đầu tư dự đoán trước và, theo giả thuyết thị trường hiệu quả, đáng có một sự điều chỉnh giá. Các bất ngờ tích cực (tiêu cực) lẽ ra phải gây ra những đợt tăng (giảm) giá phù hợp và nhanh chóng. Một số nghiên cứu đã được tiến hành bằng cách sử dụng dữ liệu từ nhiều thị trường trên khắp thế giới. Hầu hết các kết quả chỉ ra rằng các bất ngờ lợi nhuận được phản ánh nhanh chóng vào giá cổ phiếu, nhưng quá trình điều chỉnh không phải lúc nào cũng hiệu quả. Cụ thể, mặc dù một sự điều chỉnh đáng kể xảy ra trước và ngay vào ngày ra thông báo, một sự điều chỉnh vẫn tiếp tục diễn ra sau khi có thông báo.<sup>41</sup>

Hệ quả của những sự điều chỉnh giá chậm chạp này là các công ty thể hiện mức bất ngờ lợi nhuận tích cực lớn nhất sau đó lại thể hiện thành quả tỷ suất sinh lợi cổ phiếu vượt trội, trong khi thành quả kém cỏi sau đó lại được thể hiện bởi các công ty có mức bất ngờ lợi nhuận thấp hoặc âm.<sup>42</sup> Phát hiện này hàm ý rằng các nhà đầu tư có thể kiếm được tỷ suất sinh lợi bất thường bằng cách sử dụng thông tin công khai hiện có thông qua việc mua cổ phiếu của các công ty có bất ngờ lợi nhuận tích cực và bán cổ phiếu của những công ty có bất ngờ lợi nhuận âm.

Mặc dù có sự ủng hộ đối với tỷ suất sinh lợi bất thường gắn liền với các bất ngờ lợi nhuận, và một số sự ủng hộ đối với các tỷ suất sinh lợi như vậy kéo dài sau giai đoạn ra thông báo, nhưng cũng có bằng chứng chỉ ra rằng các tỷ suất sinh lợi bất thường quan sát được này là sản phẩm ngẫu nhiên của những nghiên cứu không kiểm soát đầy đủ chi phí giao dịch và rủi ro.<sup>43</sup>

#### **Phát hành Lần đầu ra Công chúng (Initial Public Offerings – IPOs)**

Khi một công ty chào bán cổ phiếu của mình ra công chúng lần đầu tiên, công ty thực hiện điều đó thông qua một đợt phát hành lần đầu ra công chúng (hay IPO). Đợt chào bán này bao gồm việc làm việc với một ngân hàng đầu tư giúp định giá và tiếp thị các cổ phiếu mới phát hành. Sau khi đợt chào bán hoàn tất, các cổ phiếu mới được giao dịch trên thị trường chứng khoán lần đầu tiên. Xét đến rủi ro mà các ngân hàng đầu tư phải đối mặt trong việc cố gắng bán một đợt phát hành mới mà mức giá thực của nó chưa được biết đến, có lẽ không có gì đáng ngạc nhiên khi thấy rằng, tính trung bình, giá bán ban đầu được đặt quá thấp và mức giá tăng vọt đáng kể ngay trong ngày giao dịch đầu tiên. Chênh lệch phần trăm giữa giá phát hành và giá đóng cửa vào cuối ngày giao dịch đầu tiên thường được gọi là mức độ định giá thấp (*degree of underpricing*).

Bằng chứng cho thấy rằng, tính trung bình, các nhà đầu tư có khả năng mua được cổ phiếu của một đợt IPO ở mức giá chào bán có thể kiếm được lợi nhuận bất thường. Ví dụ, trong thời kỳ bong bóng internet giai đoạn 1995–2000, nhiều đợt IPO đã kết thúc ngày giao dịch đầu tiên với mức tăng hơn 100 phần trăm. Tuy nhiên, thành quả như vậy không phải lúc nào cũng xảy ra. Đôi khi các đợt phát hành được định giá quá cao, đồng nghĩa với việc giá cổ phiếu sụt giảm ngay trong ngày giao dịch đầu tiên. Ngoài ra, bằng chứng cũng cho thấy rằng các nhà đầu tư mua vào sau đợt chào bán ban đầu không thể kiếm được lợi nhuận bất thường bởi vì giá cả điều chỉnh nhanh chóng về các giá trị “thực”, điều này ủng hộ hiệu quả thị trường dạng bán mạnh. Trên thực tế, thành quả dài hạn tiếp theo của các đợt IPO nhìn chung được phát hiện là thấp hơn mức trung bình. Xét tổng thể, việc định giá thấp IPO và thành quả kém cỏi sau đó gợi ý rằng thị trường đã quá lạc quan lúc ban đầu (tức là các nhà đầu tư phản ứng thái quá).

> 40 Xem Jones, Rendleman, và Latané (1984).

> 41 Không có gì đáng ngạc nhiên khi người ta thường lập luận rằng phản ứng chậm chạp này đóng góp vào quy luật đà tăng trưởng (*momentum pattern*).

> 42 Một quy luật tương tự đã được ghi nhận trên thị trường trái phiếu doanh nghiệp, nơi giá trái phiếu phản ứng quá chậm trước các thông báo lợi nhuận mới của công ty cũng như trước những thay đổi trong xếp hạng tín nhiệm nợ của công ty.

> 43 Xem Brown (1997) để có bản tóm tắt các bằng chứng ủng hộ sự tồn tại của bất thường này. Xem Zarowin (1989) để biết bằng chứng liên quan đến vai trò của quy mô trong việc giải thích tỷ suất sinh lợi bất thường trước các bất ngờ; Alexander, Goff, và Peterson (1989) về bằng chứng liên quan đến chi phí giao dịch và các chiến lược lợi nhuận ngoài kỳ vọng; và Kim và Kim (2003) về bằng chứng chỉ ra rằng các tỷ suất sinh lợi bất thường có thể được giải thích bởi các nhân tố rủi ro.

<!-- PDF Page 155 -->

Một số nhà nghiên cứu đã kiểm tra kỹ lưỡng lý do tại sao các đợt IPO có vẻ mang lại tỷ suất sinh lợi bất thường. Do quy mô nhỏ của các công ty IPO và phương pháp tính tỷ trọng đều cho các mẫu nghiên cứu, những gì có vẻ là một bất thường có thể chỉ đơn giản là một sản phẩm ngẫu nhiên (*artifact*) của phương pháp luận nghiên cứu.<sup>44</sup>

#### **Khả năng Dự đoán Tỷ suất sinh lợi Dựa trên Thông tin Trước đó (Predictability of Returns Based on Prior Information)**

Một số nhà nghiên cứu đã ghi nhận rằng tỷ suất sinh lợi vốn cổ phần có liên hệ với thông tin trước đó về các yếu tố như lãi suất, tỷ lệ lạm phát, độ biến động của cổ phiếu, và tỷ suất cổ tức.<sup>45</sup> Nhưng việc phát hiện ra rằng tỷ suất sinh lợi vốn cổ phần bị ảnh hưởng bởi những thay đổi trong các yếu tố kinh tế cơ bản không phải là bằng chứng về sự kém hiệu quả của thị trường và sẽ không mang lại tỷ suất sinh lợi giao dịch bất thường.<sup>46</sup>

Hơn nữa, mối quan hệ giữa tỷ suất sinh lợi cổ phiếu và thông tin trước đó không nhất quán theo thời gian. Ví dụ, trong một nghiên cứu, mối quan hệ giữa giá cổ phiếu và tỷ suất cổ tức đã chuyển từ dương sang âm trong các giai đoạn khác nhau.<sup>47</sup> Do đó, một chiến lược giao dịch dựa trên tỷ suất cổ tức sẽ không mang lại tỷ suất sinh lợi bất thường một cách nhất quán.

#### **Hàm ý đối với các Chiến lược Đầu tư (Implications for Investment Strategies)**

Mặc dù việc xem xét các bất thường vừa được mô tả là rất thú vị, nhưng việc cố gắng hưởng lợi từ chúng trên thực tế lại không hề dễ dàng. Trên thực tế, hầu hết các nhà nghiên cứu đều kết luận rằng các bất thường quan sát được không phải là sự vi phạm hiệu quả thị trường mà đúng hơn là kết quả của các phương pháp luận thống kê được sử dụng để phát hiện ra các bất thường đó. Hệ quả là, nếu các phương pháp luận được hiệu chỉnh lại cho đúng, hầu hết các bất thường này đều biến mất.<sup>48</sup> Một điểm khác cần xem xét là trong một thị trường hiệu quả, các phản ứng thái quá (*overreactions*) có thể xảy ra, nhưng các phản ứng dưới mức (*under-reactions*) cũng xảy ra tương tự.<sup>49</sup> Do đó, tính trung bình, các thị trường vẫn là hiệu quả. Nói cách khác, các nhà đầu tư phải đối mặt với nhiều thách thức khi họ cố gắng chuyển hóa các bất thường thống kê thành lợi nhuận kinh tế. Hãy xem xét trích dẫn sau đây liên quan đến các bất thường từ tạp chí _The Economist_ (“Frontiers of Finance Survey,” ngày 9 tháng 10 năm 1993):

> Nhiều bất thường có thể được lý giải thỏa đáng. Khi chi phí giao dịch được tính đến, thực tế là giá cổ phiếu có xu hướng phản ứng thái quá với tin tức, giảm trở lại vào ngày hôm sau khi có tin tốt và bật tăng trở lại vào ngày hôm sau khi có tin xấu, hóa ra lại không thể khai thác được: những sự đảo chiều giá luôn nằm gọn trong chênh lệch giá chào mua - chào bán (*bid-ask spread*). Những hiệu ứng khác như hiệu ứng công ty nhỏ, hoạt động hiệu quả trong vài năm rồi lại thất bại trong vài năm. Những hiệu ứng khác nữa hóa ra chỉ đơn thuần là các đại diện (*proxies*) cho phần thưởng của việc chấp nhận rủi ro. Nhiều bất thường đã biến mất kể từ khi (và bởi vì) sự chú ý được hướng vào chúng.

Thật khó để hình dung việc ủy thác khoản tiền tiết kiệm hưu trí của bạn cho một nhà quản lý có chiến lược dựa trên việc mua chứng khoán vào các ngày thứ Hai, vốn có xu hướng có tỷ suất sinh lợi trung bình âm, và bán chúng vào các ngày thứ Sáu. Thứ nhất, tỷ suất sinh lợi âm vào ngày thứ Hai chỉ đơn thuần là một mức trung bình, vì vậy trong bất kỳ tuần cụ thể nào, chúng hoàn toàn có thể là số dương. Ngoài ra, một chiến lược như vậy sẽ phát sinh chi phí giao dịch rất lớn. Thậm chí quan trọng hơn, các nhà đầu tư có lẽ sẽ cảm thấy không thoải mái khi đầu tư tiền vốn của mình vào một chiến lược không có cơ sở lý luận kinh tế nền tảng thuyết phục nào.

> 44 Xem Brav, Geczy, và Gompers (1995).

> 45 Xem, ví dụ, Fama và Schwert (1977) cùng Fama và French (1988).

> 46 Xem Fama và French (2008).

> 47 Schwert (2003, Chương 15).

> 48 Fama (1998).

> 49 Điểm này được nêu ra bởi Fama (1998).


<!-- PDF Page 156 -->

# **<mark>8</mark>**

### **TÀI CHÍNH HÀNH VI (BEHAVIORAL FINANCE)**

mô tả tài chính hành vi (*behavioral finance*) và sự liên quan tiềm tàng của nó đối với việc thấu hiểu các bất thường thị trường

**Tài chính hành vi (*Behavioral finance*)** nghiên cứu hành vi của nhà đầu tư để hiểu cách con người đưa ra quyết định, ở cấp độ cá nhân và tập thể. Tài chính hành vi không giả định rằng con người xem xét tất cả các thông tin hiện có khi ra quyết định và hành động một cách duy lý bằng cách tối đa hóa hữu dụng (*utility*) trong phạm vi ràng buộc ngân sách cũng như cập nhật các kỳ vọng nhất quán với công thức Bayes. Các hành vi phát sinh có thể ảnh hưởng đến những gì được quan sát thấy trên các thị trường tài chính. Theo nghĩa rộng hơn, tài chính hành vi cố gắng giải thích tại sao các cá nhân lại đưa ra những quyết định mà họ thực hiện, cho dù những quyết định này là hợp lý (*rational*) hay phi lý trí (*irrational*). Trọng tâm của phần lớn các công trình nghiên cứu trong lĩnh vực này là về các thiên lệch hành vi (*behavioral biases*) ảnh hưởng đến các quyết định đầu tư. Hành vi của các cá nhân, đặc biệt là các thiên lệch hành vi của họ, đã được đưa ra như một lời giải thích khả dĩ cho một số bất thường định giá.

Hầu hết các mô hình định giá tài sản đều giả định rằng các thị trường là hợp lý và giá trị nội tại của một chứng khoán phản ánh sự hợp lý này. Nhưng hiệu quả thị trường và các mô hình định giá tài sản không đòi hỏi mỗi cá nhân đều phải hợp lý—mà đúng hơn, chỉ đòi hỏi rằng bản thân thị trường là hợp lý. Nếu các cá nhân chệch hướng khỏi sự hợp lý, những cá nhân khác được giả định là sẽ quan sát thấy sự chệch hướng này và phản ứng tương ứng. Những phản ứng này đưa thị trường tiến về trạng thái hiệu quả. Nếu điều này không xảy ra trên thực tế, có thể giải thích một số bất thường thị trường bằng cách tham chiếu đến các hành vi quan sát được và các thiên lệch hành vi.

#### **Ác cảm Thua lỗ (Loss Aversion)**

Trong hầu hết các mô hình tài chính, giả định được đặt ra là các nhà đầu tư có tâm lý ngại rủi ro (*risk averse*). **Ngại rủi ro (*Risk aversion*)** đề cập đến xu hướng con người không thích rủi ro và đòi hỏi tỷ suất sinh lợi kỳ vọng cao hơn để đền bù cho việc tiếp xúc với rủi ro tăng thêm. Tài chính hành vi cho phép khả năng rằng sự bất mãn xuất phát từ một khoản thua lỗ vượt quá sự hài lòng xuất phát từ một khoản lợi nhuận có cùng quy mô. **Ác cảm thua lỗ (*Loss aversion*)** đề cập đến xu hướng con người ghét các khoản thua lỗ nhiều hơn mức họ thích các khoản lợi nhuận tương đương. Điều này dẫn đến một sự ưu tiên mạnh mẽ cho việc né tránh thua lỗ thay vì đạt được lợi nhuận.<sup>50</sup> Một số người lập luận rằng các lý thuyết hành vi về ác cảm thua lỗ có thể giải thích hiện tượng phản ứng thái quá quan sát được trên các thị trường. Nếu ác cảm thua lỗ quan trọng hơn sự ngại rủi ro, các nhà nghiên cứu sẽ quan sát thấy rằng các nhà đầu tư phản ứng thái quá.<sup>51</sup> Mặc dù ác cảm thua lỗ có thể giải thích bất thường phản ứng thái quá, bằng chứng cũng cho thấy rằng việc phản ứng dưới mức (*under-reaction*) cũng phổ biến không kém gì phản ứng thái quá, điều này phản bác lại các lập luận đó.

#### **Hiệu ứng Bầy đàn (Herding)**

Hành vi bầy đàn đã được đưa ra như một lời giải thích khả dĩ cho hiện tượng phản ứng dưới mức và phản ứng thái quá trên các thị trường tài chính. **Hiệu ứng bầy đàn (*Herding*)** xảy ra khi các nhà đầu tư giao dịch ở cùng một phía của thị trường đối với cùng các chứng khoán, hoặc khi các nhà đầu tư phớt lờ thông tin và/hoặc phân tích riêng của chính họ và hành động giống như các nhà đầu tư khác. Hiệu ứng bầy đàn là hoạt động giao dịch co cụm (*clustered trading*) có thể dựa trên hoặc không dựa trên thông tin.<sup>52</sup> Hiệu ứng bầy đàn có thể dẫn đến phản ứng dưới mức hoặc phản ứng thái quá trước thông tin tùy thuộc vào hướng đi của đám đông.

> 50 Xem DeBondt và Thaler (1985) cùng Tversky và Kahneman (1981).

> 51 Xem Fama (1998).

> 52 Thuật ngữ được sử dụng khi có hiệu ứng bầy đàn không dựa trên thông tin là “hiệu ứng bầy đàn giả tạo” (*“spurious herding”*).

<!-- PDF Page 157 -->

#### **Sự Quá Tự tin (Overconfidence)**

Một thiên lệch hành vi được đưa ra để giải thích các bất thường định giá là sự quá tự tin (*overconfidence*). Nếu các nhà đầu tư quá tự tin, họ đánh giá quá cao khả năng của bản thân trong việc xử lý và diễn giải thông tin về một chứng khoán. Các nhà đầu tư quá tự tin có thể không xử lý thông tin một cách thích hợp, và nếu có một số lượng đủ lớn những nhà đầu tư này, các cổ phiếu sẽ bị định giá sai.<sup>53</sup> Nhưng hầu hết các nhà nghiên cứu đều lập luận rằng sự định giá sai này chỉ mang tính tạm thời, và giá cả cuối cùng sẽ tự điều chỉnh lại. Nếu phải mất một khoảng thời gian đủ dài để giá cả được định giá đúng trở lại và sự định giá sai này là có thể dự đoán được, các nhà đầu tư có thể kiếm được lợi nhuận bất thường.

Bằng chứng đã gợi ý rằng sự quá tự tin dẫn đến việc định giá sai tại các thị trường Hoa Kỳ, Vương quốc Anh, Đức, Pháp, và Nhật Bản.<sup>54</sup> Tuy nhiên, sự quá tự tin này chủ yếu diễn ra ở các công ty có tốc độ tăng trưởng cao hơn, vốn có mức giá phản ứng chậm trước thông tin mới.<sup>55</sup>

#### **Hiệu ứng Thác Thông tin (Information Cascades)**

Một ứng dụng của các lý thuyết hành vi vào thị trường và việc định giá tập trung vào vai trò của sự học hỏi cá nhân (*personal learning*) trên thị trường. Sự học hỏi cá nhân là những gì các nhà đầu tư học được bằng cách quan sát kết quả của các giao dịch và những gì họ học được từ “các cuộc trò chuyện”—những ý tưởng được chia sẻ giữa các nhà đầu tư về các tài sản cụ thể và về thị trường.<sup>56</sup> Sự tương tác xã hội và hiệu ứng lây lan (*contagion*) phát sinh là rất quan trọng trong việc định giá và có thể giải thích những hiện tượng như sự thay đổi giá mà không có tin tức đi kèm và những sai lầm trong định giá.

Các thiên lệch mà các nhà đầu tư mắc phải có thể dẫn đến hành vi bầy đàn hoặc thác thông tin (*information cascades*). Hiệu ứng bầy đàn và thác thông tin là những khái niệm có liên quan nhưng không đồng nhất với nhau. Một **thác thông tin (*information cascade*)** là sự truyền tải thông tin từ những người tham gia hành động trước tiên và các quyết định của họ ảnh hưởng đến quyết định của những người khác. Những người đang hành động dựa trên lựa chọn của người khác có thể đang phớt lờ những ưu tiên của chính mình để bắt chước lựa chọn của người khác. Cụ thể, thác thông tin có thể xảy ra liên quan đến việc công bố thông tin kế toán bởi vì thông tin kế toán có thể khó diễn giải và có thể chứa nhiều nhiễu (*noisy*). Ví dụ, việc công bố lợi nhuận rất khó diễn giải bởi vì cần phải hiểu con số đó đã được tính ra như thế nào, và chứa nhiều nhiễu bởi vì không chắc chắn lợi nhuận hiện tại hàm ý điều gì về lợi nhuận tương lai.

Thác thông tin có thể dẫn đến sự tự tương quan (*serial correlation*) của tỷ suất sinh lợi cổ phiếu, điều này nhất quán với các bất thường phản ứng thái quá. Liệu thác thông tin có dẫn đến việc định giá đúng hay không? Một số người lập luận rằng nếu một thác thông tin đang dẫn về phía một giá trị không chính xác, thác thông tin này là “mong manh” (*“fragile”*) và sẽ được điều chỉnh lại bởi vì các nhà đầu tư cuối cùng sẽ đặt nhiều trọng số hơn vào thông tin đại chúng hoặc hoạt động giao dịch của một nhà giao dịch có thông tin đã được công nhận.<sup>57</sup> Thác thông tin, mặc dù được ghi nhận trên các thị trường, không nhất thiết đồng nghĩa với việc các nhà đầu tư có thể khai thác sự hiểu biết về chúng như những cơ hội giao dịch sinh lời.

Liệu thác thông tin có hợp lý (*rational*) hay không? Nếu các nhà giao dịch có thông tin (*informed traders*) hành động trước và các nhà giao dịch không có thông tin (*uninformed traders*) bắt chước các nhà giao dịch có thông tin, hành vi này là nhất quán với sự hợp lý. Hoạt động giao dịch bắt chước của các nhà giao dịch không có thông tin có thể giúp thị trường phản ánh thông tin liên quan và cải thiện hiệu quả thị trường.<sup>58</sup> Tuy nhiên, hoạt động giao dịch bắt chước có thể dẫn

> 53 Một khía cạnh khác của sự quá tự tin là các nhà đầu tư quá tự tin vào khả năng lựa chọn các khoản đầu tư và quản lý danh mục của mình có xu hướng ít sử dụng sự đa dạng hóa hơn, mà chỉ đầu tư vào những gì quen thuộc nhất. Do đó, hành vi của nhà đầu tư có thể ảnh hưởng đến kết quả đầu tư—tỷ suất sinh lợi và rủi ro—mà không có hàm ý gì đối với tính hiệu quả của các thị trường.

> 54 Scott, Stumpp, và Xu (2003) cùng Boujelbene Abbes, Boujelbene, và Bouri (2009).

> 55 Scott, Stumpp, và Xu (2003).

> 56 Hirshleifer và Teoh (2009).

> 57 Avery và Zemsky (1999).

> 58 Một khả năng thay thế khác là các nhà giao dịch không có thông tin chiếm đa số trong những người tham gia thị trường và những người bắt chước thực hiện việc bắt chước không phải vì họ đồng ý với hành động của số đông mà vì họ đang tìm cách hành động dựa trên hành động của các nhà giao dịch không có thông tin.

<!-- PDF Page 158 -->

đến sự phản ứng thái quá trước thông tin. Bằng chứng thực nghiệm chỉ ra rằng thác thông tin diễn ra mạnh hơn đối với một cổ phiếu khi chất lượng thông tin liên quan đến công ty đó là thấp.<sup>59</sup> Thác thông tin có thể làm tăng cường lượng thông tin hiện có cho các nhà đầu tư.

#### **Các Thiên lệch Hành vi Khác (Other Behavioral Biases)**

Các thiên lệch hành vi khác đã được đưa ra để giải thích hành vi quan sát được của nhà đầu tư bao gồm:

- **thiên lệch đại diện (*representativeness*)** — các nhà đầu tư đánh giá thông tin mới và xác suất của các kết quả dựa trên sự tương đồng với trạng thái hiện tại hoặc với một phân loại quen thuộc;

- **kế toán tâm lý (*mental accounting*)** — các nhà đầu tư theo dõi các khoản lãi và lỗ cho các khoản đầu tư khác nhau trong các tài khoản tâm lý riêng biệt và đối xử với các tài khoản đó một cách khác nhau;

- **thiên lệch bảo thủ (*conservatism*)** — các nhà đầu tư có xu hướng phản ứng chậm trước thông tin mới và tiếp tục duy trì các quan điểm hoặc dự báo trước đó của họ; và

- **đóng khung hẹp (*narrow framing*)** — các nhà đầu tư tập trung vào các vấn đề một cách cô lập và phản ứng với các vấn đề dựa trên cách thức các vấn đề đó được đặt ra.<sup>60</sup>

Ý tưởng cơ bản đằng sau tài chính hành vi là các nhà đầu tư là con người và do đó không hoàn hảo. Những hành vi chưa hoàn toàn hợp lý quan sát được này có thể giúp giải thích các bất thường định giá quan sát được. Niềm tin mà các nhà đầu tư có về giá trị của một tài sản nhất định có thể không đồng nhất (*homogeneous*). Nhưng một vấn đề vẫn còn gây tranh cãi là liệu những hiểu biết sâu sắc này có thể giúp một người nào đó xác định và khai thác bất kỳ sự định giá sai nào hay không. Nói cách khác, liệu các nhà đầu tư có thể sử dụng kiến thức về các thiên lệch hành vi để dự đoán giá tài sản sẽ bị ảnh hưởng như thế nào và hành động dựa trên những dự đoán đó để kiếm được lợi nhuận bất thường hay không?

#### **Tài chính Hành vi và Nhà đầu tư (Behavioral Finance and Investors)**

Các thiên lệch hành vi có thể ảnh hưởng đến tất cả những người tham gia thị trường, từ nhà đầu tư mới vào nghề cho đến nhà quản lý đầu tư giàu kinh nghiệm nhất. Sự hiểu biết về tài chính hành vi có thể giúp những người tham gia thị trường nhận ra các thiên lệch hành vi của chính họ và của những người khác. Nhờ sự nhận thức này, họ có thể phản ứng và đưa ra các quyết định được cải thiện tốt hơn, ở cả cấp độ cá nhân và tập thể.

#### **Tài chính Hành vi và Thị trường Hiệu quả (Behavioral Finance and Efficient Markets)**

Việc sử dụng tài chính hành vi để giải thích việc định giá quan sát được là một phần quan trọng của việc thấu hiểu cách thức các thị trường vận hành và cách thức giá cả được xác định. Liệu có một lời giải thích mang tính hành vi cho các bất thường thị trường hay không vẫn là một cuộc tranh luận. Các bất thường định giá liên tục được phát hiện, và sau đó các lời giải thích mang tính thống kê và hành vi được đưa ra để giải thích các bất thường này.

Một mặt, nếu các nhà đầu tư buộc phải duy lý để các thị trường hiệu quả tồn tại, thì tất cả những sự bất hoàn hảo của các nhà đầu tư con người gợi ý rằng các thị trường không thể hiệu quả được. Mặt khác, nếu tất cả những gì cần thiết để các thị trường trở nên hiệu quả là việc các nhà đầu tư không thể đánh bại thị trường một cách nhất quán trên cơ sở điều chỉnh theo rủi ro, thì bằng chứng thực tế quả thực ủng hộ hiệu quả thị trường.

> 59 Avery và Zemsky (1999) cùng Bikhchandani, Hirshleifer, và Welch (1992).

> 60 Để xem tổng thuật về các vấn đề hành vi này, xem Hirshleifer (2001).

<!-- PDF Page 159 -->

## **TÓM TẮT (SUMMARY)**

Bài đọc này đã cung cấp một cái nhìn tổng quan về lý thuyết và bằng chứng liên quan đến hiệu quả thị trường, đồng thời đã thảo luận về các dạng hiệu quả thị trường khác nhau cũng như các hàm ý đối với phân tích cơ bản, phân tích kỹ thuật, và quản lý danh mục đầu tư. Kết luận chung được rút ra từ giả thuyết thị trường hiệu quả là không thể đánh bại thị trường một cách nhất quán bằng cách tạo ra tỷ suất sinh lợi vượt quá mức kỳ vọng tương ứng với mức độ rủi ro của khoản đầu tư.

Các điểm chính bổ sung bao gồm:

- Tính hiệu quả của một thị trường bị ảnh hưởng bởi số lượng người tham gia thị trường và độ sâu bao phủ của các nhà phân tích (*depth of analyst coverage*), tính sẵn có của thông tin, và các giới hạn đối với giao dịch.

- Có ba dạng thị trường hiệu quả, mỗi dạng dựa trên những gì được coi là thông tin được sử dụng trong việc xác định giá tài sản.Ở dạng yếu (*weak form*), giá tài sản phản ánh đầy đủ tất cả dữ liệu thị trường, tức là đề cập đến tất cả các thông tin về giá và khối lượng giao dịch trong quá khứ. Ở dạng bán mạnh (*semi-strong form*), giá tài sản phản ánh tất cả các thông tin đã được công chúng biết đến và hiện có sẵn. Ở dạng mạnh (*strong form*), giá tài sản phản ánh đầy đủ mọi thông tin, bao gồm cả thông tin đại chúng và thông tin nội bộ/tư nhân.

- Giá trị nội tại (*Intrinsic value*) đề cập đến giá trị thực của một tài sản, trong khi giá trị thị trường (*market value*) đề cập đến mức giá mà tại đó một tài sản có thể được mua hoặc bán. Khi các thị trường là hiệu quả, hai giá trị này phải bằng nhau hoặc rất gần nhau. Nhưng khi các thị trường không hiệu quả, hai giá trị này có thể phân kỳ đáng kể.

- Hầu hết các bằng chứng thực nghiệm đều ủng hộ ý tưởng rằng các thị trường chứng khoán tại các quốc gia phát triển có hiệu quả dạng bán mạnh; tuy nhiên, bằng chứng thực nghiệm không ủng hộ dạng mạnh của giả thuyết thị trường hiệu quả.

- Một số bất thường đã được ghi nhận đi ngược lại khái niệm hiệu quả thị trường, bao gồm bất thường quy mô (*size anomaly*), bất thường tháng Giêng (*January anomaly*), và các bất thường người chiến thắng–kẻ thua cuộc (*winners–losers anomalies*). Tuy nhiên, trong hầu hết các trường hợp, các bằng chứng trái chiều vừa ủng hộ vừa bác bỏ bất thường đó.

- Tài chính hành vi sử dụng tâm lý học con người, chẳng hạn như các thiên lệch hành vi, nhằm cố gắng giải thích các quyết định đầu tư. Trong khi tài chính hành vi rất hữu ích trong việc thấu hiểu các quyết định quan sát được, một thị trường vẫn có thể được coi là hiệu quả ngay cả khi những người tham gia thị trường thể hiện các hành vi có vẻ phi lý trí, chẳng hạn như hiệu ứng bầy đàn (*herding*).

<!-- PDF Page 160 -->

## **TÀI LIỆU THAM KHẢO (REFERENCES)**

- Alexander, John C., Delbert Goff, and Pamela P. Peterson. 1989. “Profitability of a Trading Strategy Based on Unexpected Earnings.” _Financial Analysts Journal_ 45, vol. , no. 4:65–71. 10.2469/faj.v45.n4.65

- Bessembinder, Hendrik and Kalok Chan. 1998. “Market Efficiency and the Returns to Technical Analysis.” _Financial Management_ 27, vol. , no. 2:5–17. 10.2307/3666289

- Bikhchandani, Sushil, David Hirshleifer, and Ivo Welch. 1992. “A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades.” _Journal of Political Economy_ 100, vol. , no. 5:992–1026. 10.1086/261849

- Brav, Alon, Christopher Geczy, and Paul A. Gompers. 1995. “The Long-Run Underperformance of Seasoned Equity Offerings Revisited.” Working paper, Harvard University.

- Brealey, Richard. 1983. “Can Professional Investors Beat the Market?” _An Introduction to Risk and Return from Common Stocks_ , 2nd edition. Cambridge, MA: MIT Press.

- Bris, Arturo, William N. Goetzmann, and Ning Zhu. 2009. “Efficiency and the Bear: Short Sales and Markets around the World.” _Journal of Finance_ 62, vol. , no. 3:1029–1079. 10.1111/j.154 0-6261.2007.01230.x

- Brown, Laurence D. 1997. “Earning Surprise Research: Synthesis and Perspectives.” _Financial Analysts Journal_ 53, vol. , no. 2:13–19. 10.2469/faj.v53.n2.2067

- Capaul, Carlo, Ian Rowley, and William Sharpe. 1993. “International Value and Growth Stock Returns.” _Financial Analysts Journal_ 49, vol. :27–36. 10.2469/faj.v49.n1.27

- Chen, Kong-Jun and Xiao-Ming Li. 2006. “Is Technical Analysis Useful for Stock Traders in China? Evidence from the Szse Component A-Share Index.” _Pacific Economic Review_ 11, vol. , no. 4:477–488. 10.1111/j.1468-0106.2006.00329.x

- Chordia, Tarun, Richard Roll, and Avanidhar Subrahmanyam. 2005. “Evidence on the Speed of Convergence to Market Efficiency.” _Journal of Financial Economics_ 76, vol. , no. 2:271–292. 10.1016/j.jfineco.2004.06.004

- DeBondt, Werner and Richard Thaler. 1985. “Does the Stock Market Overreact?” _Journal of Finance_ 40, vol. , no. 3:793–808. 10.2307/2327804

- Deng, Xiaohu, Sandra Mortal, and Vishal Gupta. 2017. “The Real Effects of Short Selling Constraints: Cross-Country Evidence.” Working paper.

- Dimson, Elroy and Carolina Minio-Kozerski. 1999. “Closed-End Funds: A Survey.” _Financial Markets, Institutions & Instruments_ 8, vol. , no. 2:1–41. 10.1111/1468-0416.00027

- Fama, Eugene F. 1970. “Efficient Capital Markets: A Review of Theory and Empirical Work.” _Journal of Finance_ 25, vol. , no. 2:383–417. 10.2307/2325486

- Fama, Eugene F. 1976. _Foundations of Finance_ . New York: Basic Books.

- Fama, Eugene F. 1998. “Market Efficiency, Long-Term Returns, and Behavioral Finance.” _Journal of Financial Economics_ 50, vol. , no. 3:283–306. 10.1016/S0304-405X(98)00026-9

- Fama, Eugene F. and Kenneth R. French. 1988. “Dividend Yields and Expected Stock Returns.” _Journal of Financial Economics_ 22, vol. , no. 1:3–25. 10.1016/0304-405X(88)90020-7

- Fama, Eugene F. and Kenneth R. French. 1995. “Size and Book-to-Market Factors in Earnings and Returns.” _Journal of Finance_ 50, vol. , no. 1:131–155. 10.2307/2329241

- Fama, Eugene F. and Kenneth R. French. 1998. “Value versus Growth: The International Evidence.” _Journal of Finance_ 53, vol. :1975–1999. 10.1111/0022-1082.00080

- Fama, Eugene F. and Kenneth R. French. 2008. “Dissecting Anomalies.” _Journal of Finance_ 63, vol. , no. 4:1653–1678. 10.1111/j.1540-6261.2008.01371.x

- Grossman, Sanford J. and Joseph E. Stiglitz. 1980. “On the Impossibility of Informationally Efficient Markets.” _American Economic Review_ 70, vol. , no. 3:393–408.

- Hirshleifer, David. 2001. “Investor Psychology and Asset Pricing.” _Journal of Finance_ 56, vol. , no. 4:1533–1597. 10.1111/0022-1082.00379

- Hirshleifer, David and Siew Hong Teoh. 2009. “Thought and Behavior Contagion in Capital Markets.” In _Handbook of Financial Markets: Dynamics and Evolution_ . Edited by Klaus Reiner Schenk-Hoppe and Thorstein Hens. Amsterdam: North Holland.

<!-- PDF Page 161 -->

- Jacobs, Bruce I. and Kenneth N. Levy. 1988. “Calendar Anomalies: Abnormal Returns at Calendar Turning Points.” _Financial Analysts Journal_ 44, vol. , no. 6:28–39. 10.2469/faj.v44. n6.28

- Jaffe, Jeffrey. 1974. “Special Information and Insider Trading.” _Journal of Business_ 47, vol. , no. 3:410–428. 10.1086/295655

- Jegadeesh, Narayan and Sheridan Titman. 2001. “Profitability of Momentum Strategies: An Evaluation of Alternative Explanations.” _Journal of Finance_ 56, vol. :699–720. 10.1111/0022-1082.00342

- Johnson, Timothy C. 2002. “Rational Momentum Effects.” _Journal of Finance_ 57, vol. , no. 2:585–608. 10.1111/1540-6261.00435

- Kim, Donchoi and Myungsun Kim. 2003. “A Multifactor Explanation of Post-Earnings Announcement Drift.” _Journal of Financial and Quantitative Analysis_ 38, vol. , no. 2:383–398. 10.2307/4126756

- Kim, Dongcheol. 2006. “On the Information Uncertainty Risk and the January Effect.” _Journal of Business_ 79, vol. , no. 4:2127–2162. 10.1086/503659

- Lee, Charles M.C., Andrei Sheifer, and Richard H. Thaler. 1990. “Anomalies: Closed-End Mutual Funds.” _Journal of Economic Perspectives_ 4, vol. , no. 4:153–164.

- Malkiel, Burton G. 1995. “Returns from Investing in Equity Mutual Funds 1971 to 1991.” _Journal of Finance_ 50, vol. :549–572. 10.2307/2329419

- Mobarek, Asma, A. Sabur Mollah, and Rafiqul Bhuyan. 2008. “Market Efficiency in Emerging Stock Market.” _Journal of Emerging Market Finance_ 7, no. 1:17–41. 10.1177/097265270700700102

- Pontiff, Jeffrey. 1995. “Closed-End Fund Premia and Returns: Implications for Financial Market Equilibrium.” _Journal of Financial Economics_ 37, 341–370. 10.1016/0304-405X(94)00800-G

- Pontiff, Jeffrey. 1996. “Costly Arbitrage: Evidence from Closed-End Funds.” _Quarterly Journal of Economics_ 111, vol. , no. 4:1135–1151. 10.2307/2946710

- Roll, Richard. 1983. “On Computing Mean Returns and the Small Firm Premium.” _Journal of Financial Economics_ 12, vol. :371–386. 10.1016/0304-405X(83)90055-7

- Rozeff, Michael S. and Mir A. Zaman. 1988. “Market Efficiency and Insider Trading: New Evidence.” _Journal of Business_ 61, vol. :25–44. 10.1086/296418

- Schwert, G. William. 2003. “Anomalies and Market Efficiency.” _Handbook of the Economics of Finance_ . Edited by George M. Constantinides, M. Harris, and Rene Stulz. Amsterdam: Elsevier Science, B. V.

- Scott, James, Margaret Stumpp, and Peter Xu. 2003. “Overconfidence Bias in International Stock Prices.” _Journal of Portfolio Management_ 29, vol. , no. 2:80–89. 10.3905/jpm.2003.319875

- Tversky, Amos and Daniel Kahneman. 1981. “The Framing of Decisions and the Psychology of Choice.” _Science_ 211, vol. , no. 30:453–458. 10.1126/science.7455683

- Yau, Jot, Thomas Schneeweis, Thomas Robinson, and Lisa Weiss. 2007. “Alternative Investments Portfolio Management.” _Managing Investment Portfolios: A Dynamic Process_ . Hoboken, NJ: John Wiley & Sons.

- Zarowin, P. 1989. “Does the Stock Market Overreact to Corporate Earnings Information?” _Journal of Finance_ 44, vol. :1385–1399. 10.2307/2328649
