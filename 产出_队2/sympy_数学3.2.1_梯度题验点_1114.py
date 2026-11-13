#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sympy 代验：数学3.2.1《单调性与最大（小）值》v18.1 新标准升格梯度题验点（1114）
对应：产出_队2/首学版_数学3.2.1_单调性与最大小值_新标准升格_并行搜索员B_1114.html 试题区
全部验点 ALL PASS → exit0；任一 FAIL → exit1
"""
import sys
import sympy as sp

x, y, a = sp.symbols('x y a', real=True)
N, fails = 0, []

def chk(name, cond):
    global N
    N += 1
    ok = bool(cond)
    print(f"验点#{N:02d} {name}: {'PASS' if ok else 'FAIL'}")
    if not ok:
        fails.append(N)

# ---------- 选择1（增函数判定·答案A） ----------
chk("选择1A: y=3x−2保序(1<2且f(1)<f(2))", 3 * 2 - 2 > 3 * 1 - 2)
f_b = lambda t: 1 / t
chk("选择1B: x=−1<1但f(−1)=−1<f(1)=1→定义域上不递减", f_b(-1) < f_b(1))
f_c = lambda t: t + 1 / t
chk("选择1C: x=0.5<1但f(0.5)>f(1)→(0,1)递减非递增", f_c(sp.Rational(1, 2)) > f_c(1))
chk("选择1C: x=0.5<3但f(0.5)<f(3)→(0,+∞)上非递减", f_c(sp.Rational(1, 2)) < f_c(3))
chk("选择1D: x=−1<0但f(−1)=1>f(0)=0→非递增", (x**2).subs(x, -1) > (x**2).subs(x, 0))

# ---------- 选择2（单调区间·答案B） ----------
vx = sp.solve(sp.Eq(sp.diff(x**2 - 2 * x - 3, x), 0), x)
chk("选择2: 对称轴x=1(开口向上→[1,+∞)递增)", vx == [1])
chk("选择2: f(0)=−3>f(1)=−4(左段递减佐证)", (x**2 - 2*x - 3).subs(x, 0) > (x**2 - 2*x - 3).subs(x, 1))
zeros = sp.solve(sp.Eq(x**2 - 2 * x - 3, 0), x)
chk("选择2: C项[−1,3]系函数值≤0的区间(零点−1,3)", set(zeros) == {-1, 3})

# ---------- 选择3（含参单调·答案A） ----------
sol = sp.solve_univariate_inequality(-a / 2 <= 1, a, relational=False)
chk("选择3: 对称轴不越右端−a/2≤1→a≥−2", sol == sp.Interval(-2, sp.oo))
g = lambda t, av: t**2 + av * t + 3
chk("选择3: a=−2临界对称轴=1·f(1)<f(2)<f(3)保序", g(1, -2) < g(2, -2) < g(3, -2))
chk("选择3: a=−3反例对称轴1.5·f(1)>f(1.25)→递增破产", g(1, -3) > g(sp.Rational(5, 4), -3))

# ---------- 填空（二次最值·答案1） ----------
f4 = -x**2 + 4 * x - 3
vx4 = sp.solve(sp.Eq(sp.diff(f4, x), 0), x)
chk("填空: 顶点x=2∈[0,3]段内", vx4 == [2] and 0 <= 2 <= 3)
chk("填空: f(2)=1>max(f(0)=−3,f(3)=0)", f4.subs(x, 2) == 1 and f4.subs(x, 2) > max(f4.subs(x, 0), f4.subs(x, 3)))

# ---------- 解答1（定义法证明x+4/x在[2,+∞)递增·最小值4） ----------
x1, x2 = sp.symbols('x1 x2', real=True, positive=True)
diff_expr = sp.simplify((x1 + 4 / x1) - (x2 + 4 / x2))
chk("解答1: 差式=(x₁−x₂)(x₁x₂−4)/(x₁x₂)因子化", sp.simplify(diff_expr - (x1 - x2) * (x1 * x2 - 4) / (x1 * x2)) == 0)
chk("解答1: x₁=2,x₂=3差<0→f(2)<f(3)", (2 + 2) - (3 + sp.Rational(4, 3)) < 0)
chk("解答1: x₁=3,x₂=4差<0→f(3)<f(4)", (3 + sp.Rational(4, 3)) - (4 + 1) < 0)
chk("解答1: x₁≥2,x₂>x₁→x₁x₂>4严格(x₁=2,x₂=2.1→4.2)", sp.Rational(21, 10) * 2 > 4)
chk("解答1: 最小值f(2)=4", 2 + sp.Rational(4, 2) == 4)

# ---------- 解答2（抽象减函数·答案[0,3/4)） ----------
I1 = sp.solve(sp.And(-2 <= 1 - x, 1 - x <= 2), x, rel=False) if False else sp.Interval(-1, 3)
I2 = sp.Interval(0, sp.Rational(4, 3))
I3 = sp.Interval.open(-sp.oo, sp.Rational(3, 4))
inter = I1.intersect(I2).intersect(I3)
chk("解答2: 三条件交集=[0,3/4)", inter == sp.Interval.Ropen(0, sp.Rational(3, 4)))
eq = sp.solve(sp.Eq(1 - x, 3 * x - 2), x)
chk("解答2: x=3/4时两括号相等(严格<不成立→端点开)", eq == [sp.Rational(3, 4)])
chk("解答2: x=0边界可取(1∈[−2,2]·−2∈[−2,2]·1>−2)", -2 <= 1 - 0 <= 2 and -2 <= -2 <= 2 and 1 > -2)

# ---------- 挑刺（两处错） ----------
chk("挑刺①: x=−1<1但f(−1)<f(1)→1/x定义域上不递减", f_b(-1) < f_b(1))
f5 = 2 / (x - 1)
chk("挑刺②: f(2)=2系最大值非最小值", f5.subs(x, 2) == 2)
chk("挑刺②: f(6)=0.4系最小值(递减端点定最值)", f5.subs(x, 6) == sp.Rational(2, 5) and sp.Rational(2, 5) < 2)

print(f"\n总验点 {N} · 失败 {len(fails)}")
if fails:
    print("FAIL:", fails); sys.exit(1)
print("ALL PASS · exit0")
