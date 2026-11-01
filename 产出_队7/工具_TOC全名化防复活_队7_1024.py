#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
工具·TOC全名化防复活批验（队7·B席·1024晚收官批⑤）
背景：e55da51 已将 3.2/3.3 装配件 TOC 括号截断×4（另同根 5 条非括号型）全名化根修完毕；
      根因=早期装配生成 TOC 条目时 name[:12] 截断（队3化学 6825992 name[:16] 同族异参）。
本件=根修收口：对在链装配件批跑「TOC条目文本 ↔ 锚点标题全文」一致性校验，
      支 --fix 将 TOC 文本自动改写为锚点标题全文（href 锚零触碰），防装配复活。
用法：python3 工具_TOC全名化防复活_队7_1024.py [file.html ...] [--fix]
退出码：0=全件零失配；1=存在失配（未用 --fix 时）；2=内部错误
"""
import sys, re, io

def check(path, fix=False):
    s = io.open(path, encoding='utf-8').read()
    # 锚点标题全文表：id="..." 元素内的文本（取 h2/h3/h1/section 常见标题容器）
    anchors = {}
    for m in re.finditer(r'<(h[1-4])\s+id="([^"]+)"[^>]*>(.*?)</\1>', s, re.S):
        txt = re.sub(r'<[^>]+>', '', m.group(3)).strip()
        anchors[m.group(2)] = txt
    # TOC 条目：<a href="#xxx" ...>text</a>（限定 toc 容器内）
    toc_spans = [m.span() for m in re.finditer(r'<div class="toc"[^>]*>.*?</div>', s, re.S)]
    mism = []
    for (a, b) in toc_spans:
        seg = s[a:b]
        for m in re.finditer(r'<a href="#([^"]+)"[^>]*>(.*?)</a>', seg, re.S):
            tgt, cur = m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip()
            full = anchors.get(tgt)
            if full is None:
                mism.append((tgt, cur, '<锚点未找到>', False)); continue
            if cur != full:
                mism.append((tgt, cur, full, True))
    if fix and mism:
        def repl(mm):
            tgt, cur = mm.group(1), mm.group(2)
            full = anchors.get(tgt)
            if full and re.sub(r'<[^>]+>', '', cur).strip() != full:
                return mm.group(0).replace(mm.group(2), full)
            return mm.group(0)
        for (a, b) in toc_spans:
            seg = s[a:b]
            seg2 = re.sub(r'<a href="#([^"]+)"[^>]*>(.*?)</a>', repl, seg, flags=re.S)
            s = s[:a] + seg2 + s[b:]
        io.open(path, 'w', encoding='utf-8').write(s)
    return len([1 for x in mism if x[1] != x[2]]), mism

def main():
    args = [a for a in sys.argv[1:]]
    fix = '--fix' in args
    files = [a for a in args if not a.startswith('--')]
    if not files:
        print('用法: 工具_TOC全名化防复活_队7_1024.py file.html... [--fix]'); return 2
    total_bad = 0
    for f in files:
        try:
            n, mism = check(f, fix)
        except Exception as e:
            print(f'[ERR] {f}: {e}'); total_bad += 1; continue
        if n == 0:
            print(f'[PASS] {f}: TOC↔标题 全名一致（防复活零失配）')
        else:
            print(f'[FAIL] {f}: 失配 {n} 条' + ('（已 --fix 修复）' if fix else ''))
            for tgt, cur, full, _ in mism:
                print(f'    #{tgt}: TOC「{cur[:24]}」 ↔ 标题「{full[:24]}」')
            total_bad += n
    return 0 if total_bad == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
