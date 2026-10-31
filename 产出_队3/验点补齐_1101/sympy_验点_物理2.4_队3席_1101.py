#!/usr/bin/env python3
# sympy验点_物理2.4_自由落体运动（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_物理2.4_A线_1031.html·锚=g=9.8（p48脚注·可取10）·h=½gt²·v=gt·v=√(2gh)
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
g = Rational(98, 10)
chk('h_1s_4_9', g*Rational(1, 2)*1**2 == Rational(49, 10))
chk('h_2s_19_6', g*Rational(1, 2)*2**2 == Rational(196, 10))
chk('v_2s_19_6', g*2 == Rational(196, 10))
chk('v_sqrt_2gh自洽', sqrt(2*g*Rational(49, 10)) == g*1)
chk('g10口径_h2s_20', Rational(10)*Rational(1, 2)*2**2 == 20)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
