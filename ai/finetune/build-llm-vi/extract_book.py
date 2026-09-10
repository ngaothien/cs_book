#!/usr/bin/env python3
"""
Script trích xuất toàn bộ nội dung sách Build-a-large-language-models.pdf
ra file text, mỗi trang được đánh dấu rõ ràng.
"""
import pymupdf

PDF_PATH = "/Users/kaka/dev/docs/cs_book/ai/finetune/Build-a-large-language-models.pdf"
OUTPUT_DIR = "/Users/kaka/dev/docs/cs_book/ai/finetune/build-llm-vi/raw"

import os
os.makedirs(OUTPUT_DIR, exist_ok=True)

doc = pymupdf.open(PDF_PATH)
total_pages = len(doc)
print(f"Total pages: {total_pages}")

# Chia thành các phần theo cấu trúc sách
sections = {
    "00-front-matter": (0, 22),      # pages 1-22
    "01-chapter1": (22, 38),          # pages 23-38
    "02-chapter2": (38, 71),          # pages 39-71
    "03-chapter3": (71, 113),         # pages 72-113
    "04-chapter4": (113, 149),        # pages 114-149
    "05-chapter5": (149, 190),        # pages 150-190
    "06-chapter6": (190, 225),        # pages 191-225
    "07-chapter7": (225, 272),        # pages 226-272
    "08-appendix-a": (272, 299),      # pages 273-299
}

# Xuất toàn bộ thành 1 file lớn
all_text_path = os.path.join(OUTPUT_DIR, "full-book.txt")
with open(all_text_path, "w", encoding="utf-8") as f:
    for i in range(total_pages):
        text = doc[i].get_text()
        f.write(f"\n{'='*80}\n")
        f.write(f"PAGE {i+1}\n")
        f.write(f"{'='*80}\n")
        f.write(text)
        f.write("\n")
print(f"Written full book to: {all_text_path}")

# Xuất từng phần riêng
for name, (start, end) in sections.items():
    filepath = os.path.join(OUTPUT_DIR, f"{name}.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        for i in range(start, min(end, total_pages)):
            text = doc[i].get_text()
            f.write(f"\n{'='*80}\n")
            f.write(f"PAGE {i+1}\n")
            f.write(f"{'='*80}\n")
            f.write(text)
            f.write("\n")
    page_count = min(end, total_pages) - start
    print(f"Written {name}.txt ({page_count} pages)")

doc.close()
print("\nDone! All raw text extracted.")
