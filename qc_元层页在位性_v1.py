#!/usr/bin/env python3
"""元层页在位性断言 v1（10/27覆盖事故后立·防兄弟session夹带回退）
用法: python3 qc_元层页在位性_v1.py
断言对象: 装配_数学*_第N章_升格版*.html 元层页三要素（⑧自画结构卡/这一章的三个坎/讲法锚视频段）
退出码: 0=全在位；1=有缺失（打印缺失清单）
注: 三坎段目前仅数4章有（样板首件），其余册断言两要素（自画结构卡+讲法锚句在16册元层页是否批量放量后再定）——
    当前精确断言=数4章三要素；其余15册候放量后扩。
"""
import glob, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
TARGETS = {'产出_队2/装配_数学必修一_第4章_升格版_1026.html': ['自画结构卡', '这一章的三个坎', '讲法锚视频段']}
fail = 0
for path, marks in TARGETS.items():
    try:
        t = io.open(path, encoding='utf-8').read()
    except FileNotFoundError:
        print(f'❌{path}: 文件不存在'); fail += 1; continue
    missing = [m for m in marks if m not in t]
    if missing:
        print(f'❌{path}: 缺{missing}（疑似被夹带commit回退——对照git log该文件最近两次改动）'); fail += 1
    else:
        print(f'✅{path}: 三要素在位')
sys.exit(1 if fail else 0)
