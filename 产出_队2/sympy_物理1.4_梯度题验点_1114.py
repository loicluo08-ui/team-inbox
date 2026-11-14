#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""物理1.4 新标准升格·闸3数字复算（新增试题答案独立验证轮·sympy机器代验·沿v2.3工序七）
验点覆盖：真题锚2025新课标T1＋选择1-3＋填空＋挑刺＋解答1-2 全部数值账"""
import sympy as sp
from sympy import Rational as R

results = []
def chk(name, expr, expect):
    val = sp.simplify(expr)
    expv = sp.simplify(expect)
    # 数值口径统一：Float与Rational/Integer按容差比对（避免浮点符号学假阳）
    if val.is_number and expv.is_number:
        ok = abs(sp.N(val, 30) - sp.N(expv, 30)) < sp.Float("1e-12")
    else:
        ok = val == expv
    results.append((name, ok, val, expect))
    return ok

# ===== 真题锚：2025新课标卷T1（CR450·120m/s匀减速14.4km→a） =====
chk("T1-1 单位坑换算", 14.4 * 1000, 14400)
chk("T1-2 v0平方", 120**2, 14400)
chk("T1-3 2x", 2 * 14400, 28800)
chk("T1-4 a=v0²/2x", R(120**2, 2 * 14400), R(1, 2))          # 0.5 → B
chk("T1-5 量级直觉t", 120 / sp.Float("0.5"), 240)             # 240 s ≈ 4分钟
# ===== 选择2：72→108 km/h / 5 s =====
chk("选2-1 km/h换算", 72 / sp.Float("3.6"), 20)
chk("选2-2 km/h换算", 108 / sp.Float("3.6"), 30)
chk("选2-3 a=Δv/Δt", R(30 - 20, 5), 2)                        # → A
# ===== 选择3：蹦床 −8→0→+6 =====
chk("选3-1 a前段", R(0 - (-8), sp.Float("0.4")), 20)          # A错(10·向下)
chk("选3-2 a后段", R(6 - 0, sp.Float("0.4")), 15)             # B错(20)
chk("选3-3 最低点a非零判据", sp.simplify(20) != 0, True)
# ===== 填空：90→18 km/h / 2 min =====
chk("填-1 换算", 90 / sp.Float("3.6"), 25)
chk("填-2 换算", 18 / sp.Float("3.6"), 5)
chk("填-3 Δv", 5 - 25, -20)
chk("填-4 a", R(-20, 120), R(-1, 6))                          # ≈−0.17
chk("填-5 近位", abs(R(-1, 6) - sp.Float("-0.17")) < R(1, 200), True)  # −1/6按2位舍入=−0.17·舍入一致性判据
# ===== 挑刺：百公里加速8 s =====
chk("挑-1 100km/h换算", 100 / sp.Float("3.6"), R(250, 9))
chk("挑-2 a≈27.8/8", sp.N((100 / sp.Float("3.6")) / 8, 3), sp.N(sp.Float(250, 40) / 9 / 8, 3))  # ≈3.47≈3.5
# ===== 解答1：20s加速到72km/h·60s匀速·10s减到18km/h =====
chk("解1-1 换算", 72 / sp.Float("3.6"), 20)
chk("解1-2 a1", R(20, 20), 1)                                 # +1 向东
chk("解1-3 换算18", 18 / sp.Float("3.6"), 5)
chk("解1-4 a3", R(5 - 20, 10), sp.Float("-1.5"))              # −1.5 向西
chk("解1-5 全程Δt", 20 + 60 + 10, 90)
chk("解1-6 平均加速度", R(5 - 0, 90), R(1, 18))               # ≈0.056
chk("解1-7 拉平均≠定义", sp.simplify(R(1, 1) + sp.Float("-1.5")) != sp.simplify(R(1, 18)), True)  # (1−1.5)/2≠1/18
# ===== 解答2：甲0→15/5s·乙20→0/10s·丙12→8/4s =====
chk("解2-1 甲a", R(15, 5), 3)
chk("解2-2 乙a", R(0 - 20, 10), -2)
chk("解2-3 丙a", R(8 - 12, 4), -1)
chk("解2-4 速度最大判据", max(15, 20, 8) == 20, True)          # 乙速度最大
chk("解2-5 变化最快判据", max(abs(3), abs(-2), abs(-1)) == 3, True)  # 甲|a|最大
# ===== 对账块读表提醒（正本原数复算） =====
chk("读表-1 火车a", R(250, 9) / 300, R(5, 54))                # ≈0.0926≈0.093
chk("读表-2 急刹每秒变化", 5 * 1, 5)

fails = [r for r in results if not r[1]]
for name, ok, val, exp in results:
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {val} (expect {exp})")
print(f"\n总验点 {len(results)} · 失败 {len(fails)}")
if fails:
    raise SystemExit(1)
print("ALL PASS")
