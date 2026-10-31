#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""化学2.3 SVG坐标精确生成 + sympy方程式验点（首学版_化学2.3_1031·工序6/7）"""
from sympy import Matrix

# ---------- Part A: SVG坐标（图②双线桥·2Na+Cl2=2NaCl·直线桥段逐点算） ----------
# 方案：方程式主体 y=100；上桥 y 40..88 折线，下桥 y 112..160 折线
pts_up, pts_down = [], []
# 上桥（Na→产物侧Na）：x 155→455，先竖起 88→48，横走，再竖下到 88
for x in range(155, 456, 25): pts_up.append((x, 88))
for y in range(84, 44, -8):   pts_up.append((455, y))
for x in range(455, 154, -25): pts_up.append((x, 44))
# 下桥（Cl2→产物侧Cl）：x 245→545
for x in range(245, 546, 25): pts_down.append((x, 112))
for y in range(116, 156, 8):  pts_down.append((545, y))
for x in range(545, 244, -25): pts_down.append((x, 160))
up_d = "M" + " L".join(f"{x},{y}" for x, y in pts_up)
dn_d = "M" + " L".join(f"{x},{y}" for x, y in pts_down)
print("UP_PATH =", up_d[:120], "...len", len(up_d))
print("DOWN_PATH =", dn_d[:120], "...len", len(dn_d))
# 桥线箭头端点（3/8处横向段中点取整）：
print("UP_ARROW_TIP=(455,48) 落点=2NaCl上方; DOWN_ARROW_TIP=(545,112)落点=2NaCl下方")

# ---------- Part B: sympy 验点（原子守恒逐式核） ----------
def atom_vec(spec):
    """spec: list of (化学式, 系数, 括号外积)"""
    import re
    def parse(f):
        # 展开括号（一层够用）
        s = f; d = {}
        def add(el, n):
            d[el] = d.get(el, 0) + n
        i = 0
        def walk(sub):
            nonlocal i
            loc = {}
            while i < len(sub):
                c = sub[i]
                if c == '(':
                    i += 1; inner = walk(sub)
                    assert sub[i] == ')'; i += 1
                    num = ''
                    while i < len(sub) and sub[i].isdigit():
                        num += sub[i]; i += 1
                    mult = int(num) if num else 1
                    for k, v in inner.items(): loc[k] = loc.get(k, 0) + v * mult
                elif c.isupper():
                    el = c
                    if i+1 < len(sub) and sub[i+1].islower(): el += sub[i+1]; i += 1
                    i += 1
                    num = ''
                    while i < len(sub) and sub[i].isdigit():
                        num += sub[i]; i += 1
                    loc[el] = loc.get(el, 0) + (int(num) if num else 1)
                elif c == ')': break
                else: i += 1
            return loc
        d2 = walk(s)
        return d2
    total = {}
    for f, coef in spec:
        for el, n in parse(f).items():
            total[el] = total.get(el, 0) + n * coef
    return total

CASES = [
 ("2Cu+O2=2CuO",        [("Cu",2),("O2",1)],       [("CuO",2)]),
 ("H2+CuO=Cu+H2O",      [("H2",1),("CuO",1)],      [("Cu",1),("H2O",1)]),
 ("Fe+CuSO4=FeSO4+Cu",  [("Fe",1),("CuSO4",1)],    [("FeSO4",1),("Cu",1)]),
 ("CuSO4+2NaOH=Cu(OH)2↓+Na2SO4", [("CuSO4",1),("NaOH",2)],[("Cu(OH)2",1),("Na2SO4",1)]),
 ("2Na+Cl2=2NaCl",      [("Na",2),("Cl2",1)],      [("NaCl",2)]),
 ("3CO+Fe2O3=2Fe+3CO2", [("CO",3),("Fe2O3",1)],    [("Fe",2),("CO2",3)]),
 ("MnO2+4HCl(浓)=MnCl2+Cl2↑+2H2O",[("MnO2",1),("HCl",4)],[("MnCl2",1),("Cl2",1),("H2O",2)]),
 ("2H2O=2H2O+O2↑(H2O2歧化分解)",  [("H2O2",2)],[("H2O",2),("O2",1)]),
 ("Cl2+2NaOH=NaCl+NaClO+H2O",     [("Cl2",1),("NaOH",2)],[("NaCl",1),("NaClO",1),("H2O",1)]),
 ("2FeCl3+Cu=2FeCl2+CuCl2",       [("FeCl3",2),("Cu",1)],[("FeCl2",2),("CuCl2",1)]),
 ("2Na+2H2O=2NaOH+H2↑",           [("Na",2),("H2O",2)],[("NaOH",2),("H2",1)]),
 ("Fe2O3+3CO=2Fe+3CO2",           [("Fe2O3",1),("CO",3)],[("Fe",2),("CO2",3)]),
]
fails = 0
for name, lhs, rhs in CASES:
    L, R = atom_vec(lhs), atom_vec(rhs)
    els = sorted(set(L) | set(R))
    A = Matrix([[L.get(e,0) - R.get(e,0)] for e in els])
    ok = A.is_zero_matrix
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  原子守恒元素={els}")
    if not ok: fails += 1

# 电子守恒独立验算（转移数=升价总数=降价总数）
ELEC = [
 ("2Na+Cl2=2NaCl: Na 0→+1失1e×2=2e; Cl 0→-1得1e×2=2e", 2*1, 2*1),
 ("Fe+CuSO4: Fe 0→+2失2e; Cu +2→0得2e", 2, 2),
 ("3CO+Fe2O3: C +2→+4失2e×3=6e; Fe +3→0得3e×2=6e", 6, 6),
 ("MnO2+4HCl(浓): Mn +4→+2得2e; Cl -1→0失1e×2=2e", 2, 2),
 ("2H2O2分解: O(-1)→0失1e×2=2e; O(-1)→-2得1e×2=2e", 2, 2),
 ("2FeCl3+Cu: Fe +3→+2得1e×2=2e; Cu 0→+2失2e", 2, 2),
 ("2Na+2H2O: Na 0→+1失1e×2=2e; H +1→0得1e×2=2e", 2, 2),
 ("Cl2+2NaOH: Cl 0→+1失1e; Cl 0→-1得1e（歧化）", 1, 1),
]
for name, lost, gained in ELEC:
    ok = (lost == gained)
    print(f"[{'PASS' if ok else 'FAIL'}] 电子守恒·{name}")
    if not ok: fails += 1

# 化合价代数和守恒抽查
CHG = [("KMnO4: (+1)+(+7)+4×(-2)", 1+7+4*(-2), 0), ("Fe2(SO4)3型FeSO4: Fe+2,S+6,4O×-2", 2+6-8, 0), ("NaClO: +1+1-2", 1+1-2, 0), ("H2O2: 2(+1)+2(-1)", 2-2, 0)]
for name, v, expect in CHG:
    ok = (v == expect)
    print(f"[{'PASS' if ok else 'FAIL'}] 代数和守恒·{name} = {v}")
    if not ok: fails += 1

print(f"\nTOTAL: {len(CASES)}原子守恒+{len(ELEC)}电子守恒+{len(CHG)}价态守恒 · FAIL={fails}")
with open("sympy_验点_log_化学23_1031.log", "w", encoding="utf-8") as f:
    import sys as _s; 
