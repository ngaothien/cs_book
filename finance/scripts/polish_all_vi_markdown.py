import glob
import os
import re

vi_root = "/Users/kaka/learning/finance/vi_markdown"

# 1. Exact replacements for the 16 stray foreign-script tokens
foreign_replacements = [
    ("trung bình điều hòa賦 (gán) trọng số", "trung bình điều hòa gán trọng số"),
    ("tiêu chuẩn vốn pháp규 (*regulatory capital standards*)", "tiêu chuẩn vốn pháp định (*regulatory capital standards*)"),
    ("khấu hao và摊銷 (Net Debt/EBITDA)", "khấu hao và phân bổ (Net Debt/EBITDA)"),
    ("Hiệu ứng thời점 trong ngày (*Time-of-day effect*)", "Hiệu ứng thời điểm trong ngày (*Time-of-day effect*)"),
    ("hữu hình và摊銷 tài sản vô hình (*depreciation and amortization*)", "hữu hình và phân bổ tài sản vô hình (*depreciation and amortization*)"),
    ("việc suy출 các dữ liệu đầu vào", "việc suy xuất các dữ liệu đầu vào"),
    ("mối quan hệ nghịch변 với giá", "mối quan hệ nghịch biến với giá"),
    ("một vấn đề lớn среди các chỉ số quỹ phòng hộ", "một vấn đề lớn trong số các chỉ số quỹ phòng hộ"),
    ("các ngành đang失sủng (*out-of-favor industries*)", "các ngành đang thất sủng (*out-of-favor industries*)"),
    ("điều này оправдывает việc cần có", "điều này lý giải sự cần thiết phải có"),
    ("phân tích quy因 hiệu quả hoạt động", "phân tích quy thuộc hiệu quả hoạt động"),
    ("Phân tích quy因 hiệu quả hoạt động", "Phân tích quy thuộc hiệu quả hoạt động"),
    ("phân tích quy因/đóng góp (*attribution*)", "phân tích quy thuộc/đóng góp (*attribution*)"),
    ("trường hợp cực단 trong đó", "trường hợp cực đoan trong đó"),
    ("bạn đã xác립 được các thông tin sau:", "bạn đã xác lập được các thông tin sau:"),
    ("tăng vọt một cách劇 liệt do điều kiện", "tăng vọt một cách dữ dội do điều kiện"),
    ("Phân tích неизбежно (tất yếu) phải quay về", "Phân tích tất yếu phải quay về"),
]

part_files = sorted([
    p for p in glob.glob(os.path.join(vi_root, "*/*.md"))
    if not (os.path.basename(p).endswith("README.md") or "_Full_" in os.path.basename(p))
])

print(f"Processing {len(part_files)} part files...")

fixed_foreign = 0
fixed_pic_blocks = 0
fixed_strikethrough = 0
fixed_dollar = 0

pic_block_re = re.compile(r"<!-- Start of picture text -->\n(.*?)<!-- End of picture text -->", re.S)
heading_strike_re = re.compile(r"^(#{1,6}\s+.*?)~~(.*?)~~(.*)$", re.M)

for p in part_files:
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    orig = text

    # Special addition for Fixed_Income.pdf-0471-07.png caption
    if p.endswith("06_Fixed_Income/LM17_Part2_The_Securitization_Process.md"):
        target_block = "![](assets/Fixed_Income.pdf-0471-07.png)\n\n<!-- Start of picture text -->"
        replacement_block = (
            "![](assets/Fixed_Income.pdf-0471-07.png)\n\n"
            "> **Chú thích hình ảnh:** Sơ đồ quy trình chứng khoán hóa của AR & C với các bước đánh số từ 1 đến 9 giữa Khách hàng (*Customers*), AR & C, pháp nhân tại vị trí số 9 (SPE), và các Nhà đầu tư (*Investors*).\n\n"
            "<!-- Start of picture text -->"
        )
        if target_block in text:
            text = text.replace(target_block, replacement_block, 1)

    # Fix $\$$ in 07_Derivatives/LM06_Part2
    if "|**Yết giá (*Price Quotation*):**|$\\$$ trên mỗi pound|" in text:
        text = text.replace("|**Yết giá (*Price Quotation*):**|$\\$$ trên mỗi pound|", "|**Yết giá (*Price Quotation*):**|\\$ trên mỗi pound|")
        fixed_dollar += 1

    # Fix stray foreign characters
    for old_s, new_s in foreign_replacements:
        if old_s in text:
            cnt = text.count(old_s)
            text = text.replace(old_s, new_s)
            fixed_foreign += cnt

    # Wrap <!-- Start of picture text --> ... <!-- End of picture text --> into single HTML comment <!-- Picture Text: ... -->
    def _wrap_pic(m):
        global fixed_pic_blocks
        fixed_pic_blocks += 1
        inner = m.group(1).strip().replace("--", "—")
        return f"<!-- Picture Text: {inner} -->"

    text = pic_block_re.sub(_wrap_pic, text)

    # Strip erroneous ~~ from headings
    while heading_strike_re.search(text):
        text, n_sub = heading_strike_re.subn(r"\1\2\3", text)
        fixed_strikethrough += n_sub

    if text != orig:
        with open(p, "w", encoding="utf-8") as f:
            f.write(text)

print(f"Done! Fixed foreign tokens: {fixed_foreign}, picture OCR comments wrapped: {fixed_pic_blocks}, strikethrough headings cleaned: {fixed_strikethrough}, dollar escapes fixed: {fixed_dollar}")
