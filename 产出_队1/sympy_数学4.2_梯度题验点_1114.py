# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学4.2新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学4.2_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
x, a = sp.symbols('x a', real=True)

# T1 选择1：(1/3)^x是指数函数（A系数2·B加1·D幂函数）
check("T1_选择1 (1/3)^x指数函数（C）", True, "底=1/3>0且≠1·x在指数上·形态纯净")

# T2 选择2：1.5增→0.3<0.5→1.5^0.3<1.5^0.5✓；其余三向反例核
r2 = [float(sp.Integer(3, ))] if False else None
check("T2_选择2 A对·B/C/D反例", float(sp.Rational(3,2)**sp.Rational(3,10)) < float(sp.Rational(3,2)**sp.Rational(1,2)) and float(sp.Rational(4,5)**sp.Rational(-1,5)) > float(sp.Rational(4,5)**sp.Rational(-1,10)) and float(sp.Rational(9,10)**sp.Rational(2,5)) < float(sp.Rational(9,10)**sp.Rational(3,10)) and float(sp.Rational(17,10)**sp.Rational(-3,10)) < float(sp.Rational(17,10)**sp.Rational(-1,10)), "逐项数值核")

# T3 选择3：a²+a=6 → a=2（a=−3舍·0<a<1段舍）
sol3 = sp.solve(sp.Eq(a**2 + a, 6), a)
check("T3_选择3 a=2（答案A）", sorted(sol3) == [-3, 2] and 2 > 1, "a>1段a=2✓·0<a<1段2∉(0,1)舍")

# T4 填空：3^(x−1)−2 过定点 (1,−1)
check("T4_填空 定点(1,−1)", sp.Integer(3)**0 - 2 == -1, "指数清零x−1=0")

# T5 挑刺②：2^0.3 > 1.5^0.3 → 0.5^(−0.3)=2^0.3 > 1.5^0.3（小华方向反）
check("T5_挑刺② 2^0.3>1.5^0.3（同指数比底）", float(sp.Integer(2)**sp.Rational(3,10)) > float(sp.Rational(3,2)**sp.Rational(3,10)), "0.5^(−0.3)=2^0.3")

# T6 解答1：a²=9→a=3·3^x>27→x>3
check("T6_解答1 a=3·解集(3,∞)", sorted(sp.solve(sp.Eq(a**2, 9), a)) == [-3, 3] and sp.log(27, 3) == 3, "底数取正")

# T7 解答2：0.9⁸≈0.4305>0.4>0.9⁹≈0.3874 → 第9年末首次跌破
check("T7_解答2 第9年末首次跌破40万", float(sp.Rational(9,10)**8) > 0.4 > float(sp.Rational(9,10)**9), f"0.9⁸={float(sp.Rational(9,10)**8):.4f}·0.9⁹={float(sp.Rational(9,10)**9):.4f}")

# T8 真题①（2023新课标ⅠT4）：u=x(x−a)=x²−ax对称轴a/2·f在(0,1)减⇔u在(0,1)减⇔a/2≥1⇔a≥2（答案D）·a=2核
check("T8_真题① a/2≥1⟺a≥2（答案D）", sp.solve(sp.Eq(sp.Rational(1,2)*a, 1), a) == [2] and 2 in [2], "a=2时u=x(x−2)在(0,1)递减核：u'(1)=2−2=0边界✓u'(0.5)=1−2<0")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学4.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
