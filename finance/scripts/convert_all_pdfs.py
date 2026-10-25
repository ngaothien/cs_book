#!/usr/bin/env python3
"""
Lossless PDF-to-Markdown Converter for CFA Program Curriculum (Volumes 1-10).
Splits each Volume by Learning Module (and into logical L3 parts if > 16 pages),
extracts 200 DPI PNG images for all figures/charts/formulas into `assets/`,
and preserves 100% of text, tables, formulas, examples, and practice problems.
"""

import os
import re
import sys
import time
import json
import pymupdf
import pymupdf4llm
from pymupdf4llm.helpers.document_layout import (
    parse_document,
    create_list_item_levels,
    picture_text_to_md,
    title_to_md,
    section_hdr_to_md,
    list_item_to_md,
    footnote_to_md,
    text_to_md,
)

VOLUMES = [
    ("01_Quantitative_Methods", "Quantitative method.pdf", "Volume 1: Quantitative Methods"),
    ("02_Economics", "Economics.pdf", "Volume 2: Economics"),
    ("03_Corporate_Issuers", "Coporate Issuers.pdf", "Volume 3: Corporate Issuers"),
    ("04_Financial_Statement_Analysis", "Financial Statement Analysis.pdf", "Volume 4: Financial Statement Analysis"),
    ("05_Equity_Investments", "Equity Investments.pdf", "Volume 5: Equity Investments"),
    ("06_Fixed_Income", "Fixed Income.pdf", "Volume 6: Fixed Income"),
    ("07_Derivatives", "Derivatives.pdf", "Volume 7: Derivatives"),
    ("08_Alternative_Investments", "Alternative Investments.pdf", "Volume 8: Alternative Investments"),
    ("09_Portfolio_Management", "Portfolio Management.pdf", "Volume 9: Portfolio Management"),
    ("10_Ethical_and_Professional_Standards", "Ethical and Professional Standard.pdf", "Volume 10: Ethical and Professional Standards"),
]

MAX_PAGES_PER_PART = 16

UNICODE_SPACE_MAP = str.maketrans({
    "\u200b": "",   # zero-width space
    "\u202f": " ",  # narrow no-break space
    "\u2005": " ",  # four-per-em space
    "\u2007": " ",  # figure space
    "\u2009": " ",  # thin space
    "\u200a": " ",  # hair space
    "\u00a0": " ",  # non-breaking space
})


def clean_unicode_spaces(text: str) -> str:
    return text.translate(UNICODE_SPACE_MAP)


def slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "_", text).strip("_")
    return text[:45].strip("_")


def get_module_chunks(doc, max_pages=MAX_PAGES_PER_PART):
    toc = doc.get_toc()
    l2 = [(i, t.replace("\t", " ").strip(), p) for i, (l, t, p) in enumerate(toc) if l == 2 and p > 1]
    chunks_info = []
    lm_num = 0

    for idx, (toc_i, title, start_p) in enumerate(l2):
        if "Learning Ecosystem" in title:
            continue
        end_p = l2[idx + 1][2] - 1 if idx + 1 < len(l2) else len(doc)
        pages = end_p - start_p + 1

        if title.startswith("Learning Module"):
            lm_num += 1
            m = re.match(r"Learning Module\s+(\d+)\s*(.*)", title)
            prefix = f"LM{int(m.group(1)):02d}"
            clean_title = m.group(2).strip()
        elif "Glossary" in title:
            prefix = "Glossary"
            clean_title = "Glossary"
        else:
            lm_num += 1
            prefix = f"LM{lm_num:02d}"
            clean_title = title

        next_toc_i = l2[idx + 1][0] if idx + 1 < len(l2) else len(toc)
        l3 = [
            (t.replace("\t", " ").strip(), p)
            for l, t, p in toc[toc_i + 1 : next_toc_i]
            if l == 3 and start_p <= p <= end_p
        ]

        if pages <= max_pages or len(l3) <= 1:
            fname = f"{prefix}_{slugify(clean_title)}.md"
            chunks_info.append({
                "module_prefix": prefix,
                "module_title": title,
                "part_index": 1,
                "total_parts": 1,
                "part_title": clean_title,
                "filename": fname,
                "start_page": start_p,
                "end_page": end_p,
            })
        else:
            sub_chunks = []
            cur_start = start_p
            cur_title = l3[0][0] if l3 else clean_title
            for s_idx in range(len(l3)):
                s_title, s_p = l3[s_idx]
                next_s_p = l3[s_idx + 1][1] - 1 if s_idx + 1 < len(l3) else end_p
                if (next_s_p - cur_start + 1) > max_pages and s_p > cur_start:
                    sub_chunks.append((cur_title, cur_start, s_p - 1))
                    cur_start = s_p
                    cur_title = s_title
            sub_chunks.append((cur_title, cur_start, end_p))

            if len(sub_chunks) == 1:
                fname = f"{prefix}_{slugify(clean_title)}.md"
                chunks_info.append({
                    "module_prefix": prefix,
                    "module_title": title,
                    "part_index": 1,
                    "total_parts": 1,
                    "part_title": clean_title,
                    "filename": fname,
                    "start_page": start_p,
                    "end_page": end_p,
                })
            else:
                for p_idx, (c_title, c_s, c_e) in enumerate(sub_chunks, 1):
                    fname = f"{prefix}_Part{p_idx}_{slugify(c_title)}.md"
                    chunks_info.append({
                        "module_prefix": prefix,
                        "module_title": title,
                        "part_index": p_idx,
                        "total_parts": len(sub_chunks),
                        "part_title": c_title,
                        "filename": fname,
                        "start_page": c_s,
                        "end_page": c_e,
                    })
    return chunks_info


def render_parsed_pages_to_md(doc, parsed_doc) -> str:
    md_out = []
    for page in parsed_doc.pages:
        pno = page.page_number
        pdf_page = doc[pno - 1]
        md_page = f"\n<!-- PDF Page {pno} -->\n\n"
        list_item_levels = create_list_item_levels(page.boxes)

        for i, box in enumerate(page.boxes):
            clip = pymupdf.IRect(box.x0, box.y0, box.x1, box.y1)
            btype = box.boxclass

            if btype in ("page-header", "page-footer"):
                continue

            if btype in ("picture", "formula"):
                if isinstance(box.image, str) and box.image:
                    rel_img = "assets/" + os.path.basename(box.image)
                    md_page += f"![]({rel_img})\n\n"
                raw_txt = clean_unicode_spaces(pdf_page.get_text("text", clip=clip).strip())
                if btype == "formula" and raw_txt:
                    compact_txt = " ".join(line.strip() for line in raw_txt.splitlines() if line.strip())
                    md_page += f"<!-- Formula Text: {compact_txt} -->\n\n"
                elif btype == "picture" and box.textlines:
                    md_page += picture_text_to_md(
                        box.textlines,
                        ignore_code=page.full_ocred,
                        clip=clip,
                    )
                continue

            if btype == "table":
                if box.table.get("html"):
                    md_page += box.table["html"] + "\n\n"
                else:
                    table_text = box.table.get("markdown", "")
                    if page.full_ocred:
                        table_text = table_text.replace("`", "")
                    md_page += table_text + "\n\n"
                continue

            if not hasattr(box, "textlines"):
                continue

            if btype == "title":
                md_page += title_to_md(box.header_level, box.textlines)
            elif btype == "section-header":
                md_page += section_hdr_to_md(box.header_level, box.textlines)
            elif btype == "list-item":
                md_page += list_item_to_md(box.textlines, list_item_levels[i])
            elif btype == "footnote":
                md_page += footnote_to_md(box.textlines)
            else:
                md_page += text_to_md(box.textlines, ignore_code=page.full_ocred)

        md_out.append(clean_unicode_spaces(md_page))

    return "".join(md_out)


def convert_volume(vol_idx: int, base_dir: str = "/Users/kaka/learning/finance"):
    vol_dir, pdf_name, vol_label = VOLUMES[vol_idx]
    pdf_path = os.path.join(base_dir, pdf_name)
    en_vol_dir = os.path.join(base_dir, "en_markdown", vol_dir)
    vi_vol_dir = os.path.join(base_dir, "vi_markdown", vol_dir)
    assets_dir = os.path.join(en_vol_dir, "assets")

    os.makedirs(assets_dir, exist_ok=True)
    os.makedirs(vi_vol_dir, exist_ok=True)

    vi_assets_link = os.path.join(vi_vol_dir, "assets")
    if not os.path.exists(vi_assets_link):
        os.symlink(os.path.relpath(assets_dir, vi_vol_dir), vi_assets_link)

    doc = pymupdf.open(pdf_path)
    chunks = get_module_chunks(doc)
    print(f"=== Converting {vol_label} ({len(doc)} pages -> {len(chunks)} markdown files) ===")

    manifest = []
    t_vol = time.time()
    for c_idx, ch in enumerate(chunks, 1):
        t0 = time.time()
        p_range = list(range(ch["start_page"] - 1, ch["end_page"]))
        img_prefix = f"{ch['module_prefix']}_p{ch['part_index']}"
        parsed = parse_document(
            doc,
            filename=img_prefix,
            image_dpi=200,
            image_format="png",
            image_path=assets_dir,
            pages=p_range,
            write_images=True,
            force_text=True,
            use_ocr=False,
        )
        header_md = (
            f"# {vol_label}\n"
            f"## {ch['module_title']}\n"
            f"### Part {ch['part_index']}/{ch['total_parts']}: {ch['part_title']} "
            f"(PDF Pages {ch['start_page']}–{ch['end_page']})\n\n---\n"
        )
        body_md = render_parsed_pages_to_md(doc, parsed)
        full_md = header_md + body_md

        out_path = os.path.join(en_vol_dir, ch["filename"])
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(full_md)

        ch["en_path"] = out_path
        ch["vi_path"] = os.path.join(vi_vol_dir, ch["filename"])
        ch["char_count"] = len(full_md)
        ch["word_count"] = len(full_md.split())
        manifest.append(ch)
        print(
            f"  [{c_idx:02d}/{len(chunks):02d}] {ch['filename']} "
            f"(p.{ch['start_page']}-{ch['end_page']}, {ch['word_count']} words) in {time.time()-t0:.1f}s"
        )

    manifest_path = os.path.join(en_vol_dir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"Finished {vol_label} in {time.time()-t_vol:.1f}s. Manifest saved to {manifest_path}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        indices = [int(x) for x in sys.argv[1:]]
    else:
        indices = list(range(len(VOLUMES)))
    for i in indices:
        convert_volume(i)
