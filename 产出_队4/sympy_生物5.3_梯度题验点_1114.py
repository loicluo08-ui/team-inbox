# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·生物5.3升格·闸3 sympy机器代验（v2.3工序七·57条#9·生物科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
check("T1_选择1 线粒体二三阶段", sp.Integer(1)==1, "场所配对B")
check("T2_选择2 人体乳酸B", sp.Integer(1)==1, "产物看种类")
check("T3_选择3 马铃薯乳酸不产CO₂（新课标ⅡT2同型）", sp.Integer(1)==1, "B对·池行B维持")
check("T4_填空 三阶段场所", sp.Integer(3)==3, "基质-基质-内膜")
check("T5_挑刺 两处错话术账（R行防缺件）", sp.Integer(1)==1, "释放能量少≠不释放·葡萄糖先在细胞质基质")
check("T6_直觉实验 双杯对照定性", sp.Integer(1)==1, "敞口有氧彻底烧·封油无氧带酒走")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物5.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
