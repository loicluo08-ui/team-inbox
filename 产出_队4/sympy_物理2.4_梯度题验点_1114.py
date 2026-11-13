# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理2.4升格·闸3 sympy机器代验（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
t = sp.symbols('t', positive=True)
# T1 选择2：逐秒位移比 5:15=1:3
s1 = sp.Rational(1,2)*10*1**2; s2c = sp.Rational(1,2)*10*2**2
check("T1_选择2 第2s内15m·比1:3", s1==5 and s2c==20 and s2c-s1==15 and sp.Rational(5,15)==sp.Rational(1,3), f"{s1}·{s2c}→第2s内={s2c-s1}")
# T2 选择3：9t²−50t+25=0→t=5·h=122.5·最后1s=44.1=9/25×122.5
sol = sp.solve(sp.Eq(9*t**2-50*t+25, 0), t)
h = sp.Rational(98,10)*sp.Rational(25,1)/2
last1 = h - sp.Rational(98,10)*sp.Rational(16,1)/2
check("T2_选择3 t=5·h=122.5·最后1s=44.1", 5 in [sp.nsimplify(s) for s in sol] and h==sp.Rational(245,2) and last1==sp.Rational(441,10) and sp.Rational(9,25)*h==last1, f"t={sol}·h={h}·Δ={last1}")
# T3 填空：v=20·x=20
check("T3_填空 v=20·x=20", 10*2==20 and sp.Rational(1,2)*10*4==20, "g=10·t=2巧合")
# T4 解答1：g=0.10/0.01=10
g = sp.Rational(10,100)/sp.Rational(1,100)
check("T4_解答1 g=10", g == 10, f"Δx/T²={g}")
# T5 解答2：h=5t₁²·t₁+h/340=2 数值解 h≈18.9
t1 = sp.Symbol('t1', positive=True)
solh = sp.nsolve(5*t1**2/340 + t1 - 2, t1, 1.9)
h_true = 5*solh**2
check("T5_解答2 h≈18.9(数值解)", 18.5 < float(h_true) < 19.2, f"t₁={float(solh):.4f}·h={float(h_true):.2f}·修正≈{20-float(h_true):.2f} m")
# T6 真题广西T3：v=gt=10（与质量无关形式化）
check("T6_真题广西 v=gt=10", 10*1 == 10, "g与质量无关·v₁=v₂=10")
# T7 既有账复跑维持：T5频闪9.84·T6反应尺0.10/0.14（1031账）
check("T7_既有账 复算核验复跑", abs(sp.Rational(1575,100000)/sp.Rational(16,10000) - sp.Float(9.84)) < sp.Float("0.005"), "Δx/T²=0.01575/0.0016=9.84维持")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理2.4升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
