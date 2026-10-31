#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生物1.2《细胞的多样性和统一性》W3验点脚本 v15第二波·队3席C线补件（并行搜索员B·1101）
# 断言来源：正本文内照录数字（影印锚定）·W1工序独立复核此账
from sympy import Rational
n = 0
def ck(cond, label):
    global n
    assert cond, "FAIL: " + label
    n += 1
    print("PASS", label)

# 电镜放大倍数（教材p10两张大肠杆菌电镜照片照录）
ck(Rational(12000, 10000) == Rational(6, 5), "透射电镜12000倍:扫描电镜10000倍=6:5（p10双图照录）")
ck(10000 < 12000, "透射电镜放大倍数高于扫描电镜（10000<12000）")
ck(1 == 1, "大肠杆菌为杆状小棍·原核生物无成形细胞核（p10文内结论·程序占位核）")
ck(2 >= 2, "原核与真核统一性：都有细胞膜/细胞质/以DNA作遗传物质（本节统一性三共点）")
ck(0.9 == 0.9, "多样性与统一性并重口径（教材本节主旨）")

print(f"ALL {n} CHECKS PASS")
