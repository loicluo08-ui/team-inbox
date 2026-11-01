#!/usr/bin/env python3
# sympy验点_数学1.2_集合间的基本关系（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：main首学版_数学1.2_队2_1031.html·锚=子集按装元素分类计数（装0/1/2/3个）·0∈{0}·∅⊆{0}
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
chk('subsets_of_3elem', 2**3 == 8)
chk('0_in_set0', 0 in {0})
chk('empty_subset_all', set() <= {0})
chk('proper_subset_count', 2**3 - 1 == 7)
chk('eq_sets_same_elems', {1, 2} == {2, 1})
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
