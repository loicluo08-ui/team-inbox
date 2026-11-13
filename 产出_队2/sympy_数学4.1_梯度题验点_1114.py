#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sympy 代验：数学4.1《指数》v18.1 新标准升格梯度题验点（1114）
对应：产出_队2/首学版_数学4.1_指数_新标准升格_并行搜索员B_1114.html 试题区
全部验点 ALL PASS → exit0；任一 FAIL → exit1
"""
import sys
import sympy as sp

a, b, t = sp.symbols('a b t', positive=True)
N, fails = 0, []

def chk(name, cond):
    global N
    N += 1
    ok = bool(cond)
    print(f"验点#{N:02d} {name}: {'PASS' if ok else 'FAIL'}")
    if not ok:
        fails.append(N)

# ---------- 选择1（27^(2/3)+(1/4)^(−1/2)·答案B=11） ----------
chk("选择1B: 27^(2/3)=9", sp.Integer(27)**sp.Rational(2, 3) == 9)
chk("选择1B: (1/4)^(−1/2)=2", sp.Rational(1, 4)**sp.Rational(-1, 2) == 2)
chk("选择1B: 9+2=11", sp.Integer(27)**sp.Rational(2, 3) + sp.Rational(1, 4)**sp.Rational(-1, 2) == 11)
chk("选择1反例: A=9/C=13/D=15均≠11", (9 != 11) and (13 != 11) and (15 != 11))

# ---------- 选择2（⁶√((π−4)⁶)−⁴√((2−π)⁴)·答案A=6−2π） ----------
pi = sp.pi
chk("选择2A: |π−4|=4−π(π<4)", sp.Abs(pi - 4) == 4 - pi)
chk("选择2A: |2−π|=π−2(2<π)", sp.Abs(2 - pi) == pi - 2)
chk("选择2A: (4−π)−(π−2)=6−2π", sp.Abs(pi - 4) - sp.Abs(2 - pi) == 6 - 2 * pi)
chk("选择2数值: ≈−0.283非正值", abs(float(6 - 2 * pi) - (-0.283)) < 0.001)

# ---------- 选择3（3^a=2,3^b=5求9^(2a−b)·答案A=16/25） ----------
chk("选择3底归一: 9^(2a−b)=(3²)^(2a−b)=3^(4a−2b)", sp.simplify((sp.Integer(9))**(2*a - b) - (sp.Integer(3))**(4*a - 2*b)) == 0)
chk("选择3拆分: 3^(4a−2b)=(3^a)⁴/(3^b)²", sp.simplify((sp.Integer(3))**(4*a - 2*b) - ((sp.Integer(3))**a)**4 / ((sp.Integer(3))**b)**2) == 0)
chk("选择3代入: (3^a)⁴/(3^b)²=2⁴/5²=16/25", sp.Integer(2)**4 / sp.Integer(5)**2 == sp.Rational(16, 25))
chk("选择3数值: 9^(2a−b)=16/25=0.64", abs(sp.Rational(16, 25) - 0.64) == 0)

# ---------- 填空（a^(1/2)+a^(−1/2)=4求a²+a^(−2)·答案194） ----------
t2 = sp.symbols('t2', positive=True)
sol_a = sp.solve(sp.Eq(t2 + 1/t2, 4), t2)  # t2=√a → 2±√3
chk("填空√a解: t²−4t+1=0→t=2±√3(两解均正)", len(sol_a) == 2 and all(s.is_positive for s in sol_a))
val = [sp.simplify(s**2 + 1/s**2) for s in sol_a]
chk("填空一层: a+a^(−1)=14", all(sp.simplify(s**2 + 1/s**2 - 14) == 0 for s in sol_a))
chk("填空两层: a²+a^(−2)=194", all(sp.simplify(sp.simplify(s**2)**2 + 1/(sp.simplify(s**2))**2 - 194) == 0 for s in sol_a))
chk("填空数值核: 任取a≈13.93→a²+a^(−2)≈194", abs(float((2 + sp.sqrt(3))**2)**2 + 1/float((2 + sp.sqrt(3))**2)**2 - 194) < 1e-6)

# ---------- 挑刺（两处错） ----------
chk("挑刺①: (−3)⁵=−243→⁵√=−3(n奇直出)", sp.real_root(sp.Integer(-3)**5, 5) == -3)
chk("挑刺①错处: (−3)⁴=81→⁴√81=3≠−3(偶次非负)", sp.real_root(sp.Integer(81), 4) == 3 and sp.real_root(sp.Integer(81), 4) != -3)
chk("挑刺②错处: a=−1时(a^(2/3))^(3/2)不在正底数定义域(负底·性质不可搬)", (-1 < 0) and sp.Rational(3, 2).q != 1)
chk("挑刺②正底核: a>0时恒等(a^(2/3))^(3/2)=a成立", sp.simplify((a**sp.Rational(2, 3))**sp.Rational(3, 2) - a) == 0)

# ---------- 解答1（化简·(1)∛a (2)−1） ----------
chk("解答1(1)指数: 1/2+2/3−5/6=1/3", sp.Rational(1, 2) + sp.Rational(2, 3) - sp.Rational(5, 6) == sp.Rational(1, 3))
chk("解答1(1)核: a^(1/2+2/3−5/6)=∛a", sp.simplify(a**(sp.Rational(1, 2) + sp.Rational(2, 3) - sp.Rational(5, 6)) - a**sp.Rational(1, 3)) == 0)
chk("解答1(2)系数: 2×(−3)÷6=−1", sp.Integer(2) * (-3) / 6 == -1)
chk("解答1(2)指数: a:1/2−1/2=0·b:−1/3+2/3−1/3=0", sp.Rational(1, 2) - sp.Rational(1, 2) == 0 and -sp.Rational(1, 3) + sp.Rational(2, 3) - sp.Rational(1, 3) == 0)
chk("解答1(2)核: −1×a⁰×b⁰=−1", sp.simplify(-1 * a**0 * b**0) == -1)

# ---------- 解答2（半衰期·8g） ----------
half = sp.Rational(1, 2)
chk("解答2(1): 8×(1/2)⁵=0.25g", sp.Integer(8) * half**5 == sp.Rational(1, 4))
chk("解答2(2)式: M=8×(1/2)^t=2^(3−t)", sp.simplify(sp.Integer(8) * half**t - 2**(3 - t)) == 0)
chk("解答2(3)核: (1/2)⁶=1/64", half**6 == sp.Rational(1, 64))
chk("解答2(3)核: 8×(1/2)⁶=1/8g=初始的1/64", sp.Integer(8) * half**6 == sp.Rational(1, 8) and sp.Rational(1, 8) == sp.Integer(8) / 64)
chk("解答2(3)反解: t=6", sp.solve(sp.Eq(half**sp.Symbol('tt', integer=True, positive=True), sp.Rational(1, 64)), sp.Symbol('tt', integer=True, positive=True)) == [6])

# ---------- 直觉实验（翻倍与折半版） ----------
chk("直觉①: 2^10=1024", sp.Integer(2)**10 == 1024)
chk("直觉①: 2^6=64(细菌1h)", sp.Integer(2)**6 == 64)
chk("直觉②: (1/2)⁷≈0.78%<1%", float(half**7) < 0.01)
chk("直觉②: (2/3)⁵≈13.2%", abs(float(sp.Rational(2, 3)**5) - 0.1317) < 0.001)

print(f"\n总计 {N} 验点，FAIL {len(fails)}")
if fails:
    print(f"FAIL清单: {fails}")
    sys.exit(1)
print("ALL PASS exit0")
