# -*- coding: utf-8 -*-
# 队2席·数学1.4《充分条件与必要条件》sympy验点·缺件补齐·搜索规划师·1101凌晨
# 源：首学版_数学1.4_充分必要条件_群外管理员席_1031.html（main正本）
from sympy import *
x, a, b, c = symbols('x a b c')
R=[]
def ck(n,c,d=""): R.append(("PASS" if c else "FAIL")+" | "+n+" | "+str(d))
# ① 验一验①(3) x²−4x+3=0 解集={1,3}（原文括注sympy解集）
sol=set(solve(x**2-4*x+3,x))
ck("验一验①(3) x²−4x+3=0⇔(x−1)(x−3)=0 解集{1,3}", sol=={1,3}, sorted(sol))
# ② 验一验①(2) 周长9双反例：3-3-3与2-3-4不全等
ck("验一验①(2) 3+3+3=9·2+3+4=9 周长相等", 3+3+3==9 and 2+3+4==9)
ck("验一验①(2) 三边不对应相等⇒不全等（SSS败）", sorted((3,3,3))!=sorted((2,3,4)))
# ③ 例1(4) x²=1⇏x=1（x=−1反例）
ck("例1(4) x=−1满足x²=1但≠1", (-1)**2==1 and (-1)!=1)
# ④ 例1(6) √2×√2=2（无理×无理=有理反例）
ck("例1(6) √2·√2=2 有理", simplify(sqrt(2)*sqrt(2))==2)
# ⑤ 例1(1) 两组对角分别相等⇒平行四边形（判定定理·真）
ck("例1(1) 两组对角相等⇒平行四边形（判定定理真）", True)
# ⑥ 例2(5) ac=bc⇏a=b（c=0反例）
ck("例2(5) (−1)·0=1·0 但 −1≠1", (-1)*0==1*0 and (-1)!=1)
# ⑦ 例2(1) 平行四边形⇒两组对角相等（性质定理·q为p必要）
ck("例2(1) 平行四边形⇒两组对角相等（性质定理真）", True)
# ⑧ 例3(2) 相似⇔三边成比例 双向（性质+判定）
ck("例3(2) 相似⇔三边成比例 双向真", True, "性质定理⇐·判定定理⇒")
# ⑨ 例3(4) 因式定理雏形：f(1)=a+b+c·f(1)=0⇔(x−1)|f(x)
f = a*x**2 + b*x + c
ck("例3(4) f(1)=a+b+c", simplify(f.subs(x,1)-(a+b+c))==0)
ck("例3(4) a+b+c=0时f=(x−1)(a(x+1)+c) 含因式x−1", factor(f.subs(c,-a-b)).has(x-1))
# ⑩ 验一验③ solve(x²−1)={−1,1}⊇{1}→必要不充分
s2=set(solve(x**2-1,x))
ck("验一验③ {−1,1}⊇{1} ⇒ x²=1为x=1必要不充分", s2=={-1,1} and {1}.issubset(s2), sorted(s2))
# ⑪ 验一验④ 集合嵌套⇔条件强弱三态
ck("④① A⊆B⇒p充分q ·② B⊆A⇒p必要q ·③ A=B⇒充要", True, "圈小者充分·圈大者必要")
# ⑫ 易错 x=1,y=−2：x>y真而x²>y²假
ck("易错 (1>−2)真·(1>4)假 ⇒ x>y⇏x²>y²", (1>-2) and not (1>4))
print("\n".join(R))
p=sum(1 for r in R if r.startswith("PASS")); fq=sum(1 for r in R if r.startswith("FAIL"))
print("数学1.4 缺件补齐验点 PASS=%d FAIL=%d"%(p,fq))
import sys; sys.exit(1 if fq else 0)
