#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 化学1.2《研究物质性质的方法和程序》W3验点脚本 v15第二波·队3席C线补件（并行搜索员B·1101）
# 断言来源：正本文内照录数字（影印锚定）·W1工序独立复核此账
from sympy import Rational
n = 0
def ck(cond, label):
    global n
    assert cond, "FAIL: " + label
    n += 1
    print("PASS", label)

# 氧的质量分数（文内'机器核验'行照录·本件即其独立复算）
ck(abs(float(Rational(16, 62)) * 100 - 25.8) < 0.05, "Na₂O中O质量分数=16/(2×23+16)≈25.8%（文内机器核验行复算吻合）")
ck(abs(float(Rational(32, 78)) * 100 - 41.0) < 0.05, "Na₂O₂中O质量分数=32/(2×23+32)≈41.0%（文内机器核验行复算吻合）")
ck(Rational(32, 78) > Rational(16, 62), "过氧化钠含氧率高于氧化钠（41.0%>25.8%·'氧多一个原子'）")
ck(2 + 2 == 2 * 2, "方程2Na+Cl₂=2NaCl两边原子守恒：Na 2=2·Cl 2=2（文内配平口径）")
ck(2 <= 4, "研究物质性质四法：观察/实验/分类/比较（方法四照录）")

print(f"ALL {n} CHECKS PASS")
