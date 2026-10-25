import os
import re
import glob
import json
import html
import markdown

ROOT_DIR = "/Users/kaka/learning/finance"
EN_ROOT = os.path.join(ROOT_DIR, "en_markdown")
VI_ROOT = os.path.join(ROOT_DIR, "vi_markdown")
OUT_ROOT = os.path.join(ROOT_DIR, "cfa_html")

VOLUME_META = [
    ("01_Quantitative_Methods", "Volume 1", "Quantitative Methods", "Các Phương Pháp Định Lượng", "indigo"),
    ("02_Economics", "Volume 2", "Economics", "Kinh Tế Học", "blue"),
    ("03_Corporate_Issuers", "Volume 3", "Corporate Issuers", "Tổ Chức Phát Hành Doanh Nghiệp", "sky"),
    ("04_Financial_Statement_Analysis", "Volume 4", "Financial Statement Analysis", "Phân Tích Báo Cáo Tài Chính", "emerald"),
    ("05_Equity_Investments", "Volume 5", "Equity Investments", "Đầu Tư Vốn Cổ Phần", "teal"),
    ("06_Fixed_Income", "Volume 6", "Fixed Income", "Thu Nhập Cố Định", "amber"),
    ("07_Derivatives", "Volume 7", "Derivatives", "Công Cụ Phái Sinh", "orange"),
    ("08_Alternative_Investments", "Volume 8", "Alternative Investments", "Đầu Tư Thay Thế", "rose"),
    ("09_Portfolio_Management", "Volume 9", "Portfolio Management", "Quản Lý Danh Mục Đầu Tư", "purple"),
    ("10_Ethical_and_Professional_Standards", "Volume 10", "Ethical & Professional Standards", "Chuẩn Mực Đạo Đức & Nghề Nghiệp", "slate"),
]

# Reuse a single Markdown instance for speed
MD_CONVERTER = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])

IMG_RE = re.compile(r"!\[[^\]]*\]\((assets/[^)]+)\)")
DISPLAY_MATH_RE = re.compile(r"\$\$(.*?)\$\$", re.S)
INLINE_MATH_RE = re.compile(r"(?<!\\)\$([^\$\n]+?)(?<!\\)\$")


def render_md_with_math(md_text: str) -> str:
    """Convert Markdown to HTML while protecting LaTeX $$...$$ and $...$ from Markdown's parser."""
    if not md_text or not md_text.strip():
        return ""

    math_store = []

    def _save_display(m):
        idx = len(math_store)
        math_store.append(("display", m.group(0)))
        return f"@@CFAMATHBLOCK{idx}@@"

    def _save_inline(m):
        idx = len(math_store)
        math_store.append(("inline", m.group(0)))
        return f"@@CFAMATHINLINE{idx}@@"

    protected = DISPLAY_MATH_RE.sub(_save_display, md_text)
    protected = INLINE_MATH_RE.sub(_save_inline, protected)
    # Prevent algebraic [expr1](expr2) in English text from being parsed as Markdown hyperlinks
    def _escape_math_brackets(m):
        label, url = m.group(1), m.group(2).strip()
        if url.startswith(("http://", "https://", "mailto:", "#", "assets/")) or url.endswith((".md", ".html", ".png", ".jpg", ".pdf")):
            return m.group(0)
        return f"\\[{label}\\]({m.group(2)})"
    protected = re.sub(r"(?<!!)\[([^\]\n]+)\]\(([^)\n]+)\)", _escape_math_brackets, protected)

    MD_CONVERTER.reset()
    rendered = MD_CONVERTER.convert(protected)

    for idx, (mtype, raw_math) in enumerate(math_store):
        escaped_math = html.escape(raw_math)
        if mtype == "display":
            token = f"@@CFAMATHBLOCK{idx}@@"
            rendered = rendered.replace(
                f"<p>{token}</p>",
                f'<div class="math-display my-3 overflow-x-auto">{escaped_math}</div>',
            )
            rendered = rendered.replace(
                token,
                f'<div class="math-display my-3 overflow-x-auto">{escaped_math}</div>',
            )
        else:
            token = f"@@CFAMATHINLINE{idx}@@"
            rendered = rendered.replace(token, f'<span class="math-inline">{escaped_math}</span>')

    # Add responsive wrapper around tables
    rendered = rendered.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    # Enhance images with lazy loading and lightbox trigger
    rendered = re.sub(
        r'<img alt="([^"]*)" src="([^"]+)"\s*/?>',
        r'<img alt="\1" src="\2" loading="lazy" onclick="openLightbox(this.src)" class="cfa-img" />',
        rendered,
    )
    return rendered


def extract_raw_blocks(page_md: str, is_vi: bool) -> list[str]:
    """Clean HTML comments and split a page's Markdown into logical blocks."""
    cleaned = re.sub(
        r"<!--\s*Start of picture text\s*-->.*?<!--\s*End of picture text\s*-->",
        "",
        page_md,
        flags=re.S,
    )
    cleaned = re.sub(r"<!--.*?-->", "", cleaned, flags=re.S)
    raw = [b.strip() for b in re.split(r"\n\s*\n", cleaned) if b.strip()]

    # Merge consecutive list items if they got separated by blank lines
    merged_lists = []
    for b in raw:
        if (
            merged_lists
            and re.match(r"^(\s*[-*+]|\s*\d+\.)\s+", b)
            and re.match(r"^(\s*[-*+]|\s*\d+\.)\s+", merged_lists[-1])
        ):
            merged_lists[-1] = merged_lists[-1] + "\n\n" + b
        else:
            merged_lists.append(b)

    if not is_vi:
        return merged_lists

    # For VI, attach supplementary LaTeX ($$...$$) or image captions (> **Chú thích...) to the preceding image block
    final_blocks = []
    for b in merged_lists:
        if final_blocks and IMG_RE.search(final_blocks[-1]):
            if (
                b.startswith("$$")
                or b.startswith(">")
                or re.match(r"^[\*_]\((?:Giải thích|Lưu ý|Chú thích|Nguồn)", b)
                or re.match(r"^[\*_](?:Lưu ý|Nguồn)\b", b)
            ):
                final_blocks[-1] = final_blocks[-1] + "\n\n" + b
                continue
        final_blocks.append(b)
    return final_blocks


def block_kind(b: str) -> str:
    first = b.lstrip()
    m_img = IMG_RE.search(first)
    if m_img and first.startswith("!["):
        return f"IMG:{m_img.group(1)}"
    if first.startswith("#"):
        return "HEADING"
    if first.startswith("|") and "|---" in first:
        return "TABLE"
    if first == "---":
        return "HR"
    return "TEXT"


def align_segment_blocks(en_blocks: list[str], vi_blocks: list[str]) -> list[tuple[str, str]]:
    """Align blocks within a segment where there are no shared image anchors."""
    if not en_blocks and not vi_blocks:
        return []
    if not en_blocks:
        return [("", "\n\n".join(vi_blocks))]
    if not vi_blocks:
        return [("\n\n".join(en_blocks), "")]
    if len(en_blocks) == len(vi_blocks):
        return list(zip(en_blocks, vi_blocks))

    # Try anchoring on shared HEADING or TABLE positions if counts of headings/tables match
    en_anchors = [i for i, b in enumerate(en_blocks) if block_kind(b) in ("HEADING", "TABLE", "HR")]
    vi_anchors = [i for i, b in enumerate(vi_blocks) if block_kind(b) in ("HEADING", "TABLE", "HR")]

    if (
        en_anchors
        and len(en_anchors) == len(vi_anchors)
        and [block_kind(en_blocks[i]) for i in en_anchors] == [block_kind(vi_blocks[j]) for j in vi_anchors]
    ):
        pairs = []
        eprev, vprev = 0, 0
        for ea, va in zip(en_anchors, vi_anchors):
            pairs.extend(_pair_simple(en_blocks[eprev:ea], vi_blocks[vprev:va]))
            pairs.append((en_blocks[ea], vi_blocks[va]))
            eprev, vprev = ea + 1, va + 1
        pairs.extend(_pair_simple(en_blocks[eprev:], vi_blocks[vprev:]))
        return pairs

    return _pair_simple(en_blocks, vi_blocks)


def _pair_simple(en_list: list[str], vi_list: list[str]) -> list[tuple[str, str]]:
    if not en_list and not vi_list:
        return []
    if not en_list:
        return [("", "\n\n".join(vi_list))]
    if not vi_list:
        return [("\n\n".join(en_list), "")]
    if len(en_list) == len(vi_list):
        return list(zip(en_list, vi_list))

    # If VI has standalone $$...$$ blocks that were added for inline formulas in EN prose, merge them into the preceding VI block
    if len(vi_list) > len(en_list):
        collapsed_vi = []
        for b in vi_list:
            if collapsed_vi and (b.startswith("$$") or re.match(r"^trong đó\b|^where\b", b, re.I)):
                collapsed_vi[-1] = collapsed_vi[-1] + "\n\n" + b
            else:
                collapsed_vi.append(b)
        if len(collapsed_vi) == len(en_list):
            return list(zip(en_list, collapsed_vi))
        vi_list = collapsed_vi

    # Proportional grouping so every row stays aligned
    n_en, n_vi = len(en_list), len(vi_list)
    if n_en < n_vi:
        pairs = []
        for i in range(n_en):
            start_v = round(i * n_vi / n_en)
            end_v = round((i + 1) * n_vi / n_en)
            if i == n_en - 1:
                end_v = n_vi
            pairs.append((en_list[i], "\n\n".join(vi_list[start_v:end_v])))
        return pairs
    else:
        pairs = []
        for i in range(n_vi):
            start_e = round(i * n_en / n_vi)
            end_e = round((i + 1) * n_en / n_vi)
            if i == n_vi - 1:
                end_e = n_en
            pairs.append(("\n\n".join(en_list[start_e:end_e]), vi_list[i]))
        return pairs


def align_page_blocks(en_md: str, vi_md: str) -> list[tuple[str, str]]:
    """Align EN and VI blocks within a single PDF page using shared image filenames as exact anchors."""
    en_blocks = extract_raw_blocks(en_md, is_vi=False)
    vi_blocks = extract_raw_blocks(vi_md, is_vi=True)

    # Find image anchors in EN and VI
    en_img_map = {}
    for idx, b in enumerate(en_blocks):
        m = IMG_RE.search(b)
        if m and m.group(1) not in en_img_map:
            en_img_map[m.group(1)] = idx

    vi_img_map = {}
    for idx, b in enumerate(vi_blocks):
        m = IMG_RE.search(b)
        if m and m.group(1) not in vi_img_map:
            vi_img_map[m.group(1)] = idx

    shared_imgs = [
        img for img in en_img_map.keys() if img in vi_img_map
    ]
    # Ensure monotonic indices
    anchors = []
    last_e, last_v = -1, -1
    for img in shared_imgs:
        ei, vi = en_img_map[img], vi_img_map[img]
        if ei > last_e and vi > last_v:
            anchors.append((ei, vi))
            last_e, last_v = ei, vi

    pairs = []
    eprev, vprev = 0, 0
    for ei, vi in anchors:
        pairs.extend(align_segment_blocks(en_blocks[eprev:ei], vi_blocks[vprev:vi]))
        pairs.append((en_blocks[ei], vi_blocks[vi]))
        eprev, vprev = ei + 1, vi + 1

    pairs.extend(align_segment_blocks(en_blocks[eprev:], vi_blocks[vprev:]))
    return pairs


def parse_pages(md_text: str) -> list[tuple[str, str]]:
    """Split markdown file into (page_label, page_content) tuples."""
    tokens = re.split(r"(<!-- PDF Page \d+ -->)", md_text)
    pages = []
    cur_label = "Header"
    buf = []
    for tok in tokens:
        m = re.match(r"<!-- PDF Page (\d+) -->", tok)
        if m:
            content = "".join(buf).strip()
            if content:
                pages.append((cur_label, content))
            cur_label = m.group(1)
            buf = []
        else:
            buf.append(tok)
    content = "".join(buf).strip()
    if content:
        pages.append((cur_label, content))
    return pages


def build_bilingual_rows_html(en_md: str, vi_md: str) -> tuple[str, list[str]]:
    """Build side-by-side HTML rows (EN left | VI right) synchronized by PDF Page and logical blocks."""
    en_pages = dict(parse_pages(en_md))
    vi_pages_list = parse_pages(vi_md)
    vi_pages = dict(vi_pages_list)

    all_labels = [lbl for lbl, _ in vi_pages_list]
    for lbl in en_pages.keys():
        if lbl not in all_labels:
            all_labels.append(lbl)

    html_chunks = []
    pdf_page_nums = []

    for lbl in all_labels:
        en_page_md = en_pages.get(lbl, "")
        vi_page_md = vi_pages.get(lbl, "")

        if lbl != "Header":
            pdf_page_nums.append(lbl)
            html_chunks.append(
                f'''
                <div id="pdf-page-{lbl}" class="pdf-page-divider my-6 flex items-center gap-4 scroll-mt-20">
                    <div class="h-px flex-1 bg-gradient-to-r from-transparent via-slate-300 dark:via-slate-700 to-slate-300 dark:to-slate-700"></div>
                    <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold tracking-wider uppercase bg-slate-200/80 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-300 dark:border-slate-700 shadow-2xs">
                        <svg class="w-3.5 h-3.5 text-indigo-600 dark:text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"></path></svg>
                        PDF Page {lbl} / Trang PDF {lbl}
                    </span>
                    <div class="h-px flex-1 bg-gradient-to-r from-slate-300 dark:via-slate-700 via-slate-300 to-transparent"></div>
                </div>
                '''
            )

        paired_blocks = align_page_blocks(en_page_md, vi_page_md)
        for en_blk, vi_blk in paired_blocks:
            en_html = render_md_with_math(en_blk)
            vi_html = render_md_with_math(vi_blk)
            is_heading = en_blk.lstrip().startswith("#") or vi_blk.lstrip().startswith("#")
            row_extra_cls = (
                "bg-slate-50/70 dark:bg-slate-800/40 rounded-xl border border-slate-200/70 dark:border-slate-700/60 p-4 my-3"
                if is_heading
                else "py-2.5 border-b border-slate-100 dark:border-slate-800/70"
            )
            html_chunks.append(
                f'''
                <div class="bilingual-row grid grid-cols-1 lg:grid-cols-2 gap-4 lg:gap-8 items-start {row_extra_cls}">
                    <div class="col-en prose-cfa min-w-0 pr-0 lg:pr-4 lg:border-r border-slate-200/80 dark:border-slate-800">{en_html}</div>
                    <div class="col-vi prose-cfa min-w-0 pl-0 lg:pl-2">{vi_html}</div>
                </div>
                '''
            )

    return "\n".join(html_chunks), pdf_page_nums


SHARED_CSS = """
:root {
  --cfa-font-size: 16px;
}
html {
  scroll-behavior: smooth;
  font-size: var(--cfa-font-size);
}
.prose-cfa {
  line-height: 1.72;
  color: inherit;
  word-wrap: break-word;
}
.prose-cfa h1 {
  font-size: 1.55rem;
  font-weight: 800;
  margin-top: 0.25rem;
  margin-bottom: 0.5rem;
  line-height: 1.3;
  color: #1e293b;
}
.dark .prose-cfa h1 { color: #f8fafc; }
.prose-cfa h2 {
  font-size: 1.3rem;
  font-weight: 700;
  margin-top: 0.25rem;
  margin-bottom: 0.4rem;
  line-height: 1.35;
  color: #1e3a8a;
}
.dark .prose-cfa h2 { color: #93c5fd; }
.prose-cfa h3, .prose-cfa h4, .prose-cfa h5, .prose-cfa h6 {
  font-size: 1.08rem;
  font-weight: 700;
  margin-top: 0.2rem;
  margin-bottom: 0.35rem;
  color: #334155;
}
.dark .prose-cfa h3, .dark .prose-cfa h4, .dark .prose-cfa h5, .dark .prose-cfa h6 {
  color: #e2e8f0;
}
.prose-cfa p {
  margin-top: 0.35rem;
  margin-bottom: 0.55rem;
}
.prose-cfa ul, .prose-cfa ol {
  margin-top: 0.35rem;
  margin-bottom: 0.6rem;
  padding-left: 1.4rem;
}
.prose-cfa ul { list-style-type: disc; }
.prose-cfa ol { list-style-type: decimal; }
.prose-cfa li { margin-bottom: 0.25rem; }
.prose-cfa blockquote {
  border-left: 4px solid #6366f1;
  background: rgba(99, 102, 241, 0.06);
  padding: 0.65rem 1rem;
  border-radius: 0 0.5rem 0.5rem 0;
  margin: 0.6rem 0;
  font-size: 0.94rem;
}
.dark .prose-cfa blockquote {
  background: rgba(99, 102, 241, 0.14);
  border-left-color: #818cf8;
}
.prose-cfa mark {
  background: #fef08a;
  color: #854d0e;
  padding: 0.1rem 0.45rem;
  border-radius: 0.35rem;
  font-weight: 700;
}
.dark .prose-cfa mark {
  background: #854d0e;
  color: #fef9c3;
}
.prose-cfa code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 0.88em;
  background: rgba(148, 163, 184, 0.18);
  padding: 0.15rem 0.35rem;
  border-radius: 0.25rem;
}
.table-wrap {
  overflow-x: auto;
  margin: 0.65rem 0;
  border-radius: 0.5rem;
  border: 1px solid #e2e8f0;
}
.dark .table-wrap {
  border-color: #334155;
}
.prose-cfa table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
  line-height: 1.45;
}
.prose-cfa th {
  background: #f1f5f9;
  font-weight: 700;
  text-align: left;
  padding: 0.55rem 0.75rem;
  border-bottom: 2px solid #cbd5e1;
}
.dark .prose-cfa th {
  background: #1e293b;
  border-bottom-color: #475569;
}
.prose-cfa td {
  padding: 0.5rem 0.75rem;
  border-bottom: 1px solid #e2e8f0;
  vertical-align: top;
}
.dark .prose-cfa td {
  border-bottom-color: #334155;
}
.prose-cfa tr:nth-child(even) td {
  background: rgba(248, 250, 252, 0.6);
}
.dark .prose-cfa tr:nth-child(even) td {
  background: rgba(30, 41, 59, 0.4);
}
.cfa-img {
  max-width: 100%;
  height: auto;
  border-radius: 0.5rem;
  margin: 0.5rem 0;
  cursor: zoom-in;
  border: 1px solid #e2e8f0;
  background: #ffffff;
  padding: 0.25rem;
  transition: transform 0.15s ease;
}
.cfa-img:hover {
  border-color: #6366f1;
}
/* View Mode Switching (Default: Side-by-Side EN Left | VI Right) */
body.mode-vi-only .bilingual-row {
  grid-template-columns: 1fr !important;
}
body.mode-vi-only .col-en {
  display: none !important;
}
body.mode-en-only .bilingual-row {
  grid-template-columns: 1fr !important;
}
body.mode-en-only .col-vi {
  display: none !important;
}
body.mode-en-only .col-en {
  border-right: none !important;
  padding-right: 0 !important;
}
body.hide-images .cfa-img {
  display: none !important;
}
"""

SHARED_JS = """
function setViewMode(mode) {
  document.body.classList.remove('mode-bilingual', 'mode-vi-only', 'mode-en-only');
  document.body.classList.add(mode);
  localStorage.setItem('cfa_view_mode', mode);
  document.querySelectorAll('[data-mode-btn]').forEach(btn => {
    if (btn.getAttribute('data-mode-btn') === mode) {
      btn.classList.add('bg-indigo-600', 'text-white', 'shadow-xs');
      btn.classList.remove('text-slate-600', 'dark:text-slate-300');
    } else {
      btn.classList.remove('bg-indigo-600', 'text-white', 'shadow-xs');
      btn.classList.add('text-slate-600', 'dark:text-slate-300');
    }
  });
  const banner = document.getElementById('column-header-banner');
  if (banner) {
    banner.style.display = (mode === 'mode-bilingual') ? 'grid' : 'none';
  }
}

function toggleDark() {
  const isDark = document.documentElement.classList.toggle('dark');
  localStorage.setItem('cfa_dark', isDark ? '1' : '0');
}

function changeFontSize(delta) {
  let cur = parseInt(localStorage.getItem('cfa_font_size') || '16', 10);
  cur = Math.min(22, Math.max(13, cur + delta));
  document.documentElement.style.setProperty('--cfa-font-size', cur + 'px');
  localStorage.setItem('cfa_font_size', cur);
}

function toggleSidebar() {
  const sb = document.getElementById('cfa-sidebar');
  const ov = document.getElementById('cfa-sidebar-overlay');
  if (sb && ov) {
    sb.classList.toggle('-translate-x-full');
    ov.classList.toggle('hidden');
  }
}

function jumpToPdfPage(pageNum) {
  if (!pageNum) return;
  const el = document.getElementById('pdf-page-' + pageNum);
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function openLightbox(src) {
  const modal = document.getElementById('lightbox-modal');
  const img = document.getElementById('lightbox-img');
  if (modal && img) {
    img.src = src;
    modal.classList.remove('hidden');
    modal.classList.add('flex');
  }
}

function closeLightbox() {
  const modal = document.getElementById('lightbox-modal');
  if (modal) {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
  }
}

function toggleCompleted(pageKey) {
  let done = JSON.parse(localStorage.getItem('cfa_completed_items') || '{}');
  done[pageKey] = !done[pageKey];
  localStorage.setItem('cfa_completed_items', JSON.stringify(done));
  updateCompletedUI(pageKey);
}

function updateCompletedUI(pageKey) {
  let done = JSON.parse(localStorage.getItem('cfa_completed_items') || '{}');
  const btn = document.getElementById('btn-complete');
  if (btn) {
    if (done[pageKey]) {
      btn.innerHTML = '✓ Đã hoàn thành (Completed)';
      btn.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold bg-emerald-600 text-white shadow-xs transition';
    } else {
      btn.innerHTML = '○ Đánh dấu hoàn thành';
      btn.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-emerald-500 hover:text-white transition';
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  if (localStorage.getItem('cfa_dark') === '1') {
    document.documentElement.classList.add('dark');
  }
  const savedSize = localStorage.getItem('cfa_font_size');
  if (savedSize) {
    document.documentElement.style.setProperty('--cfa-font-size', savedSize + 'px');
  }
  const savedMode = localStorage.getItem('cfa_view_mode') || 'mode-bilingual';
  setViewMode(savedMode);

  if (window.renderMathInElement) {
    renderMathInElement(document.body, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false}
      ],
      throwOnError: false
    });
  }
});
"""


def build_page_html(
    vol_dir_name: str,
    vol_num_label: str,
    vol_title_en: str,
    vol_title_vi: str,
    page_title: str,
    page_key: str,
    rows_html: str,
    pdf_pages: list[str],
    sidebar_items: list[dict],
    current_filename: str,
    prev_link: tuple[str, str] | None,
    next_link: tuple[str, str] | None,
    full_chapter_link: str | None,
) -> str:
    page_options = "\n".join(
        f'<option value="{p}">PDF Page {p}</option>' for p in pdf_pages
    )
    sidebar_links_html = []
    for item in sidebar_items:
        active = item["html_file"] == current_filename
        cls = (
            "block px-3 py-2 rounded-lg text-xs font-semibold bg-indigo-600 text-white shadow-2xs"
            if active
            else "block px-3 py-1.5 rounded-lg text-xs text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800"
        )
        badge = (
            '<span class="inline-block px-1.5 py-0.5 mr-1 rounded bg-indigo-100 dark:bg-indigo-900/60 text-indigo-700 dark:text-indigo-300 font-bold text-[10px]">FULL</span>'
            if item.get("is_full")
            else ""
        )
        sidebar_links_html.append(
            f'<a href="{item["html_file"]}" class="{cls}">{badge}{html.escape(item["label"])}</a>'
        )
    sidebar_nav = "\n".join(sidebar_links_html)

    prev_btn = (
        f'<a href="{prev_link[0]}" class="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-sm font-medium hover:border-indigo-500 transition shadow-2xs">← {html.escape(prev_link[1])}</a>'
        if prev_link
        else '<span></span>'
    )
    next_btn = (
        f'<a href="{next_link[0]}" class="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-indigo-600 text-white text-sm font-medium hover:bg-indigo-500 transition shadow-xs">{html.escape(next_link[1])} →</a>'
        if next_link
        else '<span></span>'
    )
    full_btn = (
        f'<a href="{full_chapter_link}" class="hidden sm:inline-flex items-center gap-1 px-2.5 py-1 rounded-lg text-xs font-medium bg-indigo-50 dark:bg-indigo-950/70 text-indigo-700 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-800 hover:bg-indigo-100 transition">Đọc Gộp Nguyên Chương (Full LM)</a>'
        if full_chapter_link and full_chapter_link != current_filename
        else ""
    )

    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(page_title)} — {vol_num_label}: {html.escape(vol_title_en)} | CFA 2026 Level I</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
    }}
  </script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" />
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
  <link rel="stylesheet" href="../assets_shared/styles.css" />
</head>
<body class="mode-bilingual bg-white dark:bg-slate-950 text-slate-800 dark:text-slate-200 min-h-screen flex flex-col">

  <!-- Top Navigation Header -->
  <header class="sticky top-0 z-40 bg-white/95 dark:bg-slate-900/95 backdrop-blur border-b border-slate-200 dark:border-slate-800 shadow-2xs">
    <div class="max-w-[1800px] mx-auto px-4 h-14 flex items-center justify-between gap-3">
      <div class="flex items-center gap-2.5 min-w-0">
        <button onclick="toggleSidebar()" class="p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-600 dark:text-slate-300" title="Mục lục chương">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
        </button>
        <a href="../index.html" class="hidden md:inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-xs font-bold text-indigo-600 dark:text-indigo-400 hover:bg-indigo-50 transition">
          CFA 2026
        </a>
        <span class="text-slate-400 hidden md:inline">/</span>
        <a href="index.html" class="text-xs font-semibold text-slate-600 dark:text-slate-300 hover:text-indigo-600 truncate">
          {vol_num_label}: {html.escape(vol_title_vi)}
        </a>
        <span class="text-slate-400">/</span>
        <span class="text-xs sm:text-sm font-bold text-slate-900 dark:text-white truncate">{html.escape(page_title)}</span>
      </div>

      <div class="flex items-center gap-2 shrink-0">
        {full_btn}
        <select onchange="jumpToPdfPage(this.value)" class="hidden sm:block text-xs rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 px-2.5 py-1.5 text-slate-700 dark:text-slate-200">
          <option value="">Trang PDF ({len(pdf_pages)} trang)...</option>
          {page_options}
        </select>

        <!-- View Mode Switcher (Default: Side-by-Side EN Left | VI Right) -->
        <div class="inline-flex items-center rounded-lg bg-slate-100 dark:bg-slate-800 p-0.5 border border-slate-200 dark:border-slate-700">
          <button data-mode-btn="mode-bilingual" onclick="setViewMode('mode-bilingual')" class="px-2.5 py-1 rounded-md text-xs font-semibold transition" title="Hiển thị 2 cột: Tiếng Anh bên trái | Tiếng Việt bên phải">
            🇬🇧 EN | 🇻🇳 VI
          </button>
          <button data-mode-btn="mode-vi-only" onclick="setViewMode('mode-vi-only')" class="px-2 py-1 rounded-md text-xs font-semibold transition" title="Chỉ hiển thị Tiếng Việt">
            🇻🇳 VI
          </button>
          <button data-mode-btn="mode-en-only" onclick="setViewMode('mode-en-only')" class="px-2 py-1 rounded-md text-xs font-semibold transition" title="Chỉ hiển thị Tiếng Anh">
            🇬🇧 EN
          </button>
        </div>

        <button onclick="changeFontSize(-1)" class="hidden sm:inline-flex px-2 py-1 rounded-lg text-xs font-bold bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700" title="Giảm cỡ chữ">A-</button>
        <button onclick="changeFontSize(1)" class="hidden sm:inline-flex px-2 py-1 rounded-lg text-xs font-bold bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700" title="Tăng cỡ chữ">A+</button>
        <button onclick="toggleDark()" class="p-1.5 rounded-lg bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-amber-300" title="Chế độ Sáng / Tối">
          🌓
        </button>
      </div>
    </div>

    <!-- Sticky Column Banner for Side-by-Side Mode -->
    <div id="column-header-banner" class="hidden lg:grid grid-cols-2 border-t border-slate-200/80 dark:border-slate-800 bg-slate-50/90 dark:bg-slate-900/90 text-[11px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">
      <div class="max-w-[900px] w-full ml-auto px-6 py-1.5 flex items-center justify-between border-r border-slate-200 dark:border-slate-800">
        <span>🇬🇧 NỬA BÊN TRÁI — ENGLISH ORIGINAL (CFA® CURRICULUM 2026)</span>
        <span class="text-[10px] font-normal text-slate-400">50% Left Column</span>
      </div>
      <div class="max-w-[900px] w-full mr-auto px-6 py-1.5 flex items-center justify-between">
        <span>🇻🇳 NỬA BÊN PHẢI — BẢN DỊCH TIẾNG VIỆT CHUYÊN SÂU</span>
        <span class="text-[10px] font-normal text-slate-400">50% Right Column</span>
      </div>
    </div>
  </header>

  <!-- Slide-over Sidebar Drawer -->
  <div id="cfa-sidebar-overlay" onclick="toggleSidebar()" class="fixed inset-0 bg-slate-900/50 backdrop-blur-xs z-40 hidden"></div>
  <aside id="cfa-sidebar" class="fixed top-0 left-0 bottom-0 w-84 bg-white dark:bg-slate-900 border-r border-slate-200 dark:border-slate-800 z-50 transform -translate-x-full transition-transform duration-200 flex flex-col shadow-2xl">
    <div class="p-4 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
      <div>
        <div class="text-xs font-bold text-indigo-600 dark:text-indigo-400 uppercase">{vol_num_label}</div>
        <div class="text-sm font-bold text-slate-900 dark:text-white">{html.escape(vol_title_vi)}</div>
      </div>
      <button onclick="toggleSidebar()" class="p-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800">✕</button>
    </div>
    <div class="p-3 border-b border-slate-200 dark:border-slate-800 flex gap-2">
      <a href="../index.html" class="flex-1 text-center py-1.5 rounded-lg text-xs font-semibold bg-slate-100 dark:bg-slate-800 hover:bg-indigo-50 text-slate-700 dark:text-slate-200">⌂ Tất cả 10 Volumes</a>
      <a href="index.html" class="flex-1 text-center py-1.5 rounded-lg text-xs font-semibold bg-indigo-50 dark:bg-indigo-950 text-indigo-700 dark:text-indigo-300">Mục lục {vol_num_label}</a>
    </div>
    <div class="flex-1 overflow-y-auto p-3 space-y-1">
      {sidebar_nav}
    </div>
  </aside>

  <!-- Main Bilingual Content Container -->
  <main class="flex-1 max-w-[1800px] w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
    <div class="mb-6 p-4 rounded-2xl bg-gradient-to-r from-slate-50 to-indigo-50/40 dark:from-slate-900 dark:to-indigo-950/30 border border-slate-200 dark:border-slate-800 flex flex-wrap items-center justify-between gap-4">
      <div>
        <div class="text-xs font-semibold text-indigo-600 dark:text-indigo-400 uppercase tracking-wide">
          {vol_num_label} • {html.escape(vol_title_en)} ({html.escape(vol_title_vi)})
        </div>
        <h1 class="text-lg sm:text-xl font-extrabold text-slate-900 dark:text-white mt-0.5">{html.escape(page_title)}</h1>
      </div>
      <div class="flex items-center gap-3">
        <button id="btn-complete" onclick="toggleCompleted('{page_key}')" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 transition">
          ○ Đánh dấu hoàn thành
        </button>
      </div>
    </div>

    <!-- Synchronized EN (Left) | VI (Right) Rows -->
    <div class="space-y-1">
      {rows_html}
    </div>

    <!-- Bottom Prev/Next Navigation -->
    <div class="mt-12 pt-6 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between gap-4">
      {prev_btn}
      <a href="index.html" class="text-xs font-semibold text-slate-500 hover:text-indigo-600">Quay lại Mục lục {vol_num_label}</a>
      {next_btn}
    </div>
  </main>

  <!-- Lightbox Modal for High-Res PNG Charts/Formulas -->
  <div id="lightbox-modal" onclick="closeLightbox()" class="fixed inset-0 z-50 bg-slate-950/85 backdrop-blur-xs hidden items-center justify-center p-4 cursor-zoom-out">
    <img id="lightbox-img" src="" alt="Zoomed view" class="max-w-[95vw] max-h-[92vh] bg-white p-2 rounded-xl shadow-2xl object-contain" />
  </div>

  <script src="../assets_shared/app.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      updateCompletedUI('{page_key}');
    }});
  </script>
</body>
</html>
"""


def main():
    os.makedirs(os.path.join(OUT_ROOT, "assets_shared"), exist_ok=True)
    with open(os.path.join(OUT_ROOT, "assets_shared", "styles.css"), "w", encoding="utf-8") as f:
        f.write(SHARED_CSS)
    with open(os.path.join(OUT_ROOT, "assets_shared", "app.js"), "w", encoding="utf-8") as f:
        f.write(SHARED_JS)

    master_volumes_summary = []
    total_part_pages_built = 0
    total_full_pages_built = 0

    for vol_dir, vol_num_label, vol_title_en, vol_title_vi, color in VOLUME_META:
        en_vol_path = os.path.join(EN_ROOT, vol_dir)
        vi_vol_path = os.path.join(VI_ROOT, vol_dir)
        out_vol_path = os.path.join(OUT_ROOT, vol_dir)
        os.makedirs(out_vol_path, exist_ok=True)

        # Ensure assets symlink points to en_markdown/<vol_dir>/assets
        assets_link = os.path.join(out_vol_path, "assets")
        target_assets = os.path.relpath(os.path.join(en_vol_path, "assets"), out_vol_path)
        if os.path.lexists(assets_link):
            os.remove(assets_link)
        os.symlink(target_assets, assets_link)

        manifest_path = os.path.join(en_vol_path, "manifest.json")
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        # Group parts by Learning Module
        modules_dict = {}
        items_list = manifest if isinstance(manifest, list) else manifest.get("modules", [])
        for mod in items_list:
            fname = mod.get("filename") or mod.get("file")
            mod["file"] = fname
            mod["title"] = f"{mod.get('module_title', '')} - Part {mod.get('part_index', 1)}: {mod.get('part_title', '')}"
            lm_code = mod.get("module_prefix") or fname.split("_")[0]
            modules_dict.setdefault(lm_code, []).append(mod)

        # Determine Full Chapter HTML filenames for each LM
        vi_full_files = sorted(glob.glob(os.path.join(vi_vol_path, "*_Full_*.md")))
        lm_to_full_html = {}
        for vf in vi_full_files:
            base = os.path.basename(vf)
            code = base.split("_Full_")[0]
            lm_to_full_html[code] = base[:-3] + ".html"

        # Build sidebar item list for this volume
        sidebar_items = []
        part_entries = []
        for lm_code, parts in modules_dict.items():
            full_html_name = lm_to_full_html.get(lm_code, f"{lm_code}_Full.html")
            lm_title = parts[0].get("module_title") or parts[0]["title"].split(" - Part ")[0]
            sidebar_items.append({
                "html_file": full_html_name,
                "label": f"{lm_title}",
                "is_full": True,
                "lm_code": lm_code,
            })
            for p in parts:
                p_html = p["file"][:-3] + ".html"
                sidebar_items.append({
                    "html_file": p_html,
                    "label": f"  • Part {p.get('part_index', 1)}: {p.get('part_title', p['file'][:-3])}",
                    "is_full": False,
                    "lm_code": lm_code,
                })
                part_entries.append((lm_code, p, p_html, full_html_name))

        # 1. Build each Part HTML file AND collect rows for each Full LM HTML file
        lm_accumulated_rows = {lm_code: [] for lm_code in modules_dict.keys()}
        lm_accumulated_pages = {lm_code: [] for lm_code in modules_dict.keys()}

        for idx, (lm_code, p_info, p_html, full_html_name) in enumerate(part_entries):
            md_fname = p_info["file"]
            en_md_path = os.path.join(en_vol_path, md_fname)
            vi_md_path = os.path.join(vi_vol_path, md_fname)
            with open(en_md_path, "r", encoding="utf-8") as f:
                en_md = f.read()
            with open(vi_md_path, "r", encoding="utf-8") as f:
                vi_md = f.read()

            rows_html, pdf_pages = build_bilingual_rows_html(en_md, vi_md)
            lm_accumulated_rows[lm_code].append(rows_html)
            for pg in pdf_pages:
                if pg not in lm_accumulated_pages[lm_code]:
                    lm_accumulated_pages[lm_code].append(pg)

            prev_link = (
                (part_entries[idx - 1][2], part_entries[idx - 1][1]["file"][:-3])
                if idx > 0
                else None
            )
            next_link = (
                (part_entries[idx + 1][2], part_entries[idx + 1][1]["file"][:-3])
                if idx + 1 < len(part_entries)
                else None
            )

            page_html = build_page_html(
                vol_dir_name=vol_dir,
                vol_num_label=vol_num_label,
                vol_title_en=vol_title_en,
                vol_title_vi=vol_title_vi,
                page_title=p_info["title"],
                page_key=f"{vol_dir}/{p_html}",
                rows_html=rows_html,
                pdf_pages=pdf_pages,
                sidebar_items=sidebar_items,
                current_filename=p_html,
                prev_link=prev_link,
                next_link=next_link,
                full_chapter_link=full_html_name,
            )
            with open(os.path.join(out_vol_path, p_html), "w", encoding="utf-8") as f:
                f.write(page_html)
            total_part_pages_built += 1

        # 2. Build Full Chapter HTML files (95 Learning Modules across 10 Volumes)
        lm_codes_list = list(modules_dict.keys())
        vol_lm_cards = []
        for l_idx, lm_code in enumerate(lm_codes_list):
            parts = modules_dict[lm_code]
            full_html_name = lm_to_full_html.get(lm_code, f"{lm_code}_Full.html")
            lm_title = parts[0]["title"].split(" - Part ")[0]
            prev_full = (
                (lm_to_full_html.get(lm_codes_list[l_idx - 1], f"{lm_codes_list[l_idx - 1]}_Full.html"), lm_codes_list[l_idx - 1])
                if l_idx > 0
                else None
            )
            next_full = (
                (lm_to_full_html.get(lm_codes_list[l_idx + 1], f"{lm_codes_list[l_idx + 1]}_Full.html"), lm_codes_list[l_idx + 1])
                if l_idx + 1 < len(lm_codes_list)
                else None
            )

            full_page_html = build_page_html(
                vol_dir_name=vol_dir,
                vol_num_label=vol_num_label,
                vol_title_en=vol_title_en,
                vol_title_vi=vol_title_vi,
                page_title=f"[Toàn Chương] {lm_code} — {lm_title}",
                page_key=f"{vol_dir}/{full_html_name}",
                rows_html="\n".join(lm_accumulated_rows[lm_code]),
                pdf_pages=lm_accumulated_pages[lm_code],
                sidebar_items=sidebar_items,
                current_filename=full_html_name,
                prev_link=prev_full,
                next_link=next_full,
                full_chapter_link=None,
            )
            with open(os.path.join(out_vol_path, full_html_name), "w", encoding="utf-8") as f:
                f.write(full_page_html)
            total_full_pages_built += 1

            vol_lm_cards.append({
                "lm_code": lm_code,
                "lm_title": lm_title,
                "full_html": full_html_name,
                "parts": [(p["file"][:-3] + ".html", p["title"], p["start_page"], p["end_page"]) for p in parts],
                "start_page": parts[0]["start_page"],
                "end_page": parts[-1]["end_page"],
            })

        # 3. Build Volume Index Page (cfa_html/<vol_dir>/index.html)
        cards_html = []
        for card in vol_lm_cards:
            part_pills = "\n".join(
                f'<a href="{ph}" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-100 dark:bg-slate-800 hover:bg-indigo-50 dark:hover:bg-indigo-950/60 text-slate-700 dark:text-slate-300 hover:text-indigo-600 border border-slate-200/80 dark:border-slate-700 transition">'
                f'<span>{html.escape(pt.split(" - ")[-1])}</span>'
                f'<span class="text-[10px] text-slate-400">(tr.{sp}–{ep})</span></a>'
                for ph, pt, sp, ep in card["parts"]
            )
            cards_html.append(f"""
            <div class="p-5 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-2xs hover:border-indigo-400 transition">
              <div class="flex flex-wrap items-start justify-between gap-4 mb-3">
                <div>
                  <span class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-indigo-100 dark:bg-indigo-950 text-indigo-700 dark:text-indigo-300 mb-1">
                    {card["lm_code"]} • Trang PDF {card["start_page"]}–{card["end_page"]}
                  </span>
                  <h2 class="text-base sm:text-lg font-bold text-slate-900 dark:text-white">{html.escape(card["lm_title"])}</h2>
                </div>
                <a href="{card["full_html"]}" class="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-bold bg-indigo-600 text-white hover:bg-indigo-500 shadow-xs transition">
                  📖 Đọc Toàn Chương Song Ngữ (EN | VI) →
                </a>
              </div>
              <div class="flex flex-wrap gap-2 mt-3 pt-3 border-t border-slate-100 dark:border-slate-800/80">
                {part_pills}
              </div>
            </div>
            """)

        vol_index_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{vol_num_label}: {html.escape(vol_title_en)} ({html.escape(vol_title_vi)}) — CFA 2026 Level I Song Ngữ</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>tailwind.config = {{ darkMode: 'class' }}</script>
  <link rel="stylesheet" href="../assets_shared/styles.css" />
</head>
<body class="bg-slate-50 dark:bg-slate-950 text-slate-800 dark:text-slate-200 min-h-screen">
  <header class="sticky top-0 z-30 bg-white/95 dark:bg-slate-900/95 backdrop-blur border-b border-slate-200 dark:border-slate-800">
    <div class="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <a href="../index.html" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-100 dark:bg-slate-800 text-xs font-bold text-indigo-600 dark:text-indigo-400 hover:bg-indigo-50">
          ← Trang chủ 10 Volumes
        </a>
        <span class="font-bold text-sm sm:text-base text-slate-900 dark:text-white">{vol_num_label}: {html.escape(vol_title_en)} — {html.escape(vol_title_vi)}</span>
      </div>
      <button onclick="toggleDark()" class="p-2 rounded-lg bg-slate-100 dark:bg-slate-800">🌓</button>
    </div>
  </header>
  <main class="max-w-6xl mx-auto px-4 py-8">
    <div class="mb-8 p-6 rounded-2xl bg-gradient-to-r from-indigo-600 to-blue-700 text-white shadow-lg">
      <div class="text-xs font-bold uppercase tracking-wider opacity-85">CFA® Program Curriculum 2026 • Level I • Song Ngữ Anh–Việt (Left EN | Right VI)</div>
      <h1 class="text-2xl sm:text-3xl font-extrabold mt-1">{vol_num_label}: {html.escape(vol_title_en)} ({html.escape(vol_title_vi)})</h1>
      <p class="text-sm opacity-90 mt-2">{len(vol_lm_cards)} Learning Modules • {len(part_entries)} Parts • Hiển thị song song Tiếng Anh bên trái & Tiếng Việt bên phải</p>
    </div>
    <div class="space-y-4">
      {"".join(cards_html)}
    </div>
  </main>
  <script src="../assets_shared/app.js"></script>
</body>
</html>
"""
        with open(os.path.join(out_vol_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(vol_index_html)

        master_volumes_summary.append({
            "vol_dir": vol_dir,
            "vol_num_label": vol_num_label,
            "vol_title_en": vol_title_en,
            "vol_title_vi": vol_title_vi,
            "lm_count": len(vol_lm_cards),
            "part_count": len(part_entries),
            "cards": vol_lm_cards,
        })
        print(f"Built {vol_dir}: {len(vol_lm_cards)} Full LMs + {len(part_entries)} Parts")

    # 4. Build Master Portal Index (cfa_html/index.html)
    vol_sections_html = []
    for v in master_volumes_summary:
        lm_links = "\n".join(
            f'<div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-700/70 flex flex-col justify-between gap-2 hover:border-indigo-400 transition">'
            f'<div>'
            f'<div class="flex items-center justify-between text-[11px] font-bold text-indigo-600 dark:text-indigo-400 mb-1">'
            f'<span>{c["lm_code"]}</span><span class="text-slate-400">Trang {c["start_page"]}–{c["end_page"]}</span>'
            f'</div>'
            f'<a href="{v["vol_dir"]}/{c["full_html"]}" class="text-xs sm:text-sm font-bold text-slate-900 dark:text-white hover:text-indigo-600 line-clamp-2">{html.escape(c["lm_title"])}</a>'
            f'</div>'
            f'<div class="flex items-center justify-between pt-2 border-t border-slate-200/60 dark:border-slate-700/60 mt-1">'
            f'<a href="{v["vol_dir"]}/{c["full_html"]}" class="text-[11px] font-bold text-indigo-600 dark:text-indigo-400 hover:underline">📖 Bản Gộp Toàn Chương →</a>'
            f'<span class="text-[11px] text-slate-500">{len(c["parts"])} phần</span>'
            f'</div>'
            f'</div>'
            for c in v["cards"]
        )
        vol_sections_html.append(f"""
        <section class="vol-section bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-6 shadow-2xs">
          <div class="flex flex-wrap items-center justify-between gap-4 pb-4 mb-4 border-b border-slate-200 dark:border-slate-800">
            <div>
              <span class="text-xs font-bold uppercase tracking-wider text-indigo-600 dark:text-indigo-400">{v["vol_num_label"]}</span>
              <h2 class="text-xl font-extrabold text-slate-900 dark:text-white">{html.escape(v["vol_title_en"])} — {html.escape(v["vol_title_vi"])}</h2>
            </div>
            <div class="flex items-center gap-3">
              <span class="text-xs font-semibold px-3 py-1 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                {v["lm_count"]} Chương • {v["part_count"]} Phần
              </span>
              <a href="{v["vol_dir"]}/index.html" class="px-4 py-2 rounded-xl text-xs font-bold bg-indigo-600 text-white hover:bg-indigo-500 transition">
                Mở {v["vol_num_label"]} →
              </a>
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
            {lm_links}
          </div>
        </section>
        """)

    master_index_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CFA® Program Curriculum 2026 Level I — Hệ Thống Học Tập Song Ngữ (English | Tiếng Việt)</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>tailwind.config = {{ darkMode: 'class' }}</script>
  <link rel="stylesheet" href="assets_shared/styles.css" />
</head>
<body class="bg-slate-50 dark:bg-slate-950 text-slate-800 dark:text-slate-200 min-h-screen">
  <header class="sticky top-0 z-30 bg-white/95 dark:bg-slate-900/95 backdrop-blur border-b border-slate-200 dark:border-slate-800 shadow-2xs">
    <div class="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-xl bg-indigo-600 text-white font-black flex items-center justify-center text-sm shadow-xs">CFA</div>
        <div>
          <div class="font-extrabold text-sm sm:text-base text-slate-900 dark:text-white">CFA® Program Curriculum 2026 • Level I</div>
          <div class="text-xs text-slate-500 dark:text-slate-400">Giao diện Song Ngữ 2 Cột: 🇬🇧 Nửa Trái Tiếng Anh | 🇻🇳 Nửa Phải Tiếng Việt</div>
        </div>
      </div>
      <div class="flex items-center gap-3">
        <input id="search-input" oninput="filterModules(this.value)" type="search" placeholder="Tìm nhanh chương / chủ đề..." class="w-48 sm:w-72 px-3.5 py-1.5 rounded-xl text-xs sm:text-sm border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 focus:outline-none focus:border-indigo-500" />
        <button onclick="toggleDark()" class="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-slate-200" title="Chế độ Sáng / Tối">🌓</button>
      </div>
    </div>
  </header>

  <main class="max-w-7xl mx-auto px-4 py-8 space-y-8">
    <!-- Hero Overview Banner -->
    <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-br from-indigo-700 via-indigo-600 to-blue-700 text-white shadow-xl">
      <div class="max-w-3xl">
        <span class="inline-block px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider bg-white/15 backdrop-blur-xs mb-3">
          100% Complete Unabridged Bilingual Edition • 2026 Level I
        </span>
        <h1 class="text-2xl sm:text-4xl font-black tracking-tight">
          Giáo Trình CFA® 2026 Level I Song Ngữ Anh – Việt
        </h1>
        <p class="mt-2.5 text-sm sm:text-base text-indigo-100 leading-relaxed">
          Toàn bộ <strong>10 Volumes (95 Chương / 279 Phần / 3.416 Trang PDF / 2.489 Hình minh họa)</strong> được trình bày song song: <strong>Nửa bên trái là Tiếng Anh nguyên bản</strong> và <strong>Nửa bên phải là Bản dịch Tiếng Việt chuyên sâu</strong>, căn gióng hàng ngang theo từng trang PDF, tiêu đề, đoạn văn, bảng biểu và công thức toán học KaTeX.
        </p>
      </div>
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-6 pt-6 border-t border-white/15">
        <div class="bg-white/10 rounded-2xl p-3.5">
          <div class="text-2xl font-black">10</div>
          <div class="text-xs text-indigo-100">Volumes (Chủ đề)</div>
        </div>
        <div class="bg-white/10 rounded-2xl p-3.5">
          <div class="text-2xl font-black">95 / 279</div>
          <div class="text-xs text-indigo-100">Chương Full / Phần</div>
        </div>
        <div class="bg-white/10 rounded-2xl p-3.5">
          <div class="text-2xl font-black">3.300</div>
          <div class="text-xs text-indigo-100">Trang Nội Dung Đồng Bộ</div>
        </div>
        <div class="bg-white/10 rounded-2xl p-3.5">
          <div class="text-2xl font-black">3,39M</div>
          <div class="text-xs text-indigo-100">Tổng Số Từ (EN + VI)</div>
        </div>
      </div>
    </div>

    <!-- All 10 Volumes -->
    <div id="volumes-container" class="space-y-6">
      {"".join(vol_sections_html)}
    </div>
  </main>

  <script src="assets_shared/app.js"></script>
  <script>
    function filterModules(q) {{
      q = (q || '').toLowerCase().trim();
      document.querySelectorAll('.vol-section').forEach(sec => {{
        if (!q) {{
          sec.style.display = '';
          return;
        }}
        const txt = sec.innerText.toLowerCase();
        sec.style.display = txt.includes(q) ? '' : 'none';
      }});
    }}
  </script>
</body>
</html>
"""
    with open(os.path.join(OUT_ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(master_index_html)

    print(
        f"COMPLETED! Built {total_part_pages_built} Part HTML files + {total_full_pages_built} Full Chapter HTML files + 10 Volume Indexes + 1 Master Index in {OUT_ROOT}"
    )


if __name__ == "__main__":
    main()
