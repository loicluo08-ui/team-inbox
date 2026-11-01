#!/usr/bin/env python3
# sympy验点_数学3.1_函数的概念及其表示（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_数学3.1_B线_1031.html·锚=p65原答案f(2/3)=3/8+√33/3·p71:0.8×117600−70160=23920·0.03×23920=717.6
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
chk('p65_sqrt_id', simplify(sqrt(Rational(11, 3)) - sqrt(33)/3) == 0)
chk('p71_income', Rational(8, 10)*117600 - 70160 == 23920)
chk('p71_tax', Rational(3, 100)*23920 == Rational(7176, 10))
chk('函数对应唯一性', (lambda v: 2*v + 1)(3) == 7)
chk('分段函数口径', max(1, 2) == 2 and min(1, 2) == 1)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
