#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全册总验·批量化锚点抽验（S10-A/B9/SVG引用/HTML锚-PDF命名目标四合一）
用法: python3 全册总验_锚点批验.py <a.html> [b.html ...]
规则: h2 id零重复零悬空·href全解析·SVG url(#)与defs配对·同名pdf命名目标数>=h2数
输出: 逐文件判定行·总exit码（有伤=1）"""
import re, sys, io, os, glob

def audit_html(path):
    s = io.open(path, encoding='utf-8').read()
    r = {}
    ids = re.findall(r'<h2 id="([^"]+)"', s)
    dup = {x for x in ids if ids.count(x) > 1}
    r['h2锚'] = f'{len(ids)}个' + (f'·重复{sorted(dup)}' if dup else '')
    allids = set(re.findall(r'id="([^"]+)"', s))
    hrefs = re.findall(r'href="#([^"]+)"', s)
    orphan = [h for h in set(hrefs) if h not in allids]
    r['toc链接'] = f'{len(hrefs)}条/全体id{len(allids)}' + (f'·悬空{orphan}' if orphan else '')
    defs = set(re.findall(r'<(?:marker|linearGradient|radialGradient|pattern)[^>]*\bid="([^"]+)"', s))
    refs = set(re.findall(r'url\(#([^)]+)\)', s))
    dangling = refs - defs
    r['SVG引用'] = f'defs{len(defs)}/引用{len(refs)}' + (f'·悬空{sorted(dangling)}' if dangling else '')
    cmark = len(re.findall(r'^(<{7}|={7}|>{7})', s, re.M))
    if cmark: r['冲突标记'] = f'{cmark}处🔴'
    pdf = path[:-5] + '.pdf'
    r['PDF命名目标'] = '无pdf'
    if os.path.exists(pdf):
        try:
            from pypdf import PdfReader
            rd = PdfReader(pdf)
            nd = rd.named_destinations
            r['PDF命名目标'] = f'{len(nd)}/{len(ids)}' + ('' if len(nd) >= len(ids) else '·不足')
        except Exception as e:
            r['PDF命名目标'] = f'解析失败{type(e).__name__}'
    bad = bool(dup or orphan or dangling or r['PDF命名目标'].startswith(('解析', '')) is False and '不足' in r['PDF命名目标'] or '解析失败' in r['PDF命名目标'])
    bad = bool(dup or orphan or dangling or '不足' in r['PDF命名目标'] or '解析失败' in r['PDF命名目标'])
    return bad, r

if __name__ == '__main__':
    files = [a for a in sys.argv[1:] if a.endswith('.html')]
    nfail = 0
    for f in files:
        bad, r = audit_html(f)
        nfail += bad
        print(f"[{'伤' if bad else '过'}] {os.path.basename(f)}: " + ' | '.join(f'{k}={v}' for k, v in r.items()))
    print(f'---\n锚点批验: {len(files)}件·伤{nfail}')
    sys.exit(1 if nfail else 0)
