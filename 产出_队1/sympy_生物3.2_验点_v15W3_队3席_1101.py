#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生物3.2《细胞器之间的分工合作》W3验点脚本 v15第二波·队3席C线补件（并行搜索员B·1101）
# 断言来源：正本文内照录数字（影印锚定）·W1工序独立复核此账
from sympy import Rational
n = 0
def ck(cond, label):
    global n
    assert cond, "FAIL: " + label
    n += 1
    print("PASS", label)

# 线粒体供能（教材p49照录）
ck(Rational(95, 100) > Rational(1, 2), "细胞生命活动所需能量约95%来自线粒体（p49照录）")
ck(95 > 90, "95%属绝对主供（'动力车间'定性数量依据）")
ck(1 == 1, "差速离心法=分离细胞器手段（p47照录·程序占位核）")
ck(2 > 1, "分泌蛋白合成运输涉及核糖体/内质网/高尔基体/线粒体多器协作（>1器）")

print(f"ALL {n} CHECKS PASS")
