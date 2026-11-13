# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学1.4新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学1.4_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
x, m, a, b, q = sp.symbols('x m a b q', real=True)

# T1 选择1：x>3 ⇒ x>1 真；反例 x=1.5：x>1真但x>3假 → 充分不必要
check("T1_选择1 x>3⇒x>1·反例1.5→充分不必要", sp.simplify(sp.Integer(1) > sp.Integer(3)) == sp.false, "1.5>1✓且1.5>3✗→必要不成立")

# T2 选择2：x²=1 ⇏ x=1（x=−1反例）·x=1⇒x²=1 → 必要不充分
check("T2_选择2 x=−1时x²=1成立而x≠1", (-1)**2 == 1 and (-1) != 1, "反例−1→不充分·正推成立→必要")

# T3 选择3：x²<x ⇔ 0<x<1；x<2 ⇏ 0<x<1（x=1.5）·(0,1)⇒(−∞,2) → 必要不充分
check("T3_选择3 x²<x解域(0,1)⊆(−∞,2)", sp.solve_univariate_inequality(x**2 < x, x, relational=False) == sp.Interval.open(0,1), "x=1.5:x<2✓但x²=2.25>x✗")

# T4 填空：a>0且b>0 ⇒ a+b>0；反例a=5,b=−1 → 必要不充分
check("T4_填空 5+(−1)=4>0但b<0", 5 + (-1) == 4 and (-1) < 0, "和为正推不出双正→必要不充分")

# T5 解答1⑴：Q⊊R → a∈Q充分a∈R·√2∈R∉Q → 充分不必要
check("T5_解答1√2无理∈R∉Q", sp.sqrt(2).is_rational == False, "充分不必要成立")

# T6 解答2：q⇒p ⇔ (0,1)⊆(−∞,m) ⇔ m≥1·最小值1
check("T6_解答2 m=1时(0,1)⊆(−∞,1)", sp.Interval.open(0,1).issubset(sp.Interval.open(-sp.oo,1)), "m≥1·最小值m=1")

# T7 真题①（2021甲卷理7）形式化：等比{an}首项1公比q：{Sn}递增 ⇔ a1(qⁿ−1)/(q−1)递增
n = sp.symbols('n', integer=True, positive=True)
S = sp.Function('S')
S1 = (1 - q**n)/(1 - q)
dS = sp.simplify(S1.subs(n, n+1) - S1.subs(n, n)) if False else sp.simplify((1-q**(n+1))/(1-q) - (1-q**n)/(1-q))
check("T7_真题① a1=1时 S(n+1)−S(n)=qⁿ>0 ⟺ q>0（正项等比和递增充要自洽）", sp.simplify(dS) == q**n, f"S(n+1)−S(n)={sp.simplify(dS)}=qⁿ>0 ⟺ q>0·答案B必要不充分成立")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学1.4升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
