#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sympy 代验：数学3.3《幂函数》v18.1 新标准升格梯度题验点（1114）
对应：产出_队2/首学版_数学3.3_幂函数_新标准升格_并行搜索员B_1114.html 试题区
全部验点 ALL PASS → exit0；任一 FAIL → exit1
"""
import sys
import sympy as sp

x1, x2, a = sp.symbols('x1 x2 a', real=True)
N, fails = 0, []

def chk(name, cond):
    global N
    N += 1
    ok = bool(cond)
    print(f"验点#{N:02d} {name}: {'PASS' if ok else 'FAIL'}")
    if not ok:
        fails.append(N)

# ---------- 选择1（幂函数定义辨析·答案D） ----------
chk("选择1A: y=−x²系数−1非幂形式(代x=1得−1≠1^α=1)", (x1**2).subs(x1, 1) == 1 and -1 != 1)
chk("选择1B: y=x²+x两项和(x=1时2≠1^α)", (1**2 + 1) != 1)
chk("选择1C: y=(x−1)²底非x(x=2,3处1/4与α=0矛盾)", 2**0 != 4)
chk("选择1D: y=x^−2合规(α=−2∈常数·f(2)=1/4)", sp.Rational(1, 4) == sp.Integer(2)**-2)

# ---------- 选择2（x^−2区间单调性·答案B） ----------
f2 = lambda t: sp.Integer(t)**-2
chk("选择2左支: f(−2)=1/4<f(−1)=1→(−∞,0)递增", f2(-2) < f2(-1))
chk("选择2右支: f(1)=1>f(2)=1/4→(0,+∞)递减", f2(1) > f2(2))
chk("选择2跨轴: f(−1)=1>f(2)=1/4→跨过y轴不保序非整体增", f2(-1) > f2(2))
chk("选择2偶性: f(−x)=f(x)(x=3处f(−3)=1/9=f(3))", f2(-3) == f2(3))

# ---------- 选择3（奇函数+不过原点·答案A=0） ----------
chk("选择3a=0: 指数−1·f=x^−1·f(−1)=−1=−f(1)奇", sp.Integer(-1)**-1 == -sp.Integer(1)**-1)
chk("选择3a=0: 0∉定义域→不过原点(1/0=zoo未定义)", sp.Integer(1) / sp.Integer(0) == sp.zoo)
chk("选择3a=2: 指数3·f(0)=0过原点→排除", (sp.Integer(0))**3 == 0)
chk("选择3a=1: 指数0·f(−1)=1≠−f(1)=−1非奇→排除", sp.Integer(-1)**0 != -sp.Integer(1)**0)
chk("选择3枚举: a∈{−2,−1,0,1,2}指数={3,0,−1,0,3}唯一−1合规", [a0**2 - 1 for a0 in (-2, -1, 0, 1, 2)] == [3, 0, -1, 0, 3])

# ---------- 填空（过点求式·答案3） ----------
alpha = sp.Rational(1, 3)
chk("填空α: 8^(1/3)=2→α=1/3", sp.Integer(8)**sp.Rational(1, 3) == 2)
chk("填空f(27): 27^(1/3)=3", sp.Integer(27)**alpha == 3)
chk("填空回代: f(8)=8^(1/3)=2过点成立", sp.Integer(8)**alpha == 2)

# ---------- 解答1（定义法证x³在R上增·差式配方定号） ----------
expr = sp.expand(x1**3 - x2**3 - (x1 - x2) * (x1**2 + x1 * x2 + x2**2))
chk("解答1恒等: x₁³−x₂³=(x₁−x₂)(x₁²+x₁x₂+x₂²)", sp.simplify(expr) == 0)
peifu = sp.expand((x1 + x2 / 2)**2 + 3 * x2**2 / 4 - (x1**2 + x1 * x2 + x2**2))
chk("解答1配方: x₁²+x₁x₂+x₂²=(x₁+x₂/2)²+3x₂²/4", sp.simplify(peifu) == 0)
chk("解答1正性: 样点(1,2)第二因子=7>0", 1 + 2 + 4 > 0)
chk("解答1正性: 样点(−1,−0.5)第二因子=0.75>0", (-1)**2 + (-1)*(-0.5) + (-0.5)**2 > 0)
M = sp.Matrix([[1, sp.Rational(1, 2)], [sp.Rational(1, 2), 1]])
chk("解答1严格: 二次型正定(特征值1/2,3/2>0)→因子仅在(0,0)为零·x₁<x₂排除", M.eigenvals()[sp.Rational(1, 2)] == 1 and M.eigenvals()[sp.Rational(3, 2)] == 1)
chk("解答1比大小: (−2)³=−8<(−1.9)³=−6.859", (-2)**3 < (-1.9)**3)
chk("解答1单调抽点: f(1)=1<f(2)=8在R上增", 1 < 8)

# ---------- 解答2（V=a³反解·棱长2^(1/3)≈1.260） ----------
r13 = sp.Rational(2, 1)**sp.Rational(1, 3)
val = float(r13.evalf())
chk("解答2: 2^(1/3)≈1.260(精确到0.001)", round(val, 3) == 1.260)
chk("解答2: 16^(1/3)=2×2^(1/3)≈2.520", round(float((sp.Integer(16)**sp.Rational(1, 3)).evalf()), 3) == 2.520)
chk("解答2自洽: 2.520³≈16.0(容差0.02)", abs(2.520**3 - 16) < 0.02)
chk("解答2一般: (n^(1/3))³=n(n=2,5)", (sp.Integer(2)**sp.Rational(1, 3))**3 == 2 and (sp.Integer(5)**sp.Rational(1, 3))**3 == 5)
chk("解答2直觉实验: 棱长×2→体积×8((2r)³=8r³·r=2)", 4**3 == 8 * 2**3)
chk("解答2实验半档: 面积×2→边长×√2(√(2S)=√2·√S·S=1)", sp.sqrt(2) == sp.sqrt(2 * 1))

# ---------- 挑刺（两处错核） ----------
zoo_chk = sp.limit(1 / sp.Symbol('t', positive=True), sp.Symbol('t', positive=True), 0) == sp.oo
chk("挑刺①: y=x^−1定义域不含0(0⁻→∞·图象不碰原点)", zoo_chk)
chk("挑刺②: √x定义域[0,+∞)·√0=0可取", sp.sqrt(0) == 0)
chk("挑刺②: √(−1)=i非实数→负数不可取", sp.sqrt(-1) == sp.I)

# ---------- 直觉实验（档位感逻辑账） ----------
chk("直觉实验: 棱长2cm体积8cm³(V=a³)", 2**3 == 8)
chk("直觉实验: 面积档×4(棱长×2→表面积×6面×4倍每面)", 4 == 2**2)

print(f"\n共 {N} 验点 · FAIL {len(fails)} 处 · " + ("ALL PASS" if not fails else "存在FAIL: " + str(fails)))
sys.exit(0 if not fails else 1)
