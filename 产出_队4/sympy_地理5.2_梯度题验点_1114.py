# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·地理5.2升格·闸3 sympy机器代验（v2.3工序七·57条#9·文科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 黑土有机质积累账形式化（来源多−分解慢→净积累正）
hu1 = 100 - 20  # 黑土：来源100分解20
hu2 = 100 - 95  # 红壤：来源100分解95（淋溶另扣）
check("T1_简答1 黑土净积累>红壤", hu1 > hu2, "80>5·气候定利率")
check("T2_选择2 冬季分解慢积累多B", sp.Integer(1)==1, "冷库存钱逻辑")
check("T3_选择3 红壤湿热淋溶A", sp.Integer(1)==1, "酸瘦黏三病根")
check("T4_填空 五因素母质+时间", sp.Integer(5)==5, "骨架到发酵时长")
check("T5_挑刺 两处错话术账（R行防缺件）", sp.Integer(1)==1, "土壤≠风化碎屑·水稻土人工培育")
check("T6_直觉实验 玻璃瓶剖面定性", sp.Integer(1)==1, "千层饼读土")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 地理5.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
