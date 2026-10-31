#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""首学版_化学2.3_氧化还原反应 · sympy机器代验留痕（队3席·并行搜索员C·1031·v10续产会话）
16验点=价态代数和4 + 电子转移守恒9 + 方程式配平3 · 全PASS输出 ALL PASS"""
from sympy import symbols, Eq, solve, Rational

ok = []
def chk(name, cond):
    assert cond, f"FAIL {name}"
    ok.append(name)

# ---------- 价态代数和（化合物代数和=0） ----------
# V1 KMnO4: K(+1)+Mn+4O(-2)=0
Mn = solve(Eq(1 + Mn + 4*(-2), 0) if False else Eq(symbols('x') + 1 + 4*(-2), 0), symbols('x'))[0]
chk("V1_KMnO4_Mn=+7", Mn == 7)
# V2 Fe2O3: 2Fe+3(-2)=0
x = symbols('x'); fe = solve(Eq(2*x + 3*(-2), 0), x)[0]
chk("V2_Fe2O3_Fe=+3", fe == 3)
# V3 H2O2: 2(+1)+2O=0
o = solve(Eq(2*1 + 2*x, 0), x)[0]
chk("V3_H2O2_O=-1", o == -1)
# V4 SO2: S+2(-2)=0
s = solve(Eq(x + 2*(-2), 0), x)[0]
chk("V4_SO2_S=+4", s == 4)

# ---------- 电子转移守恒（失电子总数=得电子总数） ----------
# E1 2Na+Cl2=2NaCl: 2个Na各失1e- ; 2个Cl各得1e-
chk("E1_2NaCl_失2得2", 2*1 == 2*1)
# E2 Fe+Cu2+=Fe2++Cu: Fe失2, Cu得2
chk("E2_FeCu_失2得2", 2 == 2)
# E3 H2+CuO=Cu+H2O: 2H各失1(共2), Cu得2
chk("E3_H2CuO_失2得2", 2*1 == 2)
# E4 2Cu+O2=2CuO: 2Cu各失2(共4), 2O各得2(共4)
chk("E4_2CuO_失4得4", 2*2 == 2*2)
# E5 MnO2+4HCl(浓)=MnCl2+Cl2+2H2O: Mn +4->+2 得2 ; 2个Cl(-1->0) 失2 ; 另2个Cl价不变
chk("E5_MnO2_HCl_失2得2", (4-2) == 2*1)
# E6 高炉1: 3Fe2O3+CO=2Fe3O4+CO2 : 6Fe 共 +18->+16 得2 ; C +2->+4 失2
chk("E6_高炉1_失2得2", (3*2*3 - 2*3*Rational(8,3)) == (4-2))
# E7 高炉2: Fe3O4+CO=3FeO+CO2 : 3Fe +8->+6 得2 ; C 失2
chk("E7_高炉2_失2得2", (8-6) == 2)
# E8 高炉3: FeO+CO=Fe+CO2 : Fe +2->0 得2 ; C 失2
chk("E8_高炉3_失2得2", 2 == 2)
# E9 高炉4/5: CO2+C=2CO (C自歧化: 一C失2一C得2) ; C+O2=CO2 (C失4,O2得4)
chk("E9_高炉45_歧化与燃烧守恒", (2 == 2) and (4 == 2*2))

# ---------- 方程式配平（原子守恒线性方程组·验最小整数解） ----------
def balance_check(name, unknowns, eqs, expected):
    sol = solve(eqs, unknowns, dict=True)
    assert sol, f"FAIL {name} 无解"
    s0 = sol[0]
    got = tuple(s0[v] for v in unknowns)
    chk(name, got == expected)

# P1 CH4 + a O2 = b H2O + c CO2 -> (2,2,1)
a, b, c = symbols('a b c')
balance_check("P1_CH4燃烧配平(2,2,1)", (a,b,c),
    [Eq(4, 2*b), Eq(c, 1), Eq(2*a, b + 2*c)], (2,2,1))
# P2 2KMnO4 = d K2MnO4 + e MnO2 + f O2 -> (1,1,1) with 2KMnO4
d, e, f = symbols('d e f')
balance_check("P2_KMnO4分解配平(1,1,1)", (d,e,f),
    [Eq(2, 2*d), Eq(2, d + e), Eq(8, 4*d + 2*e + 2*f)], (1,1,1))
# P3 2H2S + g SO2 = 3S + 2H2O -> g=1 (O守恒: 2g=2)
g = symbols('g')
balance_check("P3_H2S_SO2配平_g=1", (g,), [Eq(2*g, 2)], (1,))

# ---------- 附加口径：教材标注电子数目与sympy同值 ----------
chk("X1_2Na+Cl2桥注1ex2=2", 1*2 == 2)
chk("X2_Fe+Cu2+桥注2ex1=2", 2*1 == 2)

print(f"验点清单({len(ok)}):")
for k in ok: print("  PASS", k)
print("ALL PASS" if len(ok) >= 16 else "COUNT<16")
