#!/usr/bin/env python3
"""元层页在位性断言 v2（10/27拆分配套·防夹带回退）
用法: python3 qc_元层页在位性_v1.py
v2断言对象（拆分后）：①独立元层页文件三要素（数4章：自画结构卡/三个坎/讲法锚视频段）
②16册装配html的META_INCLUDE占位在位（防占位被误删致渲染丢元层页）
退出码: 0=全在位；1=缺失清单
"""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
fail = 0
# ①独立文件三要素（数4章样板）
p = '产出_元层页/元层页_数4.html'
try:
    t = io.open(p, encoding='utf-8').read()
    missing = [m for m in ['自画结构卡','这一章的三个坎','讲法锚视频段'] if m not in t]
    if missing: print(f'❌{p}: 缺{missing}'); fail += 1
    else: print(f'✅{p}: 三要素在位')
except FileNotFoundError:
    print(f'❌{p}: 文件不存在'); fail += 1
# ②16册占位在位
CANON = ['产出_队2/装配_数学必修一_第1章_升格版_1026.html','产出_队2/装配_数学必修一_第2章_升格版_1026.html',
 '产出_队2/装配_数学必修一_第3章_1024.html','产出_队2/装配_数学必修一_第4章_升格版_1026.html',
 '产出_队3/装配_化学必修一_第1章_升格版_1026.html','产出_队3/装配_化学必修一_第2章_升格版_1026.html',
 '产出_队3/装配_化学必修一_第3章_升格版_1026.html','产出_队4/装配_物理必修一_第1章_1024.html',
 '产出_队4/装配_物理必修一_第2章_1024.html','产出_队4/装配_物理必修一_第3章_1024.html',
 '产出_队4/装配_物理必修一_第4章_1024.html','产出_队1/装配_生物B2章组成细胞的分子_首件_1024.html',
 '产出_队1/装配_生物B3章细胞的基本结构_连跑_1024.html','产出_队1/装配_生物B4章细胞的物质输入和输出_连跑_1024.html',
 '产出_队1/装配_生物B5章细胞的能量供应和利用_连跑_1024.html','产出_队1/装配_生物B6章细胞的生命历程_连跑_1024.html']
n_ok = 0
for f in CANON:
    try:
        t = io.open(f, encoding='utf-8').read()
        if '<!--META_INCLUDE:' in t: n_ok += 1
        else: print(f'❌{f}: 占位缺失'); fail += 1
    except FileNotFoundError:
        print(f'❌{f}: 文件不存在'); fail += 1
print(f'占位在位: {n_ok}/16')
sys.exit(1 if fail else 0)
