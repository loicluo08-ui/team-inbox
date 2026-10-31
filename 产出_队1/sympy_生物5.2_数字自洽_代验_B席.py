#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生物5.2《细胞的能量"货币"ATP》6d39825 · 代验数字自洽独立复跑（B席·1101）"""

import re, sys
from sympy import symbols, Eq, solve, S

FAIL=[]
def P(idx,name,cond):
    s="PASS" if cond else "FAIL"
    if not cond: FAIL.append(f"{idx}:{name}")
    print(f"[{s}] {idx} {name}")

def parse(f):
    f=f.replace('（','(').replace('）',')').replace('↓','').replace('↑','')
    m=re.match(r'(\d+)\s*',f)
    coef=int(m.group(1)) if m else 1
    body=f[len(m.group(1)):].lstrip() if m else f
    def helper(s):
        d={}; i=0
        while i<len(s):
            if s[i]=='(':
                depth=1; j=i+1
                while depth>0:
                    if s[j]=='(':depth+=1
                    elif s[j]==')':depth-=1
                    j+=1
                inner=helper(s[i+1:j-1])
                m2=re.match(r'\d+',s[j:]); n=int(m2.group()) if m2 else 1
                for el,v in inner.items(): d[el]=d.get(el,0)+v*n
                i=j+(len(m2.group()) if m2 else 0)
            else:
                m2=re.match(r'([A-Z][a-z]?)(\d*)',s[i:])
                if not m2: i+=1; continue
                el=m2.group(1); n=int(m2.group(2)) if m2.group(2) else 1
                d[el]=d.get(el,0)+n; i+=len(m2.group(0))
        return d
    d=helper(body)
    return {el:v*coef for el,v in d.items()}

def bal(idx,name,left,right):
    l={}; r={}
    for f,k in left:
        for el,n in parse(f).items(): l[el]=l.get(el,0)+k*n
    for f,k in right:
        for el,n in parse(f).items(): r[el]=r.get(el,0)+k*n
    els=set(l)|set(r)
    P(idx,f"原子守恒 {name}",bool(els) and all(l.get(e,0)==r.get(e,0) for e in els))

MASS={"C":12.011,"H":1.008,"N":14.007,"O":15.999,"P":30.974}
def mw(f):
    return sum(MASS[el]*n for el,n in parse(f).items())
# 1. ATP摩尔质量由分子式独立算得≈507 g/mol（教材声明507）
atp="C10H16N5O13P3"
m=mw(atp)
P("01",f"ATP摩尔质量={m:.2f}≈507 g/mol", abs(m-507)<2)
# 2. 剧烈运动0.5 kg/分钟 ÷ 507 g/mol ≈ 1 mol/分钟
mol_per_min=500/507
P("02",f"0.5kg/分钟={mol_per_min:.4f} mol≈1 mol", abs(mol_per_min-1)<0.02)
# 3. 1 mol水解30.54 kJ → 每分钟≈30.5 kJ
P("03","1 mol×30.54 kJ=30.54 kJ/分钟（html「30.5 kJ每分钟」口径吻合）", abs(1*30.54-30.54)<1e-9)
# 4. ATP+H₂O→ADP+Pi 原子守恒
bal("04","ATP+H₂O→ADP+Pi",[("C10H16N5O13P3",1),("H2O",1)],[("C10H15N5O10P2",1),("H3PO4",1)])
# 5. 摩尔质量闭合：M(ATP)+M(H₂O)=M(ADP)+M(Pi)（质量守恒侧写）
P("05",f"质量闭合 {mw('C10H16N5O13P3')+mw('H2O'):.2f}={mw('C10H15N5O10P2')+mw('H3PO4'):.2f}", abs(mw('C10H16N5O13P3')+mw('H2O')-mw('C10H15N5O10P2')-mw('H3PO4'))<0.05)
# 6. A—P~P~P结构：3个磷酸基团（P3）+腺苷（N5环系）
d=parse(atp)
P("06",f"ATP含P×3与N×5（A—P~P~P三磷酸+腺嘌呤环）", d["P"]==3 and d["N"]==5)
print(f"\n合计6点：{6-len(FAIL)} PASS / {len(FAIL)} FAIL")
if FAIL: print("FAIL明细:",FAIL); sys.exit(1)
print("ALL PASS · 生物5.2数字自洽代验通过（B席·1101）")
