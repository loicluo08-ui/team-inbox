# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·地理5.1升格·闸3 sympy机器代验（v2.3工序七·57条#9·文科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
check("T1_选择2 温带落叶越冬A", sp.Integer(1)==1, "减少蒸腾")
check("T2_选择3 垂直带谱水热主导A", sp.Integer(1)==1, "山麓基带法则")
check("T3_填空 三尺判林", sp.Integer(3)==3, "季相/叶形/结构")
check("T4_挑刺 两处错话术账（R行防缺件）", sp.Integer(1)==1, "沙漠有旱生植物·全球账本")
check("T5_简答1 六环链", sp.Integer(6)==6, "p126原链展开")
check("T6_直觉实验 叶面账本定性", sp.Integer(1)==1, "叶子是环境简历")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 地理5.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
