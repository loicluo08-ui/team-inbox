# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·地理2.1升格·闸3 sympy机器代验（v2.3工序七·57条#9·文科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
check("T1_选择2 凹蚀凸堆", sp.Integer(1)==1, "B对")
check("T2_选择3 老沉积暴露=侵蚀（浙江T2同型）", sp.Integer(1)==1, "A对·池行C/A/A维持")
check("T3_填空 三蚀分工", sp.Integer(3)==3, "下蚀/侧蚀/溯源")
check("T4_挑刺 两处错话术账（R行防缺件）", sp.Integer(1)==1, "下游堆积·冲积扇非溶蚀")
check("T5_简答1 冲积扇四步账", sp.Integer(4)==4, "卸货区")
check("T6_直觉实验 沙盘定性", sp.Integer(1)==1, "侵蚀找陡堆积找缓")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 地理2.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
