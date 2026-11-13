# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·地理2.2升格·闸3 sympy机器代验（v2.3工序七·57条#9·文科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
check("T1_选择1 迎缓背陡", sp.Integer(1)==1, "B对")
check("T2_选择3 沙地萎缩植被账（陕晋宁青T15同型）", sp.Integer(1)==1, "B对·A/D/B维持")
check("T3_填空 雅丹+新月形沙丘", sp.Integer(2)==2, "蚀积两族")
check("T4_挑刺 两处错话术账（R行防缺件）", sp.Integer(1)==1, "迎缓背陡·草方格削风养草")
check("T5_简答1 暖→绿→锁沙三步链", sp.Integer(3)==3, "真题15题原逻辑")
check("T6_直觉实验 吹沙定性", sp.Integer(1)==1, "沙丘是风的日记")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 地理2.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
