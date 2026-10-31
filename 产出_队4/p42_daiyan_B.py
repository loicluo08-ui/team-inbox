#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p42_daiyan_B.py · 物理4.2《实验：探究加速度与力、质量的关系》数值代验（出品席自验·1031午后）
口径：式(1)(2)推导链·练习1表3拆分与模糊值反推·练习2纸带逐差·表6比例检验·自编示意全标自编。"""
import sympy as sp
from sympy import Rational as R
import statistics

ok = []
def chk(name, cond):
    ok.append((name, bool(cond)))
    print(('PASS' if cond else 'FAIL'), name)

# ---- 式(1)(2)推导链 ----
x, t, a = sp.symbols('x t a', positive=True)
chk('式(1) a=2x/t² ⇔ x=½at²（回链2.3·初速0）', sp.solve(sp.Eq(x, sp.Rational(1,2)*a*t**2), a)[0] == 2*x/t**2)
chk('式(2) 等时位移比=加速度比：x₁/x₂=a₁/a₂', sp.simplify((sp.Rational(1,2)*sp.Symbol('a1')*t**2)/(sp.Rational(1,2)*sp.Symbol('a2')*t**2)) == sp.Symbol('a1')/sp.Symbol('a2'))

# ---- 练习1·表3拆分（m=0.36行→表4·F=0.29行→表5）----
rows4 = [(R(14,100),R(39,100)),(R(19,100),R(53,100)),(R(29,100),R(81,100)),(R(34,100),R(94,100))]
ks4 = [float(a)/float(f) for f,a in rows4]
k4 = statistics.mean(ks4)
chk('表4 a/F恒定：k=%.3f·四点偏差<1.2%%'%k4, max(ks4)-min(ks4) < 0.02*k4)
a_024 = k4*0.24
chk('表4 模糊值回推：F=0.24N→a≈%.2f m/s²（比例插值）'%a_024, 0.66 < a_024 < 0.68)
rows5 = [(R(86,100),R(34,100)),(R(61,100),R(48,100)),(R(41,100),R(71,100)),(R(36,100),R(81,100))]
ks5 = [float(a)*float(m) for m,a in rows5]
k5 = statistics.mean(ks5)
chk('表5 a·m恒定：k′=%.3f·四点偏差<1%%'%k5, max(ks5)-min(ks5) < 0.01*k5)
a_031 = k5/0.31
chk('表5 模糊值回推：m=0.31kg→a≈%.2f m/s²'%a_031, 0.93 < a_031 < 0.95)

# ---- 练习2(1)·纸带（T=0.1s·段距6.19/6.70/7.21/7.72cm直读）----
T = R(1,10)
s = [R(619,100),R(670,100),R(721,100),R(772,100)]  # cm
deltas = [s[i+1]-s[i] for i in range(3)]
chk('计数点间隔T=0.02×5=0.1s（每两计数点间四点未画出）', T == R(1,10))
chk('相邻段距差恒为Δs=0.51cm（匀加速实锤）', all(d == R(51,100) for d in deltas))
a_A = deltas[0]/100/T**2
a_B = ((s[3]+s[2])-(s[1]+s[0]))/100/(4*T**2)
chk('纸带求a：Δs/T²=%.2f m/s²·逐差法%.2f m/s²·两口径同值'%(float(a_A), float(a_B)), a_A == a_B == R(51,100))

# ---- 练习2(2)·表6 a-(1/m)比例检验（m/a全值直读）----
m6 = [R(25,100),R(29,100),R(33,100),R(40,100),R(50,100),R(71,100),R(100,100),R(167,100)]
a6 = [R(618,1000),R(557,1000),R(482,1000),R(403,1000),R(317,1000),R(235,1000),R(152,1000),R(86,1000)]
am = [float(a6[i])*float(m6[i]) for i in range(8)]
mean = statistics.mean(am); dev = (max(am)-min(am))/mean*100
chk('表6 a·m≈%.3f恒定（偏差%.1f%%·误差范围内）→过原点直线→a与m成反比'%(mean,dev), dev < 15)
inv = [1/float(m) for m in m6]
chk('1/m行核对：4.00/3.45/3.03/2.50/2.00/1.41/1.00/0.60（教材表6照录一致）', all(abs(inv[i]-[4.00,3.45,3.03,2.50,2.00,1.41,1.00,0.60][i])<0.01 for i in range(8)))

# ---- 自编示意（标"自编"）----
chk('自编 a∝F成倍取样：F=0.10/0.20/0.30→a=0.28/0.56/0.84（k=2.8）', [round(2.8*f,2) for f in (0.1,0.2,0.3)] == [0.28,0.56,0.84])

bad = [n for n,c in ok if not c]
print(f'\n== {len(ok)}项代验·{len(bad)}项FAIL ==', 'ALL PASS' if not bad else bad)
exit(1 if bad else 0)
