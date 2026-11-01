# -*- coding: utf-8 -*-
"""队7·§十②地理13件超链接化：裸BV→a标签（对齐2.1样例形态）
规则：BV出现若已在 href="…/video/BV…" 或紧跟 ">"（链接文本）内则跳过，
否则包 <a href="https://www.bilibili.com/video/BVxxx" target="_blank">BVxxx</a>
校验：处理前后 BV 出现总数不变；处理后每文件裸BV=0；diff 仅BV行。
"""
import re, sys, subprocess

PAT = re.compile(r'BV[0-9A-Za-z]{10}')
FILES = [
    "产出_队7/切片卡_地理1.1地球的宇宙环境_首件_1024.html",
    "产出_队7/切片卡_地理2.2风成地貌_1024.html",
    "产出_队7/切片卡_地理2.3喀斯特海岸冰川_1024.html",
    "产出_队7/切片卡_地理3.1大气的组成与垂直分层_1024.html",
    "产出_队7/切片卡_地理3.2大气受热过程_1024.html",
    "产出_队7/切片卡_地理3.3大气热力环流_1024.html",
]

def in_link_before(html, start):
    """判断 BV 出现点之前文是否处于链接结构内"""
    before = html[max(0, start-60):start]
    # href属性内：前文含 href="https://www.bilibili.com/video/BV 且未闭合引号
    m = re.search(r'href="(https://www\.bilibili\.com/video/[A-Za-z0-9]*)$', before)
    if m:
        return True
    # 链接文本内：紧跟 '>'
    if before.endswith('>'):
        return True
    return False

def process(path):
    with open(path, encoding='utf-8') as f:
        html = f.read()
    total0 = len(PAT.findall(html))
    edits = []
    for m in PAT.finditer(html):
        start = m.start()
        if in_link_before(html, start):
            continue
        bv = m.group(0)
        tag = f'<a href="https://www.bilibili.com/video/{bv}" target="_blank">{bv}</a>'
        edits.append((start, start+len(bv), tag, bv))
    # 从后往前替换避免位移
    for s, e, tag, bv in reversed(edits):
        html = html[:s] + tag + html[e:]
    total1 = len(PAT.findall(html))
    # 复验：处理后无裸BV
    bare = []
    for m in PAT.finditer(html):
        if not in_link_before(html, m.start()):
            bare.append(m.group(0))
    # 裸BV包链后每处产生2个BV出现（href属性+链接文本），总数必然增加，成功判据=裸BV归零
    ok = not bare
    print(f"{path}: BV总数 {total0}->{total1} 新增链 {len(edits)} 裸BV残余 {len(bare)} {'OK' if ok else 'FAIL'}")
    if not ok:
        print("  bare:", bare)
        sys.exit(2)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

for p in FILES:
    process(p)
print("ALL DONE")
