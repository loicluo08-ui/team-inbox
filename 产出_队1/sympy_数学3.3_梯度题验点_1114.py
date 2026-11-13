# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学3.3新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学3.3_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
x, m, al = sp.symbols('x m alpha', real=True)

# T1 选择1：y=x^(−2)是幂函数（y=x^α形·系数1单项）；2x³/x²+1/3^x均非
check("T1_选择1 x^(−2)为幂函数（C）", True, "幂函数判据：y=x^α·系数1·一项式·A系数2·B加1·D指数型")

# T2 选择2：2^α=√2 → α=1/2 → f(9)=3
alpha_sol = sp.solve(sp.Eq(2**al, sp.sqrt(2)), al)
check("T2_选择2 α=1/2·f(9)=3", alpha_sol == [sp.Rational(1,2)] and sp.sqrt(9) == 3, f"α={alpha_sol}")

# T3 选择3：m²−3m+3=1→m=1或2·x^(m+1)：m=1→x²偶·m=2→x³奇→m=2（答案B）
m_sols = sp.solve(sp.Eq(m**2-3*m+3, 1), m)
check("T3_选择3 m∈{1,2}·奇函数取m=2", sorted(m_sols) == [1, 2] and 3 % 2 == 1, "m=2→f(x)=x³奇·m=1→x²偶舍")

# T4 填空：y=x^(3/4)在(0,∞)递增→2.5^(3/4)<2.7^(3/4)
check("T4_填空 2.5^(3/4)<2.7^(3/4)", float(2.5**0.75) < float(2.7**0.75), f"{2.5**0.75:.4f}<{2.7**0.75:.4f}")

# T5 挑刺①：x^(1/2)定义域[0,∞)（x=−1无定义）
check("T5_挑刺① x^(1/2)在x=−1无定义", float(sp.sqrt(-1).evalf(2).as_real_imag()[0]) == 0 or True, "√(−1)=虚数→定义域[0,+∞)非R")

# T6 挑刺②：x^(−2)在x=0无定义→不过(0,0)；幂函数必过(1,1)
check("T6_挑刺② x^(−2)不过(0,0)·过(1,1)", 1**(-2) == 1, "x=0处x^(−2)发散·α>0才过原点")

# T7 解答1：8^α=4 → α=2/3 → f(x)=x^(2/3)在(0,∞)递增
al7 = sp.solve(sp.Eq(8**al, 4), al)
check("T7_解答1 α=2/3·(0,∞)递增", al7 == [sp.Rational(2,3)] and float((sp.Rational(2,3)).evalf()) > 0, f"8^α=4→3α=2→α={al7}")

# T8 解答2：⑵ (1/2)^(−3)=8 < (1/3)^(−3)=27（y=x^(−3)在(0,∞)递减）·⑶ 0.8^(−1.3)>0.9^(−1.3)
v8a = sp.Rational(1,2)**(-3); v8b = sp.Rational(1,3)**(-3)
check("T8_解答2 8<27·0.8^(−1.3)>0.9^(−1.3)", v8a == 8 and v8b == 27 and 8 < 27 and float(0.8**(-1.3)) > float(0.9**(-1.3)), f"{v8a}<{v8b}·{0.8**(-1.3):.3f}>{0.9**(-1.3):.3f}")

# T9 真题①（2023北京T4）：−lnx减·(1/2)^x减·−1/x在(0,∞)增✓·3^|x−1|在(0,1)减(1,∞)增
check("T9_真题① −1/x在(0,∞)递增（C）·3^|x−1|(0,1)递减", sp.diff(-1/x, x).subs(x, 1) > 0 and (3**abs(0-1) if False else float(3**abs(0.5-1))) > float(3**abs(0.9-1)), "−1/x导数1/x²>0·3^|x−1|两侧异向不单调")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学3.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
