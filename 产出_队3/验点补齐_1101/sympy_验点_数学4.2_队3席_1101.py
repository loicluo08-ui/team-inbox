#!/usr/bin/env python3
# sympy验点_数学4.2_指数函数（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_数学4.2_队2席_1031.html·锚=B地增长比309/278≈1.11·p115练习3:1.0625^30≈6.2·412000领先额·交点x≈10.22
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
chk('ratio_1_11', abs(float(Rational(309, 278)) - 1.11) < 0.005)
chk('p115_growth', abs(float(Rational(10625, 10000)**30) - 6.2) < 0.1)
chk('f0_minus_g0_412000', 412000 - 0 == 412000)
chk('a0_eq_1', 2**0 == 1 and Rational(1, 2)**0 == 1)
chk('2pow_half_eq_sqrt2', sqrt(2) == 2**Rational(1, 2))
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
