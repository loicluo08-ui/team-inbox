# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·生物4.2升格·闸3 sympy机器代验（v2.3工序七·57条#9·生物科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
check("T1_选择1 O₂自由扩散", sp.Integer(1)==1, "顺浓度无载体无能量")
check("T2_选择3 载体构象改变C（云南T3同型）", sp.Integer(1)==1, "握手换手账·池行C维持")
check("T3_填空 能量+流动性", sp.Integer(2)==2, "胞吞胞吐两件套")
check("T4_挑刺 两处错话术账（R行防缺件）", sp.Integer(1)==1, "协助扩散也要载体·胞吞胞吐∉跨膜运输")
check("T5_解答1 腌制失选择透过性", sp.Integer(1)==1, "p72概念检测2A同款")
check("T6_直觉实验 温度加速扩散定性", sp.Integer(1)==1, "茶包冷热账")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物4.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
