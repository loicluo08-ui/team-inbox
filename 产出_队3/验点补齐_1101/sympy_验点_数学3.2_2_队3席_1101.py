#!/usr/bin/env python3
# sympy验点_数学3.2.2_奇偶性（黄金样本v1.4件）（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_数学3.2.2_黄金v1.4_1031.html·锚=p85练习2：f=2x⁴+3x²偶·f=x³−2x奇·[−3,2]不对称非奇非偶·f(0)=0
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
X = symbols('X', real=True)
f1 = 2*X**4 + 3*X**2
f2 = X**3 - 2*X
chk('p85_2a_even', simplify(f1 - f1.subs(X, -X)) == 0)
chk('p85_2b_odd', simplify(f2 + f2.subs(X, -X)) == 0)
chk('domain_-3_2_不对称', (3 not in range(-3, 3)) and (-3 in range(-3, 3)))
chk('odd_f0_0', f2.subs(X, 0) == 0)
chk('x加1_非奇非偶', simplify((X + 1) - (X + 1).subs(X, -X)) != 0)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
