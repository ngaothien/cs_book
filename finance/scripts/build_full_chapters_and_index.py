#!/usr/bin/env python3
"""
Builds consolidated full-chapter Markdown files (`LMXX_Full_<Slug>.md`) from the translated Part files
so the user has BOTH:
1. Single complete file per chapter (Learning Module)
2. Split part files for long chapters
And generates Volume-level and Master `README.md` index files in `vi_markdown/`.
"""

import os
import re
import json
from collections import defaultdict

BASE_DIR = "/Users/kaka/learning/finance"
EN_ROOT = os.path.join(BASE_DIR, "en_markdown")
VI_ROOT = os.path.join(BASE_DIR, "vi_markdown")

VOLUMES = [
    ("01_Quantitative_Methods", "Tập 1: Phương pháp Định lượng (Quantitative Methods)"),
    ("02_Economics", "Tập 2: Kinh tế học (Economics)"),
    ("03_Corporate_Issuers", "Tập 3: Tổ chức Phát hành Doanh nghiệp (Corporate Issuers)"),
    ("04_Financial_Statement_Analysis", "Tập 4: Phân tích Báo cáo Tài chính (Financial Statement Analysis)"),
    ("05_Equity_Investments", "Tập 5: Đầu tư Cổ phiếu (Equity Investments)"),
    ("06_Fixed_Income", "Tập 6: Chứng khoán Thu nhập Cố định (Fixed Income)"),
    ("07_Derivatives", "Tập 7: Công cụ Phái sinh (Derivatives)"),
    ("08_Alternative_Investments", "Tập 8: Đầu tư Thay thế (Alternative Investments)"),
    ("09_Portfolio_Management", "Tập 9: Quản lý Danh mục Đầu tư (Portfolio Management)"),
    ("10_Ethical_and_Professional_Standards", "Tập 10: Chuẩn mực Đạo đức & Nghề nghiệp (Ethical and Professional Standards)"),
]


def slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "_", text).strip("_")
    return text[:45].strip("_")


def build_all():
    master_lines = [
        "# Giáo Trình CFA® Program Curriculum 2026 – Level I (Bản Dịch Tiếng Việt Toàn Văn)\n",
        "> **Thông tin bộ tài liệu:**\n",
        "> - **Nguồn gốc:** Trọn bộ 10 Tập (*Volumes 1–10*) giáo trình chính thức CFA® Program Curriculum 2026 Level I (**3.416 trang PDF**).\n",
        "> - **Quy mô bản dịch:** **94 Chương (*Learning Modules* + Phụ lục/Glossary)** được chia thành **279 file thành phần (*Parts*)** và **95 file tổng hợp nguyên chương (*Full Modules*)**, tổng cộng hơn **2,14 triệu từ tiếng Việt**.\n",
        "> - **Đặc điểm:** Dịch toàn văn 100% (không tóm tắt, không lược bỏ), giữ nguyên toàn bộ hình ảnh/biểu đồ PNG gốc (`assets/`), công thức chuẩn hóa LaTeX (`$$...$$`), bảng biểu Markdown (`Exhibits`), ví dụ thực hành (*Examples*), câu hỏi (*Question Sets*) và bài tập cuối chương kèm lời giải chi tiết (*Practice Problems & Solutions*).\n\n",
        "## Tổng Quan 10 Tập (Volumes 1–10)\n",
        "| Tập | Chủ đề (Topic) | Số Chương (Modules) | Số File Chi Tiết (Parts) | Tổng Số Từ Tiếng Việt | Mục Lục Chi Tiết |\n",
        "| :--- | :--- | :---: | :---: | :---: | :--- |\n",
    ]

    vol_sections = []

    for vol_dir, vol_title in VOLUMES:
        manifest_path = os.path.join(EN_ROOT, vol_dir, "manifest.json")
        manifest = json.load(open(manifest_path, encoding="utf-8"))
        vi_vol_dir = os.path.join(VI_ROOT, vol_dir)

        # Group by module_prefix
        by_mod = defaultdict(list)
        for item in manifest:
            by_mod[item["module_prefix"]].append(item)

        vol_vi_words = 0
        vol_readme = [
            f"# {vol_title}\n\n",
            "| Mã Chương | Tên Chương (Learning Module) | Trang PDF | File Nguyên Chương (Full) | Các File Tách Phần (Parts) | Số Từ (VI) |\n",
            "| :---: | :--- | :---: | :--- | :--- | :---: |\n",
        ]

        mod_rows_for_master = []

        for prefix, items in by_mod.items():
            raw_mod_title = items[0]["module_title"]
            clean_mod_title = re.sub(r"^Learning Module\s+\d+\s*", "", raw_mod_title).strip()
            start_p = items[0]["start_page"]
            end_p = items[-1]["end_page"]

            part_contents = []
            mod_words = 0
            part_links_vol = []
            part_links_master = []

            for it in items:
                vi_path = it["vi_path"]
                txt = open(vi_path, encoding="utf-8").read()
                w = len(txt.split())
                mod_words += w
                vol_vi_words += w
                part_contents.append(txt)
                fn = it["filename"]
                p_idx = it["part_index"]
                part_links_vol.append(f"[Part {p_idx}]({fn})")
                part_links_master.append(f"[Part {p_idx}]({vol_dir}/{fn})")

            if len(items) == 1:
                full_fn = items[0]["filename"]
            else:
                full_fn = f"{prefix}_Full_{slugify(clean_mod_title)}.md"
                full_path = os.path.join(vi_vol_dir, full_fn)
                combined_header = (
                    f"# {vol_title}\n"
                    f"## {raw_mod_title} (Trang PDF {start_p}–{end_p})\n\n---\n\n"
                )
                combined_body = "\n\n---\n\n".join(part_contents)
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write(combined_header + combined_body)

            vol_readme.append(
                f"| **{prefix}** | {clean_mod_title} | tr. {start_p}–{end_p} | "
                f"[{full_fn}]({full_fn}) | {', '.join(part_links_vol)} | {mod_words:,d} |\n"
            )
            mod_rows_for_master.append(
                f"| **{prefix}** | {clean_mod_title} | tr. {start_p}–{end_p} | "
                f"[{full_fn}]({vol_dir}/{full_fn}) | {', '.join(part_links_master)} | {mod_words:,d} |\n"
            )

        with open(os.path.join(vi_vol_dir, "README.md"), "w", encoding="utf-8") as f:
            f.writelines(vol_readme)

        master_lines.append(
            f"| **{vol_dir[:2]}** | **{vol_title}** | {len(by_mod)} | {len(manifest)} | "
            f"**{vol_vi_words:,d}** | [Xem mục lục]({vol_dir}/README.md) |\n"
        )

        vol_sec = [
            f"\n---\n\n## {vol_title}\n\n",
            "| Mã Chương | Tên Chương (Learning Module) | Trang PDF | File Nguyên Chương (Full) | Các File Tách Phần (Parts) | Số Từ (VI) |\n",
            "| :---: | :--- | :---: | :--- | :--- | :---: |\n",
        ] + mod_rows_for_master
        vol_sections.extend(vol_sec)

    master_lines.extend(vol_sections)
    master_readme_path = os.path.join(VI_ROOT, "README.md")
    with open(master_readme_path, "w", encoding="utf-8") as f:
        f.writelines(master_lines)

    print(f"Successfully generated all full-chapter files and {master_readme_path}")


if __name__ == "__main__":
    build_all()
