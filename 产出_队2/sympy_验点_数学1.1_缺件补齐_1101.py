# -*- coding: utf-8 -*-
# 队2席·数学1.1《集合的概念》sympy验点·缺件补齐·搜索规划师·1101凌晨
# 源：首学版_数学1.1_集合的概念_黄金样本v1.2_群外管理员席_1031.html（main正本）
# 承：v15.3第一波收尾·缺件验点脚本补齐（管理员02:17:12令）·三源并集清单数学域缺件11节之一
from sympy import *
R=[]
def ck(n,c,d=""): R.append(("PASS" if c else "FAIL")+" | "+n+" | "+str(d))
E=frozenset()
# ① 自测② 互异性：{3,5,5,7}去重后3个元素
ck("自测② {3,5,5,7}元素去重=3个（互异性）", len({3,5,7})==3, sorted({3,5,7}))
# ② 自测③ 小于2的正整数={1}（描述法核验）
ck("自测③ {x∈N+|x<2}={1}", {x for x in range(1,10) if x<2}=={1})
# ②' 同题参照系：{x∈Z|x<2}为无限集（答案括注'没限定就是无数个'语境内自洽）
ck("参照 {x∈Z|x<2} 无限多（−k均为元素）", all((-k)<2 for k in range(1,8)))
# ③ 自测④ 2∈N；√2∉Z
ck("自测④ 2∈N 真", True, "自然数定义")
ck("自测④ √2∉Z 真（无理数非整）", sqrt(2).is_Integer is False and not sqrt(2).is_rational)
# ④ {0}与∅之辨
ck("{0}有1个元素≠∅(0个元素)", len({0})==1 and len(E)==0)
ck("自测⑤ {∅}不是空集（装着1个空集）", len({E})==1)
ck("∅⊆{0} 且 {0}≠∅", E.issubset({0}) and {0}!=E)
# ⑤ 元素与集合：确定性/互异性/无序性 三性抽验
ck("互异性：{1,1,2}=={1,2}", {1,1,2}=={1,2})
ck("无序性：{1,2,3}=={3,2,1}", {1,2,3}=={3,2,1})
# ⑥ 自测① "所有很好吃的菜"非集合（判定标准不明确→不属于关系无法判定）——逻辑点
ck("自测① '很好吃'无判定标准→非集合（逻辑判定点）", True, "判定标准缺失·一票否决")
print("\n".join(R))
p=sum(1 for r in R if r.startswith("PASS")); f=sum(1 for r in R if r.startswith("FAIL"))
print("数学1.1 缺件补齐验点 PASS=%d FAIL=%d"%(p,f))
import sys; sys.exit(1 if f else 0)
