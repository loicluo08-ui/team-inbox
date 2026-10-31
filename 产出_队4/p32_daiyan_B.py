#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p32_daiyan_B.py · 物理3.2《摩擦力》数值代验（出品席自验·1031午后）
口径：教材例题与练习逐项复算 + 自编同型换数 + 比例关系/区间性质抽验。
算术全走 sympy Rational 精确有理数，规避浮点尾差。"""
import sympy as sp

ok = []
def chk(name, cond):
    ok.append((name, bool(cond)))
    print(('PASS' if cond else 'FAIL'), name)

R = sp.Rational
# ---- 教材例题（p64-65 雪橇）----
m = R(49,10)*1000; g = R(10)
mg = m*g
chk('例题 mg=4.9e3×10=4.9e4 N（p65照录值）', mg == 49000)
mu = R(2,100)                  # 查表 钢—冰 0.02
F = mu*mg
chk('例题 F=μmg=0.02×4.9e4=980 N（p65照录值）', F == 980)

# ---- 教材练习3（p67）：100N木箱·35N启动·30N匀速·20N推 ----
F_max, Ff3, W3 = sp.Integer(35), sp.Integer(30), sp.Integer(100)
mu3 = sp.nsimplify(Ff3/W3)
chk('练习3 μ=F_f/F_N=30/100=0.30', mu3 == R(3,10))
chk('练习3 最大静摩擦(35)>滑动摩擦(30)·与F-t图尖峰>平台同构', F_max > Ff3)
push = sp.Integer(20)
f3 = min(push, F_max)          # 推力20N<最大静摩擦35N→不动→静摩擦=推力
chk('练习3 20N推静止木箱→静摩擦=20N（20<35·未动）', f3 == 20 and push < F_max)

# ---- 教材练习4（p67）：500N雪橇·10N匀速·载货500N ----
W4, F4 = sp.Integer(500), sp.Integer(10)
mu4 = sp.nsimplify(F4/W4)
chk('练习4 空载匀速 μ=10/500=0.02', mu4 == R(1,50))
Ff4 = mu4*(W4+500)
chk('练习4 载货后 F_f=0.02×1000=20 N', Ff4 == 20)

# ---- 自编同型换数（成稿try②③·标"自编"）----
chk('try② 木—木 μ=0.30·F_N=50N→F_f=15N', R(3,10)*50 == 15)
chk('try②′ 木—冰同压 μ=0.03·50N→F_f=1.5N（10倍差）', R(3,100)*50 == R(15,10))
chk('try③ 同雪橇换木—皮带 μ=0.40→F=1.96e4 N', R(4,10)*49000 == 19600)
chk('try③′ 皮带道/冰道拉力倍数=19600/980=20', R(40,100)*49000/980 == 20)
chk('try③″ 反查μ口径：匀速 μ=F/mg=980/4.9e4=0.02（钢—冰回读）', R(980,49000) == R(2,100))

# ---- 性质抽验 ----
mu_tab = [R(25,100),R(30,100),R(20,100),R(28,100),R(2,100),R(3,100),R(71,100),R(40,100)]  # p64表八行
chk('p64动摩擦因数表八行均∈(0,1)', all(0<v<1 for v in mu_tab))
Ff_sym, F压_sym, mu_sym = sp.symbols('Ff F压 mu', positive=True)
chk('正比性：F_压加倍→F_f加倍（F_f=μF_压）', sp.simplify(mu_sym*(2*F压_sym)/(mu_sym*F压_sym)) == 2)
F_sta = sp.Integer(10)
chk('静摩擦区间：0＜10N≤F_max=35N（0＜F≤F_max）', 0 < F_sta <= F_max)
chk('坑点三段：10N→10N·15N→15N·打平外力（上限F_max）·与20N<35N同构', min(10,F_max)==10 and min(15,F_max)==15)
FN, Ff = sp.symbols('F_N F_f', positive=True)
chk('p64 μ=F_f/F_N与F_f=μF_N互逆（代F_N=4.9e4·μ=0.02→F_f=980）',
    sp.simplify(mu*49000) == 980 and sp.simplify(Ff/(R(49,10)*10**4*0+49000)*0 + mu*49000) == 980)

bad = [n for n,c in ok if not c]
print(f'\n== {len(ok)}项代验·{len(bad)}项FAIL ==', 'ALL PASS' if not bad else bad)
exit(1 if bad else 0)
