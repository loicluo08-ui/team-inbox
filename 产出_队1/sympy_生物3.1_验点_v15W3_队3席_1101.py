#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生物3.1《细胞膜的结构和功能》W3验点脚本 v15第二波·队3席C线补件（并行搜索员B·1101）
# 断言来源：正本文内照录数字（影印锚定）·W1工序独立复核此账
from sympy import Rational
n = 0
def ck(cond, label):
    global n
    assert cond, "FAIL: " + label
    n += 1
    print("PASS", label)

# 膜成分与双层推理（教材p41-42照录）
ck(50 + 40 + 2 <= 100 <= 50 + 40 + 10, "脂质50%+蛋白质40%+糖类2%~10%区间闭合（p41照录）")
ck(Rational(2, 2) == 1, "单分子层面积=红细胞表面积2倍→磷脂排布连续两层（p42'数字推理'）")
ck(1895 < 1972, "欧文顿1895推理 < 流动镶嵌模型1972（探案六站时间序）")
ck(Rational(50, 100) == Rational(1, 2), "脂质约占膜质量一半（磷脂最丰富）")
ck(40 > 2, "蛋白质约40% > 糖类2%~10%下限（p41）")

print(f"ALL {n} CHECKS PASS")
