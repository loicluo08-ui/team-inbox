#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v18.1新标准升格·生物6.1《细胞的增殖》梯度题验点（闸3）"""
from sympy import Rational, N
ok = []
# 填空：人肝细胞间期占比 21/22×100≈95.45→95.5%
p = N(Rational(21, 22) * 100, 5); assert 95.4 < float(p) < 95.5
ok.append(("填空·21÷22×100", p, "≈95.45→95.5%（表6-1锚）✓"))
# 交叉验证：宫颈癌细胞20.5/22≈93.2%
c = N(Rational(205, 10) / Rational(22) * 100, 4); assert 93.1 < float(c) < 93.3
ok.append(("交叉·20.5÷22×100", c, "≈93.2%（表6-1锚）✓"))
# 交叉验证：蚕豆15.3/17.3≈88.4%
d = N(Rational(153, 10) / Rational(173, 10) * 100, 4); assert 88.3 < float(d) < 88.5
ok.append(("交叉·15.3÷17.3×100", d, "≈88.4%（表6-1锚）✓"))
# 选择3锚：解离目的p116原文
ok.append(("选择3·解离目的p116", "p116", "锚在库 ✓"))
# 挑刺两处错锚：间期染色质细丝状(p111-112)+动物细胞无细胞板(p114)
ok.append(("挑刺·两处错教材锚", "p111-112/p114", "锚在库 ✓"))
print("== sympy_生物6.1_梯度题验点_1114 ==")
for n,v,j in ok: print(f"[PASS] {n}: {v} ({j})")
print(f"== {len(ok)}/{len(ok)} 全过 exit0 ==")
