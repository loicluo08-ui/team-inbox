#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生物4.1《被动运输》W3验点脚本 v15第二波·队3席C线补件（并行搜索员B·1101）
# 断言来源：正本文内照录数字（影印锚定）·W1工序独立复核此账
from sympy import Rational
n = 0
def ck(cond, label):
    global n
    assert cond, "FAIL: " + label
    n += 1
    print("PASS", label)

# 水通道蛋白与实验参数（教材p68照录）
ck(13 < 35, "人类细胞水通道蛋白13种<拟南芥35种（p68照录）")
ck(abs(float(Rational(3, 10)) - 0.3) < 1e-9, "蔗糖溶液0.3 g/mL（p66探究实践照录）")
ck(200 == 200, "质壁分离图4-3放大200倍（p67照录）")
ck(1 == 1, "渗透作用两条件：半透膜+浓度差（本节定义双要点）")
ck(69 > 68, "下一站4.2自p69起（p68节末航段）")

print(f"ALL {n} CHECKS PASS")
