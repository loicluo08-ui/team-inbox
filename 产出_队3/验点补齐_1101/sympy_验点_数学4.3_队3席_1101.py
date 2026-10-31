#!/usr/bin/env python3
# sympy验点_数学4.3_对数（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_数学4.3_队2B_1031.html·锚=log1.112≈6.64（B地翻倍年数）·log2 8=3·lg100=2·换底lg6/lg2
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
chk('log1p11_2_664', abs(float(log(2, Rational(111, 100))) - 6.64) < 0.01)
chk('log2_8_eq_3', log(8, 2) == 3)
chk('lg100_eq_2', log(100, 10) == 2)
chk('log_a_1_eq_0', log(1, 5) == 0)
chk('换底公式', abs(float(log(6, 2) - log(6, 10)/log(2, 10))) < 1e-12)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
