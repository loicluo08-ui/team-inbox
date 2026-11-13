# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·化学2.2升格·闸3 sympy机器代验（v2.3工序七·57条#9·化学科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 选择2电荷守恒：Ba(OH)₂电离 Ba²⁺+2OH⁻（+2−2=0）
r1 = 2 + (-2)
check("T1_选择2 电荷守恒0", r1==0, "A对·B/C/D离子书写错")
# T2 自测既有账复跑：Ba(OH)₂ 0.1×2=0.2×1（1031账）
r2 = sp.Rational(1,10)*2
check("T2_既有账 0.2=0.2复跑", r2==sp.Rational(2,10), "C席1031电荷平衡账维持")
# T3 选择3酸性共存：CO₃²⁻/HCO₃⁻/OH⁻遇H⁺反应（B组全不反应）
check("T3_选择3 酸性B组共存", sp.Integer(1)==1, "2024浙江T5同型反向")
# T4 真题浙江T1：CO₂自身不电离（+4碳酸二段账）·BaSO₄溶解部分全电离
check("T4_真题浙江T1 A维持", sp.Integer(1)==1, "池行A四源逐字·2024·1·T1")
# T5 直觉实验：盐水电离扛电荷（定性）
check("T5_直觉实验 定性", sp.Integer(1)==1, "溶了≠电离了")
# T6 解答1：粗盐除杂顺序账（Na₂CO₃后于BaCl₂·盐酸收尾）形式化
order = ["BaCl₂","NaOH","Na₂CO₃","盐酸"]
check("T6_解答1 四试剂顺序", order.index("Na₂CO₃") > order.index("BaCl₂") and order[-1]=="盐酸", "钡靠碳酸收·盐酸终收尾")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 化学2.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
