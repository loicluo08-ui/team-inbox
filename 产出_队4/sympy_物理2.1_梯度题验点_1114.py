# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理2.1升格·闸3 sympy机器代验（v2.3工序七·57条#9）
# 结果留痕sympy_物理2.1_梯度题验点_1114.txt
import sympy as sp

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择2：计数点1到6=5个间隔·5×0.1=0.5 s
check("T1_选择2 5×0.1=0.5s", 5 * sp.Rational(1, 10) == sp.Rational(1, 2), "间隔数=点数−1")

# T2 选择3：位移差恒定16-12=20-16=24-20=4mm；第3段v=0.020/0.1=0.2（C错证2.0）
d = [sp.Integer(16) - 12, sp.Integer(20) - 16, sp.Integer(24) - 20]
r2c = sp.Rational(20, 1000) / sp.Rational(1, 10)
check("T2_选择3 差恒4mm·第3段0.2m/s", d == [4, 4, 4] and r2c == sp.Rational(1, 5), f"差={d}·v₃={r2c}")

# T3 填空：65/3.6=18.0555→18.06（两位小数）
r3 = sp.Rational(65, 1) / sp.Rational(36, 10)
check("T3_填空 65/3.6≈18.06", abs(float(r3) - 18.0556) < 0.001, f"65/3.6={float(r3):.6f}")

# T4 解答1：v_N=(3.2+3.8)cm/0.2s=0.070/0.2=0.35 m/s
r4 = sp.Rational(70, 1000) / sp.Rational(2, 10)
check("T4_解答1 0.070/0.2=0.35", r4 == sp.Rational(7, 20) and float(r4) == 0.35, f"v_N={r4}")

# T5 解答2：Δv=3/3.6≈0.833·a=0.833/2≈0.42
r5a = sp.Rational(3, 1) / sp.Rational(36, 10)
r5b = r5a / 2
check("T5_解答2 Δv=5/6·a≈0.42", r5a == sp.Rational(5, 6) and abs(float(r5b) - 0.42) < 0.005, f"Δv={r5a}·a={float(r5b):.4f}")

# T6 真题甲卷：a=2k=2×68=136 cm/s²（池行自洽复核）
r6 = 2 * sp.Integer(68)
check("T6_甲卷 a=2k=136", r6 == 136, "k=68.0 cm/s²")

# T7 既有账复跑维持：54/3.6=15·86/3.6=215/9≈23.89（自测③）·5/18≈0.28·6/18≈0.33（列车表）
r7a = sp.Rational(54, 36, ); r7a = sp.Rational(54, 1) / sp.Rational(36, 10)
r7b = sp.Rational(86, 1) / sp.Rational(36, 10)
check("T7_既有账 15·23.89复跑", r7a == 15 and r7b == sp.Rational(215, 9), f"54→{r7a}·86→{float(r7b):.4f}")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理2.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
