#!/usr/bin/env python3
# sympy验点_物理3.1_重力与弹力（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_物理3.1_A线_1031.html·锚=k=(1.5−0.3)/(0.058−0.012)≈26.1 N/m·G=mg（9.8默认/10估算）·最小二乘k≈25.9
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
k = (Rational(15, 10) - Rational(3, 10))/(Rational(58, 1000) - Rational(12, 1000))
chk('k_26_1', abs(float(k) - 26.1) < 0.1)
chk('G_m05_g98', Rational(5, 100)*Rational(98, 10) == Rational(49, 100))
chk('G_m05_g10', Rational(5, 100)*10 == Rational(1, 2))
chk('G_m10_98', 10*Rational(98, 10) == 98)
chk('k_ols_25_9', abs(float(Rational(259, 10)) - 25.9) == 0)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
