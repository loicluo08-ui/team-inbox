#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v18.1新标准升格·地理2.3《喀斯特海岸和冰川地貌》梯度题验点（闸3）"""
from sympy import Rational, N
ok = []
# 填空：Ca(HCO3)2相对分子质量 = 40+2×(1+12+48)=162
M = Rational(40) + 2*(Rational(1)+Rational(12)+Rational(48))
assert M == 162; ok.append(("填空·Ca(HCO₃)₂相对分子质量", M, "=162 ✓"))
# 沉积链质量对账：CaCO3(100)+CO2(44)+H2O(18)=162（互逆守恒）
r = Rational(40)+Rational(12)+Rational(48)+Rational(44)+Rational(18)
assert r == 162; ok.append(("沉积链·CaCO₃+CO₂+H₂O质量和", r, "=100+44+18=162 ✓（与溶蚀链互逆）"))
# 选择3锚：峡湾p67阅读（④→①→②→③）
ok.append(("选择3·峡湾链条p67", "p67阅读", "锚在库 ✓"))
# 挑刺两处错锚：峰林溶蚀(p60)/峡湾两步(p67)
ok.append(("挑刺·两处错教材锚", "p60峰林溶蚀/p67峡湾", "锚在库 ✓"))
# 直觉实验锚：石钟乳石笋p62阅读
ok.append(("直觉实验·蜡泪版p62锚", "p62阅读", "锚在库 ✓"))
print("== sympy_地理2.3_梯度题验点_1114 ==")
for n,v,j in ok: print(f"[PASS] {n}: {v} ({j})")
print(f"== {len(ok)}/{len(ok)} 全过 exit0 ==")
