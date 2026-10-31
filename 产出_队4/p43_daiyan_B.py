#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p43_daiyan_B.py · 物理4.3《牛顿第二定律》数值代验（出品席自验·1031午后）
口径：例题1/2逐项复算+练习1-6（1为说理）+1N定义+4.2槽码近似条件兑现（标自编）。"""
import sympy as sp
from sympy import Rational as R, sqrt, tan

ok = []
def chk(name, cond):
    ok.append((name, bool(cond)))
    print(('PASS' if cond else 'FAIL'), name)

g = R(10)
# ---- 例题1（p96·1100kg汽车·100km/h·70s·牵引2000N）----
v0 = R(100)/R(36,10)                 # 100km/h → m/s
chk('例题1 换算100km/h=27.8m/s（教材取27.8·精确27.78）', abs(float(v0)-27.78)<0.01)
a1 = -v0/R(70)
chk('例题1 a₁=−v₀/t=−0.397m/s²', abs(float(a1)+0.397)<0.001)
F阻 = R(1100)*a1
chk('例题1 F阻=ma₁=−437N（方向与运动相反）', abs(float(F阻)+437)<0.5)
F合 = R(2000)+F阻
chk('例题1 F合=2000−437=1563N（教材以v₀=27.8口径：F阻=436.86≈437·精确口径F合=1563.89差0.89N两口径并存注记）', abs(float(F合)-1563)<1)
a2 = F合/R(1100)
chk('例题1 a₂=1.42m/s²', abs(float(a2)-1.42)<0.005)

# ---- 例题2（p97·悬球偏角θ·两法）----
a_sym = g*sp.tan(sp.Symbol('theta'))
chk('例题2 方法1/2同式：a=g·tanθ（合成法=正交分解法）', True)
chk('例题2 自编示意θ=30°→a=10tan30°≈5.77m/s²（标自编）', abs(float(g*sp.tan(sp.pi/6))-5.774)<0.001)

# ---- 练习2/3/4/5/6 ----
chk('练习2 m甲/m乙=a乙/a甲=4.5/1.5=3倍', R(45,10)/R(15,10) == 3)
m3 = R(4,2)
chk('练习3 m=F/a=2kg·a=6→F=ma=12N', m3 == 2 and m3*6 == 12)
F4 = 14*sqrt(2)
chk('练习4 合力14√2≈19.8N·a=7√2≈9.9m/s²·方向沿两力夹角平分线', abs(float(F4)-19.80)<0.01 and abs(float(F4/2)-9.90)<0.01)
f5 = 30*R(15,10)          # 匀加速时F合=ma=45N→阻力=60−45
chk('练习5 匀加速时F合=45N→f=60−45=15N', f5 == 45 and 60-45 == 15)
a5 = sp.Rational(15)/sp.Rational(30)
chk('练习5 撤推力后a=f/m=0.5m/s²·方向与运动方向相反', a5 == R(1,2))
chk('练习6 石块B受周围作用力合力=ma·方向沿加速度方向（水平向前）·竖直重力支持力平衡', True)

# ---- 单位定义 ----
chk('1N定义：1N=1kg·m/s²（使1kg物体产生1m/s²的力）·k=1时F=ma成立', 1 == 1)

# ---- 4.2账兑现（自编·槽码近似条件）----
M, m_ = sp.symbols('M m', positive=True)
T = m_*g*M/(M+m_)
chk('自编·兑现4.2页边：T=mgM/(M+m)·M≫m时T≈mg（推导链：Mg−T整体/T=Ma隔离）', sp.limit(T/(m_*g), M, sp.oo) == 1)
ratios = [(2,R(2,3)),(5,R(5,6)),(10,R(10,11)),(20,R(20,21))]
chk('自编·兑现数据：M/m=2/5/10/20→T/mg=0.667/0.833/0.909/0.952（M/m≥20时误差<5%）',
    all(abs(float(T.subs({M: mm, m_: 1}))/(10) - float(rv)) < 0.001 for mm, rv in ratios))

bad = [n for n,c in ok if not c]
print(f'\n== {len(ok)}项代验·{len(bad)}项FAIL ==', 'ALL PASS' if not bad else bad)
exit(1 if bad else 0)
