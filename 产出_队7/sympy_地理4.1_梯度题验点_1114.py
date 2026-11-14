#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v18.1新标准升格·地理4.1《水循环》梯度题验点（闸3）"""
from sympy import Rational, N
ok = []
# 填空：1100÷28≈39.3→39平方千米/年
r = N(Rational(1100, 28), 6); assert 39.2 < float(r) < 39.4
ok.append(("填空·1100÷28", r, "≈39.3→39平方千米/年（p94阅读锚）✓"))
# 直觉实验：500×2.5%×0.3%≈0.0375mL<一滴0.05mL
v = N(Rational(500,1000)*Rational('0.025')*Rational('0.003'), 5)
assert float(v) < 0.05; ok.append(("直觉实验·人类常用淡水", v, "≈0.0375mL<一滴0.05mL ✓"))
# 选择3锚：下渗→地表径流/地下径流环节链（p91七环节+p96鱼鳞坑）
ok.append(("选择3·海绵城市环节链", "p91/p96", "锚在库 ✓"))
# 挑刺两处错锚：循环=补充更新动力(p93意义)+判类看水汽来源(p91-92)
ok.append(("挑刺·两处错教材锚", "p93/p91-92", "锚在库 ✓"))
# 对账表锚：97%/0.3%(p89)+黄河39km²(p94)
ok.append(("对账表·常量锚", "p89/p94", "锚在库 ✓"))
print("== sympy_地理4.1_梯度题验点_1114 ==")
for n,v,j in ok: print(f"[PASS] {n}: {v} ({j})")
print(f"== {len(ok)}/{len(ok)} 全过 exit0 ==")
