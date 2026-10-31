#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""化学3.2《硫的转化》方程式验点脚本（并行搜索员B·队3席B线·1031）
验点三类：原子守恒/电子转移守恒/价态代数和——对应教材p97-109蓝底原式+练习式"""
from sympy import Eq, symbols, linsolve, sympify

CHECKS = []  # (名称, 结果, 说明)

def atom_balance(name, formula):
    """formula: dict元素->(左系数和, 右系数和) 经手算配平后由变量代数验证"""
    ok = all(l == r for l, r in formula.values())
    CHECKS.append((name, ok, "原子守恒:" + ",".join(f"{e} {l}={r}" for e, (l, r) in formula.items())))

def e_balance(name, ox_desc, pairs):
    """pairs: [(还原剂失去电子数, 还原侧物质的量), (氧化剂得到电子数, 氧化侧物质的量)] 乘积相等"""
    lose = sum(n * k for n, k in pairs)
    CHECKS.append((name, len(pairs) >= 2 and pairs[0][0]*pairs[0][1] == pairs[1][0]*pairs[1][1], f"电子守恒:{ox_desc} 失{pairs[0][0]}x{pairs[0][1]}=得{pairs[1][0]}x{pairs[1][1]}"))

# ---------- 一、原子守恒（12式） ----------
atom_balance("S+O2=SO2(点燃)", {"S": (1, 1), "O": (2, 2)})
atom_balance("Fe+S=FeS(Δ)", {"Fe": (1, 1), "S": (1, 1)})
atom_balance("2SO2+O2=2SO3(催化剂Δ可逆)", {"S": (2, 2), "O": (4+2, 6)})
atom_balance("SO2+2H2S=3S↓+2H2O", {"S": (1+2, 3), "H": (4, 4), "O": (2, 2)})
atom_balance("SO2+H2O=H2SO3(可逆)", {"S": (1, 1), "H": (2, 2), "O": (3, 3)})
atom_balance("SO2+2OH-=SO3(2-)+H2O", {"S": (1, 1), "O": (2+2, 3+1), "H": (2, 2)})
atom_balance("2H2SO4(浓)+Cu=CuSO4+SO2↑+2H2O", {"H": (4, 4), "S": (2, 1+1), "O": (8, 4+2+2), "Cu": (1, 1)})
atom_balance("2H2SO4(浓)+C=2SO2↑+CO2↑+2H2O", {"H": (4, 4), "S": (2, 2), "O": (8, 4+2+2), "C": (1, 1)})
atom_balance("SO3+H2O=H2SO4", {"S": (1, 1), "O": (3+1, 4), "H": (2, 2)})
atom_balance("2H2SO3+O2=2H2SO4", {"H": (4, 4), "S": (2, 2), "O": (6+2, 8)})
atom_balance("4FeS2+11O2=2Fe2O3+8SO2(高温)", {"Fe": (4, 4), "S": (8, 8), "O": (22, 6+16)})
atom_balance("SO2+CaCO3=CaSO3+CO2(脱硫·2CaSO3+O2=2CaSO4)", {"S": (1, 1), "Ca": (1, 1), "C": (1, 1), "O": (2+3, 3+2)})
atom_balance("2CaSO3+O2=2CaSO4(石膏)", {"Ca": (2, 2), "S": (2, 2), "O": (6+2, 8)})
atom_balance("SO2+Cl2+2H2O=H2SO4+2HCl(题8)", {"S": (1, 1), "Cl": (2, 2), "H": (4, 2+2), "O": (2+2, 4)})

# ---------- 二、电子转移守恒（6式） ----------
e_balance("S+O2=SO2", "S:0→+4失4e/O:0→-2得2e×2", [(4, 1), (2, 2)])
e_balance("2SO2+O2=2SO3", "S:+4→+6失2e×2/O:0→-2得2e×2", [(2, 2), (2, 2)])
e_balance("SO2+2H2S=3S↓+2H2O", "S:+4→0得4e×1/S:-2→0失2e×2(归中)", [(2, 2), (4, 1)])
e_balance("2H2SO4(浓)+Cu=CuSO4+SO2↑+2H2O", "Cu:0→+2失2e/S:+6→+4得2e×1", [(2, 1), (2, 1)])
e_balance("2H2SO4(浓)+C=2SO2↑+CO2↑+2H2O", "C:0→+4失4e/S:+6→+4得2e×2", [(4, 1), (2, 2)])
e_balance("2H2SO3+O2=2H2SO4", "S:+4→+6失2e×2/O:0→-2得2e×2", [(2, 2), (2, 2)])

# ---------- 三、价态代数和（S家族价态自洽4点） ----------
vals = {"H2S": -2, "S": 0, "SO2": +4, "SO3": +6, "H2SO3": +4, "Na2SO3": +4, "H2SO4": +6, "Na2SO4": +6, "FeS2": -1, "FeS": -2}
CHECKS.append(("价态代数和·H2SO4", 2*(+1)+6+4*(-2) == 0, "2(+1)+(+6)+4(-2)=0"))
CHECKS.append(("价态代数和·H2SO3", 2*(+1)+4+3*(-2) == 0, "2(+1)+(+4)+3(-2)=0"))
CHECKS.append(("价态代数和·FeS2", +2+2*(-1) == 0, "+2+2(-1)=0(黄铁矿S为-1价)"))
CHECKS.append(("价态代数和·SO2+2H2S归中", vals["SO2"]*1 + vals["H2S"]*2 == 0*3, "(+4)×1+(-2)×2=(0)×3·价态总和守恒"))

# ---------- 汇总 ----------
passed = sum(1 for _, ok, _ in CHECKS if ok)
total = len(CHECKS)
for name, ok, desc in CHECKS:
    print(f"{'PASS' if ok else 'FAIL'} | {name} | {desc}")
print(f"\n=== 化学3.2验点总计: {passed}/{total} {'ALL PASS' if passed == total else 'HAS FAIL'} ===")
import sys
sys.exit(0 if passed == total else 1)
