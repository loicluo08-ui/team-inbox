#!/usr/bin/env python3
# sympy验点_数学3.2.1_单调性与最大小值（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_数学3.2.1_B线_1031.html·锚=h(t)=−4.9t²+14.7t+18顶点t=1.5最大h≈29
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
t1 = symbols('t1', real=True)
h = -Rational(49, 10)*t1**2 + Rational(147, 10)*t1 + 18
chk('vertex_t_1_5', Rational(147, 10)/(2*Rational(49, 10)) == Rational(3, 2))
chk('vertex_h_29', abs(float(h.subs(t1, Rational(3, 2))) - 29.025) < 0.01)
chk('单调性_斜率判据', diff(2*x + 1, x).is_positive)
chk('f_x2_min_0', minimum(x**2, x) == 0)
chk('1x导数', diff(1/x, x).equals(-1/x**2))
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
