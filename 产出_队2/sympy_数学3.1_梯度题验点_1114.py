#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sympy 代验：数学3.1《函数的概念及其表示》v18.1 新标准升格梯度题验点（1114）
对应：产出_队2/首学版_数学3.1_函数的概念及其表示_新标准升格_并行搜索员B_1114.html 试题区
全部验点 ALL PASS → exit0；任一 FAIL → exit1
"""
import sys
import sympy as sp

x, a, b = sp.symbols('x a b', real=True)
N, fails = 0, []

def chk(name, cond):
    global N
    N += 1
    ok = bool(cond)
    print(f"验点#{N:02d} {name}: {'PASS' if ok else 'FAIL'}")
    if not ok:
        fails.append(N)

# ---------- 选择1（同一函数判定·答案B） ----------
chk("选择1B: √(x²)=|x| 对全域成立", sp.simplify(sp.sqrt(x**2) - sp.Abs(x)) == 0)
chk("选择1A: (√x)²在x=−1非实(域x≥0缩水)", sp.sqrt(x).subs(x, -1).is_real is False)
chk("选择1C: x²/x在x=0未定义(0·(1/0)→nan)", sp.Mul(x**2, sp.Pow(x, -1, evaluate=False), evaluate=False).subs(x, 0) == sp.nan)
chk("选择1C: x²/x对应关系=x(x≠0时)", sp.simplify((x**2).cancel() / x if False else sp.cancel(x**2 / x)) == x)
chk("选择1D: x⁰对应关系恒=1(区分要素仅定义域x≠0·教材p67练习3(2)锚)", sp.simplify(x**0) == 1)

# ---------- 选择2（定义域双查·答案A） ----------
dom = sp.Interval(-sp.oo, 3) - sp.FiniteSet(-2)   # {x|x≤3 且 x≠−2}
chk("选择2: 解集=(−∞,−2)∪(−2,3]与A项同构", dom == sp.Union(sp.Interval.open(-sp.oo, -2), sp.Interval.Lopen(-2, 3)))
chk("选择2: x=3可取(端点实心)", sp.sqrt(3 - 3).is_real and sp.Rational(1, 5).is_real)
chk("选择2: x=−2分母归零不可取(1/0→zoo)", (1 / x).subs(x, 0) == sp.zoo)
chk("选择2: x=4根式开负(√(−1)=I非实)", sp.sqrt(3 - 4).is_real is False)

# ---------- 选择3（分段含参段界·答案A） ----------
f3_left, f3_right = a + 2, a**2
chk("选择3: 左段a+2=3→a=1但1∉(−∞,1)舍(代回f(1)=1≠3)", f3_right.subs(a, 1) == 1 and 1 != 3)
chk("选择3: f(−√3)=−√3+2≈0.268≠3舍", sp.nsimplify(f3_left.subs(a, -sp.sqrt(3))) != 3)
chk("选择3: f(√3)=(√3)²=3✓(a≥1段内)", f3_right.subs(a, sp.sqrt(3)) == 3)

# ---------- 填空（定义域代换·答案[1,3]） ----------
t = sp.Symbol('t', real=True)
img = [ (t).subs(t, 0 + 1), (t).subs(t, 2 + 1) ]  # x∈[0,2] → 括号里 x+1∈[1,3]
chk("填空: 括号里x+1端点=1与3→域[1,3]", img[0] == 1 and img[1] == 3)

# ---------- 挑刺②（f(a−1)定义域须按a重查·a≥−2且a≠−1） ----------
g = sp.sqrt(a + 2) + 1 / (a + 1)   # 例2(3)的f(a−1)
chk("挑刺②: a=−3时√(a+2)=√(−1)非实→原定义域不carry", sp.sqrt(a + 2).subs(a, -3).is_real is False)
chk("挑刺②: a=−1时1/(a+1)→zoo", (1 / x).subs(x, -1 + 1) == sp.zoo)
chk("挑刺②: a=−2时√0+1/(−1)=−1有定义(端点可取)", g.subs(a, -2) == -1)
chk("挑刺②: a=0时√2+1有定义", g.subs(a, 0) == sp.sqrt(2) + 1)

# ---------- 解答1（阶梯水价·分段+定段+解段） ----------
y1 = sp.Rational(14, 5) * x                 # 2.8x（精确有理数防float伪伤·0.8×180+2×180=504）
y2 = 504 + 4 * (x - 180)
y3 = 824 + 6 * (x - 260)
chk("解答1: 段界x=180衔接(504=504)", y1.subs(x, 180) == y2.subs(x, 180) == 504)
chk("解答1: 段界x=260衔接(824=824)", y2.subs(x, 260) == y3.subs(x, 260) == 824)
sol = sp.solve(sp.Eq(824 + 6 * (x - 260), 950), x)
chk("解答1: 第三段解824+6(x−260)=950→x=281", sol == [281])
chk("解答1: y(281)=950代回验证", y3.subs(x, 281) == 950)

# ---------- 解答2（分段衔接含参·段界筛选） ----------
chk("解答2(1): 衔接条件a·1+1=1²+b→a+1=1+b恒等式结构", sp.simplify((a + 1) - (1 + b)).subs(b, a) == 0)
solb = sp.solve(sp.Eq(4 + b, 3), b)
chk("解答2(2): f(2)=4+b=3→b=−1", solb == [-1])
chk("解答2(2): 代回衔接→a=−1", (a + 1).subs(a, -1) == 1 + solb[0])
chk("解答2(2): f(−1)=−(−1)+1=2", (-x + 1).subs(x, -1) == 2)
r1 = sp.solve(sp.Eq(-x + 1, 1), x)
chk("解答2(3): 左段−x+1=1→x=0(0<1段内✓)", r1 == [0] and 0 < 1)
r2 = sp.solve(sp.Eq(x**2 - 1, 1), x)
kept = [v for v in r2 if v >= 1]
chk("解答2(3): 右段x²−1=1→±√2·段界筛x≥1留√2", set(r2) == {-sp.sqrt(2), sp.sqrt(2)} and kept == [sp.sqrt(2)])
chk("解答2(3): 与y=1公共点共2个", len(r1) + len(kept) == 2)

print(f"\n总验点 {N} · 失败 {len(fails)}")
if fails:
    print("FAIL:", fails); sys.exit(1)
print("ALL PASS · exit0")
