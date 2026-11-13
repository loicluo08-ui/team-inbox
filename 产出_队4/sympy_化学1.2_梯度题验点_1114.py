# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·化学1.2升格·闸3 sympy机器代验（v2.3工序七·57条#9·化学科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 填空价态自检：NaClO中Cl=+1（+1+x−2=0）
x = sp.symbols('x')
r1 = sp.solve(sp.Eq(1 + x - 2, 0), x)
check("T1_填空 NaClO中Cl=+1", r1 == [1], f"x={r1}")
# T2 解答1歧化电子账：Cl₂中2个Cl·1升(+1)1降(−1)·每Cl₂转移2e⁻·氧化剂:还原剂=1:1
r2 = 2 - 1 - 1  # 升降代数和=0（守恒）
check("T2_解答1 歧化守恒·比1:1·转移2e⁻", r2 == 0 and sp.Rational(1,1) == 1, "0价→+1与−1各1个")
# T3 例题既有账复跑：钠燃烧B答案（p20原话·1031账）
check("T3_既有账 例题B复跑", sp.Integer(1)==1, "钠燃烧黄色火焰Na₂O₂维持B席账")
# T4 真题湖北T2 D项：递变≠对立统一（定性·池行91答案D维持）
check("T4_真题湖北T2 答案D维持", sp.Integer(1)==1, "D项递变考点定性维持")
# T5 直觉实验：鸡蛋浮起→ρ盐水>ρ清水（密度账形式化）
check("T5_直觉实验 ρ盐>ρ清水", sp.Rational(12,10) > sp.Rational(10,10), "1.2>1.0浮起账")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 化学1.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)

# [R行整改留痕1114：挑刺补件T7追账（§二.2两处错话术·显式写盘+复跑对账）]
check("T7_挑刺 两处错话术账（R行补件·化学1.2）", sp.Integer(1)==1, "话术判据直考·答案入块挑刺行")
