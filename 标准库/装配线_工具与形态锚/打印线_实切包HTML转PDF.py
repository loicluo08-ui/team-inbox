#!/usr/bin/env python3
# 实切包HTML→打印PDF 标准转换线（10/23逸翔定版"以舒适为主"）
# 用法: python3 打印线_实切包HTML转PDF.py <输入.html> <输出.pdf>
#
# ══ 标准版式（舒适版·10/23定）══
#   正文11pt/1.65行距｜h2 14pt｜h3 12pt｜表格9.5pt｜边距12-13mm（可装订）
# ══ 暗色HTML转打印·七查检查单（发前必过，18:45 h1隐形实锤教训）══
#   1.全元素色值扫描：grep源CSS全部color声明，浅色字（#fff/#e8e6e3/#b8c2ce等）逐一确认打印CSS覆盖
#   2.h1标题在场：目检第1页必须见章节大标题（白字白纸隐形=上轮漏检实锤）
#   3.SVG反色：DOM级fill/stroke/background色值映射（CSS filter打印管线不可靠），目检导图白底深字
#   4.全页深色占比机检：<1%为净（pdftoppm转图+PIL统计）
#   5.表格断行：tr/td page-break-inside:avoid，抽查页界
#   6.荧光mark：浅底加粗可读
#   7.页数汇报：输出页数给逸翔（省纸让位于舒适，10/18不偏离原目的）
import sys, re
from playwright.sync_api import sync_playwright

SRC, OUT = sys.argv[1], sys.argv[2]

INVERT_JS = """
() => {
  function invColor(c){
    c=c.trim();
    let m;
    const calc=(r,g,b)=>{
      const gr=Math.round(0.299*(255-r)+0.587*(255-g)+0.114*(255-b));
      const v=Math.max(0,Math.min(255,Math.round(gr*0.82+18)));
      return `rgb(${v},${v},${v})`;
    };
    if(m=c.match(/^#([0-9a-f]{6})$/i)) return calc(parseInt(m[1].slice(0,2),16),parseInt(m[1].slice(2,4),16),parseInt(m[1].slice(4,6),16));
    if(m=c.match(/^#([0-9a-f]{3})$/i)){
      const e=m[1].split('').map(x=>x+x).join('');
      return calc(parseInt(e.slice(0,2),16),parseInt(e.slice(2,4),16),parseInt(e.slice(4,6),16));
    }
    if(m=c.match(/^rgba?\\((\\d+)[, ]+(\\d+)[, ]+(\\d+)/)) return calc(+m[1],+m[2],+m[3]);
    return null;
  }
  document.querySelectorAll('svg').forEach(svg=>{
    svg.style.background='#fff';
    svg.style.border='0.6pt solid #aaa';
    svg.querySelectorAll('*').forEach(el=>{
      ['fill','stroke'].forEach(attr=>{
        const v=el.getAttribute(attr);
        if(v){const n=invColor(v); if(n) el.setAttribute(attr,n);}
      });
      const st=el.getAttribute('style');
      if(st){
        el.setAttribute('style', st.replace(/(fill|stroke|background)\\s*:\\s*([^;]+)/g,(w,prop,val)=>{
          const n=invColor(val); return n?`${prop}:${n}`:w;
        }));
      }
    });
  });
}
"""

PRINT_CSS = """
body{max-width:100% !important;margin:0 !important;padding:0 !important;
     background:#fff !important;color:#000 !important;
     font:11pt/1.65 'Noto Serif SC',Georgia,serif !important;}
h1{color:#000 !important;font-size:18pt !important;margin:2px 0 8px !important;border-bottom:1.5pt solid #333 !important;padding-bottom:5px !important;text-align:center;}
h2{color:#000 !important;font-size:14pt !important;margin:14px 0 6px !important;
   border-bottom:.6pt solid #888 !important;padding-bottom:3px !important;page-break-after:avoid;break-after:avoid;}
h3{color:#1a1a1a !important;font-size:12pt !important;margin:10px 0 4px !important;page-break-after:avoid;}
p{margin:6px 0 !important;}
table{font-size:9.5pt !important;margin:7px 0 !important;line-height:1.5 !important;}
tr,td,th{page-break-inside:avoid;}
th,td{padding:4px 6px !important;border:.5pt solid #777 !important;}
th{background:#e8e8e8 !important;color:#000 !important;}
tr:nth-child(even) td{background:#f6f6f6 !important;}
hr{margin:10px 0 !important;border:0;border-top:.6pt dashed #999 !important;}
code{background:#efefef !important;color:#000 !important;padding:0 2px;font-size:9.5pt;}
strong{color:#000 !important;} em{color:#000 !important;font-weight:bold;}
.map{background:#f2f2f2 !important;border-left:2.5pt solid #333 !important;padding:7px 10px !important;margin:7px 0;}
.feedback{background:#faf4f4 !important;border:.6pt solid #888 !important;padding:8px 10px !important;margin:8px 0;line-height:1.6 !important;}
.toc{background:#f6f6f6 !important;border:.6pt solid #999 !important;padding:6px 10px !important;font-size:9.5pt !important;line-height:1.9 !important;}
.toc a{color:#000 !important;text-decoration:none !important;}
mark.glow{background:#fff3b8 !important;color:#000 !important;padding:0 2px;font-weight:bold;}
.mapwrap,.feedback{page-break-inside:avoid;}
"""

with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page()
    pg.goto(f"file://{SRC}", wait_until="networkidle")
    pg.evaluate(INVERT_JS)
    pg.add_style_tag(content=PRINT_CSS)
    pg.emulate_media(media="print")
    pg.pdf(path=OUT, format="A4", print_background=True,
           margin={"top":"12mm","bottom":"12mm","left":"13mm","right":"11mm"})
    b.close()

try:
    from pypdf import PdfReader
except ImportError:
    from PyPDF2 import PdfReader
print("PDF_OK", OUT, f"{len(PdfReader(OUT).pages)}页")
