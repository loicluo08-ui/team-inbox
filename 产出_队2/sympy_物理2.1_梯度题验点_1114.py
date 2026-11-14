#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""物理2.1 新标准升格·闸3数字复算（新增试题答案独立验证轮·sympy机器代验·沿v2.3工序七）
验点覆盖：真题锚两题（浙江16Ⅰ/甲卷T23）＋选择1-3＋填空＋挑刺＋解答1-2 全部数值账
留痕注：首跑逮本脚本两处笔误自纠（①list传参致sympy报错→改逐段验点②cm→m单位换算漏写×14处→补/100·
内容数值全程无误·修正后复跑全绿）"""
import sympy as sp
from sympy import Rational as R

results = []
def chk(name, expr, expect):
    val = sp.simplify(expr)
    expv = sp.simplify(expect)
    if val.is_number and expv.is_number:
        ok = abs(sp.N(val, 30) - sp.N(expv, 30)) < sp.Float("1e-12")
    else:
        ok = val == expv
    results.append((name, ok, val, expect))
    return ok

# ===== 真题1：2023.1浙江16Ⅰ实验I（读数两源口径） =====
chk("真1-1 两账换算", sp.Float("0.02") * 5, sp.Float("0.1"))        # 50Hz×5=0.1s
chk("真1-2 2T", sp.Float("0.02") * 2, sp.Float("0.04"))
chk("真1-3 x13源一", sp.Float("8.60") - sp.Float("2.75"), sp.Float("5.85"))
chk("真1-4 v2源一(cm→m)", R(585, 100) / sp.Float("0.04") / 100, sp.Float("1.4625"))  # ≈1.46
chk("真1-5 x13源二", sp.Float("8.65") - sp.Float("2.75"), sp.Float("5.90"))
chk("真1-6 v2源二(cm→m)", R(590, 100) / sp.Float("0.04") / 100, sp.Float("1.475"))   # ≈1.48
chk("真1-7 歧异带(cm→m)", (sp.N(R(585, 100) / sp.Float("0.04") / 100, 5) > 1.46) and (sp.N(R(590, 100) / sp.Float("0.04") / 100, 5) < 1.48), True)
# ===== 真题2：2023全国甲卷T23 =====
chk("真2-1 间隔数账", sp.Float("0.1") * 3, sp.Float("0.3"))          # A→D三间隔
chk("真2-2 v̄AD", R(2400, 100) / sp.Float("0.3"), sp.Float("80.00"))
chk("真2-3 a=2k", sp.Float("68.0") * 2, sp.Float("136.0"))           # cm/s²
chk("真2-4 换算m/s²", sp.Float("136.0") / 100, sp.Float("1.36"))
chk("真2-5 截距口径", sp.Float("68.0") * sp.Float("0.3") + sp.Float("59.0"), sp.Float("79.4"))
chk("真2-6 散差", abs(sp.Float("80.00") - sp.Float("79.4")), sp.Float("0.6"))
chk("真2-7 推导自洽", sp.simplify(sp.Float("0.5") * 2 - 1), 0)        # k=½a→a=2k恒等
# ===== 选择2：5点4间隔 =====
chk("选2-1 间隔数", 5 - 1, 4)
chk("选2-2 时间", 4 * sp.Float("0.1"), sp.Float("0.4"))              # → C
# ===== 选择3/填空：纸带2.0/2.6/3.2/3.8/4.4 cm =====
chk("选3-1a 点距差①", sp.Float("2.6") - sp.Float("2.0"), sp.Float("0.6"))
chk("选3-1b 点距差②", sp.Float("3.2") - sp.Float("2.6"), sp.Float("0.6"))
chk("选3-1c 点距差③", sp.Float("3.8") - sp.Float("3.2"), sp.Float("0.6"))
chk("选3-1d 点距差④", sp.Float("4.4") - sp.Float("3.8"), sp.Float("0.6"))
chk("选3-2 v3合计", R(26, 10) + R(32, 10), R(58, 10))                # (2.6+3.2)=5.8 cm
chk("选3-3 v3=0.29(cm→m)", R(58, 10) / sp.Float("0.2") / 100, sp.Float("0.29"))
chk("选3-4 单段误用值(cm→m)", R(32, 10) / sp.Float("0.1") / 100, sp.Float("0.32"))
chk("填-1 v2合计", R(20, 10) + R(26, 10), R(46, 10))
chk("填-2 v2=0.23(cm→m)", R(46, 10) / sp.Float("0.2") / 100, sp.Float("0.23"))
chk("填-3 v5合计", R(38, 10) + R(44, 10), R(82, 10))
chk("填-4 v5=0.41(cm→m)", R(82, 10) / sp.Float("0.2") / 100, sp.Float("0.41"))
chk("填-5 点2到5时间", (5 - 2) * sp.Float("0.1"), sp.Float("0.3"))
chk("填-6 增量", sp.Float("0.29") - sp.Float("0.23"), sp.Float("0.06"))
# ===== 挑刺：0.26错值 vs 0.29真值 =====
chk("挑-1 单段误用(cm→m)", R(26, 10) / sp.Float("0.1") / 100, sp.Float("0.26"))
chk("挑-2 真值(cm→m)", R(58, 10) / sp.Float("0.2") / 100, sp.Float("0.29"))
# ===== 解答1：纸带1.8/2.4/3.0/3.6/4.2 cm =====
chk("解1-1 v2(cm→m)", R(42, 10) / sp.Float("0.2") / 100, sp.Float("0.21"))
chk("解1-2 v3(cm→m)", R(54, 10) / sp.Float("0.2") / 100, sp.Float("0.27"))
chk("解1-3 v4(cm→m)", R(66, 10) / sp.Float("0.2") / 100, sp.Float("0.33"))
chk("解1-4 点1到6时间", (6 - 1) * sp.Float("0.1"), sp.Float("0.5"))
chk("解1-5 误算值(cm→m)", R(42, 10) / sp.Float("0.16") / 100, sp.Float("0.2625"))
chk("解1-6 偏大判据(cm→m)", (sp.N(R(42, 10) / sp.Float("0.16") / 100, 5) > 0.21), True)
chk("解1-7 增量恒定", sp.Float("0.27") - sp.Float("0.21"), sp.Float("0.06"))
# ===== 解答2：v̄=6.5/7.5/8.5/9.5 cm/s @ 0.1-0.4 s（全cm口径） =====
chk("解2-1 斜率", R(95, 10) - R(65, 10), sp.Float("3.0"))            # 3=10×0.3
chk("解2-2 ½a", R(3, 1) / sp.Float("0.3"), 10)                       # cm/s²
chk("解2-3 a", 10 * 2, 20)                                           # a=20 cm/s²
chk("解2-4 截距vO", R(65, 10) - 10 * sp.Float("0.1"), sp.Float("5.5"))
chk("解2-5 预测v̄", sp.Float("5.5") + 10 * sp.Float("0.5"), sp.Float("10.5"))
chk("解2-6 距离=v̄t", sp.Float("10.5") * sp.Float("0.5"), sp.Float("5.25"))
chk("解2-7 位移式自洽", sp.Float("5.5") * sp.Float("0.5") + 10 * sp.Float("0.25"), sp.Float("5.25"))
chk("解2-8 两口径等", sp.Float("10.5") * sp.Float("0.5") - (sp.Float("5.5") * sp.Float("0.5") + 10 * sp.Float("0.25")), 0)

fails = [r for r in results if not r[1]]
for name, ok, val, exp in results:
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {val} (expect {exp})")
print(f"\n总验点 {len(results)} · 失败 {len(fails)}")
if fails:
    raise SystemExit(1)
print("ALL PASS")
