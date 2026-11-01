#!/usr/bin/env python3
# sympy验点_物理3.5_共点力的平衡（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_物理3.5_A线_1031.html·锚=μ=0.4→θ≈21.8°·h=b·tanθ=2.4双路互证·μ=0.5→h=3m·F=500×9.8×(0.5+0.3×0.866)=3723N
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
import math
chk('theta_21_8', abs(math.degrees(math.atan(0.4)) - 21.8) < 0.1)
chk('h_2_4_双路互证', abs(6*math.tan(math.atan(0.4)) - 2.4) < 1e-12)
chk('mu05_h_3m', 0.5*6 == 3.0)
chk('theta_26_6', abs(math.degrees(math.atan(0.5)) - 26.565) < 0.01)
chk('F_3723N', abs(500*9.8*(0.5 + 0.3*0.866) - 3723) < 1)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
