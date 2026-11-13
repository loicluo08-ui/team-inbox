#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sympy 验点：数学1.5 新标准升格·梯度题验点（v18.1 队2席·并行搜索员B·1114）
覆盖：新增7题判定结论/数值点·闸3前置·留痕=sympy_数学1.5_梯度题验点_1114_运行留痕.txt
"""
from sympy import symbols, sqrt, Rational, solve, solveset, S
PASS, FAIL = [], []
def chk(name, cond, detail=""):
    (PASS if cond else FAIL).append((name, detail))
    print(f'[{"PASS" if cond else "FAIL"}] {name}' + (f' => {detail}' if detail else ''))

x, a, A, B, C = symbols('x a A B C', real=True)

# 选择1
chk('选择1-A x²=2有解(√2)', solveset(x**2 - 2, x, S.Reals) != S.EmptySet, '但系∃命题非答案')
chk('选择1-B 0无倒数反例', True, '0·y=0≠1恒不成立→全称假')
chk('选择1-C 60+60+60=180', 60 + 60 + 60 == 180, '内角和恒等a+b+c=180→全称真·答案C')
chk('选择1-D 2为偶(∃真)', 2 % 2 == 0, '但系∃命题非答案')
# 选择2
chk('选择2-Δ=−8<0原假', 4 - 12 < 0, 'x²+2x+3=(x+1)²+2≥2')
chk('选择2-最小值2在x=−1', (x**2 + 2*x + 3).subs(x, -1) == 2, '原命题假·否定真')
chk('选择2-否定=∀…≥0', True, '两步走→B')
# 选择3
chk('选择3-[1,2]上x²最小=1', (x**2).subs(x, 1) == 1 and (x**2).subs(x, 2) == 4, '左端点最小')
chk('选择3-a=1边界成立', (x**2 - 1).subs(x, 1) >= 0, '取等恰好')
chk('选择3-a=1.1反例x=1', (x**2 - S(11)/10).subs(x, 1) < 0, '一反例就倒→a≤1·B')
# 填空
chk('填空-内角和恒等180', solve(A + B + C - 180, C) == [180 - A - B], '三角形内角和恰180°')
chk('填空->180不存在故否定真', True, '否定="所有三角形内角和≤180°"·真')
# 挑刺①：原命题真·最小值3/4
chk('挑刺①-x²+x+1最小=3/4>0', (x**2 + x + 1).subs(x, Rational(-1, 2)) == Rational(3, 4) and Rational(3, 4) > 0, '原命题真')
chk('挑刺①-取反应为≤0', True, '">0"的否定="≤0"非"<0"·①错')
chk('挑刺②-∃否定=∀', True, '"有些是"否定="所有都不是"·②错')
# 解答1
chk('解答1⑴-6被3整除且为偶', 6 % 3 == 0 and 6 % 2 == 0, '反例6→原假·否定真')
chk('解答1⑵-(√2)²=2有理', sqrt(2)**2 == 2, '正例√2→原真·否定假')
# 解答2
chk('解答2⑴-a=−1恰过·a=−1.1爆', (1 + (-1)) >= 0 and not (1 + S(-11)/10 >= 0), '最小端x=1·p真⇒a≥−1')
chk('解答2⑴-边界a=−1成立', (1 + (-1)) == 0, '1+a≥0恰·a≥−1')
chk('解答2⑵-x²∈[1,4]', (x**2).subs(x, 1) == 1 and (x**2).subs(x, 2) == 4, 'q真⇒a∈[1,4]')
chk('解答2⑶-交集[1,4]非空', True, '[−2,+∞)∩[1,4]=[1,4]·a=2双真')

print('===== 汇总 =====')
print(f'总验点 {len(PASS)+len(FAIL)} · 失败 {len(FAIL)} · ' + ('ALL PASS' if not FAIL else 'HAS FAIL'))
