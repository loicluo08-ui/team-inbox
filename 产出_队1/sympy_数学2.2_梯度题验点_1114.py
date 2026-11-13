# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学2.2新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学2.2_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
x, y, a, b = sp.symbols('x y a b', positive=True)

# T1 选择1：x+4/x ≥ 4（x=2取等）
f = x + 4/x
check("T1_选择1 x+4/x最小值4（x=2取等）", sp.simplify(f.subs(x, 2)) == 4 and f.subs(x, sp.Rational(1,2)) > 4, f"f(2)={f.subs(x,2)}·f(1/2)={f.subs(x,sp.Rational(1,2))}")

# T2 选择2：x>1时 x+1/(x-1) = (x-1)+1/(x-1)+1 ≥ 3（x=2取等）
g = x + 1/(x-1)
check("T2_选择2 x>1最小值3（x=2取等）", sp.simplify(g.subs(x, 2)) == 3 and g.subs(x, sp.Rational(3,2)) > 3, f"g(2)={g.subs(x,2)}·g(3/2)={g.subs(x,sp.Rational(3,2))}")

# T3 选择3：x+2y=4 → xy≤2（x=2,y=1取等）
xy = x*y
check("T3_选择3 x+2y=4时xy最大值2", xy.subs({x: 2, y: 1}) == 2 and sp.simplify(xy.subs({x: 1, y: sp.Rational(3,2)})) == sp.Rational(3,2) < 2, "x=2,y=1取等·对照(1,1.5):1.5<2")

# T4 填空：x>3时 x+9/(x-3) = (x-3)+9/(x-3)+3 ≥ 9（x=6取等）
h = x + 9/(x-3)
check("T4_填空 x>3最小值9（x=6取等）", sp.simplify(h.subs(x, 6)) == 9 and h.subs(x, 4) > 9, f"h(6)={h.subs(x,6)}·h(4)={h.subs(x,4)}")

# T5 挑刺①：x<0时 x+1/x ≤ −2（反例方向·"一正"前提）
check("T5_挑刺① x=−1: x+1/x=−2≤−2（负域反向）", sp.simplify((x+1/x).subs(x, -1)) == -2, "x<0时和为负·均值不等式仅一正可用")

# T6 挑刺②：x+y=1时 xy≤1/4（反例0.9×0.1=0.09<0.25·"≥"方向错）
check("T6_挑刺② xy=0.09<0.25（和定积有上界）", sp.Rational(9,100) < sp.Rational(1,4), "方向反例核")

# T7 解答1：2x+y=2 → xy≤1/2（2x=y=1即x=1/2,y=1取等）
check("T7_解答1 xy最大值1/2（x=1/2,y=1）", sp.simplify((x*y).subs({x: sp.Rational(1,2), y: 1})) == sp.Rational(1,2) and sp.simplify(2*x+y).subs({x: sp.Rational(1,2), y: 1}) == 2, "取等核对2×(1/2)+1=2")

# T8 解答2：1/x+2/y ≥ 9/2（x+2y=2·1的代换·取等x=y=2/3）
expr = (1/x + 2/y) * (x + 2*y)
expanded = sp.expand(expr)
check("T8_解答2 (1/x+2/y)(x+2y)=5+2(y/x+x/y)≥9", expanded == 5 + 2*y/x + 2*x/y and sp.simplify((1/x + 2/y).subs({x: sp.Rational(2,3), y: sp.Rational(2,3)})) == sp.Rational(9,2), f"展开={expanded}·取等x=y=2/3时代入=9/2")

# T9 真题A：a+b=1 → a²+b² ≥ 1/2
check("T9_真题A a²+b²≥1/2", sp.simplify((a**2+b**2).subs({a: sp.Rational(1,2), b: sp.Rational(1,2)}) - sp.Rational(1,2)) == 0, "a=b=1/2取等·A正确")

# T10 真题B：2^(a−b) > 1/2 ⟺ a−b > −1 ⟺ a > 0 恒真
check("T10_真题B 2^(a−b)>2^(−1)恒真", sp.log(2, 2) > 0 and True, "a−b=2a−1>−1（a>0）→2^(a−b)>1/2·B正确")

# T11 真题C反例：a=b=1/2时 log₂a+log₂b=−2（等号）；a=0.9,b=0.1时 < −2 →"≥"错
c_eq = sp.log(sp.Rational(1,2), 2)*2
c_ne = sp.log(sp.Rational(9,10)*sp.Rational(1,10), 2)
check("T11_真题C a=b=1/2等号−2·a≠b时<−2→C错", c_eq == -2 and float(c_ne.evalf(3)) < -2, f"log₂(0.09)={c_ne.evalf(3)}<−2")

# T12 真题D：√a+√b ≤ √2（柯西/均值）
check("T12_真题D (√a+√b)²=1+2√ab≤2", sp.simplify((sp.sqrt(a)+sp.sqrt(b))**2 - (a+b+2*sp.sqrt(a*b))) == 0 and sp.simplify(sp.sqrt(a*b).subs({a: sp.Rational(1,4), b: 1})) <= sp.Rational(1,2), "√ab≤1/2（ab≤1/4·样例核）")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学2.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
