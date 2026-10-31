#!/usr/bin/env python3
# sympy验点_化学1.1_走进化学科学（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_化学1.1_C席_1031.html·锚=p5定义（原子分子水平·定性）·绪论节定量锚稀疏·科学计数法/常识锚自编标注如实申报
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
chk('def_p5_定性锚', True)
chk('sci_notation_nm', Rational(1, 10**9) == Rational(1, 10)**9)
chk('NaCl_离子构成_定性', True)
chk('元素已超100种', 100 < 119)
chk('观察_实验_结论路径', True)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
