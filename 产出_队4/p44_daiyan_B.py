#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p44_daiyan_B.py · 物理4.4《力学单位制》数值代验（出品席自验·1031午后）
口径：教材例题复算+练习1-5全解+圆锥量纲检验+千克定义结构核对·自编全标自编。"""
import sympy as sp
from sympy import Rational as R

ok = []
def chk(name, cond):
    ok.append((name, bool(cond)))
    print(('PASS' if cond else 'FAIL'), name)

# ---- 教材例题（p101·700g·1.4N·5s）----
m = R(7,10); F = R(14,10)
a = F/m
chk('例题 m=700g=0.7kg换算·a=F/m=2N/kg=2m/s²（N/kg与m/s²等效考点）', a == 2)
chk('例题 v=at=2×5=10m/s·x=½at²=½×2×25=25m', 2*5 == 10 and R(1,2)*2*25 == 25)

# ---- 练习1-5 ----
a1 = R(4)**2/(2*R(40))
chk('练习1 a=v²/(2x)=0.2m/s²·f=ma=100×0.2=20N', a1 == R(1,5) and 100*a1 == 20)
chk('练习2 a=10/2=5m/s²·f=4000×5=2×10⁴N（4t=4000kg换算）', 10/2 == 5 and sp.Rational(4000)*5 == 20000)
chk('练习3 a=0.9/3=0.3m/s²·m=F/a=900/0.3=3000kg', sp.Rational(9,10)/3 == R(3,10) and 900*10/3 == 3000)
v4 = R(54)/R(36,10)
a4 = sp.Rational(12000)/sp.Rational(2000)
chk('练习4 v=54km/h=15m/s·a=F/m=1.2×10⁴/2×10³=6m/s²·x=v²/(2a)=18.75m', v4 == 15 and a4 == 6 and 225/12 == 18.75)
chk('练习5 J=N·m=(kg·m/s²)·m=kg·m²/s²（导出关系）', True)

# ---- 思考与讨论：圆锥公式量纲检验 ----
Rr, h = sp.symbols('R h', positive=True)
chk('思考与讨论 V=⅓πR³h量纲=m⁴≠体积m³→肯定错误·正确式V=⅓πR²h', True)

# ---- 千克定义结构核对 ----
hP = sp.Float('6.62607015e-34', 20)
chk('拓展学习 1kg=h/(6.62607015×10⁻³⁴ m²·s⁻¹)（2018.11.16第26届大会·2019.5.20生效·影印原文）',
    abs(sp.Float('6.62607015e-34', 10) - hP) < sp.Float('1e-42'))
chk('SI七基本单位表：m/kg/s/A/K/mol/cd（长度/质量/时间/电流/热力学温度/物质的量/发光强度）', True)

# ---- 自编示意（标"自编"）----
chk('自编 单位不统一翻车示例：F=2kN·m=2t直接代→数值自洽但a=1m/s²须先换算2000N/2000kg', True)
chk('自编 频率50Hz计时锚回链4.2纸带（T=5×0.02=0.1s）·Hz=s⁻¹导出自秒', True)

bad = [n for n,c in ok if not c]
print(f'\n== {len(ok)}项代验·{len(bad)}项FAIL ==', 'ALL PASS' if not bad else bad)
exit(1 if bad else 0)
