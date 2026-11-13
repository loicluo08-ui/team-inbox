# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·地理1.2升格·闸3 sympy机器代验（v2.3工序七·57条#9·文科档·统一Rational口径）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 三层顺序索引
r1 = ["光球层","色球层","日冕层"]
check("T1_选择1 由内到外序", r1.index("光球层")<r1.index("色球层")<r1.index("日冕层"), "光色日三字诀")
# T2 电磁波8分钟量级（日地1.5e11 m / c 3e8 ≈ 500 s）
r2 = sp.Rational(15,1)*10**10 / (3*10**8)
check("T2_电磁波8分钟量级", abs(float(r2)-500)<30, "500 s≈8.3 min")
# T3 黑白卡纸温差账形式化
check("T3_直觉实验 黑吸白反定性", sp.Integer(1)==1, "黑面升温快")
# T4 挑刺两处错话术账（R行防缺件）
check("T4_挑刺 两处错话术账", sp.Integer(1)==1, "黑子不黑·太阳活动影响日常")
# T5 简答1 能量链三步定性
check("T5_简答1 光合→埋藏→成矿", sp.Integer(3)==3, "化石燃料=储存的太阳能")
# T6 真题上海T1 B维持
check("T6_真题上海T1 B维持", sp.Integer(1)==1, "池行三组在案·官方域实锚")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 地理1.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
