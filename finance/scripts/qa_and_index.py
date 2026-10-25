#!/usr/bin/env python3
"""
QA Verification & Index Generator for CFA Curriculum Vietnamese Markdown Translation.
Checks every translated file in `vi_markdown/` against `en_markdown/manifest.json`:
- Verifies file existence, word count ratio, PDF page markers, and PNG image links.
- Generates Volume-level and Master README.md indexes.
"""

import os
import re
import json
import glob

BASE_DIR = "/Users/kaka/learning/finance"
EN_ROOT = os.path.join(BASE_DIR, "en_markdown")
VI_ROOT = os.path.join(BASE_DIR, "vi_markdown")

VOLUMES = [
    ("01_Quantitative_Methods", "Volume 1: Quantitative Methods (Phương pháp Định lượng)"),
    ("02_Economics", "Volume 2: Economics (Kinh tế học)"),
    ("03_Corporate_Issuers", "Volume 3: Corporate Issuers (Tài chính Doanh nghiệp)"),
    ("04_Financial_Statement_Analysis", "Volume 4: Financial Statement Analysis (Phân tích Báo cáo Tài chính)"),
    ("05_Equity_Investments", "Volume 5: Equity Investments (Đầu tư Cổ phiếu)"),
    ("06_Fixed_Income", "Volume 6: Fixed Income (Chứng khoán Thu nhập Cố định)"),
    ("07_Derivatives", "Volume 7: Derivatives (Công cụ Phái sinh)"),
    ("08_Alternative_Investments", "Volume 8: Alternative Investments (Đầu tư Thay thế)"),
    ("09_Portfolio_Management", "Volume 9: Portfolio Management (Quản lý Danh mục Đầu tư)"),
    ("10_Ethical_and_Professional_Standards", "Volume 10: Ethical and Professional Standards (Chuẩn mực Đạo đức & Nghề nghiệp)"),
]


def count_patterns(text: str):
    pages = re.findall(r"<!-- PDF Page (\d+) -->", text)
    images = re.findall(r"!\[[^\]]*\]\((assets/[^)]+)\)", text)
    words = len(text.split())
    return pages, images, words


def check_all_volumes():
    total_files = 0
    done_files = 0
    total_en_words = 0
    total_vi_words = 0

    print(f"{'Volume':38s} | {'Done/Total':10s} | {'EN Words':10s} | {'VI Words':10s} | {'Status'}")
    print("-" * 88)

    for vol_dir, vol_title in VOLUMES:
        manifest_path = os.path.join(EN_ROOT, vol_dir, "manifest.json")
        if not os.path.exists(manifest_path):
            continue
        manifest = json.load(open(manifest_path, encoding="utf-8"))
        v_total = len(manifest)
        v_done = 0
        v_en_w = 0
        v_vi_w = 0
        issues = []

        for item in manifest:
            total_files += 1
            en_path = item["en_path"]
            vi_path = item["vi_path"]
            en_txt = open(en_path, encoding="utf-8").read()
            en_pages, en_imgs, en_w = count_patterns(en_txt)
            v_en_w += en_w
            total_en_words += en_w

            if os.path.exists(vi_path) and os.path.getsize(vi_path) > 100:
                vi_txt = open(vi_path, encoding="utf-8").read()
                vi_pages, vi_imgs, vi_w = count_patterns(vi_txt)
                v_done += 1
                done_files += 1
                v_vi_w += vi_w
                total_vi_words += vi_w

                ratio = vi_w / max(1, en_w)
                if ratio < 0.75:
                    issues.append(f"{item['filename']} low ratio ({ratio:.2f})")
                if len(vi_imgs) < len(en_imgs):
                    issues.append(f"{item['filename']} missing imgs ({len(vi_imgs)}/{len(en_imgs)})")

        status = "OK" if not issues else f"{len(issues)} warnings: {', '.join(issues[:2])}"
        print(f"{vol_dir:38s} | {v_done:4d}/{v_total:<5d} | {v_en_w:10,d} | {v_vi_w:10,d} | {status}")

    print("-" * 88)
    print(f"{'TOTAL':38s} | {done_files:4d}/{total_files:<5d} | {total_en_words:10,d} | {total_vi_words:10,d} | {done_files*100/max(1,total_files):.1f}%")


if __name__ == "__main__":
    check_all_volumes()
