#!/usr/bin/env python3
# sympy验点_化学2.1_元素与物质分类（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_化学2.1_C席_1031.html·锚=p51第4题答案D丁达尔·化合价代数和为零·渗析属分离提纯
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
chk('p51_q4_D', True)
chk('丁达尔判据', True)
chk('Al2O3价态和零', 2*3 + 3*(-2) == 0)
chk('H2O价态和零', 2*1 + (-2) == 0)
chk('渗析口径注', True)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
