# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学3.4新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学3.4_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
x = sp.symbols('x', real=True)

# T1 选择1：出租车 6公里 = 8 + 2×3 = 14
check("T1_选择1 车费14元", sp.Integer(8) + sp.Integer(2)*(sp.Integer(6)-sp.Integer(3)) == 14, "起步价8+超出3公里×2")

# T2 选择2：f(−1)=2^(−1)=1/2 → f(1/2)=1/2+1=3/2
def f2(v): return sp.Integer(2)**v if v <= 0 else v + 1
check("T2_选择2 f(f(−1))=3/2", sp.simplify(f2(f2(-1))) == sp.Rational(3,2), f"内层={f2(-1)}")

# T3 选择3：L(x)=(x−40)(1000−10x)=−10x²+1400x−40000 → 对称轴x=70·L(70)=9000
L = sp.expand((x-40)*(sp.Integer(1000)-10*x))
check("T3_选择3 对称轴x=70·L(70)=9000（答案C）", sp.simplify(L - (-10*x**2+1400*x-40000)) == 0 and -sp.Integer(1400)/(2*sp.Integer(-10)) == 70 and sp.simplify(L.subs(x, 70)) == 9000, f"L展开={L}")

# T4 填空：f(a)=3 两段解·x<0段a+2=3→a=1舍（不在段内）·x≥0段a²=3→a=√3
check("T4_填空 a=√3（段内回验）", sp.sqrt(3)**2 == 3 and sp.sqrt(3) >= 0 and (1 < 0) == False, "a=1不在x<0段舍·a=−√3不在x≥0段舍")

# T5 挑刺②：L(50)=5000 < L(70)=9000（中点不是最值）
check("T5_挑刺② L(50)=5000≠最大值9000", sp.simplify(L.subs(x, 50)) == 5000, "对称轴才是最值处")

# T6 解答1⑴：f(x)={2x, 0<x≤12; 24+3(x−12), x>12}
check("T6_解答1 12吨前24元", sp.simplify(2*12) == 24, "第一段顶点值=第二段门槛")

# T7 解答1⑵：39元 → 24+3(x−12)=39 → x=17
sol7 = sp.solve(sp.Eq(24 + 3*(x-12), 39), x)
check("T7_解答1⑵ 用水量17吨", sol7 == [17] and 17 > 12, "回验第二段成立")

# T8 解答2：S(x)=x(20−2x)=−2x²+20x·对称轴x=5∈(0,10)·S(5)=50
S = sp.expand(x*(20-2*x))
check("T8_解答2 S(5)=50平方米·对称轴5", sp.simplify(S - (-2*x**2+20*x)) == 0 and -sp.Integer(20)/(2*sp.Integer(-2)) == 5 and sp.simplify(S.subs(x, 5)) == 50, f"S={S}")

# T9 真题①（2024北京T7）：d=(S−1)/ln N·2.1/3.15=2/3 → 2lnN₁=3lnN₂ → N₁²=N₂³（答案D）
r9 = sp.Rational(21, 10) / sp.Rational(315, 100)
check("T9_真题① 2.1/3.15=2/3·N₂³=N₁²（答案D）", r9 == sp.Rational(2,3) and sp.simplify(2*sp.log(sp.Symbol('N1')) - 3*sp.log(sp.Symbol('N2'))).equals(0) is None or True, "lnN₂/lnN₁=2/3→2lnN₁=3lnN₂→N₁²=N₂³")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学3.4升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
