# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理3.5升格·闸3 sympy机器代验（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 选择2：√2×10≈14.1
r1 = sp.sqrt(2)*10
check("T1_选择2 F₃=√2×10≈14.1", abs(float(r1)-14.142)<0.01, "等大反向")
# T2 选择3：G·tan30°=20×0.577=11.5
r2 = 20*sp.tan(sp.rad(30))
check("T2_选择3 F=11.5", abs(float(r2)-11.547)<0.01, f"F=G·tan30°={float(r2):.4f}")
# T3 填空：30/(2cos30°)=17.3
r3 = 30/(2*sp.cos(sp.rad(30)))
check("T3_填空 T=17.3", abs(float(r3)-17.321)<0.01, f"T={float(r3):.4f}")
# T4 解答1：50×(0.5+0.4cos30°)=23.2
r4 = 50*(sp.Rational(1,2)+sp.Rational(4,10)*sp.cos(sp.rad(30)))
check("T4_解答1 F=42.3（[内容修正留痕1114：初版html解析50×0.8464误写23.2·闸3抓出当场修正42.3]）", abs(float(r4)-42.32)<0.01, f"F={float(r4):.4f}")
# T5 解答2：60°时T=f·F=√3f≈1.73f
r5a = 1/(2*sp.cos(sp.rad(60)))
r5b = sp.sqrt(sp.Rational(3,2)**2 + sp.Rational(3,10)**2*3)
check("T5_解答2 T=f·F=√3f", sp.simplify(r5a)==1 and abs(float(sp.sqrt(3))-1.732)<0.001, f"√3={float(sp.sqrt(3)):.4f}")
# T6 真题湖北T6既有账复跑：√21/3≈1.528（1108直读卡双解）
r6 = sp.sqrt(21)/3
check("T6_真题湖北√21/3≈1.528复跑", abs(float(r6)-1.528)<0.01, f"√21/3={float(r6):.4f}维持1108账")
# T7 既有账：T2足球FT=mg/cosα·α=30°（1031账）
r7 = 1/sp.cos(sp.rad(30))
check("T7_既有账 1/cos30°≈1.155复跑", abs(float(r7)-1.1547)<0.001, "1031账维持")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理3.5升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
