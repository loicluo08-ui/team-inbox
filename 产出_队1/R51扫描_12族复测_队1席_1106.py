#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R-51宽口径12族复测：print硬闸 + html可见层/foot分账（foot嵌套正确解析）"""
import re, os, sys, glob, subprocess, unicodedata

T12 = ['sympy','影印','卷源','本席','留痕','施工','候锚','随件','裁定','已交付','在产','池标']
RX = [(r'dui[0-9]+','dui*'),(r'[0-9a-f]{7}','hex7'),
      (r'(?:contentId|ts)\s*[=:：]?\s*\d{9,}','ts号'),(r'R-\d{3,4}','R件号')]
WL = ['教材配套真题']  # 白名单句面

def norm(s): return re.sub(r'\s+','',unicodedata.normalize('NFKC',s))

def split_foot(raw):
    i = raw.find('class="foot"')
    if i < 0: return raw, ''
    start = raw.rfind('<div', 0, i)
    depth = 0; j = start
    while j < len(raw):
        m = re.search(r'<div\b|</div>', raw[j:])
        if not m: break
        j += m.end()
        if m.group(0).startswith('<div'): depth += 1
        else:
            depth -= 1
            if depth == 0: break
    return raw[:start], raw[start:j]

def strip_html(raw):
    raw = re.sub(r'<title[^>]*>.*?</title>','',raw,flags=re.S)
    raw = re.sub(r'<style[^>]*>.*?</style>','',raw,flags=re.S)
    raw = re.sub(r'<script[^>]*>.*?</script>','',raw,flags=re.S)
    return re.sub(r'<[^>]+>','',raw)

def hits(t):
    out = []
    for w in WL: t = t.replace(norm(w), '◇')
    for tok in T12:
        for m in re.finditer(re.escape(tok), t):
            out.append((tok, t[max(0,m.start()-28):m.start()+34]))
    for pat, name in RX:
        for m in re.finditer(pat, t):
            out.append((name+':'+m.group(0)[:14], t[max(0,m.start()-28):m.start()+34]))
    return out

def run(dom, fileglob, printglob):
    base = {'bio':'产出_队1','geo':'产出_队7'}[dom]
    print(f'\n######## {dom} ########')
    # print硬闸
    for f in sorted(glob.glob(printglob)):
        t = norm(subprocess.run(['pdftotext', f, '-'], capture_output=True, text=True).stdout)
        hh = hits(t)
        if hh:
            print(f'\n-- [PRINT硬闸⚠️] {os.path.basename(f)} ({len(hh)}处)')
            for tok, ctx in hh: print(f'   {tok} …{norm(ctx)[:50]}…')
    # html 分账
    for f in sorted(glob.glob(fileglob)):
        raw = open(f, encoding='utf-8').read()
        vis, foot = split_foot(raw)
        hv = hits(norm(strip_html(vis)))
        hf = hits(norm(strip_html(foot)))
        if hv:
            print(f'\n-- [HTML可见层⚠️] {os.path.basename(f)} ({len(hv)}处)')
            for tok, ctx in hv[:14]: print(f'   {tok} …{norm(ctx)[:50]}…')
        if hf:
            print(f'-- [HTML-foot豁免账] {os.path.basename(f)} ({len(hf)}处)')

if __name__ == '__main__':
    run('bio', '产出_队1/首学版_生物*.html', '产出_队1/print渲染V2.2_生物*.pdf')
    run('geo', '产出_队7/首学版_地理*.html', '产出_队7/print渲染V2.2_地理*.pdf')
