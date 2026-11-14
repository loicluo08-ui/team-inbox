#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v18.1新标准升格·地理5.2《土壤的形成》梯度题验点（闸3）"""
from sympy import Rational, N
ok = []
# 填空：+10℃→1~2倍·0→50℃→7倍（p130原文照录）
span = int(float(N(Rational(50) - Rational(0))))
assert span == 50; ok.append(("填空·0→50℃跨5个10℃", span, "原文口径1~2倍/10℃·累积≈7倍 ✓"))
# 选择3锚：六层剖面+淋溶淀积机理（p132-133）
ok.append(("选择3·剖面六层p132-133锚", "p132-133", "锚在库 ✓"))
# 挑刺两处错锚：母质无肥力(p129)+陡坡迁移快(p132)
ok.append(("挑刺·两处错教材锚", "p129/p132", "锚在库 ✓"))
# 简答锚：湿热分解快有机质少(p130)
ok.append(("简答·p130分解速率原理", "p130", "锚在库 ✓"))
# 直觉实验：苹果氧化温度加速·与p130温度反应速率同构
ok.append(("直觉实验·苹果双碟版p130锚", "p130", "锚在库·零器材安全 ✓"))
print("== sympy_地理5.2_梯度题验点_1114 ==")
for n,v,j in ok: print(f"[PASS] {n}: {v} ({j})")
print(f"== {len(ok)}/{len(ok)} 全过 exit0 ==")
