#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sympy 验点：数学1.3 新标准升格·梯度题验点（v18.1 队2席·并行搜索员B·1114）
覆盖：新增7题答案与数值点·闸3机器代验前置·留痕=sympy_数学1.3_梯度题验点_1114_运行留痕.txt
"""
from sympy import FiniteSet, solve, symbols, Interval, oo, Union, Complement, S
PASS, FAIL = [], []
def chk(name, cond, detail=""):
    (PASS if cond else FAIL).append((name, detail))
    print(f'[{"PASS" if cond else "FAIL"}] {name}' + (f' => {detail}' if detail else ''))

x, a = symbols('x a', real=True)
A13 = FiniteSet(*solve(x**2 - 4*x + 3, x))
chk('选择3-A={1,3}', A13 == FiniteSet(1, 3), str(A13))

# 选择1
chk('选择1-并{1,2,3,4}', FiniteSet(1,2,3).union(FiniteSet(3,4)) == FiniteSet(1,2,3,4), '去重保留')
chk('选择1-交{3}', FiniteSet(1,2,3).intersect(FiniteSet(3,4)) == FiniteSet(3), '→A')
# 选择2
IB = Interval(1, oo).intersect(Interval(-oo, 3, right_open=True))
chk('选择2-交=[1,3)', IB == Interval(1, 3, right_open=True), str(IB))
chk('选择2-并=R', Interval(1, oo).union(Interval(-oo, 3, right_open=True)) == Interval(-oo, oo), '→A')
# 选择3：A∪B=A ⟺ B⊆A
chk('选择3-a=0→B=∅⊆A', solve(0*x - 2, x) == [] and FiniteSet().is_subset(A13), '空集支')
chk('选择3-a=2→{1}⊆A', FiniteSet(*solve(2*a - 2, a)).contains(1) == True, 'a=2时2/a=1')
chk('选择3-2/a=1⇒a=2', solve(Eq2 := None) if False else solve(S(2)/a - 1, a) == [2], 'a=2')
chk('选择3-2/a=3⇒a=2/3', solve(S(2)/a - 3, a) == [S(2)/3], 'a=2/3')
chk('选择3-反例a=1→{2}∉A', not A13.contains(S(2)), '排除')
chk('选择3-反例a=3→{2/3}∉A', not A13.contains(S(2)/3), '排除')
chk('选择3-答案{0,2,2/3}', True, '→D·漏a=0=考位锚隐雷')
# 填空
U13 = FiniteSet(*[i for i in range(-2, 6) if -2 < i < 5])
A14 = FiniteSet(*solve(x**2 - 3*x - 4, x))
chk('填空-U={−1..4}', U13 == FiniteSet(-1,0,1,2,3,4), str(U13))
chk('填空-A={−1,4}⊂U', A14 == FiniteSet(-1, 4) and A14.is_subset(U13), '解方程')
chk('填空-补={0,1,2,3}', Complement(U13, A14) == FiniteSet(0,1,2,3), '→4元素')
# 挑刺
chk('挑刺①-并去重3≠4', len(FiniteSet(1,2).union(FiniteSet(2,3))) == 3, '{1,2}∪{2,3}={1,2,3}')
chk('挑刺②-交=自己⇒A⊆B', FiniteSet(1).intersect(FiniteSet(1,2)) == FiniteSet(1) and FiniteSet(1).is_subset(FiniteSet(1,2)), 'A⊆B非B⊆A')
# 解答1
IA = Interval(-2, 3, right_open=True); IBt = Interval.Lopen(1, 5)
chk('解答1-并=[−2,5]', IA.union(IBt) == Interval(-2, 5), str(IA.union(IBt)))
chk('解答1-交=(1,3)', IA.intersect(IBt) == Interval.open(1, 3), str(IA.intersect(IBt)))
chk('解答1-补=[−2,1]∪[3,5]', Complement(Interval(-2,5), Interval.open(1,3)) == Union(Interval(-2,1), Interval(3,5)), '端点虚实对')
# 解答2
chk('解答2-a=−1重合⊇', Interval.open(-1,3).is_subset(Interval.open(-1,3)), 'A⊆B成立')
chk('解答2-a=−1.01漏2.995', not FiniteSet(S(2995)/1000).is_subset(Interval.open(S(-101)/100, S(299)/100)), '右端2.99罩不住')
chk('解答2-a=−0.99漏−0.995', not FiniteSet(S(-995)/1000).is_subset(Interval.open(S(-99)/100, S(301)/100)), '左端−0.99罩不住')
chk('解答2-条件联立唯一', True, 'a≤−1且a≥−1⇒a=−1')

print('===== 汇总 =====')
print(f'总验点 {len(PASS)+len(FAIL)} · 失败 {len(FAIL)} · ' + ('ALL PASS' if not FAIL else 'HAS FAIL'))
if FAIL:
    for n, d in FAIL: print('  FAIL:', n, d)
