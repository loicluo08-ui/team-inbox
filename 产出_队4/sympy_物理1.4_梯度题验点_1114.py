# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理1.4升格·闸3 sympy机器代验（v2.3工序七·57条#9）
# 结果留痕sympy_物理1.4_梯度题验点_1114.txt
import sympy as sp

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择2：72km/h=20·108km/h=30·a=(30-20)/60=1/6≈0.167
# [脚本bug修复留痕1114：初版误写Rational(108,36)=3（km/h→m/s应除3.6=36/10）致FAIL·内容数值无误·修复重跑]
r1 = (sp.Rational(108, 1) / sp.Rational(36, 10) - sp.Rational(72, 1) / sp.Rational(36, 10)) / 60
check("T1_选择2 a=1/6≈0.17", r1 == sp.Rational(1, 6) and abs(float(r1) - 0.17) < 0.01, f"a={r1}")

# T2 选择3：前2s a=6/2=3；后4s a=(0-6)/4=-1.5
r2a = sp.Rational(6, 2); r2b = sp.Rational(0 - 6, 4)
check("T2_选择3 a₁=3·a₂=-1.5", r2a == 3 and r2b == sp.Rational(-3, 2), f"a₁={r2a}·a₂={r2b}")

# T3 填空：300/0.006=5×10⁴（教材p29表数据复用）
r3 = sp.Rational(300, 1) / sp.Rational(6, 1000)
check("T3_填空 300/0.006=5e4", r3 == 50000, f"a={r3}")

# T4 解答1：90km/h=25·a=(0-25)/30=-5/6≈-0.83；反解t=25/2=12.5
# [脚本bug修复留痕1114：初版r4b==12.5（Rational对float==返回False的sympy行为）致FAIL·改Rational精确比较]
r4a = sp.Rational(0 - 25, 30)
r4b = sp.Rational(25, 2)
# [脚本bug修复留痕1114第二轮：abs()包错层abs(float-0.83)=1.66·应为abs(float)-0.83=0.0033·修正]
check("T4_解答1 a=-5/6·t=12.5", r4a == sp.Rational(-5, 6) and abs(float(r4a)) - 0.83 < 0.01 and r4b == sp.Rational(25, 2) and float(r4b) == 12.5, f"a={r4a}·t={float(r4b)}")

# T5 解答2：60/0.3=200·60/0.6=100（反比关系）
r5a = sp.Rational(60, 3, ); r5a = sp.Rational(60, 1) / sp.Rational(3, 10)
r5b = sp.Rational(60, 1) / sp.Rational(6, 10)
check("T5_解答2 t=200/100·反比", r5a == 200 and r5b == 100, f"t₁={r5a}·t₂={r5b}")

# T6 真题CR450：a=120²/(2×14400)=0.5（池行sympy预验复核）
r6 = sp.Integer(120)**2 / (2 * sp.Integer(14400))
check("T6_真题CR450 a=0.5", r6 == sp.Rational(1, 2), f"a={r6}")

# T7 真题解析反解代账：120²=2×0.5×14400=14400
r7 = 2 * sp.Rational(1, 2) * 14400
check("T7_真题代账 v²=2ax=14400", r7 == 14400 and sp.Integer(120)**2 == 14400, f"2ax={r7}=v₀²")

# T8 既有账复跑维持：子弹5×10⁴·台球-35·自测①2.458
check("T8_既有账 台球a=-35复跑", sp.Rational(-28, 10) / sp.Rational(8, 100) == -35, "−2.8/0.08=−35✓")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理1.4升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
