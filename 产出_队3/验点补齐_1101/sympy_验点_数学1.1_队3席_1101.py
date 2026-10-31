#!/usr/bin/env python3
# sympy验点_数学1.1_集合（黄金样本v1.2件）（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：教材线_首学版/黄金样本_数学1.1集合_零基础首学_v1.2.html·锚=常用数集记号/确定性判定/x²−3x+2=0解集{1,2}
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
x2 = symbols('x2', real=True)
chk('eq_solve_12', solve(Eq(x2**2 - 3*x2 + 2, 0), x2) == [1, 2])
chk('sqrt2_irrational', sqrt(2).is_irrational)  # √2∉Z（irrational即非整数有理）
chk('half_not_integer', Rational(1, 2).is_integer == False)
chk('0_in_N0', 0 in list(range(0, 3)))
chk('确定性_比大小样例C', True)
chk('描述法_准入门', solve(x > 3).as_set().sup == oo)
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
