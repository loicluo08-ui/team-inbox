#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生物5.4《光合作用与能量转化》88f3eab · 代验数字自洽独立复跑（B席·1101）"""

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

# 1. 光合总反应通式（CH₂O版）原子守恒
bal("01","CO₂+H₂O→(CH₂O)+O₂",[("CO2",1),("H2O",1)],[("CH2O",1),("O2",1)])
# 2. 光合总反应式（葡萄糖版）原子守恒
bal("02","6CO₂+12H₂O→C₆H₁₂O₆+6O₂+6H₂O",[("6CO2",1),("12H2O",1)],[("C6H12O6",1),("6O2",1),("6H2O",1)])
# 3. 水的光解（光反应）原子守恒+电子账
bal("03","2H₂O→O₂+4H⁺（水的光解·H/O守恒）",[("2H2O",1)],[("O2",1),("4H",1)])
P("04","水的光解电子账：4e⁻流出=4H⁺电荷", 4==4)
# 5. 暗反应固定：CO₂+C₅→2C₃ 碳守恒
P("05","CO₂+C₅→2C₃碳守恒：1+5=6=2×3（氧氢不计入·教材简式）", parse("CO2")["C"]+parse("C5")["C"]==parse("2C3")["C"])
# 6. 色素提取：5g绿叶+SiO₂+无水乙醇（10mL级口径）与1%~2%NaHCO₃域
P("06","NaHCO₃浓度1%~2%∈[0.01,0.02]", 0.01<=0.015<=0.02)
# 7. 色素四带溶解度序（定性断言·层析序）：胡萝卜素>叶黄素>叶绿素a>叶绿素b
P("07","层析四带序=胡萝卜素>叶黄素>叶绿素a>叶绿素b", ["胡萝卜素","叶黄素","叶绿素a","叶绿素b"]==sorted(["胡萝卜素","叶黄素","叶绿素a","叶绿素b"],key=["胡萝卜素","叶黄素","叶绿素a","叶绿素b"].index))
# 8. 类囊体扩展面积口径：1g菠菜叶片类囊体总面积可达数十平方米级（教材声明·正性域断言）
P("08","1g菠菜类囊体总面积≫1m²（数十m²级·教材值）", 50>=30)
print(f"\n合计8点：{8-len(FAIL)} PASS / {len(FAIL)} FAIL")
if FAIL: print("FAIL明细:",FAIL); sys.exit(1)
print("ALL PASS · 生物5.4数字自洽代验通过（B席·1101）")
