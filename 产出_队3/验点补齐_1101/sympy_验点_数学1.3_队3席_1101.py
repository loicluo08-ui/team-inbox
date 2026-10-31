#!/usr/bin/env python3
# sympy验点_数学1.3_集合的基本运算（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_数学1.3_队2席_1031.html·锚=p12练习1：A={3,5,6,8}B={4,5,7,8}；p13练习2：U={1..7}A={2,4,5}B={1,3,5,7}
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
A = {3, 5, 6, 8}; B = {4, 5, 7, 8}
chk('p12_A_and_B', A & B == {5, 8})
chk('p12_A_or_B', A | B == {3, 4, 5, 6, 7, 8})
U = set(range(1, 8)); A2 = {2, 4, 5}; B2 = {1, 3, 5, 7}
chk('p13_compl_B', (U - B2) == {2, 4, 6})
chk('p13_A_and_complB', A2 & (U - B2) == {2, 4})
chk('U_has_7', max(U) == 7)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
