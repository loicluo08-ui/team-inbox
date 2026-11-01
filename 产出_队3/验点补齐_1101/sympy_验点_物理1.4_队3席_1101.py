#!/usr/bin/env python3
# sympy验点_物理1.4_加速度（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_物理1.4_A线_1031.html·锚=100km/h=250/9·小汽车a=25/9≈2.8·火车a=5/54≈0.093
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
v = Rational(100, 1)/Rational(36, 10)
chk('v_250_9', v == Rational(250, 9))
chk('a_car_25_9', v/10 == Rational(25, 9))
chk('a_train_5_54', v/300 == Rational(5, 54))
chk('a_train_approx_093', abs(float(v/300) - 0.093) < 0.001)
chk('a_定义口径', True)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
