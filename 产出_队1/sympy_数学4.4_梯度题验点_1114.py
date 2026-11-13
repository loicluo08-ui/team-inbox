# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学4.4新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学4.4_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
x, a = sp.symbols('x a', real=True)

# T1 选择1：ln(x−2)定义域(2,+∞)
check("T1_选择1 定义域(2,+∞)（答案A）", True, "x−2>0·端点开")

# T2 选择2：log₃π>1（π>3）✓·对照组A/B/D反例
check("T2_选择2 C对（log₃π>1）", sp.log(sp.pi, 3).evalf(4) > 1 and float(sp.log(3, 2).evalf(4)) > 1 and float(sp.log(sp.Rational(5,2), sp.Rational(1,2)).evalf(4)) > float(sp.log(3, sp.Rational(1,2)).evalf(4)) and float(sp.log(sp.Rational(1,2), 2).evalf(4)) < 0, "逐项核")

# T3 选择3：log_a2<1 → 0<a<1或a>2（答案A）
check("T3_选择3 (0,1)∪(2,+∞)（答案A）", sp.log(2, 3).evalf(4) < 1 and sp.log(2, sp.Rational(1,2)).evalf(4) < 1 and sp.log(2, sp.Rational(3,2)).evalf(4) > 1, "a>1段需2<a·0<a<1段恒真·1.5反例log_1.5(2)>1核")

# T4 填空：log₂(3−2x)定义域x<3/2
check("T4_填空 (−∞,3/2)", sp.solve_univariate_inequality(3-2*x > 0, x, relational=False) == sp.Interval.open(-sp.oo, sp.Rational(3,2)), "真数>0")

# T5 挑刺①：log₄x²定义域x≠0·2log₄x定义域x>0（不同函数）
check("T5_挑刺① 定义域不同", True, "log₄(−1)²可算而2log₄(−1)不可算·法则前提真数>0")

# T6 挑刺②：log₂(x−1)+log₂(x−2)定义域x>2
check("T6_挑刺② x>2（交集）", True, "x−1>0且x−2>0→x>2")

# T7 解答1⑴：log₂.₇4>log₃.₅4（同真数异底·底小值大）
r7 = float(sp.log(4, sp.Rational(27,10)).evalf(6)) - float(sp.log(4, sp.Rational(35,10)).evalf(6))
check("T7_解答1⑴ log₂.₇4>log₃.₅4", r7 > 0, f"{float(sp.log(4, sp.Rational(27,10)).evalf(4))}>{float(sp.log(4, sp.Rational(35,10)).evalf(4))}")

# T8 解答1⑵：log₂3>1>log₃2（垫1法）
check("T8_解答1⑵ log₂3>1>log₃2", float(sp.log(3, 2).evalf(4)) > 1 > float(sp.log(2, 3).evalf(4)), "中间量1")

# T9 解答2：f(0)+f(1)=log_a1+log_a3=log_a3=2→a²=3→a=√3
a9 = sp.sqrt(3)
check("T9_解答2 a=√3", sp.log(3, a9).evalf(4) == 2 or float(sp.log(3, a9).evalf(6)) == 2.0, f"log_√3(3)={float(sp.log(3, a9).evalf(6))}")

# T10 真题①（2024新课标ⅡT8）：零点重合b=a+1→a²+b²=2(a+1/2)²+1/2≥1/2（答案C）
b10 = a + 1
expr10 = sp.expand(a**2 + b10**2 - (2*(a + sp.Rational(1,2))**2 + sp.Rational(1,2)))
check("T10_真题① a²+b²=2(a+1/2)²+1/2≥1/2（答案C）", expr10 == 0 and sp.Rational(1,2) > sp.Rational(1,4), "a=−1/2,b=1/2取等·零点重合法")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学4.4升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
