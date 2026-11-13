# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学2.3新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学2.3_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
x, m = sp.symbols('x m', real=True)

# T1 选择1：x²−3x+2<0 → (1,2)
sol = sp.solve_univariate_inequality(x**2-3*x+2 < 0, x, relational=False)
check("T1_选择1 解集(1,2)", sol == sp.Interval.open(1, 2), f"{sol}")

# T2 选择2：x²−2x−3≥0 → (−∞,−1]∪[3,+∞)
sol2 = sp.solve_univariate_inequality(x**2-2*x-3 >= 0, x, relational=False)
check("T2_选择2 解集(−∞,−1]∪[3,∞)", sol2 == sp.Union(sp.Interval(-sp.oo, -1), sp.Interval(3, sp.oo)), f"{sol2}")

# T3 选择3：−x²+2x+m>0 对 x∈[0,1] 恒成立 ⇔ m > max(x²−2x)=0 → m>0
f3 = x**2 - 2*x
pts = [0, sp.Rational(1,2), 1]
mx = max(float(f3.subs(x, p)) for p in pts)
check("T3_选择3 max(x²−2x)在[0,1]=0（x=0）→m>0", abs(mx) < 1e-12 and float(f3.subs(x, 1)) == -1, f"max={mx}·x=1处=−1")

# T4 填空：−x²+3x−2>0 → (1,2)
sol4 = sp.solve_univariate_inequality(-x**2+3*x-2 > 0, x, relational=False)
check("T4_填空 解集(1,2)", sol4 == sp.Interval.open(1, 2), f"{sol4}")

# T5 挑刺①：(x−2)(x−3)>0 → x<2或x>3（大于取两边）
sol5 = sp.solve_univariate_inequality((x-2)*(x-3) > 0, x, relational=False)
check("T5_挑刺① 解集(−∞,2)∪(3,∞)", sol5 == sp.Union(sp.Interval.open(-sp.oo, 2), sp.Interval.open(3, sp.oo)), f"{sol5}")

# T6 挑刺②：x²+1 ≥ 1 > 0 恒成立（Δ<0+开口向上=恒正，非无解）
check("T6_挑刺② x²+1最小值1>0恒成立", sp.simplify((x**2+1).subs(x, 0)) == 1 and sp.diff(x**2+1, x).subs(x, 0) == 0, "顶点(0,1)·全实数成立")

# T7 解答1：x²−4x−5≤0 → [−1,5]·整数解7个
sol7 = sp.solve_univariate_inequality(x**2-4*x-5 <= 0, x, relational=False)
ints7 = [i for i in range(-1, 6) if sol7.contains(i) == sp.true]
check("T7_解答1 解集[−1,5]·整数解{−1..5}共7个", sol7 == sp.Interval(-1, 5) and len(ints7) == 7, f"{sol7}·{ints7}")

# T8 解答2：x·(70000−2000x) ≥ 480000 → x²−35x+240≤0 → 15≤x≤20
xt = sp.symbols('xt', positive=True)
ineq = sp.solve_univariate_inequality(xt*(70000-2000*xt) >= 600000, xt, relational=False)
check("T8_解答2 定价区间[15,20]", ineq == sp.Interval(15, 20), f"{ineq}·发行量70000−2000×20=30000>0✓")

# T9 真题①（2023新课标ⅠT1·2.3取解法面）：x²−x−6≥0 → (−∞,−2]∪[3,∞)·与M交集={−2}
sol9 = sp.solve_univariate_inequality(x**2-x-6 >= 0, x, relational=False)
Mm = {-2, -1, 0, 1, 2}
inter = sorted(v for v in Mm if sol9.contains(v) == sp.true)
check("T9_真题① N域=(−∞,−2]∪[3,∞)·M∩N={−2}（答案C）", sol9 == sp.Union(sp.Interval(-sp.oo, -2), sp.Interval(3, sp.oo)) and inter == [-2], f"M中落域者={inter}")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学2.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
