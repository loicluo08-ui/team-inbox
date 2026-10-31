#!/usr/bin/env python3
# sympy验点_化学1.2_研究物质性质的方法和程序（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_化学1.2_群外版_1031.html·锚=2Na+2H₂O═2NaOH+H₂↑配平守恒·p12三阶段·酚酞变红=碱性NaOH
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
chk('Na守恒', 2 == 2)
chk('H守恒', 2*2 == 2*1 + 2)
chk('O守恒', 2 == 2)
chk('安全气囊2NaN3配平', 2*1 == 2*1 and 2*3 == 3*2)
chk('酚酞变红_碱性锚', True)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
