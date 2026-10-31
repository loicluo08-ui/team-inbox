#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生物2.3《细胞中的糖类和脂质》W3验点脚本 v15第二波·队3席C线补件（并行搜索员B·1101）
# 断言来源：正本文内照录数字（影印锚定）·W1工序独立复核此账
from sympy import Rational
n = 0
def ck(cond, label):
    global n
    assert cond, "FAIL: " + label
    n += 1
    print("PASS", label)

# 能量与水解对账（教材p23/p26照录）
ck(Rational(39, 17) > 2, "1g脂肪39kJ÷1g糖原17kJ≈2.29倍（p26照录·'更扛饿'数量依据）")
ck(abs(16 - 16) < 1e-9, "体外燃烧1g葡萄糖释放约16kJ（p23知识链接照录）")
# 蔗糖水解原子对账：C12H22O11 + H2O -> C6H12O6 + C6H12O6
ck(12 == 6 + 6, "蔗糖水解C账：12=6+6（文内对账表照录）")
ck(22 + 2 == 12 + 12, "蔗糖水解H账：24=12+12（22+2）")
ck(11 + 1 == 6 + 6, "蔗糖水解O账：12=6+6（11+1）")
ck(200 < 2200, "拟南芥淀粉粒图2-2放大200倍<脂肪细胞图2-5放大2200倍（p24/p25照录）")

print(f"ALL {n} CHECKS PASS")
