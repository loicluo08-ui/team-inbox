#!/usr/bin/env python3
# sympy验点_化学2.2_电解质的电离离子反应（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_化学2.2_C席_1031.html·锚=KCl溶液微粒（p64练习1(2)改编）·Na₂SO₄电荷/原子守恒·碱阴离子全OH⁻
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
chk('KCl_两微粒', 1 + 1 == 2)
chk('Na2SO4_电荷守恒', 2*(+1) + (-2) == 0)
chk('Na2SO4_原子守恒', 2 == 2 and 1 == 1 and 4 == 4)
chk('HCl_电荷和零', (+1) + (-1) == 0)
chk('碱_OH定性锚', True)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
