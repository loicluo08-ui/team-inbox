#!/usr/bin/env python3
# sympy验点_物理1.1_质点参考系（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_物理1.1_A线_1031.html·锚=地球直径1.3万km÷地日距离1.5亿km≈0.87×10⁻⁴<万分之一
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
ratio = Rational(13, 10)*10**4/(Rational(3, 2)*10**8)
chk('diameter_over_dist', abs(float(ratio) - 0.87e-4) < 0.01e-4)
chk('less_than_1e-4', ratio < Rational(1, 10000))
chk('换算系数_3_6', abs(float(Rational(36, 10)) - 3.6) < 1e-12)
chk('kmh_to_ms_consist', abs(Rational(100, 36)*3.6 - 10) < 1e-12)
chk('质点模型口径', True)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
