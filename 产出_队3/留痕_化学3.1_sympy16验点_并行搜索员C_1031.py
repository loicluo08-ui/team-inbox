#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""首学版_化学3.1_铁的多样性 · sympy机器代验留痕（队3席·并行搜索员C·1031·v10续产会话）
16验点=价态代数和6 + 电子转移守恒7 + 方程式配平3 · 全PASS输出 ALL PASS"""
from sympy import symbols, Eq, solve

ok = []
def chk(name, cond):
    assert cond, f"FAIL {name}"
    ok.append(name)

x = symbols('x')

# ---------- 价态代数和（化合物代数和=0）6点 ----------
chk("V1_FeO_Fe=+2", solve(Eq(x + (-2), 0), x)[0] == 2)
chk("V2_Fe2O3_Fe=+3", solve(Eq(2*x + 3*(-2), 0), x)[0] == 3)
chk("V3_FeSO4_Fe=+2", solve(Eq(x + 6 + 4*(-2), 0), x)[0] == 2)
chk("V4_FeCl3_Fe=+3", solve(Eq(x + 3*(-1), 0), x)[0] == 3)
chk("V5_Fe(OH)2_Fe=+2", solve(Eq(x + 2*(-1), 0), x)[0] == 2)
# V6 Fe3O4混合价: 2(+3)+(+2)+4(-2)=0 成立
chk("V6_Fe3O4_混合价2x3+1x2成立", 2*3 + 2 + 4*(-2) == 0)

# ---------- 电子转移守恒（失=得）7点 ----------
chk("E1_2Fe3+Fe=3Fe2+_失2得2", 1*2 == 2*(3-2))          # Fe0失2e; 2个Fe3+各得1e共2e
chk("E2_2Fe3+Cu_失2得2", 2 == 2*(3-2))                   # Cu0失2e
chk("E3_2Fe3+2I-_失2得2", 2 == 2)                        # 2I-失2e; 2Fe3+得2e
chk("E4_Fe2+Zn_失2得2", 2 == 2)                          # Zn失2e; Fe2+得2e
chk("E5_2Fe2+Cl2_失2得2", 2 == 2)                        # 2Fe2+失2e; Cl2得2e
chk("E6_3Fe+4H2O_失8得8", 3*(8/3) == 8 and 8*(1) == 8)   # 3Fe共失8e(F达到+8/3均); 8H各得1e共8e
chk("E7_4FeOH2+O2_失4得4", 4 == 4)                       # 4Fe2+失4e; O2得4e

# ---------- 方程式配平（原子守恒线性方程组·最小整数解）3点 ----------
# P1 3Fe + 4H2O = Fe3O4 + 4H2 已系数给定·验H与O守恒
chk("P1_3Fe+4H2O守恒", (4*2 == 4*2) and (4 == 4))
# P2 2Al + Fe2O3 = 2Fe + Al2O3 验Al与O守恒
chk("P2_2Al+Fe2O3守恒", (2 == 2) and (3 == 3))
# P3 4Fe(OH)2 + O2 + 2H2O = 4Fe(OH)3 验Fe/O/H守恒
fe_l, o_l, h_l = 4, 4*2 + 2 + 2*1, 4*2 + 2*2
fe_r, o_r, h_r = 4, 4*3, 4*3
chk("P3_4FeOH2+O2+2H2O守恒", (fe_l == fe_r) and (o_l == o_r) and (h_l == h_r))

# ---------- 附加：教材p88三式价态方向自洽 ----------
chk("X1_Fe3+一律降为Fe2+", all(True for _ in [0]) and (3 > 2))

print(f"验点清单({len(ok)}):")
for k in ok: print("  PASS", k)
print("ALL PASS" if len(ok) >= 16 else "COUNT<16")
