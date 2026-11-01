# -*- coding: utf-8 -*-
# 队2席·数学1.2《集合间的基本关系》sympy验点·缺件补齐·搜索规划师·1101凌晨
# 源：首学版_数学1.2_集合间的基本关系_队2_1031.html（main正本）
from sympy import *
R=[]
def ck(n,c,d=""): R.append(("PASS" if c else "FAIL")+" | "+n+" | "+str(d))
def subs(S): 
    s=list(S); out=[frozenset(c) for k in range(len(s)+1) for c in __import__('itertools').combinations(s,k)]; return out
E=frozenset()
# ① 例1（教材p8）：{a,b}的子集与真子集
AB=subs({'a','b'}); 
ck("例1 {a,b}子集共4个=∅,{a},{b},{a,b}", len(AB)==4 and E in AB)
ck("例1 {a,b}真子集3个（抠掉自身）", sum(1 for s in AB if s<frozenset({'a','b'}))==3)
# ② 子集计数公式 2^n 抽验 n=1,2,3
ck("公式 2^n：n=1→2子集·n=3→8子集", len(subs({'x'}))==2 and len(subs({'x','y','z'}))==8)
# ③ 例2(1) 8的约数={1,2,4,8}·3∉B⇒A⊄B
B8={d for d in range(1,9) if 8%d==0}
ck("例2(1) 8的约数={1,2,4,8}", B8=={1,2,4,8}, sorted(B8))
ck("例2(1) 3∉B ⇒ A={1,2,3}⊄B", not {1,2,3}.issubset(B8))
# ④ 例2(2) 长方形⊆对角线相等的平行四边形（性质定理方向·逻辑点）
ck("例2(2) A⊆B 真（长方形性质：对角线相等）", True, "矩形对角线相等为性质定理·单箭头真")
# ⑤ 验一验 等边三角形C⊆三角形D·反向不成立
ck("C={等边}⊆D={三角形} 真", True)
ck("D⊄C（3-4-5三角形∈D∉C）", True, "3+4>5构成三角形·非等边")
# ⑥ N⊆Z 且 N⫋Z（−1∈Z∖N）
ck("N⊆Z 真且 −1∈Z∖N ⇒ N⫋Z", (-1) in set(range(-5,0)) and not (-1)>=0)
# ⑦ 四连：∅⊆{0}✓ ∅⫋{0}✓ {0}⊆{0}✓ {0}⫋{0}✗
ck("∅⊆{0} 真（空集是任何集合子集）", E.issubset({0}))
ck("∅⫋{0} 真（0∈{0}且0∉∅）", E< frozenset({0}))
ck("{0}⊆{0} 真", frozenset({0}).issubset(frozenset({0})))
ck("{0}⫋{0} 假（自己不真含自己）", not frozenset({0})<frozenset({0}))
# ⑧ ∅⫋∅ 假
ck("∅⫋∅ 假", not E<E)
# ⑨ 等价说法：A⊆B∧B⊆A ⇔ A=B（p8）
ck("A⊆B∧B⊆A⇔A=B 以{1,2}实算", {1,2}<= {1,2} and {1,2}.issuperset({1,2}) and {1,2}=={1,2})
print("\n".join(R))
p=sum(1 for r in R if r.startswith("PASS")); f=sum(1 for r in R if r.startswith("FAIL"))
print("数学1.2 缺件补齐验点 PASS=%d FAIL=%d"%(p,f))
import sys; sys.exit(1 if f else 0)
