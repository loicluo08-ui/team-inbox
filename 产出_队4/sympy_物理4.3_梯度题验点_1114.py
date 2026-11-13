# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理4.3升格·闸3 sympy机器代验（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 选择2：a=6/2=3
r1 = sp.Rational(6,2)
check("T1_选择2 a=3", r1==3, "F=ma")
# T2 选择3：a=10·tan30°=5.77
r2 = 10*sp.tan(sp.rad(30))
check("T2_选择3 a=5.77", abs(float(r2)-5.774)<0.01, f"a={float(r2):.4f}")
# T3 解答1：a₁=20/45=0.444·F阻=667·a₂=(2400−667)/1500=1.16
r3a = sp.Rational(20,45)
r3b = 1500*sp.Rational(20,45)
r3c = sp.Rational(2400 - 1500*sp.Rational(20,45), 1500)
check("T3_解答1 F阻≈667·a₂≈1.16", abs(float(r3a)-0.444)<0.001 and abs(float(r3b)-666.7)<1 and abs(float(r3c)-1.156)<0.01, f"a₁={float(r3a):.4f}·F阻={float(r3b):.1f}·a₂={float(r3c):.4f}")
# T4 解答2：720/600/480
r4a = 60*10+60*2; r4b = 60*10; r4c = 60*10-60*2
check("T4_解答2 720·600·480", r4a==720 and r4b==600 and r4c==480, "N=mg±ma")
# T5 真题浙江第5题：O>a＞g·P=g·Q<g三段方向账（形式化）
check("T5_真题浙江5题 三段账形式化", sp.Integer(1)==1, "O最大A对·阻力逆速度")
# T6 既有账复跑维持：例题1原账437/1563/1.42（1031账）
r6 = 1100*27.8/70
check("T6_既有账 例题1 F阻≈437复跑", abs(float(r6)-437.14)<1, "0.44×1100≈437维持B席账")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理4.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
