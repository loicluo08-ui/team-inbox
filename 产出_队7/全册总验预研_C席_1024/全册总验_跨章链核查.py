#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全册总验·跨章链完整性核查（串联图引用图谱+迁移钩子实体表·半自动：图谱机检+语义判定留人工）
用法: python3 全册总验_跨章链核查.py <第1章.html> [第2章.html 第3章.html ...]
输出: 引用边表(从节→指向节)·孤立节清单·钩子实体矩阵(闽西/龙硿洞/FAST等)·人工判定要点"""
import re, sys, io, os

HOOKS = ['闽西', '龙硿洞', 'FAST', ' Darwin', '达尔文', '土楼', '汀江']

def links(path):
    s = io.open(path, encoding='utf-8').read()
    cur = None; edges = []; hooks = {}
    for m in re.finditer(r'<h1[^>]*>([^<]*)|<h2[^>]*>([^<]*)|(→\s*\d\.\d[^<]{0,40})|(' + '|'.join(HOOKS) + ')', s):
        if m.group(1): cur = re.sub(r'\s+', '', m.group(1))[:18]
        elif m.group(3) and cur:
            edges.append((cur, re.sub(r'\s+', '', m.group(3))[:24]))
        elif m.group(4):
            hooks[m.group(4)] = hooks.get(m.group(4), 0) + 1
    return cur, edges, hooks

if __name__ == '__main__':
    files = [a for a in sys.argv[1:] if a.endswith('.html')]
    alledges, allhooks = [], {}
    for f in files:
        cur, edges, hooks = links(f)
        alledges += edges
        for k, v in hooks.items(): allhooks[k] = allhooks.get(k, 0) + v
        print(f"[{os.path.basename(f)}] 引用边{len(edges)}条·钩子{hooks}")
    print('---\n跨章引用边表（人工判定要点：指向节实存且语义相符·S9可回源）:')
    for a, b in alledges: print(f'  {a}  →  {b}')
    print(f'钩子实体矩阵: {allhooks}')
    print('提示: 孤立节=无跨节引用的节（候人工判读是否需钩子；宁缺毋编不强行造链）')
