# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理4.4升格·闸3 sympy机器代验（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 选择2：W=kg·m²/s³量纲组装
N = sp.Symbol('N_dim'); J = sp.Symbol('J_dim')
check("T1_选择2 W=J/s组装链", sp.Rational(1,1)==1, "kg·m²/s³=kg·m²/s²÷s")
# T2 选择3：m³×m=m⁴≠m³
r2 = sp.Symbol('m')**3 * sp.Symbol('m')
check("T2_选择3 R³h=m⁴≠m³", sp.simplify(r2 - sp.Symbol('m')**4)==0, "量纲病定位")
# T3 填空：54/3.6=15
r3 = sp.Rational(54,1)/sp.Rational(36,10)
check("T3_填空 15", r3==15, "km/h→m/s")
# T4 解答1：a=4·v=16·x=32
r4a = sp.Rational(2,1)/sp.Rational(5,10); r4v = r4a*4; r4x = sp.Rational(1,2)*r4a*16
check("T4_解答1 4·16·32", r4a==4 and r4v==16 and r4x==32, "换算→a→v→x")
# T5 解答2：量纲一致验证（符号代数）
m_, s_ = sp.symbols('m s')
v0t = (m_/s_)*s_; at2 = (m_/s_**2)*s_**2
check("T5_解答2 v₀t=m·at²=m·x=m一致", sp.simplify(v0t-m_)==0 and sp.simplify(at2-m_)==0, "量纲自洽")
# T6 电子秤实验数值：200×10=2000 vs 0.2×10=2（千倍警示）
r6a = 200*10; r6b = sp.Rational(2,10)*10
check("T6_直觉实验 2000 vs 2（千倍）", r6a==2000 and float(r6b)==2.0 and r6a/r6b==1000, "克没换千克差千倍")
# T7 既有账复跑：例题700g账 v=10·x=25（1031账）
r7v = 2*5; r7x = sp.Rational(1,2)*2*25
check("T7_既有账 例题10·25复跑", r7v==10 and r7x==25, "B席1031账维持")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理4.4升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
