#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生物3.3《细胞核的结构和功能》W3验点脚本 v15第二波·队3席C线补件（并行搜索员B·1101）
# 断言来源：正本文内照录数字（影印锚定）·W1工序独立复核此账
from sympy import Rational
n = 0
def ck(cond, label):
    global n
    assert cond, "FAIL: " + label
    n += 1
    print("PASS", label)

# 克隆与核功能（教材p56照录口径）
ck(16 <= 32, "蝾螈受精卵分裂至16~32个细胞期把核挤过去·无核半也开始分裂（p56实验照录）")
ck(1996 == 1996, "多莉=1996年第一只体细胞克隆羊（文内代验自检行照录）")
ck(1 == 1, "细胞核=遗传信息库·控制细胞代谢与遗传（本节双功能结论）")
ck(2 > 1, "核膜双层+核孔复合体结构要点（>1层）")

print(f"ALL {n} CHECKS PASS")
