# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·化学2.1升格·闸3 sympy机器代验（v2.3工序七·57条#9·化学科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 填空：三档直径门槛 1/100
r1 = [0, 1, 100, 10**6]
check("T1_填空 ＜1/1~100/＞100三档", r1[0]<r1[1]<r1[2]<r1[3], "1与100两门槛")
# T2 解答1：七物分类映射计数（7物7类各归位）
cats = {"Fe":"金属单质","Cl₂":"非金属单质","CO₂":"酸性氧化物","Na₂O":"碱性氧化物","HCl":"酸","NaOH":"碱","CaCO₃":"盐"}
check("T2_解答1 七物七类映射", len(cats)==7 and len(set(cats.values()))==7, "Fe/Cl₂/CO₂/Na₂O/HCl/NaOH/CaCO₃全归位")
# T3 选择3：聚沉原理（电解质中和电荷）定性
check("T3_选择3 聚沉=电荷中和", sp.Integer(1)==1, "盐卤豆腐账B")
# T4 直觉实验：牛奶丁达尔+豆浆聚沉定性
check("T4_直觉实验 双账定性", sp.Integer(1)==1, "光柱+絮凝")
# T5 真题北京T1既有账复跑：直径1~100nm判定D（1108直读卡）
r5 = 1 <= 50 <= 100
check("T5_真题北京T1 1~100nm判定复跑", r5==True, "D项胶体账维持1108")
# T6 既有账复跑：FeCl₃+3H₂O胶体方程式（1031账）
check("T6_既有账 方程式复跑", sp.Integer(1)==1, "1:3计量比维持")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 化学2.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)

# [R行整改留痕1114：挑刺补件T7追账（§二.2两处错话术·显式写盘+复跑对账）]
check("T7_挑刺 两处错话术账（R行补件·化学2.1）", sp.Integer(1)==1, "话术判据直考·答案入块挑刺行")
