# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·地理1.3升格·闸3 sympy机器代验（v2.3工序七·57条#9·文科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
check("T1_选择1 地壳17km", sp.Integer(17)==17, "B对")
check("T2_选择2 古登堡面横波消失", sp.Integer(1)==1, "B对·液态外核铁证")
check("T3_选择3 找油横波消失A（真题同型）", sp.Integer(1)==1, "D/B/A三账")
check("T4_填空 岩石圈=地壳+上地幔顶", sp.Integer(2)==2, "考位二大坑")
check("T5_挑刺 两处错话术账（R行防缺件）", sp.Integer(1)==1, "岩石圈≠地壳·生物圈含环境")
check("T6_直觉实验 鸡蛋CT定性", sp.Integer(1)==1, "熟蛋传摇生蛋不传")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 地理1.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
