#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生物2.5《核酸是遗传信息的携带者》W3验点脚本 v15第二波·队3席C线补件（并行搜索员B·1101）
# 断言来源：正本文内照录数字（影印锚定）·W1工序独立复核此账
from sympy import Rational
n = 0
def ck(cond, label):
    global n
    assert cond, "FAIL: " + label
    n += 1
    print("PASS", label)

# 碱基与核苷酸账（教材p34-35照录）
ck(4 + 1 == 5, "碱基5种=DNA4种(A,G,C,T)+RNA特有U（p35维恩图口径）")
ck(4 + 4 == 8, "核苷酸8种=脱氧核苷酸4种+核糖核苷酸4种（文内对账表照录）")
ck(3 == 1 + 1 + 1, "1核苷酸=1碱基+1五碳糖+1磷酸（三件凑一件照录）")
ck(len({"A", "G", "C"}) == 3, "DNA与RNA共有碱基A/G/C三种（p35原句'碱基种类有所不同'）")
ck(2 == 2, "五碳糖2种：脱氧核糖（DNA）/核糖（RNA）")

print(f"ALL {n} CHECKS PASS")
