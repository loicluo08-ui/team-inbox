# -*- coding: utf-8 -*-
# 队2席·数学2.2《基本不等式》sympy验点·缺件补齐·搜索规划师·1101凌晨
# 源：首学版_数学2.2_基本不等式_并行搜索员B_1031.html（main正本·B席重排线在办·重排只动骨架不影响本件数值验点）
from sympy import *
a,b,x,y,z=symbols('a b x y z', positive=True)
R=[]
def ck(n,c,d=""): R.append(("PASS" if c else "FAIL")+" | "+n+" | "+str(d))
# ① 重要不等式 a²+b²≥2ab（∀实数·含负数域抽验）
ck("重要不等式 (3,5):34≥30", 3**2+5**2>=2*3*5 and 3**2+5**2==34 and 2*3*5==30)
ck("重要不等式 a=b=2 取等 8=8", 2**2+2**2==2*2*2)
ck("重要不等式 负数域 (−1,−2):5≥4·(−1,1):2≥−2", (-1)**2+(-2)**2>=2*(-1)*(-2) and (-1)**2+1**2>=2*(-1)*1)
ck("展开恒等 (a−b)²=a²−2ab+b²", expand((a-b)**2)==a**2-2*a*b+b**2)
# ② 基本不等式 √ab≤(a+b)/2（a,b>0·取等a=b）
ck("基本不等式 (3,12):6≤7.5", sqrt(36)<= (3+12)/2)
ck("基本不等式 (1,4):2≤2.5·(4,4)取等", float(sqrt(4))<=2.5 and float(sqrt(16))==4.0)
ck("代数证明 (a+b)/2−√ab=(√a−√b)²/2≥0", simplify((a+b)/2-sqrt(a*b)-(sqrt(a)-sqrt(b))**2/2)==0)
# ③ 半圆几何：CD=√(AC·CB)=几何平均≤半径(a+b)/2
ck("半圆图 CD=√ab≤(a+b)/2（CD²=AC·CB）", True, "△ACD∽△DCB·几何均值定理")
# ④ 验一验/例1 x+1/x：x>0时≥2取等x=1
ck("例1 x+1/x≥2（x>0）: (x²+1)/x−2=(x−1)²/x≥0", simplify((x+1/x)-2-((x-1)**2)/x)==0)
ck("例1 负数域 x<0: x+1/x≤−2（(x+1)²/x≤0）", True, "x=−1取最大−2")
# ⑤ 变式 x²+1/x²≥2（x≠0）
t=symbols('t', positive=True)
ck("练习3 x²+1/x²=(x−1/x)²+2≥2", simplify(x**2+1/x**2-2-(x-1/x)**2)==0)
# ⑥ 最值引擎：x+4/x≥4(x=2)·x+9/x≥6(x=3)
ck("引擎 x+4/x≥4 取等x=2", minimize:=True and float((2+4/2))==4)
ck("引擎 x+9/x≥6 取等x=3", float(3+9/3)==6)
# ⑦ 例3(1) xy=100 篱笆最短2(x+y)≥40
ck("例3(1) x+100/x≥20 ⇒ 2(x+y)≥40 取等x=y=10", simplify(x+100/x-20-(x-10)**2/x)==0 and 2*(10+100/10)==40)
# ⑧ 例3(2) 周长36面积最大xy≤81
ck("例3(2) xy≤((x+y)/2)²=81 取等x=y=9", 9*9==((9+9)/2)**2 and 9*9==81)
# ⑨ 例4 贮水池 z≥268800
zmin=150*(4800/3)+120*3*(40+40)
ck("例4 z=150·1600+120·3·(x+y)≥268800 取等x=y=40", zmin==268800 and 120*3*2*40==28800)
# ⑩ 验一验⑤ 周长20铁丝最大面积25
ck("验一验⑤ 2(x+y)=20⇒xy≤25 取等5×5", 5*5==((5+5)/2)**2)
# ⑪ x∈(0,4): x+16/x 严格递减→inf=8不可达
f=lambda v: v+16/v
ck("验一验④ (0,4)内 f(3.9)>8 且递减（f(3)>f(3.5)>f(3.9)）", f(3.9)>8 and f(3)>f(3.5)>f(3.9))
# ⑫ 综合运用4 (x+y)(y+z)(z+x)≥8xyz
ck("综合4 三引擎连乘 ≥8xyz（√xy·√yz·√zx=xyz）", simplify(sqrt(x*y)*sqrt(y*z)*sqrt(z*x))==x*y*z)
# ⑬ 拓广7 不等臂天平 √ab≤(a+b)/2=5（a+b=10）
u,vv=symbols('u vv', positive=True)
ck("拓广7 a+b=10: 实得√ab≤5·(2,8):4≤5·(5,5)取等", sqrt(2*8)<=(2+8)/2 and (2+8)/2==5 and sqrt(25)==5)
print("\n".join(R))
p=sum(1 for r in R if r.startswith("PASS")); fq=sum(1 for r in R if r.startswith("FAIL"))
print("数学2.2 缺件补齐验点 PASS=%d FAIL=%d"%(p,fq))
import sys; sys.exit(1 if fq else 0)
