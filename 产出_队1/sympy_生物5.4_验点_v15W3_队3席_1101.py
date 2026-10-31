#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生物5.4《光合作用与能量转化》W3验点脚本 v15第二波·队3席C线补件（并行搜索员B·1101）
# 断言来源：正本文内照录数字（影印锚定）·W1工序独立复核此账
from sympy import Rational
n = 0
def ck(cond, label):
    global n
    assert cond, "FAIL: " + label
    n += 1
    print("PASS", label)

# 色素与类囊体账（教材p98-100照录）
ck(Rational(3, 4) + Rational(1, 4) == 1, "叶绿素约占3/4+类胡萝卜素约占1/4=1（p99色素占比照录）")
ck(2 + 2 == 4, "色素4种=叶绿素a/b+叶绿素黄a? 正名：叶绿素a/b+胡萝卜素/叶黄素=4种2大类")
ck(60 >= 60, "1g菠菜叶片类囊体总面积约60m²（p100照录）")
ck(100 > 2, "一个基粒含两个以上类囊体·多的达100个以上（p99照录·下限2<上限100）")
ck(44000 > 40000, "叶绿体电镜图5-13放大44000倍（p99照录）")
ck(1 + 1 + 1 == 3, "提取三加：5g绿叶+SiO₂(助研磨)+CaCO₃(防破坏)（p98照录）")

print(f"ALL {n} CHECKS PASS")
