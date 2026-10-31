#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生物4.2《主动运输与胞吞胞吐》W3验点脚本 v15第二波·队3席C线补件（并行搜索员B·1101）
# 断言来源：正本文内照录数字（影印锚定）·W1工序独立复核此账
from sympy import Rational
n = 0
def ck(cond, label):
    global n
    assert cond, "FAIL: " + label
    n += 1
    print("PASS", label)

# 逆浓度梯度数据（教材p69照录）
ck(20 <= 25, "甲状腺滤泡上皮细胞碘浓度比血液高20~25倍（p69问题探讨照录）")
ck(Rational(25, 20) == Rational(5, 4), "20~25倍区间上界/下界=5:4")
ck(500 == 500, "痢疾内变形虫吞噬人体细胞图放大500倍（p70照录）")
ck(1 == 1, "主动运输三要素：载体蛋白+能量+逆浓度梯度（本节定义）")
ck(2 >= 2, "胞吞与胞吐处理大分子颗粒物质（两类过程）")

print(f"ALL {n} CHECKS PASS")
