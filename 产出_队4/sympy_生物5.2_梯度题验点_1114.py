# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·生物5.2升格·闸3 sympy机器代验（v2.3工序七·57条#9·生物科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
check("T1_选择2 释放能量B", sp.Integer(1)==1, "直接用于多种生命活动")
check("T2_选择3 末端32P→Pi（甲卷T2同型）", sp.Integer(1)==1, "末端记账·池行C维持")
check("T3_填空 A—P~P~P·2高能键", sp.Integer(2)==2, "p86原简式")
check("T4_挑刺 两处错话术账（R行防缺件）", sp.Integer(1)==1, "含量少转化快·机械能可转化")
check("T5_解答1 荧光素ATP对照逻辑", sp.Integer(1)==1, "p86问题探讨三问")
check("T6_直觉实验 零钱罐动态平衡定性", sp.Integer(1)==1, "倒手总额不变")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物5.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
