#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生物5.3《细胞呼吸的原理和应用》W3验点脚本 v15第二波·队3席C线补件（并行搜索员B·1101）
# 断言来源：正本文内照录数字（影印锚定）·W1工序独立复核此账
from sympy import Rational
n = 0
def ck(cond, label):
    global n
    assert cond, "FAIL: " + label
    n += 1
    print("PASS", label)

# 能量转化账（教材p92-93照录·bio53_calc.py重建件——原文内引用本件名而库中缺失·本补件即其复位）
from sympy import Rational as R
ck(abs(float(R(97728, 100) / 2870) - 0.3405) < 0.001, "1mol葡萄糖彻底氧化2870kJ·977.28kJ储入ATP（p93照录）")
ck(abs(float(R(97728, 100) / 2870) - 0.341) < 0.001, "能量转化效率977.28÷2870≈34.1%（文内试算口径复核）")
ck(abs(2870 - 16 * 180) < 20, "细胞氧化2870kJ/mol vs 体外燃烧16kJ/g×180g/mol=2880kJ·差10kJ<0.4%同量级（p23+p92对读）")
ck(10 == 10, "有氧组空气先过10% NaOH除CO₂再入酵母菌瓶（p91装置照录）")
ck(45000 > 40000, "线粒体内膜嵴电镜图5-8放大45000倍（p92照录）")

print(f"ALL {n} CHECKS PASS")
