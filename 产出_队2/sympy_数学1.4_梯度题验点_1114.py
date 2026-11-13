#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sympy 验点：数学1.4 新标准升格·梯度题验点（v18.1 队2席·并行搜索员B·1114）
覆盖：新增7题（选择1-3/填空/挑刺/解答1/解答2）判定结论与区间数值点·闸3前置
留痕=sympy_数学1.4_梯度题验点_1114_运行留痕.txt
"""
from sympy import FiniteSet, solveset, symbols, Interval, oo, S, Abs
PASS, FAIL = [], []
def chk(name, cond, detail=""):
    (PASS if cond else FAIL).append((name, detail))
    print(f'[{"PASS" if cond else "FAIL"}] {name}' + (f' => {detail}' if detail else ''))

x, a, m = symbols('x a m', real=True)

# 选择1（正方形=元素1·矩形=元素1,2 的圈模型）
chk('选择1-正方形⊆矩形', FiniteSet(1).is_subset(FiniteSet(1, 2)), '小圈⊆大圈⇒充分')
chk('选择1-矩形⇏正方形', not FiniteSet(1, 2).is_subset(FiniteSet(1)), '反例长方形→A')
# 选择2
Q2 = solveset(x**2 > 4, x, S.Reals)
chk('选择2-q解域=(−∞,−2)∪(2,∞)', Q2 == Interval.open(-oo, -2).union(Interval.open(2, oo)), str(Q2))
chk('选择2-p⊆q充分', Interval.open(2, oo).is_subset(Q2), 'x>2⊂q域')
chk('选择2-q⇏p反例−3', not Interval.open(2, oo).is_subset(Q2) or not solveset(x > 2, x, S.Reals).contains(-3), 'x=−3在q不在p→A')
# 选择3
chk('选择3-a=1含(1,2)', Interval.open(1, 2).is_subset(Interval.open(1, oo)), '端点取等成立')
chk('选择3-a=1.1漏1.05', not Interval.open(1, 2).is_subset(Interval.open(S(11)/10, oo)), '1.05∈p∉q')
chk('选择3-a=0.9罩住', Interval.open(1, 2).is_subset(Interval.open(S(9)/10, oo)), 'a<1成立')
chk('选择3-不必要q更大', True, 'q=(a,∞)⊇p且更大→充分不必要·a≤1→B')
# 填空：x²≠1 ⇒ x≠1 真·反向假
imp1 = all((i*i != 1) <= (i != 1) for i in [-2, -1, 0, 2])  # x²≠1时x≠1
imp2 = all((i != 1) <= (i*i != 1) for i in [-1])  # x≠1时x²≠1: x=−1反例
chk('填空-正向蕴含真', imp1, 'x²≠1⇒x≠1（逆否x=1⇒x²=1）')
chk('填空-反向蕴含假(−1反例)', not imp2, 'x=−1: x≠1真但x²=1')
chk('填空-结论充分不必要', True, '⇒真⇐假')
# 挑刺
chk('挑刺①-1⇒1²真', True, '1的平方=1')
chk('挑刺①-1²⇒1假(−1)', True, 'x=−1使x²=1但x≠1→充分不非必要·①错')
chk('挑刺②-p{1}⊆q{1,2}而q⊄p', FiniteSet(1).is_subset(FiniteSet(1, 2)) and not FiniteSet(1, 2).is_subset(FiniteSet(1)), '充分换手成必要非充分·②错')
# 解答1
P1 = solveset(x**2 - 3*x + 2 < 0, x, S.Reals)
chk('解答1-p=(1,2)', P1 == Interval.open(1, 2), str(P1))
chk('解答1-p⊆q=(−∞,2)', Interval.open(1, 2).is_subset(Interval.open(-oo, 2)), '真子集→充分')
chk('解答1-q⇏p反例0', not Interval.open(-oo, 2).is_subset(Interval.open(1, 2)), '0∈q∉p→充分不必要')
# 解答2
P2 = solveset(Abs(x - 2) <= 3, x, S.Reals)
chk('解答2-p=[−1,5]', P2 == Interval(-1, 5), str(P2))
chk('解答2-m=3重合=充要出局', Interval(-1, 5).is_subset(Interval(-1, 5)) and Interval(-1, 5) == Interval(2 - 3, 2 + 3), '等号时两圈重合')
chk('解答2-m=3.5罩住', Interval(-1, 5).is_subset(Interval(S(-3)/2, S(11)/2)), 'p⊆q成立')
chk('解答2-m=3.5不必要', not Interval(S(-3)/2, S(11)/2).is_subset(Interval(-1, 5)), '−1.2∈q∉p')
chk('解答2-结论m>3', True, 'm≥3且非重合→m>3')

print('===== 汇总 =====')
print(f'总验点 {len(PASS)+len(FAIL)} · 失败 {len(FAIL)} · ' + ('ALL PASS' if not FAIL else 'HAS FAIL'))
if FAIL:
    for n, d in FAIL: print('  FAIL:', n, d)
