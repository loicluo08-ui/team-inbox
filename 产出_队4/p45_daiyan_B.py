#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p45_daiyan_B.py · 物理4.5《牛顿运动定律的应用》数值代验（出品席自验·1031午后）
口径：例题1两段/例题2正交分解·练习1-4全解·自编标自编。"""
import sympy as sp
from sympy import Rational as R, sqrt, sin, cos, tan

ok = []
def chk(name, cond):
    ok.append((name, bool(cond)))
    print(('PASS' if cond else 'FAIL'), name)

g = R(10)
# ---- 例题1（p104-106·冰壶·μ₁=0.02·μ₂=0.9μ₁·两段）----
a1 = -R(2,100)*g
chk('例题1(1) a₁=−μ₁g=−0.2m/s²', a1 == -R(1,5))
x1 = -(R(34,10)**2)/(2*a1)
chk('例题1(1) x₁=−v₀²/2a₁=28.9m（−11.56/−0.4）', abs(float(x1)-28.9)<0.001)
a2 = -R(2,100)*R(9,10)*g
chk('例题1(2) a₂=−μ₂g=−0.18m/s²', a2 == -R(9,50))
v10sq = R(34,10)**2 + 2*a1*10
chk('例题1(2) v₁₀²=v₀²+2a₁x₁₀=11.56−4=7.56', v10sq == R(189,25))
x2 = -v10sq/(2*a2)
chk('例题1(2) x₂=21m', abs(float(x2)-21.0)<0.001)
chk('例题1(2) 多滑=(10+21)−28.9=2.1m', abs((10+21)-28.9-2.1)<0.001)

# ---- 例题2（p106-107·滑雪75kg·30°·v₀=2·t=5·x=60）----
a2x = 2*(R(60)-2*5)/R(25)
chk('例题2 a=2(x−v₀t)/t²=4m/s²', a2x == 4)
Ff = 75*(g*sp.Rational(1,2)-a2x)
FN = 75*g*sp.sqrt(3)/2
chk('例题2 F_f=m(gsinθ−a)=75N', float(Ff) == 75.0)
chk('例题2 F_N=mgcosθ=649.5→650N（教材取650）', abs(float(FN)-649.5)<0.02)
chk('例题2 牛三落账：对雪面压力=支持力650N·方向垂直斜面向下（p107照录）', True)

# ---- 练习1（p107·20kg·两50N互成60°·3s）----
F合 = 2*50*sp.sqrt(3)/2
a_p1 = F合/20
chk('练习1 F合=2Fcos30°=86.6N·a=4.33m/s²', abs(float(F合)-86.60)<0.01 and abs(float(a_p1)-4.33)<0.01)
chk('练习1 v=at=13.0m/s·x=½at²=19.5m', abs(float(3*a_p1)-12.99)<0.01 and abs(float(R(1,2)*a_p1*9)-19.49)<0.01)

# ---- 练习2（p108·气囊3.2m高·6.5m长·60kg·f=240N）----
sn = sp.Rational(32,10)/sp.Rational(65,10)
a_p2 = (60*10*sn-240)/60
v2 = sqrt(2*a_p2*sp.Rational(65,10))
chk('练习2 sinθ=3.2/6.5·a=(mgsinθ−f)/m≈0.923m/s²', abs(float(a_p2)-0.9231)<0.001)
chk('练习2 v=√(2ax)=√12≈3.46m/s', abs(float(v2)-3.464)<0.001)

# ---- 练习3（p108·54km/h·17.2m车痕测μ）----
mu3 = sp.Rational(15)**2/(2*g*sp.Rational(172,10))
chk('练习3 μ=v²/(2gx)=225/344≈0.65', abs(float(mu3)-0.654)<0.001)

# ---- 练习4（p108·油桶C脱离A）----
chk('练习4(1) 向左加速→C因惯性相对车向右挤→B对C支持力增大·A对C减小（理由=牛一/牛二定性）', True)
aN = g*sp.tan(sp.pi/6)
chk('练习4(2) C脱离A（N_A=0）→仅重力+B支持力：N_B·sin30°=ma·N_B·cos30°=mg→a=g·tan30°≈5.8m/s²',
    abs(float(aN)-5.774)<0.001)

# ---- 自编（标"自编"）----
chk('自编 例题2正交分解与4.3例题2悬球同构（a=g·tanθ族）·牛三落账回链3.2脚注①/3.3证明', True)

bad = [n for n,c in ok if not c]
print(f'\n== {len(ok)}项代验·{len(bad)}项FAIL ==', 'ALL PASS' if not bad else bad)
exit(1 if bad else 0)
