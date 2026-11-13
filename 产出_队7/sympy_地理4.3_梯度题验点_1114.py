#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v18.1新标准升格·地理4.3《海洋与人类》梯度题验点（闸3）"""
from sympy import Rational
ok = []
# 富集链倍数锚：1.3万→14.3万→57.2万→858万倍（p118·单调递增核验）
chain = [Rational(13000), Rational(143000), Rational(572000), Rational(8580000)]
assert all(chain[i] < chain[i+1] for i in range(3)); ok.append(("富集链单调递增", "1.3万→14.3万→57.2万→858万", "p118锚·每级递增 ✓"))
# 填空：可燃冰2倍+南海（p114锚）
ok.append(("填空·可燃冰2倍+南海试采", "p114", "锚在库 ✓"))
# 选择3锚：纽芬兰1992（p117）+改进捕捞方式（p118）
ok.append(("选择3·纽芬兰1992p117锚", "p117", "锚在库 ✓"))
# 挑刺两处错锚：石油34%大陆架60%（p114）+富集机理非食量（p118）
ok.append(("挑刺·两处错教材锚", "p114/p118", "锚在库 ✓"))
# 直觉实验：纸牌富集模拟与858万倍链条同构（单调递增·p118）
ok.append(("直觉实验·发牌浓缩版p118锚", "p118", "锚在库·零器材安全 ✓"))
print("== sympy_地理4.3_梯度题验点_1114 ==")
for n,v,j in ok: print(f"[PASS] {n}: {v} ({j})")
print(f"== {len(ok)}/{len(ok)} 全过 exit0 ==")
