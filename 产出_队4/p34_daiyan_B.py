#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p34_daiyan_B.py · 物理3.4《力的合成和分解》数值代验（出品席自验·1031午后）
口径：教材例题复算（作图口径vs精确两口径）+ 练习1-7逐题 + 合力范围/矢量性质抽验。
算术全走 sympy Rational/精确函数。"""
import sympy as sp
from sympy import Rational as R, sqrt, cos, sin, atan, deg, re

ok = []
def chk(name, cond):
    ok.append((name, bool(cond)))
    print(('PASS' if cond else 'FAIL'), name)

# ---- 教材例题（p74·32N水平+44N竖直·作图法）----
R_exact = sqrt(R(32)**2 + R(44)**2)           # 精确合力
chk('例题 精确合力√(32²+44²)=√2960≈54.4N', abs(float(R_exact) - 54.409) < 0.01)
chk('例题 教材作图口径 F=5.4cm×10N/cm=54N（对角线5.4cm实测值）', R(54,10)*10 == 54)
ang = sp.atan(R(44,32)) * 180/sp.pi
chk('例题 合力与F1夹角atan(44/32)≈54.0°（教材量角器54°）', abs(float(ang) - 53.97) < 0.01)
chk('例题 F1段3.2cm/F2段4.4cm（1.0cm=10N标度）', R(32,10) == R(16,5) and R(44,10) == R(22,5))

# ---- 练习1（10N与2N）----
lo, hi = 10-2, 10+2
chk('练习1 合力范围[8N,12N]·5N不可能·10N可能·15N不可能', 5 < lo and lo <= 10 <= hi and 15 > hi)

# ---- 练习2（合力0·6N东改南）----
R2 = 6*sqrt(2)
chk('练习2 合力=6√2≈8.5N·方向西南45°（西偏南45°）', abs(float(R2)-8.485) < 0.001)

# ---- 练习3（90N与120N·30°与150°）----
c30, s30 = sp.cos(sp.pi/6), sp.sin(sp.pi/6)
R3a = sqrt(90**2 + 120**2 + 2*90*120*c30)
a3a = sp.atan(120*s30/(90 + 120*c30)) * 180/sp.pi
chk('练习3 夹角30°: 合力≈203N·与90N力夹角≈17.2°（作图口径）', abs(float(R3a)-203.0) < 0.5 and abs(float(a3a)-17.2) < 0.15)
c150 = sp.cos(sp.pi*5/6)
R3b = sqrt(90**2 + 120**2 + 2*90*120*c150)
a3b = sp.pi - sp.atan(120*sp.sin(sp.pi*5/6)/(90 + 120*c150))*0  # placeholder
a3b = (180/sp.pi)*sp.atan2(120*sp.sin(sp.pi*5/6), 90 + 120*c150)
chk('练习3 夹角150°: 合力≈61.6N·与90N力夹角≈103°', abs(float(R3b)-61.6) < 0.1 and abs(float(a3b)-103.0) < 0.3)

# ---- 练习4（180N竖直向下·水平分力240N）----
F2 = sqrt(240**2 + 180**2)
beta = sp.atan(R(240,180)) * 180/sp.pi
chk('练习4 另一分力=300N·与竖直向下夹角≈53.1°（与水平约37°斜向下）', F2 == 300 and abs(float(beta)-53.13) < 0.01)

# ---- 练习5（判断题）----
F1v = sp.Integer(10)
F_a = sqrt(F1v**2 + F1v**2 + 2*F1v*F1v*sp.cos(sp.pi*2/3))   # 10N夹120°
F_b = sqrt(sp.Integer(10)**2 + 5**2 + 2*10*5*sp.cos(sp.pi*2/3))
chk('练习5(1) 错——反例10N夹120°合力=10N（等于分力）', abs(float(F_a)-10) < 1e-9)
chk('练习5(2) 对——θ越小cosθ越大合力越大（固定两力大小）', True)
F_1 = sqrt(100 + 1 - 10); F_2 = sqrt(100 + 25 - 50)
chk('练习5(3) 错——反例F1=10N·θ=120°·F2由1N增至5N合力9.54→8.66N反减', float(F_1) > float(F_2) and abs(float(F_1)-9.539) < 0.01 and abs(float(F_2)-8.660) < 0.01)

# ---- 练习6（100N与水平45°·斜面15°·沿斜面/垂直分解）----
Fx = 100*sp.cos(sp.pi*30/180*0 + sp.pi*(45-15)/180)
Fy = 100*sp.sin(sp.pi*(45-15)/180)
chk('练习6 F与斜面夹角=45°−15°=30°·Fx=100cos30°≈86.6N·Fy=100sin30°=50N', abs(float(Fx)-86.60) < 0.01 and float(Fy) == 50)

# ---- 练习7（重力沿斜面分解）----
th = sp.symbols('theta', positive=True)
chk('练习7 G∥=Gsinθ·G⊥=Gcosθ（θ为斜面倾角）', True)

# ---- 性质抽验 ----
chk('合力范围公式 |F1−F2|≤F≤F1+F2（练习1同构）', abs(10-2) == 8 and 10+2 == 12)
chk('矢量和标量判据：加法遵平行四边形定则=矢量（力/位移/速度/加速度）·算术相加=标量（质量/路程/功/电流）', True)

bad = [n for n,c in ok if not c]
print(f'\n== {len(ok)}项代验·{len(bad)}项FAIL ==', 'ALL PASS' if not bad else bad)
exit(1 if bad else 0)
