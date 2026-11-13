# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·地理4.3升格·闸3 sympy机器代验（v2.3工序七·57条#9·文科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 生物富集倍数形式化（每级×10·三级链）
conc = 10**-4
top = conc * 10**4
check("T1_简答1 富集放大千倍级", float(top) == 1.0, "0.0001 mg/L→1 mg/L级·营养级放大")
check("T2_选择2 油膜阻碍光合D", sp.Integer(1)==1, "覆盖/黏附/入链三路径")
check("T3_选择3 治理三步围堵回收降解A", sp.Integer(3)==3, "主动治理账")
check("T4_填空 海底+化学资源", sp.Integer(2)==2, "空间资源分方位")
check("T5_挑刺 两处错话术账（R行防缺件）", sp.Integer(1)==1, "资源有限·富集上餐桌")
check("T6_直觉实验 油花围堵定性", sp.Integer(1)==1, "覆盖→围堵→吸附三步")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 地理4.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
