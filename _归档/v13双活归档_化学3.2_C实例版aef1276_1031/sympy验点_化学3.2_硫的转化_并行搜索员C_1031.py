#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""化学3.2 硫的转化 · sympy机器验点 v1（并行搜索员C·队3席·1031）
验点范围：主件html全部化学方程式16条（零空间法配平逐元素复核）+ p109练习12黄铁矿计算。
输出：逐条PASS/FAIL + 计算留痕。"""
from sympy import Matrix, Rational
from math import gcd
from functools import reduce

def balance_check(name, reactants, products, note=""):
    """reactants/products: 各物质{元素:原子数}列表；零空间求最小正整数系数组"""
    els = sorted({e for d in reactants + products for e in d})
    A = Matrix([[d.get(e, 0) for d in reactants] + [-(d.get(e, 0)) for d in products] for e in els])
    ns = A.nullspace()
    ok = len(ns) >= 1
    detail = "无零空间解"
    if ok:
        v = ns[0]
        L = reduce(lambda a, b: a * b, [t.q for t in v])
        ints = [int(t * L) for t in v]
        g = reduce(gcd, [abs(i) for i in ints if i != 0])
        ints = [i // g for i in ints]
        if all(i > 0 for i in ints):
            detail = "系数=" + str(ints)
        else:
            ok = False; detail = "系数含非正项:" + str(ints)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail} {note}")
    return ok

results = []

results.append(balance_check("1  S+O2=SO2(点燃)",
    [{"S":1},{"O":2}], [{"S":1,"O":2}]))
results.append(balance_check("2  Fe+S=FeS(Δ)",
    [{"Fe":1},{"S":1}], [{"Fe":1,"S":1}]))
results.append(balance_check("3  2SO2+O2⇌2SO3(催化剂Δ)",
    [{"S":2,"O":4},{"O":2}], [{"S":2,"O":6}], "(预配系数2/1/2复核)"))
results.append(balance_check("4  SO2+2H2S=3S↓+2H2O",
    [{"S":1,"O":2},{"S":2,"H":4}], [{"S":3},{"H":4,"O":2}]))
results.append(balance_check("5  SO2+H2O⇌H2SO3",
    [{"S":1,"O":2},{"H":2,"O":1}], [{"S":1,"O":3,"H":2}]))
results.append(balance_check("6  SO2+2OH-=SO3^2-+H2O(离子式)",
    [{"S":1,"O":2},{"O":2,"H":2}], [{"S":1,"O":3},{"H":2,"O":1}]))
results.append(balance_check("7  2H2SO4(浓)+Cu=CuSO4+SO2↑+2H2O",
    [{"H":4,"S":2,"O":8},{"Cu":1}], [{"Cu":1,"S":1,"O":4},{"S":1,"O":2},{"H":4,"O":2}]))
results.append(balance_check("8  2H2SO4(浓)+C=2SO2↑+CO2↑+2H2O",
    [{"H":4,"S":2,"O":8},{"C":1}], [{"S":2,"O":4},{"C":1,"O":2},{"H":4,"O":2}]))
results.append(balance_check("9  SO3+H2O=H2SO4",
    [{"S":1,"O":3},{"H":2,"O":1}], [{"S":1,"O":4,"H":2}]))
results.append(balance_check("10 2H2SO3+O2=2H2SO4",
    [{"S":2,"O":6,"H":4},{"O":2}], [{"S":2,"O":8,"H":4}]))
results.append(balance_check("11 4FeS2+11O2=2Fe2O3+8SO2(高温)",
    [{"Fe":4,"S":8},{"O":22}], [{"Fe":4,"O":6},{"S":8,"O":16}]))
results.append(balance_check("12 SO2+CaCO3=CaSO3+CO2(脱硫·自编)",
    [{"S":1,"O":2},{"Ca":1,"C":1,"O":3}], [{"Ca":1,"S":1,"O":3},{"C":1,"O":2}]))
results.append(balance_check("13 2CaSO3+O2=2CaSO4(脱硫·自编)",
    [{"Ca":2,"S":2,"O":6},{"O":2}], [{"Ca":2,"S":2,"O":8}]))
results.append(balance_check("14 SO2+Cl2+2H2O=H2SO4+2HCl(练习8答案侧·自编)",
    [{"S":1,"O":2},{"Cl":2},{"H":4,"O":2}], [{"S":1,"O":4,"H":2},{"H":2,"Cl":2}]))
results.append(balance_check("15 BaSO3+2HCl=BaCl2+SO2↑+H2O(练习9答案侧·自编)",
    [{"Ba":1,"S":1,"O":3},{"H":2,"Cl":2}], [{"Ba":1,"Cl":2},{"S":1,"O":2},{"H":2,"O":1}]))
results.append(balance_check("16 BaSO3+H2SO4=BaSO4+SO2↑+H2O(练习9答案侧·自编)",
    [{"Ba":1,"S":1,"O":3},{"S":1,"O":4,"H":2}], [{"Ba":1,"S":1,"O":4},{"S":1,"O":2},{"H":2,"O":1}]))

# 练习12：1吨含杂质25%黄铁矿 → 98%浓硫酸（S损失为零）
m_ore = Rational(1000)                       # kg
m_feS2 = m_ore * Rational(75, 100)           # 750 kg
M_feS2 = Rational(56 + 2 * 32, 1000)         # 0.120 kg/mol
n_feS2 = m_feS2 / M_feS2
n_h2so4 = n_feS2 * 2                         # FeS2→2H2SO4（S守恒）
m_pure = n_h2so4 * Rational(98, 1000)        # kg
m_solution = m_pure / Rational(98, 100)      # 98%浓硫酸 kg
print(f"\n练习12留痕：m(FeS2)={m_feS2} kg · M=0.120 kg/mol · n(FeS2)={n_feS2} mol")
print(f"  n(H2SO4)=2n={n_h2so4} mol · m(纯H2SO4)={m_pure} kg · m(98%溶液)={m_solution} kg")
r12 = (m_solution == Rational(1250))
print(f"[{'PASS' if r12 else 'FAIL'}] 练习12 = {m_solution} kg（1.25吨）")
results.append(r12)

print(f"\n合计：{sum(1 for r in results if r)}/{len(results)} PASS")
print("ALL PASS" if all(results) else "HAS FAIL")
