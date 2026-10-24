#!/usr/bin/env python3
# C7页码driver（队4·B席·1024）——标准打印线变体：display_header_footer页脚页码+C5已随CSS注入
# 依据=标准库/装配线_工具与形态锚/打印线_实切包HTML转PDF.py（INVERT反色逻辑沿用）·变体仅增页脚
import sys
from playwright.sync_api import sync_playwright

SRC, OUT = sys.argv[1], sys.argv[2]

INVERT_JS = open("标准库/装配线_工具与形态锚/打印线_实切包HTML转PDF.py").read().split('INVERT_JS = """')[1].split('"""')[0]
# 源py字符串字面量反转义：\\( → \(（正则转义还原）
INVERT_JS = INVERT_JS.encode().decode("unicode_escape")
# 标准PRINT_CSS整体沿用+C5机制增强（表格/卡块/引用防跨页断裂·S10 C5）
PRINT_CSS = open("标准库/装配线_工具与形态锚/打印线_实切包HTML转PDF.py").read().split('PRINT_CSS = """')[1].split('"""')[0].encode().decode("unicode_escape")
PRINT_CSS += "\ntable,blockquote,.secdiv,.mind,.selftest,.chapmap{page-break-inside:avoid;}\ntr,li{page-break-inside:avoid;}\n"

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto(f"file://{os.path.abspath(SRC)}" if (os := __import__("os")) else SRC, wait_until="networkidle")
    pg.evaluate(INVERT_JS)
    pg.add_style_tag(content=PRINT_CSS)
    pg.emulate_media(media="print")
    pg.pdf(path=OUT, format="A4", print_background=True,
           display_header_footer=True,
           header_template="<span></span>",
           footer_template=("<div style=\"width:100%;font-size:8px;color:#333;text-align:center;\">"
                            "物理必修一 · 第一章 运动的描述　<span class=\"pageNumber\"></span> / <span class=\"totalPages\"></span></div>"),
           margin={"top": "12mm", "bottom": "14mm", "left": "13mm", "right": "11mm"})
    b.close()

try:
    from pypdf import PdfReader
except ImportError:
    from PyPDF2 import PdfReader
print("PDF_OK", OUT, f"{len(PdfReader(OUT).pages)}页")
