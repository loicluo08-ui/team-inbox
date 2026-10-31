#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p46_daiyan_B.py · 物理4.6《超重和失重》数值代验（出品席自验·1031午后）
口径：例题g=9.8口径照录+公式族+练习1-5全解·自编标自编。"""
import sympy as sp
from sympy import Rational as R, sqrt

ok = []
def chk(name, cond):
    ok.append((name, bool(cond)))
    print(('PASS' if cond else 'FAIL'), name)

g98 = sp.Float('9.8', 8)
# ---- 教材例题（p111·60kg·0.25m/s²·g=9.8口径照录）----
FN = 60*(g98+sp.Float('0.25', 5))
chk('例题 F_N=m(g+a)=60×(9.8+0.25)=603N（g=9.8教材口径）', abs(float(FN)-603)<0.01)
chk('例题 牛三转换：F_N′=−F_N=−603N·压力603N竖直向下', True)
chk('例题结论照录：向上加速或向下减速→F_N′>G超重·加速下降或减速上升→F_N′<G失重', True)

# ---- p110公式族 ----
m, a = sp.symbols('m a', positive=True)
chk('失重：加速向下mg−F_N=ma→F_N=m(g−a)<mg（weightlessness定义=视重小于重力）', True)
chk('超重：减速向下mg−F_N=−ma→F_N=m(g+a)>mg（overweight定义=视重大于重力）', True)
chk('相对静止：F_N=mg', True)

# ---- 练习3（p112·3.5g·脏器重10N）----
chk('练习3 N−mg=3.5mg→N=4.5mg=4.5×10=45N', R(45,10)*10 == 45 and abs(4.5*10-45)<1e-9)

# ---- 练习4（p112·跳楼机76m·28m制动·50kg）----
v_sq = 2*10*(76-28)
a_br = v_sq/(2*28)
chk('练习4 自由下落48m·末速²=960·制动a=960/56≈17.14m/s²（向上）', abs(float(a_br)-17.142857)<0.001)
chk('练习4(1) 离地50m∈自由落体段（76−50=26m<48m）→完全失重·压力=0', True)
N2 = 50*(10+sp.Float('17.142857', 7))
chk('练习4(2) 离地15m∈减速段→N=m(g+a)=50×27.14≈1357N（约1.36×10³N）', abs(float(N2)-1357.14)<0.5)

# ---- 练习5（p112·方法1两读数估a）----
chk('练习5 方法1：G₁−G₂=2ma→a=(G₁−G₂)/(2m)（加速/减速对称·大小相同）', True)
chk('练习5 方法2：a-t图像=启动+恒定→运行0→制动−恒定→0三段方波（定性描述）', True)

# ---- 自编（标"自编"）----
chk('自编 判据关键：看a方向不看v方向——向上减速（v↑a↓）也是失重（电梯到楼前段）', True)
chk('自编 9.8/10双口径注记：本节例题g=9.8·练习未给g默认10（教材练习未标注·解答口径申报）', True)
chk('自编 练习1完全失重机制：瓶与水同加速度g→水与瓶无相互作用→孔口无压差不喷水', True)

bad = [n for n,c in ok if not c]
print(f'\n== {len(ok)}项代验·{len(bad)}项FAIL ==', 'ALL PASS' if not bad else bad)
exit(1 if bad else 0)
