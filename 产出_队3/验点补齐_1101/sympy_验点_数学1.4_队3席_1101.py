#!/usr/bin/env python3
# sympy验点_数学1.4_充分必要条件（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_数学1.4_群外管理员席_1031.html·锚=菱形判定真·x²=1⇏x=1（x=−1反例）·真值表四组合
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
truth = [(p, q, (not p) or q) for p in (True, False) for q in (True, False)]
chk('implies_truth_table', truth == [(True, True, True), (True, False, False), (False, True, True), (False, False, True)])
chk('x2_eq_1_two_roots', set(solve(Eq(x**2, 1), x)) == {-1, 1})
chk('x2_not_suff_for_x1', not ({-1, 1} <= {1}))
chk('x1_suff_for_x2', {1} <= {-1, 1})
chk('逆否_等价性', ((not True) or False) == (not (True and (not False))))
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
