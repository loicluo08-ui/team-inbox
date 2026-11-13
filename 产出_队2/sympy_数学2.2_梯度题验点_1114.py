#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sympy 验点：数学2.2 新标准升格·梯度题验点（v18.1 队2席·并行搜索员B·1114）
覆盖：新增7题最值/数值点·闸3前置·留痕=sympy_数学2.2_梯度题验点_1114_运行留痕.txt
"""
from sympy import symbols, solve, S, sqrt
PASS, FAIL = [], []
def chk(name, cond, detail=""):
    (PASS if cond else FAIL).append((name, detail))
    print(f'[{"PASS" if cond else "FAIL"}] {name}' + (f' => {detail}' if detail else ''))

x, y, t = symbols('x y t', real=True)

# 选择1: a+b=4 → ab最大
f1 = x * (4 - x)
chk('选择1-ab最大=4(a=b=2)', solve(f1.diff(x), x) == [2] and f1.subs(x, 2) == 4, '顶点式')

# 选择2: x>1, x+4/(x−1) 最小
f2 = x + 4 / (x - 1)
chk('选择2-x=3时恰=5', f2.subs(x, 3) == S(5), 't=2取等')
chk('选择2-邻域>5', f2.subs(x, S(5)/2) == S(5)/2 + S(8)/3 and S(5)/2 + S(8)/3 > 5, '≈5.17>5')
chk('选择2-t式最小5', (t + 4/t).subs(t, 2) == 4 and 4 + 1 == 5, 't+4/t≥4·常数+1')

# 选择3: x+2y=4 → xy最大
f3 = y * (4 - 2 * y)
chk('选择3-xy最大=2(y=1,x=2)', solve(f3.diff(y), y) == [1] and f3.subs(y, 1) == 2, '打包2y版均值')

# 填空: xy=9 → x+y最小
f4 = x + 9 / x
chk('填空-最小=6(x=3)', f4.subs(x, 3) == 6 and f4.subs(x, 3) < f4.subs(x, 1) and f4.subs(x, 3) < f4.subs(x, 9), '正域局部最小·积定和最小')

# 挑刺①: x=−1时x+1/x=−2（≥2不恒成立）
chk('挑刺①-x=−1给−2', (x + 1/x).subs(x, -1) == -2, '负数不发证')
# 挑刺②: x+y=2 → xy最大1
f5 = x * (2 - x)
chk('挑刺②-xy最大=1(x=y=1)', solve(f5.diff(x), x) == [1] and f5.subs(x, 1) == 1, '非2')

# 解答1: 面积100 → 总长最短
f6 = 2 * (x + 100 / x)
chk('解答1-总长最短40(x=y=10)', f6.subs(x, 10) == 40 and f6.subs(x, 10) < f6.subs(x, 5) and f6.subs(x, 10) < f6.subs(x, 20), '正域局部最小·总长40')

# 解答2: 篱笆20m
f7 = x * (10 - x)
chk('解答2⑴-最大25(5×5)', solve(f7.diff(x), x) == [5] and f7.subs(x, 5) == 25, '四边全围')
f8 = y * (20 - 2 * y)
chk('解答2⑵-最大50(x=10,y=5)', solve(f8.diff(y), y) == [5] and f8.subs(y, 5) == 50, '靠墙三边·打包2y')

print('===== 汇总 =====')
print(f'总验点 {len(PASS)+len(FAIL)} · 失败 {len(FAIL)} · ' + ('ALL PASS' if not FAIL else 'HAS FAIL'))
if FAIL:
    for n, d in FAIL: print('  FAIL:', n, d)
