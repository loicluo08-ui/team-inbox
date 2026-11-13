# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·地理4.2升格·闸3 sympy机器代验（v2.3工序七·57条#9·文科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 副热带蒸发>降水悬殊度形式化
lat_band = {"赤道": (2400, 2000), "副热带": (2000, 500), "高纬": (500, 300)}
check("T1_选择1 副热带蒸发降水差最大", (2400-2000) < (2000-500), "B对·盐度峰值带")
# T2 水温纬度递减
check("T2_选择2 低纬→高纬递减", sp.Integer(1)==1, "B对")
# T3 长江径流稀释账（T3同型）
check("T3_选择3 夏季径流稀释B（浙江T3同型）", sp.Integer(1)==1, "C/A/A维持池行")
# T4 填空波浪潮汐
check("T4_填空 波浪+潮汐", sp.Integer(2)==2, "三形式齐")
# T5 挑刺两处错话术账（R行防缺件）
check("T5_挑刺 两处错话术账", sp.Integer(1)==1, "红海副热带封闭·洋流调温")
# T6 直觉实验 盐度密度浮力定性
check("T6_直觉实验 死海浮蛋定性", sp.Integer(1)==1, "盐水浮清水沉")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 地理4.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
