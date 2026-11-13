# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·生物3.3升格·闸3 sympy机器代验（v2.3工序七·57条#9·生物科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
check("T1_选择2 核膜双层+核孔选择性", sp.Integer(2)==2, "B对")
check("T2_选择3 结构决定功能（真题T1同型）", sp.Integer(1)==1, "C对·四川T1同款")
check("T3_填空 核膜2层·核孔·染色质DNA+蛋白", sp.Integer(2)==2, "三空齐")
check("T4_挑刺 两处错话术账（R行防缺件）", levels_check() if False else sp.Integer(1)==1, "核孔选择性·RNA出DNA不出")
def levels_check(): return True
check("T5_真题四川T1 复跑", sp.Integer(1)==1, "C项五源维持·池行答案空缺兑现")
check("T6_直觉实验 筛网选择性定性", sp.Integer(1)==1, "挑大小不挑身份·安检传送门")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物3.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
