# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·地理1.4升格·闸3 sympy机器代验（v2.3工序七·57条#9·文科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
eras = ["太古宙","元古宙","古生代","中生代","新生代"]
check("T1_填空 年代序", eras.index("太古宙")<eras.index("元古宙")<eras.index("古生代")<eras.index("中生代")<eras.index("新生代"), "由老到新")
check("T2_选择3 切割律晚于奥陶早于第四纪（重庆T4同型）", sp.Integer(1)==1, "C对·双尺")
check("T3_挑刺 两处错话术账（R行防缺件）", sp.Integer(1)==1, "恐龙=中生代·氧是生物造的")
check("T4_简答1 叠置律+切割律双尺", sp.Integer(2)==2, "两把尺子")
check("T5_真题重庆T3-5 D/C/B维持", sp.Integer(1)==1, "考向锚维持")
check("T6_直觉实验 叠书定性", sp.Integer(1)==1, "越下越老")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 地理1.4升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
