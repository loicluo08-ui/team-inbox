#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全册总验·打印七查批跑（C1-C8可机检部分·C1/C3目检项输出候选页清单供人工）
用法: python3 全册总验_打印七查批跑.py <a.pdf> [b.pdf ...] [--html 对应html]
检查: 页数/C2首页h1/C4深色占比(60dpi·<100灰度·超1%页清单)/C6页脚页码/页码核对(h1节锚顺序游标线性)"""
import re, sys, os, glob, subprocess, tempfile

def page_text(pdf, pg):
    t = subprocess.run(['pdftotext', '-f', str(pg), '-l', str(pg), pdf, '-'], capture_output=True, text=True)
    return re.sub(r'\s+', '', t.stdout)

def audit(pdf, html=None):
    r, hard = [], 0
    from pypdf import PdfReader
    n = len(PdfReader(pdf).pages)
    r.append(f'🄲8页数={n}')
    p1 = page_text(pdf, 1)
    r.append(f'🄲2首页有字={"✅" if len(p1) > 20 else "⚠️疑白页"}')
    if len(p1) <= 20: hard += 1
    # C4 深色占比
    tmp = tempfile.mkdtemp()
    subprocess.run(['pdftoppm', '-r', '60', '-png', pdf, os.path.join(tmp, 'p')], check=True)
    from PIL import Image
    over, worst, worstp = 0, 0.0, ''
    for f in sorted(glob.glob(os.path.join(tmp, 'p-*.png'))):
        im = Image.open(f).convert('L'); px = list(im.getdata())
        d = sum(1 for v in px if v < 100) / len(px) * 100
        if d >= 1: over += 1
        if d > worst: worst, worstp = d, os.path.basename(f)
    r.append(f'🄲4超1%页={over}/{n}·最高{worst:.2f}%({worstp})' + ('·候目检暗底块' if over else ''))
    # C6/页脚页码
    anypg = page_text(pdf, min(2, n))
    r.append(f'🄲7页脚页码{"✅" if re.search(r"第\d+页", anypg) else "无(标准线版)"}')
    # 页码核对（顺序游标）
    if html:
        import io
        hs = io.open(html, encoding='utf-8').read()
        h1s = re.findall(r'<h1[^>]*>([^<]{4,40})', hs)
        anchors = [re.sub(r'\s+', '', re.sub(r'<[^>]+>', '', x))[:10] for x in h1s]
        pgs = {pg: page_text(pdf, pg) for pg in range(1, n + 1)}
        seq, pos, miss = [], 1, []
        for a in anchors:
            hit = next((pg for pg in range(pos, n + 1) if a in pgs[pg]), None)
            seq.append(hit); pos = hit or pos
            if hit is None: miss.append(a)
        bad = [(i, seq[i], seq[i+1]) for i in range(len(seq)-1) if seq[i] and seq[i+1] and seq[i] > seq[i+1]]
        r.append(f'页码核对: h1锚{len(anchors)}·缺{miss if miss else "无"}·倒挂{bad if bad else "无"}')
        if miss or bad: hard += 1
    return hard, r

if __name__ == '__main__':
    args = sys.argv[1:]
    html = args[args.index('--html') + 1] if '--html' in args else None
    pdfs = [a for a in args if a.endswith('.pdf')]
    nfail = 0
    for f in pdfs:
        hard, r = audit(f, html if html and os.path.basename(html)[:-5] == os.path.basename(f)[:-5] else None)
        nfail += hard
        print(f"[硬伤{hard}] {os.path.basename(f)}")
        for x in r: print('   ', x)
    print(f'---\n七查批跑: {len(pdfs)}件·硬伤{nfail}（C1/C3目检候选页=C4超1%页清单）')
    sys.exit(1 if nfail else 0)
