#!/usr/bin/env python3
"""装配TOC全名化工具 v1.0（队7·报告汇总员·1024晚·管理员放量令②根修件）
根因链（据B席e55da51工作单＋本席装配批实录）：
  装配时TOC条目文本曾取 name[:12]（队3化学6825992系name[:16]同族异参）→h2全名被截断
  （"易错卡（6张，考前翻一遍"恰12字符）。B席e55da51已对3.2/3.3九条做内容层全名化；
  本件=装配工具层根修：TOC条目文本=h2全名（href锚零动），防重装配复活。
用法：
  python3 工具_装配TOC全名化_队7_1024.py check <html...>   # 三分类报告（截断型/设计型/失配型）
  python3 工具_装配TOC全名化_队7_1024.py fix   <html...>   # 仅改写截断型→h2全名（href零动·原文件备份.bak）
边界：
  - 章级件（含"本册目录"短标签导航设计·如装配_地理必修一前三章_第N章）：短标签系设计口径
    （B席e55da51§一.4申报候裁），fix拒触（--force-design放行），check照常报告
  - 正件canonical无TOC结构，天然零触碰；单节件识别特征=TOC含"本节目录"+锚#sN
退出码：0=无截断型失配；2=check发现截断型；3=fix有未处理失配（设计型/失配型残留）
"""
import re, sys, shutil, signal
try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # 防管道下游提前关闭致BrokenPipe
except (AttributeError, ValueError):
    pass

def h2_map(html):
    out = {}
    for m in re.finditer(r'<h2 id="((?:s|sec)\d+)"[^>]*>([\s\S]*?)</h2>', html):
        full = re.sub(r'<[^>]+>', '', m.group(2))
        out[m.group(1)] = re.sub(r'\s+', ' ', full).strip()
    return out

def links(html):
    return [(m.start(), m.end(), m.group(1), m.group(2)) for m in
            re.finditer(r'<a href="#((?:s|sec)\d+)"[^>]*>([^<]+)</a>', html)]

def is_chapter_piece(html):
    return ('本册目录' in html) or ('chapmap' in html)

def classify(html):
    hm, chap = h2_map(html), is_chapter_piece(html)
    rep = []
    for s, e, aid, txt in links(html):
        full = hm.get(aid)
        if full is None:
            rep.append(('失配', aid, txt, '悬空锚（无对应h2）', s, e, txt)); continue
        if txt == full:
            continue
        if full.startswith(txt) and len(txt) >= 2:
            kind = '设计' if chap else '截断'
            rep.append((kind, aid, txt, full, s, e, full))
        else:
            rep.append(('失配', aid, txt, full, s, e, full))
    return rep, chap, hm

def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ('check', 'fix'):
        print(__doc__); sys.exit(1)
    mode, files = sys.argv[1], [a for a in sys.argv[2:] if not a.startswith('--')]
    force = '--force-design' in sys.argv
    total = 0
    for f in files:
        html = open(f, encoding='utf-8').read()
        rep, chap, hm = classify(html)
        trunc = [r for r in rep if r[0] == '截断']
        print(f"—— {f}（{'章级件·短标签设计口径' if chap else '节级件'}）："
              f"截断{len(trunc)} 设计{sum(1 for r in rep if r[0]=='设计')} 失配{sum(1 for r in rep if r[0]=='失配')}")
        for kind, aid, txt, full, *_ in rep:
            print(f"   [{kind}] #{aid} 「{txt[:24]}」→「{full[:36]}」")
        if mode == 'fix' and trunc:
            if chap and not force:
                print("   fix拒触：章级件短标签系设计口径候裁（--force-design放行）"); total = max(total, 3); continue
            bak = f + '.bak'
            shutil.copyfile(f, bak)
            for _, aid, txt, full, s, e, _ in sorted(trunc, key=lambda r: -r[4]):
                seg = html[s:e].replace('>' + txt + '</a>', '>' + full + '</a>', 1)
                html = html[:s] + seg + html[e:]  # 仅替换链接文本·<a>属性零动
            open(f, 'w', encoding='utf-8').write(html)
            print(f"   fix完成：{len(trunc)}条全名化（href零动·备份{bak}）")
            total = max(total, 0)
        elif mode == 'check' and trunc:
            total = max(total, 2)
    sys.exit(total)

if __name__ == '__main__':
    main()
