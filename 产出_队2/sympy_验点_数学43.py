# -*- coding: utf-8 -*-
"""数学4.3《对数》sympy验点·并行搜索员B·队2席·1031·承3.4/4.1先例"""
import sympy as sp
from sympy import log as L, sqrt as sq, Rational as R, symbols, Eq, N, expand, simplify
from sympy import E as eE, pi
from sympy.core.relational import Eq as REq
res = []
def chk(name, expr, expect):
    try:
        v = simplify(expr)
        tol = max(1e-9, abs(float(expect))*2e-4) if not isinstance(expect,str) else 1e-9
        ok = bool(abs(float(N(v)) - float(expect)) < tol) if not isinstance(expect, str) else None
        if ok is None:
            res.append((name, "SKIP")); return
        res.append((name, "PASS" if ok else f"FAIL v={N(v,6)} exp={expect}"))
    except Exception as ex:
        res.append((name, f"ERR {str(ex)[:50]}"))
def chkeq(name, left, right):
    try:
        ok = bool(simplify(left - right) == 0)
        res.append((name, "PASS" if ok else f"FAIL d={N(simplify(left-right),6)}"))
    except Exception as ex:
        res.append((name, f"ERR {str(ex)[:50]}"))

# 例1 互化
chkeq("P01_log5_625", L(625,5), 4)
chkeq("P02_log2_1/64", L(R(1,64),2), -6)
chkeq("P03_(1/2)^-4=16", R(1,2)**(-4), 16)
chkeq("P04_lg0.01", L(R(1,100),10), -2)
chk("P05_ln10", N(L(10,eE),6), 2.302585)
# 例2 求x
chkeq("P06_64^(-2/3)", R(64,1)**(R(-2,3)), R(1,16))
chkeq("P07_8^(1/6)=sqrt2", R(8,1)**(R(1,6)), sq(2))
x = symbols('x')
sol8 = sp.solve(REq(-L(eE**2, eE), x), x)
res.append(("P08_lne2=-2解x", "PASS" if float(N(sol8[0] - (-2))) < 1e-9 else f"FAIL {sol8}"))
# 例3
chkeq("P09_lgsqrt100", L(sq(100),10), 1)
chkeq("P10_log2(4^7*2^5)", L(R(4,1)**7*R(2,1)**5,2), 19)
# 练习1
chkeq("P11_log3(27*9^2)", L(R(27,1)*R(9,1)**2,3), 7)
chkeq("P12_lg5+lg2", L(5,10)+L(2,10), 1)
chkeq("P13_ln3+ln1/3", L(3,eE)+L(R(1,3),eE), 0)
chkeq("P14_log35-log315", L(5,3)-L(15,3), -1)
# 例4 ln(x²√y/√z)
X,Y,Z = symbols('X Y Z', positive=True)
lhs = L(X**2*sq(Y)/sq(Z), eE); rhs = 2*L(X,eE)+R(1,2)*L(Y,eE)-R(1,2)*L(Z,eE)
chkeq("P15_例4恒等", expand_log := sp.expand_log(lhs, force=True), rhs)
# 换底公式
chkeq("P16_换底log2_3", L(3,2), L(3,10)/L(2,10))
chk("P17_lg2/lg1.11≈6.6422", N(L(R(2,1),10)/L(R(111,100),10),4), 6.6422)
# 例5 地震
chkeq("P18_dLgE=1.5", (R(48,10)+R(15,10)*R(9,1))-(R(48,10)+R(15,10)*R(8,1)), R(3,2))
chk("P19_10^1.5≈31.6→32", N(10**R(3,2),4), 31.6228)
chk("P20_E1/E2≈31.62→32", N(10**R(3,2),4), 31.6228)
# 习题T3
chkeq("P21_T3(1)log2_2+log2_1/2", L(2,2)+L(R(1,2),2), 0)
chkeq("P22_T3(3)lg1/4-lg25", L(R(1,4),10)-L(25,10), -2)
chkeq("P23_T3(4)", 2*L(25,5)-3*L(64,2), -14)
chkeq("P24_T3(5)", L(L(16,2),2), 2)
chkeq("P25_T3(6)", L(25,5)*L(4,2)*L(9,3), 8)
# T4(4) log8[log4(log3 x)]=0 → x=81
chkeq("P26_T4(4)x=81", L(L(L(81,3),4),8), 0)
# T6(1) xlog3(4)=1 → 4^x+4^-x=10/3
xx = symbols('xx', positive=True)
xxv = sp.solve(REq(xx*L(4,3), 1), xx)[0]
chkeq("P27_T6(1)值", R(4,1)**xxv + R(4,1)**(-xxv), R(10,3))
# T7(1) logab·logbc·logca=1
A,B,C = symbols('A B C', positive=True)
chkeq("P28_T7(1)恒等", L(B,A)*L(C,B)*L(A,C), 1)
# T8 GDP翻两番
t8 = L(4,10)/L(R(1065,1000),10)
chk("P29_翻两番≈22.0年", N(t8,4), 22.0134)
# T9 (1.01/0.99)^365
chk("P30_T9(1)倍数≈1480", N((R(101,100)/R(99,100))**365,4), 1480.66)
t10_ = L(10,10)/L(R(101,100)/R(99,100),10)
chk("P31_T9(2)10倍≈115.1天", N(t10_,3), 115.125)
# T10 酒驾 100(0.7)^t<20 → t>log0.2/log0.7≈4.512→至少5h
t_ = L(R(1,5),10)/L(R(7,10),10)
chk("P32_T10临界≈4.51", N(t_,4), 4.512)
v33 = float(N(100*R(7,10)**5))
res.append(("P33_5h后16.8<20", "PASS" if v33 < 20 else f"FAIL v={v33}"))
# 基本性质
chkeq("P34_loga1=0", L(1,7), 0)
chkeq("P35_loga_a=1", L(7,7), 1)
n_pass = sum(1 for _,s in res if s=="PASS")
n_fail = sum(1 for _,s in res if s.startswith("FAIL") or s.startswith("ERR"))
for nm, s in res: print(f"{nm}: {s}")
print(f"== TOTAL {len(res)} | PASS {n_pass} | FAIL/ERR {n_fail} ==")
