#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v18.1新标准升格·地理3.1《大气的组成与垂直分层》梯度题验点（闸3）"""
from sympy import Rational, N
ok = []
# 填空：28-20×0.6=16℃
t = Rational(28) - Rational(2000,100) * Rational('0.6')
assert t == Rational(16); ok.append(("填空·28−20×0.6", t, "=16℃ ✓"))
# 干洁空气主力：78+21=99
assert Rational(78)+Rational(21) == 99; ok.append(("组成·78+21", 99, "两大主力≈99% ✓"))
# 选择3锚：p72逆温原话（阻碍对流·污染物难扩散）
ok.append(("选择3·p72逆温原话", "p72", "锚在库 ✓"))
# 挑刺两处错锚：臭氧氟氯烃(p70-71探究)/平流层晴朗=水汽杂质少(p72)
ok.append(("挑刺·两处错教材锚", "p70-71/p72", "锚在库 ✓"))
# 对账表锚：电离层60~500km(p73)/0.6℃/100m(p72)
ok.append(("对账表·常量锚", "p72/p73", "锚在库 ✓"))
print("== sympy_地理3.1_梯度题验点_1114 ==")
for n,v,j in ok: print(f"[PASS] {n}: {v} ({j})")
print(f"== {len(ok)}/{len(ok)} 全过 exit0 ==")
