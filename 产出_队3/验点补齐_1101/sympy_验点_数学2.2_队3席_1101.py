#!/usr/bin/env python3
# sympy验点_数学2.2_基本不等式（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_数学2.2_B线_1031.html·锚=p44原句a²+b²≥2ab等号a=b·数值组验证
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
a2 = symbols('a2', positive=True)
chk('ineq_3_4', 9 + 16 >= 2*3*4 and 9 + 16 - 24 == 1)
chk('等号取a_eq_b', 4 + 4 == 2*2*2)
chk('ineq_1_5', 1 + 25 >= 10)
chk('AM_GM_1_5', sqrt(Rational(1, 5)) <= 3)
chk('symbolic_ineq', simplify(a2**2 + 4 - 4*a2 - (a2 - 2)**2) == 0)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
