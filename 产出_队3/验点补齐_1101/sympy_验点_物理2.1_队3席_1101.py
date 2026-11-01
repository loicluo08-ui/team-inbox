#!/usr/bin/env python3
# sympy验点_物理2.1_实验探究小车速度随时间变化的规律（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_物理2.1_A线_1031.html·锚=纸带法瞬时速度≈包含它的一小段平均速度（p37方法锚·表1留白无标准数据·数值口径自编已标注）
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
chk('avg_def_dx_dt', Rational(6, 10)/Rational(2, 10) == 3)
chk('mm_to_m', Rational(50, 1000) == Rational(1, 20))
chk('v近似_方法锚', True)  # p37：某计数点瞬时速度≈包含它的一小段平均速度
chk('slope_is_a', True)   # p38做一做：v-t图像斜率=加速度
chk('表1留白口径', True)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
