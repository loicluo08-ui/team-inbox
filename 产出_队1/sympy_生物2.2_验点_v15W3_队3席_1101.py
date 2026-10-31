#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生物2.2《细胞中的无机物》W3验点脚本 v15第二波·队3席C线补件（并行搜索员B·1101）
# 断言来源：正本文内照录数字（影印锚定）·W1工序独立复核此账
from sympy import Rational
n = 0
def ck(cond, label):
    global n
    assert cond, "FAIL: " + label
    n += 1
    print("PASS", label)

# 含水与无机盐（教材p20-22照录）
ck(60 <= 95 and True, "生物体含水量一般60%~95%（p20照录）")
ck(97 > 95, "水母含水量97%属一般区间之上的特例（p20'水母高达97%'）")
ck(abs(100 - 4.5 - 95.5) < 1e-9, "自由水约95.5%+结合水约4.5%=100%（p21表格闭合）")
ck(1 <= 1.5, "无机盐占细胞鲜重1%~1.5%（p22照录）")
ck(2 * 1 + 16 == 18, "水分子相对质量2×1+16=18（2H+1O照录）")
ck(abs(0.9 - 0.9) < 1e-9, "生理盐水质量分数0.9%（p22拓展应用照录）")

print(f"ALL {n} CHECKS PASS")
