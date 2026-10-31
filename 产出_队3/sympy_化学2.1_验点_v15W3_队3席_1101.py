#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 化学2.1《元素与物质分类》W3验点脚本 v15第二波·队3席C线补件（并行搜索员B·1101）
# 断言来源：正本文内照录数字（影印锚定）·W1工序独立复核此账
from sympy import Rational
n = 0
def ck(cond, label):
    global n
    assert cond, "FAIL: " + label
    n += 1
    print("PASS", label)

# 化合价代数和为零（p45照录）
ck(2 + (-2) == 0, "CO中C(+2)+O(-2)=0（p45照录）")
ck(4 + 2 * (-2) == 0, "CO₂中C(+4)+2O(-2)=0（p45照录）")
ck(2 * 1 + 4 + 3 * (-2) == 0, "Na₂CO₃：2Na(+1)+C(+4)+3O(-2)=0（文内价-类二维图点位）")
ck(2 * 3 + 3 * (-2) == 0, "Fe₂O₃：2Fe(+3)+3O(-2)=0（文内铁物质'定坐标'）")
ck(Rational(8, 3) > 2, "Fe₃O₄平均价态8/3≈+2.67（介于+2与+3之间·混合价态口径）")
ck(4 - 2 == 2, "碳在CO₂(+4)与CO(+2)价差2（p45'化合价也会变'）")

print(f"ALL {n} CHECKS PASS")
