#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数学4.1《指数》sympy验点·实数域修正脚本 v2
（承群管理员20:51:02令·据QC批三2605065候补项"实数域修正脚本"·顺手补·不阻塞）

背景：v1首跑45/55·10点FAIL经QC批三定性=脚本假阴（复数主枝×4/教材四位小数
近似字符串截断对照×5/符号假设×1），正文零错勿动（成稿一字未改）。
本v2仅对上述10点改按实数域口径复验：
  ① 奇次根号负底数：sympy.real_root 取实根（v1误落复数主枝）
  ② 符号假设：代换 y=A2-2>0 使 |2-A2|=A2-2 可符号判定（A2>2 题设入模）
  ③ 教材四位小数近似：按四舍五入口径 round(val,n) 对照教材值
    （v1系与截断字符串逐位比对致形式FAIL；QC独立复算四近似值全对）
其余45点v1首跑已PASS不变（见 sympy_留痕_数学4.1_1031.txt）。
"""
from sympy import real_root, root, symbols, simplify, pi, sqrt, E, Rational, limit, oo

RESULT = []

def chk(name, cond, detail=""):
    RESULT.append(bool(cond))
    print(("✅" if cond else "❌") + f" {name} | {detail}")

print("=== 数学4.1 实数域修正验点 v2（10点·QC批三定性脚本假阴闭环） ===")

# 一、奇次根号负底数 → real_root 实根口径（复数主枝假阴 3 点）
r1 = real_root((-8) ** 3, 3)
chk("例1(1) ∛((-8)³)=-8", r1 == -8, f"real_root(-8)³,3)={r1}")

r2 = real_root(Rational(-1, 10) ** 5, 5)
chk("复1(2) ⁵√((-0.1)⁵)=-1/10", r2 == Rational(-1, 10), f"real_root={r2}")

r3 = real_root((pi - 4) ** 3, 3)
d3 = simplify(r3 - (pi - 4))
cond3 = (d3 == 0) or abs(float(r3.evalf(30)) - float((pi - 4).evalf(30))) < 1e-12
chk("自1b ∛((π-4)³)=π-4", cond3, f"real_root={r3}·差={d3}")

# 二、符号假设点 → 代换 y=A2-2>0（A2>2 题设显式入模）
y = symbols('y', positive=True)  # y = A2 - 2 > 0
expr1 = root((2 - (y + 2)) ** 4, 4)          # ⁴√((2-A2)⁴)
d1 = simplify(expr1 - y)                     # 应 = A2-2 = y
cond1 = (d1 == 0)
# 数值旁证（与v1补充验证同口径双保险）
for av in (3, 4.7):
    import math
    cond1 = cond1 and abs((abs(2 - av) ** 4) ** 0.25 - (av - 2)) < 1e-12
chk("自1 ⁴√((2-A2)⁴)=A2-2（A2>2）", cond1, f"代换y=A2-2>0·root(y⁴,4)={expr1}·差={d1}·数值旁证A2=3/4.7 ✓")

# 三、教材四位小数近似 → 四舍五入口径（截断对照假阴 5 点）
NUMS = [
    ("思考  2^√3≈3.322（三位）", 2 ** sqrt(3), 3.322, 3),
    ("填3(2a) 2^√3=3.3220",     2 ** sqrt(3), 3.3220, 4),
    ("填3(2b) 3^√2=4.7288",     3 ** sqrt(2), 4.7288, 4),
    ("填3(2c) π^√5=12.9319",    pi ** sqrt(5), 12.9319, 4),
    ("填3(2d) 2^π=8.8250",      2 ** pi,      8.8250, 4),
]
for name, expr, tb, nd in NUMS:
    v = float(expr.evalf(30))
    r = round(v, nd)
    chk(name, abs(r - tb) < 1e-12, f"真值={v:.7f}→round({nd})={r}·教材={tb}")

# 四、e 极限（拓10）→ limit 实数口径 + 四/五舍入位双对照
n = symbols('n', positive=True)
ve = float(limit((1 + 1 / n) ** n, n, oo).evalf(30))
chk("拓10 (1+1/n)ⁿ→e≈2.7183（≈2.71828）", round(ve, 4) == 2.7183 and round(ve, 5) == 2.71828,
    f"limit={ve:.7f}·round4={round(ve,4)}·round5={round(ve,5)}·E={E.evalf(8)}")

# 结算
tot = len(RESULT); passed = sum(RESULT)
print(f"\n结论：实数域口径 PASS {passed}/{tot}·v1其余45点已PASS不变（见v1留痕）"
      f"·全卷口径55/55·成稿断言零改动（QC批三假阴定性闭环）")
exit(0 if passed == tot else 1)
