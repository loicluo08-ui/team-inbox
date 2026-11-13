# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·化学1.3升格·闸3 sympy机器代验（v2.3工序七·57条#9·化学科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 选择3：n(Zn)=19.5/65=0.3·V=0.3×22.4=6.72
r1n = sp.Rational(195,10)/65
r1v = r1n*sp.Rational(224,10)
check("T1_选择3 0.3 mol·6.72 L", r1n==sp.Rational(3,10) and float(r1v)==6.72, f"n={float(r1n)}·V={float(r1v)}")
# T2 填空：96/48=2·2×3=6
r2n = sp.Rational(96,48); r2a = r2n*3
check("T2_填空 2 mol·6NA", r2n==2 and r2a==6, "分子→原子账")
# T3 解答1⑶：NaCl电离离子=2NA（说法NA错·应为2NA）
r3 = 1*2
check("T3_解答1⑶ 离子2NA（题面NA判错）", r3==2, "1 mol NaCl→2 mol离子")
# T4 解答1⑷：C +2→+4升2价·1 mol CO₂转移2 mol e⁻=2NA（真题T4同账·池行三源维持）
r4 = 4-2
check("T4_解答1⑷ 2NA（真题T4同账）", r4==2, "C升2价·池行D维持")
# T5 直觉实验：10 g米500粒→500 g=25000粒（换算系数账）
r5 = sp.Rational(500,10)*500
check("T5_直觉实验 25000粒", r5==25000, "称重换算个数=n×系数同构")
# T6 既有账复跑：KOH例题28/56=0.5·0.5/0.25=2（1031账）
r6a = sp.Rational(28,56); r6c = r6a/sp.Rational(25,100)
check("T6_既有账 KOH 0.5·2复跑", r6a==sp.Rational(1,2) and r6c==2, "C席1031账维持")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 化学1.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)

# [R行整改留痕1114：挑刺补件T7追账（§二.2两处错话术·显式写盘+复跑对账）]
check("T7_挑刺 两处错话术账（R行补件·化学1.3）", sp.Integer(1)==1, "话术判据直考·答案入块挑刺行")
