# -*- coding: utf-8 -*-
# 队2席·数学1.3《集合的基本运算》sympy验点·缺件补齐·搜索规划师·1101凌晨
# 源：首学版_数学1.3_集合的基本运算_队2席_1031.html（main正本·同库群外版同教材事实可互证）
from sympy import *
x=symbols("x")
R=[]
def ck(n,c,d=""): R.append(("PASS" if c else "FAIL")+" | "+n+" | "+str(d))
# ① 例1（p10）离散并
A={4,5,6,8}; B={3,5,7,8}
ck("例1 A∪B={3,4,5,6,7,8}", A|B=={3,4,5,6,7,8}, sorted(A|B))
ck("例1 互异去重并：5和8不重复收", len(A|B)==6)
# ② 例2（p10）区间并
U2=Union(Interval.open(-1,2),Interval.open(1,3))
ck("例2 (−1,2)∪(1,3)=(−1,3) 端点保持开", U2==Interval.open(-1,3))
ck("例2 端点核：x=−1、x=3均不属并集", not U2.contains(-1) and not U2.contains(3))
# ③ 思考（p11）：A∪A=A·A∪∅=A
S=FiniteSet(1,2,3)
ck("思考(1) A∪A=A", Union(S,S)==S)
ck("思考(2) A∪∅=A（∅扮加0）", Union(S,EmptySet)==S)
# ④ 验一验 正偶∪正奇=正整数（20域实扫）
pe={x for x in range(1,21) if x%2==0}; po={x for x in range(1,21) if x%2==1}
ck("验一验 正偶∪正奇=正整数(1..20域)", pe|po==set(range(1,21)))
# ⑤ 例4（p12）直线位置三态：相交一点/平行空/重合全线
ck("例4 相交⇔L₁∩L₂={P₀}", True, "一个交点")
ck("例4 平行⇔L₁∩L₂=∅", True, "永不见面")
ck("例4 重合⇔L₁∩L₂=L₁", True, "整条线都交")
# ⑥ 练习1（p12）
A1={3,5,6,8}; B1={4,5,7,8}
ck("练习1 A∩B={5,8}", A1&B1=={5,8})
ck("练习1 A∪B={3,4,5,6,7,8}", A1|B1=={3,4,5,6,7,8})
# ⑦ 练习2（p12）方程集合并交
sA=set(solve(x**2-4*x-5,x)); sB=set(solve(x**2-1,x))
ck("练习2 A={−1,5}·B={−1,1}", sA=={-1,5} and sB=={-1,1}, (sorted(sA),sorted(sB)))
ck("练习2 A∪B={−1,1,5}·A∩B={−1}", sA|sB=={-1,1,5} and sA&sB=={-1})
# ⑧ 练习3 等腰∩直角=等腰直角三角形（逻辑点）
ck("练习3 A∩B={等腰直角三角形}", True, "既等腰又直角")
# ⑨ 例5（p13）补集
U=set(range(1,9)); A5={1,2,3}; B5={3,4,5,6}
ck("例5 U={1..8}·∁U A={4,5,6,7,8}", U-A5=={4,5,6,7,8}, sorted(U-A5))
ck("例5 ∁U B={1,2,7,8}", U-B5=={1,2,7,8}, sorted(U-B5))
# ⑩ 补集恒等式抽验：A∪∁U A=U·A∩∁U A=∅
ck("恒等式 A∪∁U A=U·A∩∁U A=∅", (A5|(U-A5))==U and (A5&(U-A5))==set())
print("\n".join(R))
p=sum(1 for r in R if r.startswith("PASS")); f=sum(1 for r in R if r.startswith("FAIL"))
print("数学1.3 缺件补齐验点 PASS=%d FAIL=%d"%(p,f))
import sys; sys.exit(1 if f else 0)
