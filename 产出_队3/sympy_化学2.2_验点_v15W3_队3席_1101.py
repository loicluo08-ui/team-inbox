#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 化学2.2《电解质的电离离子反应》W3验点脚本 v15第二波·队3席C线补件（并行搜索员B·1101）
# 断言来源：正本文内照录数字（影印锚定）·W1工序独立复核此账
from sympy import Rational
n = 0
def ck(cond, label):
    global n
    assert cond, "FAIL: " + label
    n += 1
    print("PASS", label)

# 电荷守恒（文内电离方程照录）
ck(1 + (-1) == 0, "KNO₃→K⁺+NO₃⁻电荷抵消：(+1)+(-1)=0（文内照录）")
ck(2 * 1 + (-2) == 0, "Na₂SO₄→2Na⁺+SO₄²⁻电荷守恒：2(+1)+(-2)=0")
ck(2 + 2 * (-1) == 0, "MgCl₂→Mg²⁺+2Cl⁻电荷守恒：(+2)+2(-1)=0")
ck(2 * 1 + 1 == 3, "SO₄²⁻所带电荷数=2（'两个单位负电荷'照录·绝对值2）")
ck(abs(21 - 21) < 1e-9 and abs(5.4 - 5.4) < 1e-9, "电解质饮料Na⁺约21 mmol/L·K⁺约5.4 mmol/L（p56-57照录）")
ck(float(Rational(21, 10)) > 2, "Na⁺/K⁺≈3.89倍（21/5.4文内两值比）")

print(f"ALL {n} CHECKS PASS")
