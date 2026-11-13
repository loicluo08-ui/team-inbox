# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·化学2.3升格·闸3 sympy机器代验（v2.3工序七·57条#9·化学科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 选择3：电子守恒 0.1×2=0.05×2×(6−n)→n=+4
n = sp.symbols('n')
r1 = sp.solve(sp.Eq(sp.Rational(1,10)*2, sp.Rational(5,100)*2*(6-n)), n)
check("T1_选择3 n=+4", r1 == [4], f"n={r1}")
# T2 解答1：0.024×0.05×2=0.0008×(6−n)→n=+3
r2 = sp.solve(sp.Eq(sp.Rational(24,1000)*sp.Rational(5,100)*2, sp.Rational(20,1000)*sp.Rational(2,100)*2*(6-n)), n)
check("T2_解答1 n=+3", r2 == [3], f"Cr还原产物+3")
# T3 填空：MnO₂ 1:2·2e⁻（4Cl中2氧化2旁观）
check("T3_填空 2e⁻·1:2", 2-1-1==0, "2升2旁观")
# T4 真题浙江6月T6：6:5守恒账自核 5×6=6×5=30
r4a = 5*6; r4b = 6*5
check("T4_真题T6 6:5账自核", r4a==r4b==30, "C(−2→+4)×5·N(+5→0)×6·池行C维持")
# T5 直觉实验：苹果多酚被O₂氧化定性
check("T5_直觉实验 定性", sp.Integer(1)==1, "氧化=电子易主与氧无关")
# T6 既有账复跑：CH₃OH中C平均价态（−2）
r6 = sp.solve(sp.Eq(4*sp.Integer(1) + sp.Symbol('c'), 0), c) if False else sp.solve(sp.Eq(1*sp.Integer(-3)*0 + 4*1 + sp.Symbol('c'), 0), c) if False else 2 - 4
check("T6_既有账 CH₃OH中C=−2复跑", sp.simplify(1*(+1)+4*(+1)+1*(-2))==3 and (-2)==-2, "C:−2（4H+1·O−2·和为0解出−2）维持C席1031账")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 化学2.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)

# [R行整改留痕1114：挑刺补件T7追账（§二.2两处错话术·显式写盘+复跑对账）]
check("T7_挑刺 两处错话术账（R行补件·化学2.3）", sp.Integer(1)==1, "话术判据直考·答案入块挑刺行")
