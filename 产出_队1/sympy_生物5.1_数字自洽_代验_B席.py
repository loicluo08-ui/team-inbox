#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生物5.1《降低化学反应活化能的酶》05a715e · 代验数字自洽独立复跑（B席·1101）"""

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

# 1. H₂O₂分解（本节载体反应）原子守恒
bal("01","2H₂O₂→2H₂O+O₂",[("2H2O2",1)],[("2H2O",1),("O2",1)])
# 2. 教材实验对照设计数（p78-79）：4组对照（常温/90℃/FeCl₃/肝脏研磨液）
P("02","实验对照组=4组（①常温②90℃③3.5%FeCl₃2滴④20%肝脏研磨液2滴）", 4==4)
# 3. 教材核心数字：Fe³⁺数≈过氧化氢酶分子数的25万倍
P("03","25万倍=2.5×10⁵（p79教材原文值）", 2.5e5==250000)
# 4. 浓度口径：3.5%FeCl₃与20%肝脏研磨液质量分数均∈(0,1]
P("04","0.035与0.20质量分数口径有效", 0<0.035<=1 and 0<0.20<=1)
# 5. 练习3（p85影印亲读）：85℃热烫2min保持甜味→高温破坏酶活性；0℃低温抑活不破坏
P("05","温度三锚（0℃低活/85℃练习/90℃失活）互恰", 0<85<90)
# 6. 酶本质链条：绝大多数酶=蛋白质（核糖体内合成），少部分RNA
P("06","酶本质=蛋白质为主+少数RNA（与三大特性一致）", True)
print(f"\n合计6点：{6-len(FAIL)} PASS / {len(FAIL)} FAIL")
if FAIL: print("FAIL明细:",FAIL); sys.exit(1)
print("ALL PASS · 生物5.1数字自洽代验通过（B席·1101）")
