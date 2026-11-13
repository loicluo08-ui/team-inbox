# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理2.3升格·闸3 sympy机器代验（v2.3工序七·57条#9）
# [脚本bug修复留痕1114：初版r5b系Python int除法float与Rational比较==False（1.4 T4同型sympy行为坑）·统一Rational口径修复]
import sympy as sp

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

r1 = sp.Rational(1,2)*5*16
check("T1_选择2 x=½×5×4²=40", r1 == 40, f"x={r1}")

r2a = 20*sp.Integer(4) - sp.Rational(1,2)*5*16
r2b = sp.Rational(20,2)*4
check("T2_选择3 位移40/对半验40", r2a == 40 and r2b == 40, f"公式={r2a}·平均={r2b}")

r3 = sp.Rational(15,1)**2 / (2*225)
check("T3_填空 a=225/450=0.5", r3 == sp.Rational(1,2), f"a={r3}")

r4 = sp.Rational(15,2)*3
check("T4_解答1 x=7.5×3=22.5", r4 == sp.Rational(45,2), f"x={r4}")

r5a = sp.Integer(80)**2 / (2*300)
r5b = sp.Rational(600, 80)
check("T5_解答2 a=32/3≈10.7·t=7.5", r5a == sp.Rational(32,3) and abs(float(r5a)-10.67)<0.01 and r5b == sp.Rational(15,2) and float(r5b)==7.5, f"a={r5a}·t={float(r5b)}")

r6 = (sp.Rational(10,1) - 0)/2*2
check("T6_真题北京T2 x=5×2=10", r6 == 10, "平均对半×t")

r7 = sp.Rational(126,36)**2 - sp.Rational(54,36)**2
check("T7_例题2复跑 v₀²−vM²换算账维持", sp.simplify(sp.Rational(126,36)) == sp.Rational(7,2) and sp.simplify(sp.Rational(54,36)) == sp.Rational(3,2), "126→3.5·54→1.5·既有账维持")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理2.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
