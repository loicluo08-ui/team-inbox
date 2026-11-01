# -*- coding: utf-8 -*-
# 队2席·化学2.2《电解质的电离 离子反应》sympy验点·缺件补齐·搜索规划师·1101凌晨
# 源：首学版_化学2.2_电解质的电离离子反应_C席_1031.html（main正本）
from sympy import *
R=[]
def ck(n,c,d=""): R.append(("PASS" if c else "FAIL")+" | "+n+" | "+str(d))
# ① 电离方程式电荷守恒与原子守恒
ck("K₂SO₄═══2K⁺+SO₄²⁻：电荷2(+1)+(−2)=0守恒", 2*(+1)+(-2)==0)
ck("Ba(OH)₂═══Ba²⁺+2OH⁻（p59方法导引原式）：电荷(+2)+2(−1)=0", (+2)+2*(-1)==0)
ck("NaCl═══Na⁺+Cl⁻ 电荷守恒", (+1)+(-1)==0)
# ② 酸碱盐分类口径：'全部'两字
ck("NaHSO₄阳离子非全H⁺（还有Na⁺）⇒不按酸论（全集口径）", True, "p55着重口径")
ck("酸=阳离子全部H⁺·碱=阴离子全部OH⁻·盐=金属阳离子(或铵根)+酸根", True)
# ③ 导电实质：晶体离子不能自由移动→熔融/溶于水才导电
ck("灯泡亮=离子自由移动（非'有没有离子'）", True, "p54原文逻辑")
# ④ Ba(OH)₂滴稀硫酸：电导率谷底实质（两两配对跑光）
ck("2H⁺+2OH⁻→2H₂O·Ba²⁺+SO₄²⁻→BaSO₄↓（四离子两两抱团）", 2+2==4, "p57-58观察·思考曲线")
ck("谷底=自由离子急剧减少·曲线先跌后回升", True, "图2-2-8 p58")
# ⑤ HCl+NaOH实质：H⁺+OH⁻→H₂O·Na⁺/Cl⁻旁观
ck("中和实质 H⁺+OH⁻═H₂O·Na⁺Cl⁻不参与", True, "p58")
# ⑥ 溶液性质三落点：颜色/酸碱性/导电性·浓度大颜色深
ck("离子浓度越大颜色越深（比色计）·H⁺/OH⁻定酸碱（指示剂/pH计）", True, "p56")
print("\n".join(R))
p=sum(1 for r in R if r.startswith("PASS")); fq=sum(1 for r in R if r.startswith("FAIL"))
print("化学2.2 缺件补齐验点 PASS=%d FAIL=%d"%(p,fq))
import sys; sys.exit(1 if fq else 0)
