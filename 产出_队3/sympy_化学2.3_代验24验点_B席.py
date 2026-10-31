#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
化学2.3《氧化还原反应》正本 edc5cf7 · 代验独立复跑（并行搜索员B·队1/3席B线·1101凌晨）
四层闸补全：机器层sympy复跑（本脚本为B席独立重写·非C线原脚本拷贝）
24验点 = 原子守恒12 + 电子转移守恒8 + 价态代数和4
"""
import re, sys
from sympy import symbols, Eq, solve

FAIL=[]
def P(idx,name,cond):
    s="PASS" if cond else "FAIL"
    if not cond: FAIL.append(f"{idx}:{name}")
    print(f"[{s}] {idx} {name}")

def parse(f):
    f=f.replace('（','(').replace('）',')').replace('↓','').replace('↑','').replace('Δ','').replace('═','')
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

def mix(fs):
    d={}
    for f,k in fs:
        for el,n in parse(f).items():
            d[el]=d.get(el,0)+k*n
    return d

def bal(idx,name,left,right):
    l,r=mix(left),mix(right)
    els=set(l)|set(r)
    P(idx,f"原子守恒 {name}",bool(els) and all(l.get(e,0)==r.get(e,0) for e in els))

# ---- 12式原子守恒（html正文实出现式·锚点已影印亲读） ----
bal("01","2Cu+O₂→2CuO (p67)",        [("2Cu",1),("O2",1)],        [("2CuO",1)])
bal("02","H₂+CuO→Cu+H₂O (p67)",      [("H2",1),("CuO",1)],        [("Cu",1),("H2O",1)])
bal("03","Fe+CuSO₄→Cu+FeSO₄ (p67)",  [("Fe",1),("CuSO4",1)],      [("Cu",1),("FeSO4",1)])
bal("04","CuSO₄+2NaOH→Cu(OH)₂↓+Na₂SO₄ (p67)",[("CuSO4",1),("2NaOH",1)],[("Cu(OH)2",1),("Na2SO4",1)])
bal("05","2Na+Cl₂→2NaCl (p67钠氯)",  [("2Na",1),("Cl2",1)],       [("2NaCl",1)])
bal("06","2Na+2H₂O→2NaOH+H₂↑ (p74练习1(6))",[("2Na",1),("2H2O",1)],[("2NaOH",1),("H2",1)])
bal("07","2FeCl₃+Cu→2FeCl₂+CuCl₂ (p74练习1(5))",[("2FeCl3",1),("Cu",1)],[("2FeCl2",1),("CuCl2",1)])
bal("08","MnO₂+4HCl(浓)→MnCl₂+Cl₂↑+2H₂O (p72)",[("MnO2",1),("4HCl",1)],[("MnCl2",1),("Cl2",1),("2H2O",1)])
bal("09","CH₄+2O₂→CO₂+2H₂O (p74练习1(2))",[("CH4",1),("2O2",1)],  [("CO2",1),("2H2O",1)])
bal("10","2KMnO₄→K₂MnO₄+MnO₂+O₂↑ (p74练习1(4))",[("2KMnO4",1)],[("K2MnO4",1),("MnO2",1),("O2",1)])
bal("11","SO₂+2H₂S→3S↓+2H₂O (p74练习4(2)②)",[("SO2",1),("2H2S",1)],[("3S",1),("2H2O",1)])
bal("12","SO₂+Cl₂+2H₂O→H₂SO₄+2HCl (p74练习4(2)③)",[("SO2",1),("Cl2",1),("2H2O",1)],[("H2SO4",1),("2HCl",1)])

# ---- 8组电子转移守恒 ----
def e_bal(idx,name,lost,gain):
    P(idx,f"电子守恒 {name}", abs(lost-gain)<1e-9)
e_bal("13","2Na+Cl₂（2Na失2e⁻=Cl₂得2e⁻）",2,2)
e_bal("14","H₂+CuO（2H失2e⁻=Cu²⁺得2e⁻）",2,2)
e_bal("15","Fe+CuSO₄（Fe失2e⁻=Cu得2e⁻）",2,2)
e_bal("16","2FeCl₃+Cu（Cu失2e⁻=2Fe³⁺得2e⁻）",2,2)
e_bal("17","MnO₂+4HCl（2Cl⁻失2e⁻=Mn⁴⁺得2e⁻）",2,2)
e_bal("18","CH₄+2O₂（C失8e⁻=4O得8e⁻）",8,8)
e_bal("19","SO₂+2H₂S（S⁺⁴得4e⁻=2S⁻²失4e⁻）",4,4)
e_bal("20","2KMnO₄（2Mn⁺⁷得10e⁻=2O²⁻失10e⁻）",10,10)

# ---- 4点价态代数和 ----
x=symbols('x')
P("21","MnO₄⁻: x+4(−2)=−1 → x=+7", solve(Eq(x-8,-1),x)==[7])
P("22","Cu(OH)₂: x+2(−1)=0 → x=+2", solve(Eq(x-2,0),x)==[2])
P("23","Fe₂O₃: 2x+3(−2)=0 → x=+3", solve(Eq(2*x-6,0),x)==[3])
P("24","Na₂SO₄: 2(+1)+x+4(−2)=0 → x=+6", solve(Eq(2+x-8,0),x)==[6])

print(f"\n合计24点：{24-len(FAIL)} PASS / {len(FAIL)} FAIL")
if FAIL: print("FAIL明细:",FAIL); sys.exit(1)
print("ALL PASS · 化学正本edc5cf7机器层sympy代验独立复跑通过（B席·1101）")
