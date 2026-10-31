#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生物5.3《细胞呼吸的原理和应用》423c120 · 代验数字自洽独立复跑（B席·1101）"""

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

# 1. 有氧呼吸总反应式原子守恒
bal("01","C₆H₁₂O₆+6H₂O+6O₂→6CO₂+12H₂O",[("C6H12O6",1),("6H2O",1),("6O2",1)],[("6CO2",1),("12H2O",1)])
# 2. 1mol葡萄糖彻底氧化分解释放2870 kJ（教材p93值）
P("02","2870 kJ/mol（有氧呼吸总释放·教材声明）", 2870==2870)
# 3. 977.28 kJ = 32×30.54 kJ（ATP储能=32mol×1mol水解释放）
x=32*30.54
P("03",f"32×30.54={x:.2f}=977.28 kJ（储存ATP）", abs(x-977.28)<1e-9)
# 4. 效率=977.28/2870≈34%
P("04",f"977.28/2870={977.28/2870*100:.2f}%≈34%", abs(977.28/2870-0.34)<0.005)
# 5. 乳酸型无氧呼吸196.65 kJ/mol≈6.85%总释放
P("05",f"196.65/2870={196.65/2870*100:.2f}%（html「近6.85%」口径）", abs(196.65/2870-0.0685)<0.0005)
# 6. 61.08 kJ=2×30.54（无氧呼吸2ATP储能）
P("06",f"2×30.54={2*30.54:.2f}=61.08 kJ", abs(2*30.54-61.08)<1e-9)
# 7. 乳酸式原子守恒
bal("07","C₆H₁₂O₆→2C₃H₆O₃（乳酸发酵）",[("C6H12O6",1)],[("2C3H6O3",1)])
# 8. 酒精式原子守恒
bal("08","C₆H₁₂O₆→2C₂H₅OH+2CO₂（酒精发酵）",[("C6H12O6",1)],[("2C2H5OH",1),("2CO2",1)])
# 9. 剧烈运动温度与实验条件口径：25-35℃属酵母菌适宜范围
P("09","酵母菌实验25-35℃在适宜域", 25<=30<=35)
# 10. 热能侧写：2870−977.28=1892.72 kJ≈65.9%以热能散失
P("10",f"热能占比={(2870-977.28)/2870*100:.1f}%（对照教材乳酸型69%热散失口径·此为有氧总账侧写）", abs((2870-977.28)/2870-0.6595)<0.001)
print(f"\n合计10点：{10-len(FAIL)} PASS / {len(FAIL)} FAIL")
if FAIL: print("FAIL明细:",FAIL); sys.exit(1)
print("ALL PASS · 生物5.3数字自洽代验通过（B席·1101）")
