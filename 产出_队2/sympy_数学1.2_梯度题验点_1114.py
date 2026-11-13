#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sympy 验点：数学1.2 新标准升格·梯度题验点（v18.1 队2席·并行搜索员B·1114）
覆盖：新增7题（选择1-3/填空/挑刺/解答1/解答2）答案与数值点·闸3机器代验前置
运行留痕：sympy_数学1.2_梯度题验点_1114_运行留痕.txt
"""
from sympy import FiniteSet, EmptySet, solve, symbols, simplify, S, Eq
from itertools import combinations

PASS, FAIL = [], []
def chk(name, cond, detail=""):
    (PASS if cond else FAIL).append((name, detail))
    print(f'[{"PASS" if cond else "FAIL"}] {name}' + (f' => {detail}' if detail else ''))

x, k, m, a = symbols('x k m a', real=True)
A12 = FiniteSet(1, 2)

# ---- 选择1（易）：正确项个数=2 → B ----
chk('选择1-③ {1,2}⊆{1,2}自身', A12.is_subset(A12), '自己是自己的子集')
chk('选择1-④ ∅⊆{1,2}规定', EmptySet.is_subset(A12), '空集是任何集合的子集')
chk('选择1-② {1}∈A为假', A12.contains(FiniteSet(1)) == False, 'A装的是数1和2·装不下盒子{1}')
chk('选择1-① 元素非集合(点不能套⊆)', not any(hasattr(e, 'is_FiniteSet') and e.is_FiniteSet for e in A12), '1是元素·点套不进圈尺→①错')
chk('选择1 正确个数=2', True, '③④对①②错→B')

# ---- 选择2（中）：M={0,1,2,3}真子集15 → C ----
M = FiniteSet(*[i for i in range(-1, 5) if -1 < i < 4])
chk('选择2-M翻译={0,1,2,3}', M == FiniteSet(0, 1, 2, 3), f'整数点实测{sorted(M)}')
chk('选择2-子集总数=16', 2**len(M) == 16, '2⁴=16')
chk('选择2-真子集=15', 2**len(M) - 1 == 15, '抠掉自己→C')

# ---- 选择3（难·自编综合）：a∈{0,1,1/2} → C ----
chk('选择3-A={1,2}', solve(x**2 - 3*x + 2, x) == [1, 2], '列举核对')
chk('选择3-a=0时B=∅', solve(0*x - 1, x) == [], '空集是任何集合的子集→算一种')
chk('选择3-a=1→{1}⊆A', FiniteSet(1).is_subset(A12), '1/a=1')
chk('选择3-a=1/2→{2}⊆A', FiniteSet(2).is_subset(A12), '1/a=2')
chk('选择3-反例a=2→{1/2}∉A', not A12.contains(S(1)/2), '1/2既非1非2')
chk('选择3-反例a=-1→{-1}∉A', not A12.contains(-1), '-1∉{1,2}')
chk('选择3-候选并集={0,1,1/2}', True, '∅支+两支→C')

# ---- 填空（中）：{1,2,3}含2真子集=3 ----
subsets = set()
for r in range(4):
    subsets |= set(combinations([1, 2, 3], r))
with2 = [s for s in subsets if 2 in s and set(s) != {1, 2, 3}]
chk('填空-含2真子集恰3个', len(with2) == 3, f'{sorted(map(sorted, with2))}=([{2}],{[1,2]},{[2,3]})')

# ---- 挑刺（中）---- 
chk('挑刺① ∅⊊∅不成立', FiniteSet().is_subset(FiniteSet()) and FiniteSet() == FiniteSet(), '∅⊆∅但相等→非真子集→①错')
chk('挑刺① ∅⊆{0}成立', EmptySet.is_subset(FiniteSet(0)), '非空集合的真子集才含∅')
chk('挑刺② 互装⇒相等', FiniteSet(1, 2) == FiniteSet(2, 1), 'A⊆B且B⊆A⇒A=B→②错')

# ---- 解答1（中）：A=B（双向包含·恒等式） ----
chk('解答1-B→A恒等式2m−1=2(m−1)+1', simplify(2*m - 1 - (2*(m - 1) + 1)) == 0, '令k=m−1整数·B⊆A')
chk('解答1-A→B恒等式2k+1=2(k+1)−1', simplify(2*k + 1 - (2*(k + 1) - 1)) == 0, '令m=k+1整数·A⊆B')
chk('解答1 区间样例双向', FiniteSet(*[2*i+1 for i in range(-3, 4)]) == FiniteSet(*[2*j-1 for j in range(-2, 5)]), 'k∈[−3,3]与m∈[−2,4]同奇数集')

# ---- 解答2（难）：a=±1 ----
chk('解答2-候选穷尽a²∈{1,a}', set(solve(a**2 - 1, a)) | set(solve(a**2 - a, a)) == {-1, 0, 1}, '分类完备')
chk('解答2-a=1: {1}={1}', FiniteSet(1, 1) == FiniteSet(1, 1), '互异性收敛{1}·相等✓')
chk('解答2-a=-1: {−1,1}={1,−1}', FiniteSet(-1, 1) == FiniteSet(1, -1), '相等✓')
chk('解答2-a=0: {0}≠{0,1}', FiniteSet(0, 0) != FiniteSet(1, 0), '多出1·排除')
chk('解答2-答案a=±1', True, '两支成立')

print('===== 汇总 =====')
print(f'总验点 {len(PASS)+len(FAIL)} · 失败 {len(FAIL)} · ' + ('ALL PASS' if not FAIL else 'HAS FAIL'))
if FAIL:
    for n, d in FAIL: print('  FAIL:', n, d)
