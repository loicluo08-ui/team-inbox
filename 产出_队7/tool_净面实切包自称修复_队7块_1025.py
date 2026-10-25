#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
工具_净面实切包自称修复_队7块_1025.py（并行搜索员C·净面队7块）
承: 管理员12:11:24队7块派令(确权单落地后按确权口径一次动工) + 词表确权单(报告汇总员·4af2509)
    口径=A4.3原文13词面钉死, 本工具只清"实切包"词面·只动title/h1系列命名标签,
    不碰内容锚/引文本体/秒窗/结构标签(tag树与属性零变更, 仅label文本词面移除)。
三段式(承C席1024幂等教训): ①逐模式计数断言替换 ②13词面复扫 ③重跑零变更断言(幂等)
"""
import hashlib, sys, io

BASE = "/tmp/team-inbox/"
# (文件, 旧串, 新串, 预期出现次数)
EDITS = [
    # 地理第1章 (2处)
    ("产出_队7/装配_地理必修一前三章_第1章_1024.html", "（实切包 1.1–1.4）", "（1.1–1.4）", 1),
    ("产出_队7/装配_地理必修一前三章_第1章_1024.html", "实切包 · 1.1–1.4 四节全", "1.1–1.4 四节全", 1),
    # 地理第2章 (2处)
    ("产出_队7/装配_地理必修一前三章_第2章_1024.html", "（实切包 2.1–2.3）", "（2.1–2.3）", 1),
    ("产出_队7/装配_地理必修一前三章_第2章_1024.html", "实切包 · 2.1–2.3", "2.1–2.3", 1),
    # 地理第3章 (2处)
    ("产出_队7/装配_地理必修一前三章_第3章_1024.html", "（实切包 3.1–3.3）", "（3.1–3.3）", 1),
    ("产出_队7/装配_地理必修一前三章_第3章_1024.html", "实切包 · 3.1–3.3 三节全", "3.1–3.3 三节全", 1),
    # 化学三章 (4处: 1章title+h1各1, 2/3章h1各1)
    ("产出_队3/装配_化学必修一_第1章_1024.html", " · 章级实切包", "", 2),
    ("产出_队3/装配_化学必修一_第2章_1024.html", " · 章级实切包", "", 1),
    ("产出_队3/装配_化学必修一_第3章_1024.html", " · 章级实切包", "", 1),
    # 生物B2章 (2处: title+h1)
    ("产出_队1/B2章_实切包_生物第2章_队1_1023.html", "第2章实切包 v1", "第2章", 1),
    ("产出_队1/B2章_实切包_生物第2章_队1_1023.html", " · 实切包 v1", "", 1),
]
WORDS13 = ["队1","队2","队3","队4","队5","队6","队7","队N","首件","claim","commit","待核",
           "帧验","底本","席","canonical","连跑","升格","工作单","实切包"]  # 20字面项=13词面(确权单§三统一词表版)
FILES = sorted(set(e[0] for e in EDITS))

def sha16(p):
    return hashlib.sha256(open(BASE+p, "rb").read()).hexdigest()[:16]

def load(p):  return io.open(BASE+p, encoding="utf-8").read()
def save(p, s): io.open(BASE+p, "w", encoding="utf-8").write(s)

print("== 修前sha256[:16] ==")
for f in FILES: print(f"  {sha16(f)}  {f}")

mode = sys.argv[1] if len(sys.argv) > 1 else "run"
total = 0
for f, old, new, exp in EDITS:
    s = load(f); c = s.count(old)
    want = 0 if mode == "rerun" else exp          # rerun模式=重跑零变更断言: 全部模式0命中且零写入
    assert c == want, f"ABORT {f}: '{old}' 期望{want}处 实测{c}处"
    if c: s = s.replace(old, new); save(f, s); total += c
    print(f"  {'零变更(幂等)' if c == 0 else '替换'} {f}: '{old[:24]}' ×{c}")
print(f"== 本轮替换 {total} 处 (rerun幂等要求=0) ==")

print("== 13词面(20字面项)复扫·八件 ==")
ok = True
for f in FILES:
    s = load(f); hits = {w: s.count(w) for w in WORDS13 if s.count(w)}
    print(f"  {f.split('/')[-1]}: {hits if hits else '全零'}")
    if "实切包" in hits: ok = False
assert ok, "实切包词面残留>0, FAIL"
print("== PASS: 实切包词面八件清零 ==")
